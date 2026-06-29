#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HarmonyOS SDK 文档 Dense 向量索引构建工具（方案 3 配套）。

使用 BGE 系列模型对 references/ 下所有 .md 文档编码为 dense 向量，
构建 FAISS 索引，与 BM25 倒排索引配合，由 search_hybrid.py 通过 RRF 融合。

默认模型：BAAI/bge-small-zh-v1.5（24M 参数，512 维，CPU 友好，约 10 分钟完成）
  - 选 small 而非 m3：CPU 推理速度差 ~20x，Top-N 召回场景下精度差距可接受
  - 与 BM25 互补：Dense 负责语义泛化，BM25 负责精确关键词匹配
模型通过 ModelScope 下载，设备自动检测 CUDA。

用法：
    python scripts/build_dense_index.py            # 默认构建
    python scripts/build_dense_index.py --force    # 强制重建
    python scripts/build_dense_index.py --batch 16 # 自定义 batch size

索引产物（位于 scripts/index/）：
    - dense_vectors.npy  : (N, 1024) fp32 向量矩阵
    - faiss.index        : FAISS IndexFlatIP 索引
    - dense_meta.json    : 索引元数据（模型/维度/构建时间）
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import time
from typing import List, Tuple

import numpy as np

# 复用 build_index.py 的文档扫描与 frontmatter 解析
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import build_index as _bi  # noqa: E402

ROOT = _bi.ROOT
REFERENCES_DIR = _bi.REFERENCES_DIR
INDEX_DIR = _bi.INDEX_DIR
MODELS_DIR = os.path.join(ROOT, "models")

DENSE_VECTORS_PATH = os.path.join(INDEX_DIR, "dense_vectors.npy")
FAISS_INDEX_PATH = os.path.join(INDEX_DIR, "faiss.index")
DENSE_META_PATH = os.path.join(INDEX_DIR, "dense_meta.json")

MODEL_NAME = "BAAI/bge-small-zh-v1.5"
EMBED_DIM = 512
MAX_SEQ_LEN = 512  # bge-small-zh-v1.5 原生支持 512
# 注：选 bge-small-zh-v1.5（24M 参数）而非 bge-m3（568M），
# 因为本场景为 CPU 推理，small 模型速度快 ~20x（5–10 分钟 vs 3+ 小时），
# 中文文档检索效果在 Top-N 召回场景下差距可接受（且与 BM25 互补）。


# ----------------------------- 文档加载 -----------------------------

def load_doc_texts() -> Tuple[List[dict], List[str]]:
    """扫描文档，返回 (元信息列表, 待编码文本列表)。

    文本构造：title + breadcrumb + 正文前 4000 字（控制编码时长）。
    顺序与 BM25 的 docs.pkl 完全一致，便于对齐 doc_id。
    """
    documents: List[dict] = []
    texts: List[str] = []

    for dp, _dn, fn in os.walk(REFERENCES_DIR):
        for f in sorted(fn):
            if not f.endswith(".md") or f in _bi.EXCLUDE_FILES:
                continue
            abs_path = os.path.join(dp, f)
            rel_path = os.path.relpath(abs_path, REFERENCES_DIR).replace("\\", "/")
            try:
                with open(abs_path, "r", encoding="utf-8", errors="replace") as fh:
                    content = fh.read()
            except OSError:
                continue
            meta, body = _bi.parse_frontmatter(content)
            title = meta.get("title", os.path.splitext(f)[0])
            breadcrumb = meta.get("breadcrumb", "")
            category = meta.get("category", rel_path.split("/")[0])
            url = meta.get("url", "")

            # 构造编码文本：标题 + 面包屑 + 正文（截断）
            body_trimmed = body.strip()[:4000]
            text = f"{title}\n{breadcrumb}\n{body_trimmed}".strip()
            if not text:
                continue

            doc_id = len(documents)
            documents.append({
                "id": doc_id,
                "path": rel_path,
                "title": title,
                "breadcrumb": breadcrumb,
                "category": category,
                "url": url,
            })
            texts.append(text)
    return documents, texts


# ----------------------------- 模型加载 -----------------------------

def load_model(model_path: str, use_gpu: bool = False):
    """加载 BGE 模型。优先使用 transformers 后端（避免 tqdm 与 PowerShell
    进度条交互导致的控制台崩溃问题），FlagEmbedding 作为备选。"""
    device = "cuda" if use_gpu else "cpu"
    try:
        import torch
        from transformers import AutoModel, AutoTokenizer
        tok = AutoTokenizer.from_pretrained(model_path)
        mdl = AutoModel.from_pretrained(model_path).to(device).eval()
        print(f"[info] 使用 transformers 加载模型，device={device}")
        return ("hf", (tok, mdl, device))
    except Exception as e:
        print(f"[warn] transformers 加载失败（{e}），回退到 FlagEmbedding")
        from FlagEmbedding import BGEM3FlagModel
        model = BGEM3FlagModel(
            model_path,
            use_fp16=use_gpu,
            device=device,
        )
        return ("flag", model)


def encode_texts(model_info, texts: List[str], batch_size: int) -> np.ndarray:
    """对文本列表编码，返回 (N, 1024) fp32 归一化向量。"""
    kind = model_info[0]
    n = len(texts)
    print(f"[info] 开始编码 {n} 篇文档，batch_size={batch_size}")

    if kind == "flag":
        model = model_info[1]
        t0 = time.time()
        embeddings = model.encode(
            texts,
            batch_size=batch_size,
            max_length=MAX_SEQ_LEN,
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False,
        )["dense_vecs"]
        elapsed = time.time() - t0
        vecs = np.asarray(embeddings, dtype=np.float32)
    else:
        import torch
        from transformers import AutoModel, AutoTokenizer
        tok, mdl, device = model_info[1]
        vecs = np.zeros((n, EMBED_DIM), dtype=np.float32)
        t0 = time.time()
        with torch.no_grad():
            for i in range(0, n, batch_size):
                batch = texts[i:i + batch_size]
                inputs = tok(batch, padding=True, truncation=True,
                             max_length=MAX_SEQ_LEN, return_tensors="pt").to(device)
                outputs = mdl(**inputs)
                # last_hidden_state mean pooling + mask
                mask = inputs["attention_mask"].unsqueeze(-1).float()
                summed = (outputs.last_hidden_state * mask).sum(1)
                counts = mask.sum(1).clamp(min=1e-9)
                emb = (summed / counts).cpu().numpy().astype(np.float32)
                vecs[i:i + len(batch)] = emb
                done = i + len(batch)
                if (i // batch_size) % 20 == 0 or done == n:
                    pct = done / n * 100
                    rate = done / (time.time() - t0 + 1e-9)
                    eta = (n - done) / (rate + 1e-9)
                    print(f"  ... {done}/{n} ({pct:.1f}%) "
                          f"rate={rate:.1f}docs/s eta={eta:.0f}s",
                          flush=True)
        elapsed = time.time() - t0

    # L2 归一化（便于内积 = 余弦相似度）
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    vecs = vecs / norms
    print(f"[info] 编码完成，耗时 {elapsed:.1f}s，"
          f"向量形状 {vecs.shape}")
    return vecs


# ----------------------------- FAISS 索引 -----------------------------

def build_faiss_index(vectors: np.ndarray) -> "faiss.Index":
    import faiss
    n, dim = vectors.shape
    index = faiss.IndexFlatIP(dim)  # 内积（向量已归一化 = 余弦）
    index.add(vectors)
    print(f"[info] FAISS 索引构建完成，{n} 个向量，dim={dim}")
    return index


# ----------------------------- 主流程 -----------------------------

def find_model_path() -> str:
    """定位模型路径。ModelScope 会把模型名中的 '.' 替换为 '___'。"""
    # 从 MODEL_NAME 推导可能的目录名
    base_name = MODEL_NAME.split("/")[-1]
    escaped_name = base_name.replace(".", "___")
    org = MODEL_NAME.split("/")[0] if "/" in MODEL_NAME else "BAAI"
    candidates = [
        os.path.join(MODELS_DIR, org, base_name),
        os.path.join(MODELS_DIR, org, escaped_name),  # modelscope 转义
        os.path.join(MODELS_DIR, base_name),
        os.path.join(MODELS_DIR, escaped_name),
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "config.json")):
            return c
    # 兜底：让 transformers 自动从 HF 下载
    return MODEL_NAME


def build_dense_index(force: bool = False, batch_size: int = 32) -> None:
    os.makedirs(INDEX_DIR, exist_ok=True)

    # 增量检测
    if not force and os.path.exists(DENSE_META_PATH) \
            and os.path.exists(DENSE_VECTORS_PATH) \
            and os.path.exists(FAISS_INDEX_PATH):
        with open(DENSE_META_PATH, "r", encoding="utf-8") as f:
            old = json.load(f)
        # 与 docs.pkl 比对文档数
        if old.get("total_docs") == _count_md_files():
            print(f"[skip] Dense 索引已是最新（built_at={old.get('built_at')}）。"
                  f"使用 --force 强制重建。")
            return

    model_path = find_model_path()
    print(f"[info] 模型路径：{model_path}")

    # 设备检测
    try:
        import torch
        use_gpu = torch.cuda.is_available()
    except Exception:
        use_gpu = False
    print(f"[info] 使用 GPU：{use_gpu}")

    # 加载文档
    documents, texts = load_doc_texts()
    print(f"[info] 待编码文档：{len(texts)} 篇")

    # 加载模型并编码
    model_info = load_model(model_path, use_gpu=use_gpu)
    vectors = encode_texts(model_info, texts, batch_size=batch_size)

    # 构建 FAISS 索引
    faiss_index = build_faiss_index(vectors)

    # 持久化
    np.save(DENSE_VECTORS_PATH, vectors)
    import faiss
    faiss.write_index(faiss_index, FAISS_INDEX_PATH)

    # 保存文档元信息（与 BM25 docs.pkl 同步），便于 search_hybrid 对齐 doc_id
    docs_path = os.path.join(INDEX_DIR, "dense_docs.pkl")
    import pickle
    with open(docs_path, "wb") as f:
        pickle.dump(documents, f, protocol=pickle.HIGHEST_PROTOCOL)

    meta = {
        "built_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "built_at_epoch": time.time(),
        "model": MODEL_NAME,
        "model_path": model_path,
        "embed_dim": EMBED_DIM,
        "total_docs": len(documents),
        "max_seq_len": MAX_SEQ_LEN,
        "device": "cuda" if use_gpu else "cpu",
        "batch_size": batch_size,
        "vectors_size_mb": round(os.path.getsize(DENSE_VECTORS_PATH) / 1024 / 1024, 2),
        "faiss_index_size_mb": round(os.path.getsize(FAISS_INDEX_PATH) / 1024 / 1024, 2),
    }
    with open(DENSE_META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"[ok] Dense 索引构建完成")
    print(f"     dense_vectors.npy : {meta['vectors_size_mb']} MB")
    print(f"     faiss.index       : {meta['faiss_index_size_mb']} MB")
    print(f"     dense_docs.pkl    : {docs_path}")
    print(f"     dense_meta.json   : {DENSE_META_PATH}")


def _count_md_files() -> int:
    n = 0
    for dp, _dn, fn in os.walk(REFERENCES_DIR):
        for f in fn:
            if f.endswith(".md") and f not in _bi.EXCLUDE_FILES:
                n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description="构建 BGE Dense 向量索引")
    ap.add_argument("--force", action="store_true", help="强制重建")
    ap.add_argument("--batch", type=int, default=32, help="batch size（默认 32）")
    args = ap.parse_args()
    build_dense_index(force=args.force, batch_size=args.batch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
