#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HarmonyOS SDK 文档 BM25 索引构建工具。

扫描 references/ 下所有 .md 文档，解析 YAML frontmatter（title/breadcrumb/category），
对标题、面包屑、正文进行分词并加权（标题 5x、面包屑 2x、正文 1x），
构建倒排索引并持久化为 pickle 文件，供 search.py 在毫秒级返回 Top N 文档。

用法：
    python scripts/build_index.py            # 默认构建索引
    python scripts/build_index.py --force    # 强制重建

索引产物（位于 scripts/index/）：
    - docs.pkl        : 文档元信息列表（id/path/title/category/length/breadcrumb/url）
    - inverted.pkl    : 倒排索引 {term: [(doc_id, tf), ...]}
    - meta.json       : 索引元数据（avg_doc_length/total_docs/构建时间/参数）
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import pickle
import re
import sys
import time
from collections import defaultdict
from typing import Dict, List, Tuple

# ----------------------------- 配置 -----------------------------

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCES_DIR = os.path.join(ROOT, "references")
INDEX_DIR = os.path.join(ROOT, "scripts", "index")

# 文件名排除（不参与索引）
EXCLUDE_FILES = {"INDEX.md", "kit-routing.md", "feature-routing.md"}

# BM25 参数
K1 = 1.5
B = 0.75

# 字段权重
TITLE_WEIGHT = 5.0
BREADCRUMB_WEIGHT = 2.0
BODY_WEIGHT = 1.0
PATH_WEIGHT = 1.0  # 路径分段也参与索引（便于按 Kit 名匹配）

# ----------------------------- 分词 -----------------------------

# 中文 Unicode 范围（基础 + 扩展 A + 兼容）
_CJK_RE = re.compile(
    r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]"
)
# 英文单词：含连字符的字母数字串
_WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_\-]*")
# CamelCase 切分
_CAMEL_RE = re.compile(r"([a-z0-9])([A-Z])")
# 前端 frontmatter
_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)

# 中英停用词（精简版，避免误杀技术词汇）
_STOPWORDS = {
    # 中文
    "的", "了", "和", "是", "在", "与", "或", "及", "为", "对", "由", "从", "到",
    "可", "可以", "能够", "应", "应当", "需要", "需", "进行", "通过", "使用",
    "用于", "用于", "以及", "等", "等", "其", "其中", "该", "这个", "这些",
    "一个", "一种", "一些", "上述", "下述", "如下", "例如", "比如",
    "不", "无", "非", "未", "若", "如果", "则", "那么", "即", "便", "都",
    # 英文
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "and", "or", "not", "but", "if", "then", "else", "for", "of", "to",
    "in", "on", "at", "by", "with", "from", "as", "into", "onto",
    "this", "that", "these", "those", "it", "its", "they", "them",
    "you", "your", "we", "our", "us", "i", "me", "my",
    "do", "does", "did", "done", "have", "has", "had",
    "will", "would", "can", "could", "should", "shall", "may", "might",
    "use", "used", "uses", "using", "example", "examples", "note", "notes",
}


def _split_camel(token: str) -> List[str]:
    """CamelCase 拆分：ArkUI -> [Ark, UI]；下移后归一为小写。"""
    if not token:
        return []
    # 先在大小写边界插入空格
    sub = _CAMEL_RE.sub(r"\1 \2", token)
    parts = [p for p in re.split(r"[\s_\-]+", sub) if p]
    out = []
    for p in parts:
        low = p.lower()
        if low:
            out.append(low)
    # 同时保留原始小写形式（ArkUI -> arkui），便于整词匹配
    whole = token.lower()
    if whole and whole not in out:
        out.append(whole)
    return out


def tokenize(text: str) -> List[str]:
    """中英文混合分词。

    - 英文：按非字母数字切分，再拆 CamelCase，统一小写
    - 中文：单字 + 二元组（bigram），解决中文无空格问题
    - 过滤停用词与单字符英文
    """
    if not text:
        return []
    tokens: List[str] = []

    # 1. 英文/数字 token
    for m in _WORD_RE.finditer(text):
        raw = m.group(0)
        for sub in _split_camel(raw):
            if len(sub) <= 1:
                continue
            if sub in _STOPWORDS:
                continue
            tokens.append(sub)

    # 2. 中文 token（单字 + bigram）
    cjk_chars = _CJK_RE.findall(text)
    if cjk_chars:
        for ch in cjk_chars:
            if ch in _STOPWORDS:
                continue
            tokens.append(ch)
        for i in range(len(cjk_chars) - 1):
            bigram = cjk_chars[i] + cjk_chars[i + 1]
            if bigram in _STOPWORDS:
                continue
            tokens.append(bigram)

    return tokens


# ----------------------------- frontmatter -----------------------------

def parse_frontmatter(content: str) -> Tuple[Dict[str, str], str]:
    """解析 YAML frontmatter，返回 (元数据字典, 去除 frontmatter 的正文)。"""
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = content[m.end():]
    meta: Dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and v:
            meta[k] = v
    return meta, body


def extract_path_segments(rel_path: str) -> str:
    """从相对路径中提取有意义的分段（去除扩展名与无意义目录词）。"""
    # 去扩展名
    no_ext = os.path.splitext(rel_path)[0]
    # 拆分
    parts = re.split(r"[\\/]+", no_ext)
    # 过滤空与无意义段
    skip = {"", ".", "harmonyos-guides", "harmonyos-references",
            "harmonyos-faqs", "best-practices", "harmonyos-releases"}
    return " ".join(p for p in parts if p and p not in skip)


# ----------------------------- 索引构建 -----------------------------

def build_index(force: bool = False) -> None:
    os.makedirs(INDEX_DIR, exist_ok=True)

    docs_path = os.path.join(INDEX_DIR, "docs.pkl")
    inverted_path = os.path.join(INDEX_DIR, "inverted.pkl")
    meta_path = os.path.join(INDEX_DIR, "meta.json")

    # 增量构建：若索引已存在且较新则跳过
    if not force and os.path.exists(meta_path) and os.path.exists(docs_path) \
            and os.path.exists(inverted_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            old_meta = json.load(f)
        old_built = old_meta.get("built_at_epoch", 0)
        # 找最新文件 mtime
        newest = 0
        for dp, _dn, fn in os.walk(REFERENCES_DIR):
            for f in fn:
                if f.endswith(".md"):
                    try:
                        newest = max(newest, os.path.getmtime(os.path.join(dp, f)))
                    except OSError:
                        pass
        if old_built >= newest:
            print(f"[skip] 索引已是最新（built_at={old_meta['built_at']}）。"
                  f"使用 --force 强制重建。")
            return

    t0 = time.time()
    documents: List[Dict] = []
    inverted: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    total_length = 0
    skipped = 0

    for dp, _dn, fn in os.walk(REFERENCES_DIR):
        for f in fn:
            if not f.endswith(".md"):
                continue
            if f in EXCLUDE_FILES:
                continue
            abs_path = os.path.join(dp, f)
            rel_path = os.path.relpath(abs_path, REFERENCES_DIR).replace("\\", "/")
            try:
                with open(abs_path, "r", encoding="utf-8", errors="replace") as fh:
                    content = fh.read()
            except OSError as e:
                print(f"[warn] 读取失败 {rel_path}: {e}", file=sys.stderr)
                skipped += 1
                continue

            meta, body = parse_frontmatter(content)
            title = meta.get("title", os.path.splitext(f)[0])
            breadcrumb = meta.get("breadcrumb", "")
            category = meta.get("category", rel_path.split("/")[0])
            url = meta.get("url", "")

            # 分词 + 加权
            tf_map: Dict[str, int] = defaultdict(int)
            for tok, w in (
                (tokenize(title), TITLE_WEIGHT),
                (tokenize(breadcrumb), BREADCRUMB_WEIGHT),
                (tokenize(extract_path_segments(rel_path)), PATH_WEIGHT),
                (tokenize(body), BODY_WEIGHT),
            ):
                for t in tok:
                    tf_map[t] += w

            doc_length = sum(tf_map.values())
            if doc_length == 0:
                skipped += 1
                continue

            doc_id = len(documents)
            documents.append({
                "id": doc_id,
                "path": rel_path,
                "title": title,
                "breadcrumb": breadcrumb,
                "category": category,
                "url": url,
                "length": doc_length,
            })
            total_length += doc_length

            for term, tf in tf_map.items():
                inverted[term].append((doc_id, tf))

    total_docs = len(documents)
    avg_doc_length = (total_length / total_docs) if total_docs else 0.0

    # 持久化
    with open(docs_path, "wb") as fh:
        pickle.dump(documents, fh, protocol=pickle.HIGHEST_PROTOCOL)
    # 倒排索引转为普通 dict 后再 dump
    inverted_plain = {k: v for k, v in inverted.items()}
    with open(inverted_path, "wb") as fh:
        pickle.dump(inverted_plain, fh, protocol=pickle.HIGHEST_PROTOCOL)

    meta = {
        "built_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "built_at_epoch": time.time(),
        "total_docs": total_docs,
        "avg_doc_length": round(avg_doc_length, 2),
        "vocabulary_size": len(inverted_plain),
        "k1": K1,
        "b": B,
        "title_weight": TITLE_WEIGHT,
        "breadcrumb_weight": BREADCRUMB_WEIGHT,
        "body_weight": BODY_WEIGHT,
        "path_weight": PATH_WEIGHT,
        "skipped": skipped,
        "references_dir": REFERENCES_DIR,
    }
    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)

    elapsed = time.time() - t0
    docs_size = os.path.getsize(docs_path) / 1024 / 1024
    inv_size = os.path.getsize(inverted_path) / 1024 / 1024
    print(f"[ok] 索引构建完成，耗时 {elapsed:.2f}s")
    print(f"     文档数: {total_docs}（跳过 {skipped}）")
    print(f"     平均文档长度: {avg_doc_length:.1f}")
    print(f"     词表大小: {len(inverted_plain)}")
    print(f"     docs.pkl     : {docs_size:.2f} MB")
    print(f"     inverted.pkl : {inv_size:.2f} MB")
    print(f"     meta.json    : {meta_path}")


def main() -> int:
    ap = argparse.ArgumentParser(description="构建 HarmonyOS SDK 文档 BM25 索引")
    ap.add_argument("--force", action="store_true", help="强制重建索引")
    args = ap.parse_args()
    build_index(force=args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())
