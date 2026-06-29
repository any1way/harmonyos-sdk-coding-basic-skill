#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HarmonyOS SDK 文档 BM25 检索工具。

加载 build_index.py 构建的倒排索引，对用户查询进行分词并按 BM25 算法打分，
返回 Top N 最相关文档（路径、标题、分类、得分、摘要）。

用法：
    python scripts/search.py "ArkUI 状态管理"
    python scripts/search.py "如何播放音频" --top 5
    python scripts/search.py "Audio Kit API" --category harmonyos-references --top 8
    python scripts/search.py "Web组件加载本地资源" --snippet
    python scripts/search.py "状态管理" --json         # 机器可读输出

输出格式（默认）：
    Top 10 results for "..." (searched 12234 docs in 0.045s)

    [1] score=15.42  guides  harmonyos-guides/.../xxx.md
        Title: ...
        Breadcrumb: ...
    [2] ...

说明：
    - 若索引不存在或过期，会自动调用 build_index.py 重建
    - 摘要片段优先展示包含查询词的上下文
"""
from __future__ import annotations

import argparse
import json
import math
import os
import pickle
import subprocess
import sys
import time
from typing import Dict, List, Optional, Tuple

# 复用 build_index 的分词器与常量
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import build_index as _bi  # noqa: E402

ROOT = os.path.dirname(_HERE)
REFERENCES_DIR = _bi.REFERENCES_DIR
INDEX_DIR = _bi.INDEX_DIR

DOCS_PATH = os.path.join(INDEX_DIR, "docs.pkl")
INVERTED_PATH = os.path.join(INDEX_DIR, "inverted.pkl")
META_PATH = os.path.join(INDEX_DIR, "meta.json")


# ----------------------------- 索引加载 -----------------------------

def _ensure_index() -> dict:
    """确保索引存在且有效，必要时自动构建。"""
    if not (os.path.exists(DOCS_PATH) and os.path.exists(INVERTED_PATH)
            and os.path.exists(META_PATH)):
        print("[info] 索引不存在，开始构建...", file=sys.stderr)
        subprocess.check_call([sys.executable, os.path.join(_HERE, "build_index.py")])
    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    # 简单的过期检测：与 references 目录最新文件 mtime 对比
    newest = 0
    for dp, _dn, fn in os.walk(REFERENCES_DIR):
        for f in fn:
            if f.endswith(".md"):
                try:
                    newest = max(newest, os.path.getmtime(os.path.join(dp, f)))
                except OSError:
                    pass
    if meta.get("built_at_epoch", 0) < newest - 1:
        print("[info] 检测到文档更新，重建索引...", file=sys.stderr)
        subprocess.check_call([sys.executable, os.path.join(_HERE, "build_index.py")])
        with open(META_PATH, "r", encoding="utf-8") as f:
            meta = json.load(f)
    return meta


def load_index() -> Tuple[List[dict], Dict[str, List[Tuple[int, int]]], dict]:
    meta = _ensure_index()
    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)
    with open(INVERTED_PATH, "rb") as f:
        inverted = pickle.load(f)
    return documents, inverted, meta


# ----------------------------- BM25 打分 -----------------------------

def bm25_score(query_terms: List[str],
               inverted: Dict[str, List[Tuple[int, int]]],
               documents: List[dict],
               avgdl: float,
               k1: float = 1.5,
               b: float = 0.75) -> Dict[int, float]:
    """对包含任一查询词的文档计算 BM25 分数。"""
    n_docs = len(documents)
    scores: Dict[int, float] = {}
    if not query_terms:
        return scores

    # 计算每个查询词的 IDF
    for term in query_terms:
        postings = inverted.get(term)
        if not postings:
            continue
        df = len(postings)
        idf = math.log(1 + (n_docs - df + 0.5) / (df + 0.5))
        for doc_id, tf in postings:
            doc_len = documents[doc_id]["length"]
            denom = tf + k1 * (1 - b + b * doc_len / (avgdl or 1.0))
            s = idf * (tf * (k1 + 1)) / denom
            scores[doc_id] = scores.get(doc_id, 0.0) + s
    return scores


# ----------------------------- 摘要 -----------------------------

def make_snippet(rel_path: str, query_terms: List[str],
                 max_len: int = 240) -> str:
    """从文档正文中提取包含查询词的上下文片段。"""
    abs_path = os.path.join(REFERENCES_DIR, rel_path)
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError:
        return ""
    # 去 frontmatter
    meta, body = _bi.parse_frontmatter(content)
    # 去除 markdown 链接/图片/标记，简化展示
    body = _bi.re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    body = _bi.re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", body)
    body = _bi.re.sub(r"[`*_>#|]+", " ", body)
    body = _bi.re.sub(r"\s+", " ", body).strip()

    if not body:
        return ""

    # 找最早出现的查询词位置（中文字符或英文词）
    lower_body = body.lower()
    positions = []
    for q in query_terms:
        if not q:
            continue
        idx = lower_body.find(q.lower())
        if idx >= 0:
            positions.append(idx)
    if not positions:
        # 没命中就取开头
        return body[:max_len] + ("..." if len(body) > max_len else "")

    center = min(positions)
    half = max_len // 2
    start = max(0, center - half)
    end = min(len(body), center + half)
    snippet = body[start:end]
    if start > 0:
        snippet = "..." + snippet
    if end < len(body):
        snippet = snippet + "..."
    return snippet


# ----------------------------- 输出 -----------------------------

def _category_short(cat: str) -> str:
    return {
        "harmonyos-guides": "guides",
        "harmonyos-references": "api",
        "harmonyos-faqs": "faq",
        "best-practices": "best",
        "harmonyos-releases": "release",
    }.get(cat, cat[:8])


def format_results(query: str,
                   hits: List[Tuple[int, float]],
                   documents: List[dict],
                   query_terms: List[str],
                   elapsed: float,
                   total_searched: int,
                   with_snippet: bool) -> str:
    lines: List[str] = []
    lines.append(f'Top {len(hits)} results for "{query}" '
                 f'(searched {total_searched} docs in {elapsed:.3f}s)')
    lines.append("")
    if not hits:
        lines.append("（无匹配文档。可尝试：拆分关键词、改用 Kit 名、去掉版本号、"
                     "或查阅 references/feature-routing.md）")
        return "\n".join(lines)
    for rank, (doc_id, score) in enumerate(hits, 1):
        doc = documents[doc_id]
        cat = _category_short(doc.get("category", ""))
        title = doc.get("title", "")
        path = doc.get("path", "")
        bc = doc.get("breadcrumb", "")
        lines.append(f"[{rank}] score={score:.2f}  {cat}  {path}")
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
                hits: List[Tuple[int, float]],
                documents: List[dict],
                query_terms: List[str],
                elapsed: float,
                total_searched: int,
                with_snippet: bool) -> str:
    results = []
    for rank, (doc_id, score) in enumerate(hits, 1):
        doc = documents[doc_id]
        item = {
            "rank": rank,
            "score": round(score, 4),
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
        "total_searched": total_searched,
        "elapsed_sec": round(elapsed, 4),
        "count": len(results),
        "results": results,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


# ----------------------------- 主入口 -----------------------------

def search(query: str,
           top: int = 10,
           category: Optional[str] = None,
           with_snippet: bool = False) -> Tuple[List[Tuple[int, float]],
                                                List[dict],
                                                List[str],
                                                float,
                                                int]:
    documents, inverted, meta = load_index()
    avgdl = meta.get("avg_doc_length", 1.0)
    query_terms = _bi.tokenize(query)

    t0 = time.time()
    scores = bm25_score(query_terms, inverted, documents, avgdl,
                        k1=meta.get("k1", 1.5), b=meta.get("b", 0.75))
    elapsed = time.time() - t0

    # 按分类过滤
    if category:
        norm_cat = {
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
        scores = {did: s for did, s in scores.items()
                  if documents[did].get("category") == norm_cat}

    # 排序取 Top N
    hits = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:top]
    return hits, documents, query_terms, elapsed, len(documents)


def main() -> int:
    ap = argparse.ArgumentParser(description="HarmonyOS SDK 文档 BM25 检索")
    ap.add_argument("query", help="查询字符串")
    ap.add_argument("--top", type=int, default=10, help="返回 Top N 结果（默认 10）")
    ap.add_argument("--category", default=None,
                    help="按分类过滤：guides/api/faq/best/release")
    ap.add_argument("--snippet", action="store_true",
                    help="展示文档摘要片段")
    ap.add_argument("--json", action="store_true",
                    help="输出 JSON（机器可读）")
    args = ap.parse_args()

    hits, documents, query_terms, elapsed, total = search(
        args.query, top=args.top, category=args.category,
        with_snippet=args.snippet,
    )

    if args.json:
        print(format_json(args.query, hits, documents, query_terms,
                          elapsed, total, args.snippet))
    else:
        print(format_results(args.query, hits, documents, query_terms,
                             elapsed, total, args.snippet))
    return 0


if __name__ == "__main__":
    sys.exit(main())
