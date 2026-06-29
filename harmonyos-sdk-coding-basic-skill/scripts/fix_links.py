#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复因 URL 含括号导致正则截断、未被替换的 Markdown 链接。

只处理 Markdown 链接 [text](url) 中的 url，不触动正文（如 source_url 元数据）。
读取 rename_plan.json 的 old_base→new_base 映射，重新扫描全量 .md 文件。
"""
from __future__ import annotations
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "references"))
LONG_ROOT = "\\\\?\\" + ROOT if os.name == "nt" else ROOT
PLAN_PATH = os.path.join(os.path.dirname(__file__), "rename_plan.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "fix_links.log")

# 改进的正则：支持 URL 内部含平衡括号（如 (CC++)、(ArkTS)）
# [^)\s(] 排除 ( ，避免吞掉括号导致截断
MD_LINK_RE = re.compile(
    r"\[(?P<text>[^\]]*)\]\((?P<url><[^>]+>|[^)\s(]*(?:\([^)]*\)[^)\s(]*)*)\)"
)


def main():
    if not os.path.isfile(PLAN_PATH):
        print(f"[error] 计划文件不存在: {PLAN_PATH}", file=sys.stderr)
        return 1

    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        plan = json.load(f)

    # 构建 basename 映射（按长度降序，避免子串误替换）
    rename_basename = {}
    for item in plan["renames"]:
        old_base = os.path.basename(item["old_path"])[:-3]  # 去 .md
        new_base = os.path.basename(item["new_path"])[:-3]
        rename_basename[old_base] = new_base
    sorted_bases = sorted(rename_basename.items(), key=lambda x: -len(x[0]))

    print(f"[info] 映射条目: {len(sorted_bases)}", flush=True)

    def replacer(m):
        text = m.group("text")
        url = m.group("url")
        new_url = url
        for old_base, new_base in sorted_bases:
            if old_base in new_url:
                new_url = new_url.replace(old_base, new_base)
                break
        if new_url != url:
            return f"[{text}]({new_url})"
        return m.group(0)

    log_lines = []
    edited_files = 0
    total_edits = 0
    processed = 0

    for dp, _dn, fns in os.walk(LONG_ROOT):
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            abs_p = os.path.join(dp, fn)
            try:
                with open(abs_p, "r", encoding="utf-8", errors="replace") as fh:
                    content = fh.read()
            except OSError:
                continue
            new_content, n = MD_LINK_RE.subn(replacer, content)
            if n > 0 and new_content != content:
                # 统计实际发生替换的链接数
                actual_edits = 0
                for m in MD_LINK_RE.finditer(content):
                    if m.group("url") != m.expand(replacer(m) and r"\1"):
                        pass
                # 简化：用 subn 的 n 作为编辑数
                try:
                    with open(abs_p, "w", encoding="utf-8") as fh:
                        fh.write(new_content)
                    edited_files += 1
                    total_edits += n
                    rel = abs_p.replace("\\\\?\\", "").replace(ROOT + os.sep, "").replace(ROOT + "/", "")
                    log_lines.append(f"[edit] {rel}: {n} 处链接")
                except OSError as e:
                    log_lines.append(f"[error] {abs_p}: {e}")
            processed += 1
            if processed % 2000 == 0:
                print(f"  ... 已处理 {processed} 个文件", flush=True)

    print(f"\n[ok] 已处理 {processed} 个文件", flush=True)
    print(f"[ok] 修改了 {edited_files} 个文件，共 {total_edits} 处链接", flush=True)

    log_lines.append(f"\n===== 修复摘要 =====")
    log_lines.append(f"已处理: {processed}")
    log_lines.append(f"修改文件: {edited_files}")
    log_lines.append(f"链接编辑: {total_edits}")
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"[ok] 日志: {LOG_PATH}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
