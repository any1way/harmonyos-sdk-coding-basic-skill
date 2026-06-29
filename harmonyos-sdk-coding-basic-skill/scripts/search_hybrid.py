#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HarmonyOS SDK 文档 Hybrid 检索工具（方案 3）。

将 BM25（精确关键词匹配）与 BGE Dense（语义匹配）两路召回结果，
通过 Reciprocal Rank Fusion (RRF) 融合后返回 Top N，兼顾精确性与语义泛化。
默认 Dense 模型为 bge-small-zh-v1.5（512 维）。

RRF 公式：score(d) = Σ_c  1 / (k + rank_c(d))，默认 k=60。

用法：
    python scripts/search_hybrid.py "ArkUI 状态管理"
    python scripts/search_hybrid.py "怎么让应用启动更快" --top 5 --snippet
    python scripts/search_hybrid.py "AVPlayer setURL" --category api
    python scripts/search_hybrid.py "音频播放" --weights 0.4 0.6 --json

依赖：
    - BM25 索引（scripts/index/docs.pkl + inverted.pkl），由 build_index.py 构建
    - Dense 索引（scripts/index/dense_vectors.npy + faiss.index），由 build_dense_index.py 构建
      首次运行时会自动触发构建（含模型下载，约 10–15 分钟）

输出：与 search.py 一致，额外显示各路排名以便分析。
"""
from __future__ import annotations

import argparse
import json
import os
import pickle
import sys
import time
from typing import Dict, List, Optional, Tuple

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import build_index as _bi  # noqa: E402
import search as _bm25  # noqa: E402
import build_dense_index as _dense  # noqa: E402

ROOT = _bi.ROOT
REFERENCES_DIR = _bi.REFERENCES_DIR
INDEX_DIR = _bi.INDEX_DIR

DENSE_VECTORS_PATH = os.path.join(INDEX_DIR, "dense_vectors.npy")
FAISS_INDEX_PATH = os.path.join(INDEX_DIR, "faiss.index")
DENSE_DOCS_PATH = os.path.join(INDEX_DIR, "dense_docs.pkl")
DENSE_META_PATH = os.path.join(INDEX_DIR, "dense_meta.json")
MODEL_PATH_CACHE = [None]  # 复用模型实例


# ----------------------------- 索引加载 -----------------------------

def _ensure_dense_index() -> None:
    """确保 dense 索引存在。"""
    if not (os.path.exists(DENSE_VECTORS_PATH)
            and os.path.exists(FAISS_INDEX_PATH)
            and os.path.exists(DENSE_DOCS_PATH)):
        print("[info] Dense 索引不存在，开始构建（首次约 10–15 分钟）...",
              file=sys.stderr)
        import subprocess
        subprocess.check_call([sys.executable,
                               os.path.join(_HERE, "build_dense_index.py")])


def load_dense_index() -> Tuple[List[dict], np.ndarray, "faiss.Index", dict]:
    _ensure_dense_index()
    import faiss
    with open(DENSE_DOCS_PATH, "rb") as f:
        docs = pickle.load(f)
    vectors = np.load(DENSE_VECTORS_PATH)
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(DENSE_META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    return docs, vectors, index, meta


# ----------------------------- Dense 检索 -----------------------------

def _get_model():
    """懒加载并缓存 BGE 模型实例。若索引记录的本地路径已失效，重新下载。"""
    if MODEL_PATH_CACHE[0] is not None:
        return MODEL_PATH_CACHE[0]
    with open(DENSE_META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    model_path = meta.get("model_path", _dense.MODEL_NAME)
    # 保护：索引存在但模型目录被删除时，重新下载
    if model_path != _dense.MODEL_NAME and not _dense._is_model_present(model_path):
        print(f"[warn] 模型目录缺失：{model_path}，重新下载...", file=sys.stderr)
        model_path = _dense.ensure_model()
    use_gpu = meta.get("device") == "cuda"
    model_info = _dense.load_model(model_path, use_gpu=use_gpu)
    MODEL_PATH_CACHE[0] = model_info
    return model_info


def dense_search(query: str, faiss_index, top_k: int = 30) -> List[Tuple[int, float]]:
    """对查询编码并做 FAISS Top K 检索，返回 [(doc_id, score), ...]。"""
    model_info = _get_model()
    vec = _dense.encode_texts(model_info, [query], batch_size=1)  # (1, 1024)
    scores, indices = faiss_index.search(vec, top_k)
    return [(int(idx), float(s))
            for idx, s in zip(indices[0], scores[0]) if idx >= 0]


# ----------------------------- RRF 融合 -----------------------------

def rrf_fuse(bm25_hits: List[Tuple[int, float]],
             dense_hits: List[Tuple[int, float]],
             k: int = 60,
             weights: Tuple[float, float] = (0.5, 0.5)) -> List[Tuple[int, float, dict]]:
    """RRF 融合两路结果，返回 [(doc_id, fused_score, rank_info), ...]。

    rank_info = {"bm25_rank": int|None, "bm25_score": float|None,
                 "dense_rank": int|None, "dense_score": float|None}
    """
    w_bm25, w_dense = weights
    bm25_rank = {doc_id: (rank + 1, score)
                 for rank, (doc_id, score) in enumerate(bm25_hits)}
    dense_rank = {doc_id: (rank + 1, score)
                  for rank, (doc_id, score) in enumerate(dense_hits)}

    all_doc_ids = set(bm25_rank.keys()) | set(dense_rank.keys())
    fused: List[Tuple[int, float, dict]] = []
    for doc_id in all_doc_ids:
        score = 0.0
        info = {"bm25_rank": None, "bm25_score": None,
                "dense_rank": None, "dense_score": None}
        if doc_id in bm25_rank:
            r, s = bm25_rank[doc_id]
            score += w_bm25 / (k + r)
            info["bm25_rank"] = r
            info["bm25_score"] = round(s, 4)
        if doc_id in dense_rank:
            r, s = dense_rank[doc_id]
            score += w_dense / (k + r)
            info["dense_rank"] = r
            info["dense_score"] = round(s, 4)
        fused.append((doc_id, score, info))
    fused.sort(key=lambda x: x[1], reverse=True)
    return fused


# ----------------------------- 摘要 -----------------------------

def make_snippet(rel_path: str, query_terms: List[str],
                 max_len: int = 240) -> str:
    return _bm25.make_snippet(rel_path, query_terms, max_len=max_len)


# ----------------------------- 输出 -----------------------------

def _category_short(cat: str) -> str:
    return _bm25._category_short(cat)


def format_results(query: str,
                   fused: List[Tuple[int, float, dict]],
                   documents: List[dict],
                   query_terms: List[str],
                   elapsed: float,
                   total_searched: int,
                   with_snippet: bool) -> str:
    lines: List[str] = []
    lines.append(f'Hybrid Top {len(fused)} results for "{query}" '
                 f'(searched {total_searched} docs in {elapsed:.3f}s)')
    lines.append("")
    if not fused:
        lines.append("（无匹配文档。可尝试：拆分关键词、改用 Kit 名、去掉版本号、"
                     "或查阅 references/feature-routing.md）")
        return "\n".join(lines)
    for rank, (doc_id, score, info) in enumerate(fused, 1):
        doc = documents[doc_id] if doc_id < len(documents) else {}
        cat = _category_short(doc.get("category", ""))
        title = doc.get("title", "")
        path = doc.get("path", "")
        bc = doc.get("breadcrumb", "")
        lines.append(f"[{rank}] rrf={score:.4f}  {cat}  {path}")
        bm25_rank = info.get("bm25_rank")
        dense_rank = info.get("dense_rank")
        lines.append(f"    BM25 rank={bm25_rank} score={info.get('bm25_score')} | "
                     f"Dense rank={dense_rank} score={info.get('dense_score')}")
        if title:
            lines.append(f"    Title: {title}")
        if bc:
            lines.append(f"    Breadcrumb: {bc}")
        if with_snippet:
            snip = make_snippet(path, query_terms)
            if snip:
                lines.append(f"    Snippet: {snip}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def format_json(query: str,
                fused: List[Tuple[int, float, dict]],
                documents: List[dict],
                query_terms: List[str],
                elapsed: float,
                total_searched: int,
                with_snippet: bool,
                weights: Tuple[float, float]) -> str:
    results = []
    for rank, (doc_id, score, info) in enumerate(fused, 1):
        doc = documents[doc_id] if doc_id < len(documents) else {}
        item = {
            "rank": rank,
            "rrf_score": round(score, 6),
            "bm25_rank": info.get("bm25_rank"),
            "bm25_score": info.get("bm25_score"),
            "dense_rank": info.get("dense_rank"),
            "dense_score": info.get("dense_score"),
            "path": doc.get("path", ""),
            "title": doc.get("title", ""),
            "breadcrumb": doc.get("breadcrumb", ""),
            "category": doc.get("category", ""),
            "url": doc.get("url", ""),
        }
        if with_snippet:
            item["snippet"] = make_snippet(doc.get("path", ""), query_terms)
        results.append(item)
    payload = {
        "query": query,
        "query_terms": query_terms,
        "weights": {"bm25": weights[0], "dense": weights[1]},
        "total_searched": total_searched,
        "elapsed_sec": round(elapsed, 4),
        "count": len(results),
        "results": results,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


# ----------------------------- 主流程 -----------------------------

def hybrid_search(query: str,
                  top: int = 10,
                  category: Optional[str] = None,
                  k: int = 60,
                  weights: Tuple[float, float] = (0.5, 0.5),
                  with_snippet: bool = False
                  ) -> Tuple[List[Tuple[int, float, dict]], List[dict],
                             List[str], float, int]:
    # 1. BM25 召回（Top 30）
    bm25_documents, inverted, bm25_meta = _bm25.load_index()
    avgdl = bm25_meta.get("avg_doc_length", 1.0)
    query_terms = _bi.tokenize(query)
    bm25_scores = _bm25.bm25_score(
        query_terms, inverted, bm25_documents, avgdl,
        k1=bm25_meta.get("k1", 1.5), b=bm25_meta.get("b", 0.75))
    if category:
        norm_cat = _normalize_category(category)
        bm25_scores = {did: s for did, s in bm25_scores.items()
                       if bm25_documents[did].get("category") == norm_cat}
    bm25_hits = sorted(bm25_scores.items(), key=lambda kv: kv[1], reverse=True)[:30]

    # 2. Dense 召回（Top 30）
    dense_documents, _dense_vecs, faiss_index, _dense_meta = load_dense_index()
    # Dense 与 BM25 文档列表需要对齐：用 dense_documents 索引
    # 但 doc_id 在两套索引中可能不同（构建顺序可能略有差异），需要按 path 对齐
    path_to_dense_id = {d["path"]: d["id"] for d in dense_documents}
    path_to_bm25_id = {d["path"]: d["id"] for d in bm25_documents}

    if category:
        # 限制 dense 在分类内检索（通过过滤路径）
        allowed_paths = {d["path"] for d in dense_documents
                         if d.get("category") == _normalize_category(category)}
    else:
        allowed_paths = None

    raw_dense = dense_search(query, faiss_index, top_k=50)
    dense_hits: List[Tuple[int, float]] = []
    # dense doc_id → bm25 doc_id 映射（最终输出用 bm25 doc_id 以统一文档列表）
    dense_id_to_bm25_id: Dict[int, int] = {}
    for dense_id, score in raw_dense:
        d_doc = dense_documents[dense_id] if dense_id < len(dense_documents) else {}
        path = d_doc.get("path", "")
        if allowed_paths and path not in allowed_paths:
            continue
        bm25_id = path_to_bm25_id.get(path)
        if bm25_id is None:
            continue  # 仅在一边存在的文档，跳过融合（极少见）
        dense_hits.append((bm25_id, score))
        dense_id_to_bm25_id[dense_id] = bm25_id
        if len(dense_hits) >= 30:
            break

    # 3. RRF 融合
    t0 = time.time()
    fused = rrf_fuse(bm25_hits, dense_hits, k=k, weights=weights)
    elapsed = time.time() - t0 + 0.001  # 至少有点耗时

    fused = fused[:top]
    return fused, bm25_documents, query_terms, elapsed, len(bm25_documents)


def _normalize_category(category: str) -> str:
    return {
        "guides": "harmonyos-guides",
        "guide": "harmonyos-guides",
        "api": "harmonyos-references",
        "references": "harmonyos-references",
        "faq": "harmonyos-faqs",
        "faqs": "harmonyos-faqs",
        "best": "best-practices",
        "best-practices": "best-practices",
        "release": "harmonyos-releases",
        "releases": "harmonyos-releases",
    }.get(category, category)


def main() -> int:
    ap = argparse.ArgumentParser(description="HarmonyOS SDK 文档 Hybrid (BM25+Dense+RRF) 检索")
    ap.add_argument("query", help="查询字符串")
    ap.add_argument("--top", type=int, default=10, help="返回 Top N（默认 10）")
    ap.add_argument("--category", default=None,
                    help="按分类过滤：guides/api/faq/best/release")
    ap.add_argument("--k", type=int, default=60, help="RRF 参数 k（默认 60）")
    ap.add_argument("--weights", type=float, nargs=2, default=[0.5, 0.5],
                    metavar=("BM25_W", "DENSE_W"),
                    help="两路融合权重，默认 0.5 0.5")
    ap.add_argument("--snippet", action="store_true", help="展示文档摘要片段")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    # 归一化权重
    w = tuple(args.weights)
    s = sum(w)
    if s > 0:
        w = (w[0] / s, w[1] / s)

    fused, documents, query_terms, elapsed, total = hybrid_search(
        args.query, top=args.top, category=args.category,
        k=args.k, weights=w, with_snippet=args.snippet,
    )

    if args.json:
        print(format_json(args.query, fused, documents, query_terms,
                          elapsed, total, args.snippet, w))
    else:
        print(format_results(args.query, fused, documents, query_terms,
                             elapsed, total, args.snippet))
    return 0


if __name__ == "__main__":
    sys.exit(main())
