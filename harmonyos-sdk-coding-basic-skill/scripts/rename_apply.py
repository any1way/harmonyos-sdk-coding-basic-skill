#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""执行长文件名重命名 + 链接引用更新。

流程：
1. 读取 rename_plan.json
2. 重命名 111 个文件
3. 遍历所有 .md 文件，用正则替换链接 url 中的旧 basename 为新 basename
4. 输出执行报告

安全策略：
- 文件重命名用 \\?\ 前缀处理长路径
- 链接替换只在 markdown 链接 url 中进行，不误伤正文
- basename 按长度降序处理，避免子串误替换
- 记录完整变更日志，便于回退
"""
from __future__ import annotations
import json
import os
import re
import sys
import shutil
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "references"))
LONG_ROOT = "\\\\?\\" + ROOT if os.name == "nt" else ROOT
PLAN_PATH = os.path.join(os.path.dirname(__file__), "rename_plan.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "rename_apply.log")

# 与 rename_plan.py 一致的链接正则
# 支持 URL 内部含平衡括号（如 (CC++)、(ArkTS)）和尖括号包裹两种格式
# [^)\s(] 排除 ( ，避免吞掉括号导致截断
MD_LINK_RE = re.compile(
    r"\[(?P<text>[^\]]*)\]\((?P<url><[^>]+>|[^)\s(]*(?:\([^)]*\)[^)\s(]*)*)\)"
)


def to_long_path(p: str) -> str:
    r"""加 \\?\ 前缀以支持长路径。"""
    if os.name == "nt" and not p.startswith("\\\\?\\"):
        return "\\\\?\\" + os.path.abspath(p)
    return p


def main():
    if not os.path.isfile(PLAN_PATH):
        print(f"[error] 计划文件不存在: {PLAN_PATH}", file=sys.stderr)
        return 1

    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        plan = json.load(f)

    renames = plan["renames"]
    print(f"[info] 待重命名文件数: {len(renames)}", flush=True)

    # 构建 basename 映射（按长度降序，避免子串误替换）
    rename_basename = {}
    for item in renames:
        old_base = os.path.basename(item["old_path"])
        new_base = os.path.basename(item["new_path"])
        rename_basename[old_base] = new_base
    sorted_bases = sorted(rename_basename.items(), key=lambda x: -len(x[0]))

    log_lines = []

    # ---- 步骤 1：重命名文件 ----
    print(f"\n[step 1] 重命名 {len(renames)} 个文件 ...", flush=True)
    renamed_count = 0
    rename_errors = []
    for item in renames:
        old_full = os.path.join(ROOT, item["old_path"])
        new_full = os.path.join(ROOT, item["new_path"])
        old_long = to_long_path(old_full)
        new_long = to_long_path(new_full)
        try:
            if not os.path.exists(old_long):
                rename_errors.append((item["old_path"], "源文件不存在"))
                continue
            os.rename(old_long, new_long)
            renamed_count += 1
            log_lines.append(f"RENAME: {item['old_path']} -> {item['new_path']}")
        except OSError as e:
            rename_errors.append((item["old_path"], str(e)))
    print(f"[ok] 成功重命名: {renamed_count}/{len(renames)}", flush=True)
    if rename_errors:
        print(f"[warn] 重命名失败: {len(rename_errors)} 个", flush=True)
        for p, e in rename_errors[:5]:
            print(f"  - {p}: {e}", flush=True)
            log_lines.append(f"RENAME_FAIL: {p} | {e}")

    # ---- 步骤 2：更新所有 .md 文件中的链接引用 ----
    print(f"\n[step 2] 扫描并更新 .md 文件中的链接引用 ...", flush=True)

    def make_replacer():
        def replacer(m):
            text = m.group("text")
            url = m.group("url")
            new_url = url
            for old_base, new_base in sorted_bases:
                if old_base in new_url:
                    new_url = new_url.replace(old_base, new_base)
                    break  # 一个 url 只含一个 basename
            if new_url != url:
                return f"[{text}]({new_url})"
            return m.group(0)
        return replacer

    replacer = make_replacer()
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
            original = content
            # 统计替换次数
            edits = 0
            def counting_replacer(m):
                nonlocal edits
                result = replacer(m)
                if result != m.group(0):
                    edits += 1
                return result
            content = MD_LINK_RE.sub(counting_replacer, content)
            if content != original:
                try:
                    with open(abs_p, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    edited_files += 1
                    total_edits += edits
                    rel = abs_p.replace("\\\\?\\", "").replace(ROOT + os.sep, "").replace(ROOT + "/", "")
                    log_lines.append(f"EDIT: {rel} ({edits} edits)")
                except OSError as e:
                    print(f"[warn] 写入失败: {abs_p}: {e}", flush=True)
            processed += 1
            if processed % 2000 == 0:
                print(f"  ... 已处理 {processed} 个文件", flush=True)

    print(f"[ok] 已处理 {processed} 个 .md 文件", flush=True)
    print(f"[ok] 修改了 {edited_files} 个文件，共 {total_edits} 处链接", flush=True)

    # ---- 输出日志 ----
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(f"=== 重命名执行日志 ===\n")
        f.write(f"成功重命名: {renamed_count}/{len(renames)}\n")
        f.write(f"重命名失败: {len(rename_errors)}\n")
        f.write(f"修改文件数: {edited_files}\n")
        f.write(f"链接编辑点: {total_edits}\n\n")
        f.write("\n".join(log_lines))
    print(f"\n[ok] 日志已写入: {LOG_PATH}", flush=True)

    print(f"\n===== 执行摘要 =====")
    print(f"重命名: {renamed_count}/{len(renames)} 成功")
    print(f"链接更新: {edited_files} 个文件, {total_edits} 处")
    print(f"失败: {len(rename_errors)} 个")
    print(f"\n[下一步] 请重建索引:")
    print(f"  python scripts/build_index.py        # BM25 索引")
    print(f"  python scripts/build_dense_index.py  # Dense 索引")

    return 0 if not rename_errors else 2


if __name__ == "__main__":
    sys.exit(main())
