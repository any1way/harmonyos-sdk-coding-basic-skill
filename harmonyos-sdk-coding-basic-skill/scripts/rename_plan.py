#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成长文件名重命名计划 + 链接引用影响面分析。

流程：
1. 扫描 references/ 下所有 .md 文件，找出基名 > 50 字符的长文件名
2. 应用缩短规则，生成新名（≤50 字符）
3. 检测新名冲突
4. 扫描所有 .md 文件内的 Markdown 链接 [text](path.md)，找出引用了长文件的位置
5. 输出 plan.json（重命名映射 + 链接更新清单）+ 人类可读摘要
"""
from __future__ import annotations
import json
import os
import re
import sys
from collections import defaultdict, Counter
from urllib.parse import unquote

ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "references"))
LONG_ROOT = "\\\\?\\" + ROOT if os.name == "nt" else ROOT
NAME_THRESHOLD = 50


# ----------------------------- 缩短规则 -----------------------------

# 规则表：按优先级匹配，第一条匹配的规则生效
# 每条规则：(regex_pattern, replacement, rule_name)
# 分为两批：PRIMARY（首轮去重前缀/中段）、SECONDARY（二次清理仍超阈值的名）
PRIMARY_RULES = [
    # 规则A：capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-XXX → capi-nxcomp-XXX
    (r"^capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-",
     "capi-nxcomp-", "A:去重前缀nxcomp"),
    (r"^capi-oh-nativexcomponent-native-xcomponent-oh-arkui-",
     "capi-nxcomp-arkui-", "A:去重前缀nxcomp-arkui"),
    (r"^capi-oh-nativexcomponent-native-xcomponent-",
     "capi-nxcomp-", "A:去重前缀nxcomp"),
    # 规则B：capi-arkui-nativemodule-XXX → capi-arkui-XXX
    (r"^capi-arkui-nativemodule-",
     "capi-arkui-", "B:去中段nativemodule"),
    # 规则B2：capi-image-nativemodule-XXX → capi-image-XXX
    (r"^capi-image-nativemodule-",
     "capi-image-", "B:去中段nativemodule"),
    # 规则C：accessibility → a11y
    (r"^capi-arkui-accessibility-",
     "capi-arkui-a11y-", "C:a11y缩写"),
    # 规则D：capi-huksexternalcryptotypeapi-oh-huks-external-XXX → capi-huks-XXX
    (r"^capi-huksexternalcryptotypeapi-oh-huks-external-",
     "capi-huks-", "D:去重前缀huks"),
    (r"^capi-huksexternalcryptotypeapi-",
     "capi-huks-", "D:去重前缀huks"),
    # 规则E：capi-avmetadataextractor-oh-avmetadataextractor-XXX → capi-avmeta-XXX
    (r"^capi-avmetadataextractor-oh-avmetadataextractor-",
     "capi-avmeta-", "E:去重前缀avmeta"),
    (r"^capi-avmetadataextractor-",
     "capi-avmeta-", "E:去重前缀avmeta"),
    # 规则F：capi-avscreencapture-oh-avscreencapture-XXX → capi-avscreencap-XXX
    (r"^capi-avscreencapture-oh-avscreencapture-",
     "capi-avscreencap-", "F:去重前缀avscreencap"),
    (r"^capi-avscreencapture-",
     "capi-avscreencap-", "F:去重前缀avscreencap"),
    # 规则G：capi-ohaudiosuite-oh-audiosuite-XXX → capi-ohaudiosuite-XXX
    (r"^capi-ohaudiosuite-oh-audiosuite-",
     "capi-ohaudiosuite-", "G:去重前缀ohaudiosuite"),
    # 规则H：capi-scsiperipheralddk-scsiperipheral-XXX → capi-scsiperiph-XXX
    (r"^capi-scsiperipheralddk-scsiperipheral-",
     "capi-scsiperiph-", "H:去重前缀scsiperiph"),
    # 规则I：capi-nativedisplaysoloist-displaysoloist-XXX → capi-nativedisp-XXX
    (r"^capi-nativedisplaysoloist-displaysoloist-",
     "capi-nativedisp-", "I:去重前缀nativedisp"),
    (r"^capi-nativecolorspacemanager-oh-",
     "capi-nativecsm-oh-", "I:去重前缀nativecsm"),
    (r"^capi-nativedisplaymanager-",
     "capi-nativedisp-", "I:去重前缀nativedisp"),
    # 规则J：capi-windowmanager-windowmanager-XXX → capi-winmgr-XXX
    (r"^capi-windowmanager-windowmanager-",
     "capi-winmgr-", "J:去重前缀winmgr"),
    # 规则K：capi-oh-nativebuffer-oh-nativebuffer-XXX → capi-oh-nativebuffer-XXX
    (r"^capi-oh-nativebuffer-oh-nativebuffer-",
     "capi-oh-nativebuffer-", "K:去重前缀"),
    (r"^capi-ohavsession-oh-avsession-",
     "capi-ohavsession-", "K:去重前缀"),
    # 规则M：capi-drawing-oh-drawing-XXX → capi-drawing-XXX
    (r"^capi-drawing-oh-drawing-",
     "capi-drawing-", "M:去重前缀"),
    # ---- 第二批：覆盖原 35 个无规则匹配项 ----
    # 规则N：notification-XXX-extension-ability-development-steps → notification-XXX-ext-ability-steps
    (r"^(notification-[a-z]+)-extension-ability-development-steps$",
     r"\1-ext-ability-steps", "N:notif-ext-steps"),
    # 规则O：use-jsvm-XXX-debugger-XXX → use-jsvm-debugger-XXX
    (r"^use-jsvm-[a-z]+-debugger-",
     "use-jsvm-debugger-", "O:jsvm-debugger"),
    # 规则P：crypto-convert-compressed-or-uncompressed-ecc-XXX → crypto-convert-ecc-XXX
    (r"^crypto-convert-compressed-or-uncompressed-ecc-",
     "crypto-convert-ecc-", "P:crypto-ecc"),
    # 规则Q：arkts-ui-widget-event-formeditextensionability-overview → arkts-widget-event-formedit-overview
    (r"^arkts-ui-widget-event-formeditextensionability-",
     "arkts-widget-event-formedit-", "Q:arkts-widget"),
    # 规则R：js-apis-inner-application-XXX → js-apis-app-XXX
    (r"^js-apis-inner-application-",
     "js-apis-app-", "R:js-apis-app"),
    # 规则S：js-apis-inner-notification-XXX → js-apis-notif-XXX
    (r"^js-apis-inner-notification-",
     "js-apis-notif-", "S:js-apis-notif"),
    # 规则T：capi-cryptoasymkeyapi-oh-XXX → capi-crypto-oh-XXX
    (r"^capi-cryptoasymkeyapi-oh-",
     "capi-crypto-oh-", "T:capi-crypto"),
    # 规则T2：capi-cryptoasymcipherapi-oh-XXX → capi-crypto-oh-XXX
    (r"^capi-cryptoasymcipherapi-oh-",
     "capi-crypto-oh-", "T:capi-crypto"),
    # 规则U：guidance-on-ndk-libc-interfaces-affected-by-permissions → guidance-ndk-libc-permissions
    (r"^guidance-on-ndk-libc-interfaces-affected-by-permissions$",
     "guidance-ndk-libc-permissions", "U:guidance-ndk"),
    # 规则V：capi-native-bundle-oh-nativebundle-XXX → capi-native-bundle-XXX
    (r"^capi-native-bundle-oh-nativebundle-",
     "capi-native-bundle-", "V:native-bundle"),
    # 规则W：arkts-basic-components-web-XXX → arkts-web-XXX
    (r"^arkts-basic-components-web-",
     "arkts-web-", "W:arkts-web"),
    # 规则X：capi-vulkan-vkXXXpropertiesohos → capi-vulkan-XXXpropsohos
    (r"^capi-vulkan-vk([a-z]+)propertiesohos",
     r"capi-vulkan-vk\1propsohos", "X:vulkan-props"),
    # 规则Y：ui-design-visual-effect-background-XXX → ui-design-bg-XXX
    (r"^ui-design-visual-effect-background-",
     "ui-design-bg-", "Y:ui-design-bg"),
    # 规则Z：ts-universal-attributes-attribute-XXX → ts-attr-XXX
    (r"^ts-universal-attributes-attribute-",
     "ts-attr-", "Z:ts-attr"),
    # 规则AA：enterprisethreatprotection-virusremediation-XXX → etp-virusremediation-XXX
    (r"^enterprisethreatprotection-virusremediation-",
     "etp-virusremediation-", "AA:etp-vr"),
    # 规则AB：huks-extension-registration-and-unregistration-arkts → huks-ext-reg-unreg-arkts
    (r"^huks-extension-registration-and-unregistration-",
     "huks-ext-reg-unreg-", "AB:huks-ext"),
    # 规则AC：capi-jsvm-jsvm-XXX → capi-jsvm-XXX
    (r"^capi-jsvm-jsvm-",
     "capi-jsvm-", "AC:jsvm"),
    # 规则AD：capi-imageprocessing-imageprocessing-XXX → capi-imgproc-XXX
    (r"^capi-imageprocessing-imageprocessing-",
     "capi-imgproc-", "AD:imgproc"),
    # 规则AE：js-apis-application-enterpriseadminextensioncontext → js-apis-app-enterpriseadminextctx
    (r"^js-apis-application-enterpriseadminextensioncontext$",
     "js-apis-app-enterpriseadminextctx", "AE:entadmin"),
    # 规则AF：capi-lowpowerXXXsink-oh-lowpowerXXXsinkcallback → capi-lowpowerXXXsink-callback
    (r"^capi-(lowpower[a-z]+sink)-oh-\1callback$",
     r"capi-\1-callback", "AF:lowpower-cb"),
    # 规则AG：capi-videoprocessing-videoprocessing-XXX → capi-videoproc-XXX
    (r"^capi-videoprocessing-videoprocessing-",
     "capi-videoproc-", "AG:videoproc"),
    # 规则AH：js-apis-inner-notificationextensionsubscriptioninfo → js-apis-notif-extsubinfo
    (r"^js-apis-inner-notificationextensionsubscriptioninfo$",
     "js-apis-notif-extsubinfo", "AH:notif-extsub"),
    # 规则AI：arkts-interaction-development-guide-XXX → arkts-interaction-XXX
    (r"^arkts-interaction-development-guide-",
     "arkts-interaction-", "AI:arkts-interaction"),
]

# 二次清理规则：当首轮缩短后仍超阈值时，对结果再做去重/缩写
SECONDARY_RULES = [
    # 去重 capi-arkui-arkui-XXX → capi-arkui-XXX
    (r"^capi-arkui-arkui-",
     "capi-arkui-", "S1:去重arkui"),
    # 去重 capi-arkui-oh-arkui-XXX → capi-arkui-XXX
    (r"^capi-arkui-oh-arkui-",
     "capi-arkui-", "S2:去重oh-arkui"),
    # 缩写 animationcontroller → animctrl
    (r"animationcontroller",
     "animctrl", "S3:animctrl"),
    # 缩写 styledstringcontroller → styledstringctrl
    (r"styledstringcontroller",
     "styledstringctrl", "S4:styledstringctrl"),
    # 缩写 textcascadepickerrangecontentarray → textcascadepickerrange
    (r"textcascadepickerrangecontentarray",
     "textcascadepickerrange", "S5:pickerrange"),
    # 缩写 accessibilityprovidercallbacks → providercallbacks
    (r"accessibilityprovidercallbacks",
     "providercallbacks", "S6:providercallbacks"),
]


def shorten_name(name: str) -> tuple[str, str] | None:
    """返回 (新名, 规则名)；若无规则匹配返回 None。

    支持多轮应用：
    1. 首轮用 PRIMARY_RULES
    2. 若结果仍超阈值，用 SECONDARY_RULES 清理
    3. 若首轮无匹配，也尝试用 SECONDARY_RULES（处理之前已缩短但仍超阈值的名）
    """
    applied_rules = []
    current = name
    matched_primary = False
    # 首轮
    for pat, repl, rule in PRIMARY_RULES:
        if re.match(pat, current):
            current = re.sub(pat, repl, current)
            applied_rules.append(rule)
            matched_primary = True
            break
    # 二次清理（首轮匹配后仍超阈值，或首轮无匹配但本身超阈值）
    if len(current) > NAME_THRESHOLD:
        for pat, repl, rule in SECONDARY_RULES:
            if re.search(pat, current):
                new_current = re.sub(pat, repl, current)
                if new_current != current:
                    current = new_current
                    applied_rules.append(rule)
                    if len(current) <= NAME_THRESHOLD:
                        break
    if current == name:
        return None  # 无任何规则匹配
    return current, "+".join(applied_rules) if applied_rules else "S:二次清理"


# ----------------------------- 扫描 -----------------------------

def scan_files(root: str):
    """返回 [(abs_path, rel_path, base, ext), ...] 全部 .md 文件。"""
    files = []
    for dp, _dn, fns in os.walk(root):
        for f in fns:
            if not f.endswith(".md"):
                continue
            abs_p = os.path.join(dp, f)
            rel_p = os.path.relpath(abs_p, root)
            base, ext = os.path.splitext(f)
            files.append((abs_p, rel_p, base, ext))
    return files


def find_long_files(files):
    """返回 [(abs, rel, base, ext), ...] 中 base 长度 > 阈值的。"""
    return [f for f in files if len(f[2]) > NAME_THRESHOLD]


def build_rename_map(long_files):
    """构建 {原rel_path: 新rel_path}，并检测冲突。"""
    rename_map = {}
    new_name_counter = Counter()
    unmatched = []
    for abs_p, rel_p, base, ext in long_files:
        result = shorten_name(base)
        if result is None:
            unmatched.append((rel_p, base, ext))
            continue
        new_base, rule = result
        # 如果缩短后仍超阈值，标记但不二次处理
        new_rel = os.path.join(os.path.dirname(rel_p), new_base + ext)
        rename_map[rel_p] = (new_rel, rule, len(base), len(new_base))
        new_name_counter[new_rel] += 1
    conflicts = {k: v for k, v in new_name_counter.items() if v > 1}
    return rename_map, conflicts, unmatched


# ----------------------------- 链接引用扫描 -----------------------------

# Markdown 链接正则：[text](url)  其中 url 以 .md 结尾或含 .md#
# 支持两种格式：[text](path) 和 [text](<path with space>)
# 支持 URL 内部含平衡括号（如 (CC++)、(ArkTS)）
# [^)\s(] 排除 ( ，避免吞掉括号导致截断
MD_LINK_RE = re.compile(
    r"\[(?P<text>[^\]]*)\]\((?P<url><[^>]+>|[^)\s(]*(?:\([^)]*\)[^)\s(]*)*)\)"
)


def normalize_link_target(url: str, current_rel_path: str) -> str | None:
    """把链接 url 解析为相对于 references/ 根的相对路径（正斜杠）。
    只处理 .md 链接，跳过 http、锚点、非 md。"""
    if url.startswith(("http://", "https://", "mailto:", "#")):
        return None
    # 去掉尖括号包裹（GitHub 风格：<path with space>）
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1]
    # 去 fragment
    path = url.split("#", 1)[0]
    if not path.endswith(".md"):
        return None
    # URL 解码（中文路径）
    path = unquote(path)
    # 解析为相对于 current_rel_path 所在目录的路径
    cur_dir = os.path.dirname(current_rel_path)
    target = os.path.normpath(os.path.join(cur_dir, path)).replace("\\", "/")
    return target


def scan_link_references(files, rename_keys_set):
    """扫描所有 .md 文件中的链接，返回引用了待重命名文件的清单。

    返回 {原rel_path: [(引用方rel_path, 行号, 原始url, 链接文本), ...]}
    """
    # 统一用正斜杠比较（rename_keys_set 可能是反斜杠）
    rename_keys_posix = {k.replace("\\", "/"): k for k in rename_keys_set}
    refs = defaultdict(list)
    for abs_p, rel_p, _base, _ext in files:
        try:
            with open(abs_p, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
        except OSError:
            continue
        for lineno, line in enumerate(content.splitlines(), 1):
            for m in MD_LINK_RE.finditer(line):
                url = m.group("url")
                text = m.group("text")
                target = normalize_link_target(url, rel_p)
                if target is None:
                    continue
                if target in rename_keys_posix:
                    orig_key = rename_keys_posix[target]
                    refs[orig_key].append((rel_p, lineno, url, text))
    return refs


# ----------------------------- 主流程 -----------------------------

def main():
    if not os.path.isdir(ROOT):
        print(f"[error] references 目录不存在: {ROOT}", file=sys.stderr)
        return 1

    print(f"[info] 扫描 references/ ...", flush=True)
    all_files = scan_files(LONG_ROOT)
    print(f"[info] 总 .md 文件数: {len(all_files)}", flush=True)

    long_files = find_long_files(all_files)
    print(f"[info] 长文件名（基名>{NAME_THRESHOLD}）: {len(long_files)}", flush=True)

    rename_map, conflicts, unmatched = build_rename_map(long_files)
    print(f"[info] 可应用规则缩短: {len(rename_map)}", flush=True)
    print(f"[info] 无规则匹配（需个案）: {len(unmatched)}", flush=True)
    print(f"[info] 新名冲突: {len(conflicts)}", flush=True)

    # 检查缩短后仍超阈值的
    still_long = [(k, v) for k, v in rename_map.items() if v[3] > NAME_THRESHOLD]
    print(f"[info] 缩短后仍超阈值: {len(still_long)}", flush=True)

    # 扫描链接引用
    print(f"[info] 扫描 .md 文件内链接引用 ...", flush=True)
    rename_keys_set = set(rename_map.keys())
    refs = scan_link_references(all_files, rename_keys_set)
    total_ref_edits = sum(len(v) for v in refs.values())
    referenced_count = len(refs)
    print(f"[info] 被引用的长文件: {referenced_count}/{len(rename_map)}", flush=True)
    print(f"[info] 链接引用总编辑点: {total_ref_edits}", flush=True)

    # 输出 plan.json
    plan = {
        "threshold": NAME_THRESHOLD,
        "total_files": len(all_files),
        "long_files_count": len(long_files),
        "rename_count": len(rename_map),
        "unmatched_count": len(unmatched),
        "conflicts_count": len(conflicts),
        "still_long_count": len(still_long),
        "referenced_count": referenced_count,
        "total_link_edits": total_ref_edits,
        "renames": [
            {
                "old_path": old,
                "new_path": new,
                "rule": rule,
                "old_len": old_len,
                "new_len": new_len,
                "referenced": old in refs,
                "ref_count": len(refs.get(old, [])),
            }
            for old, (new, rule, old_len, new_len) in sorted(
                rename_map.items(), key=lambda kv: -kv[1][2])
        ],
        "unmatched": [
            {"path": p, "base": b, "ext": e, "len": len(b)}
            for p, b, e in sorted(unmatched, key=lambda x: -len(x[1]))
        ],
        "conflicts": list(conflicts.items()),
        "still_long": [
            {"path": old, "new": new, "rule": rule, "new_len": nl}
            for old, (new, rule, _ol, nl) in still_long
        ],
        "link_references": {
            old: [{"from": f, "line": ln, "url": u, "text": t}
                  for f, ln, u, t in refs[old]]
            for old in refs
        },
    }
    plan_path = os.path.join(os.path.dirname(__file__), "rename_plan.json")
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    print(f"\n[ok] 计划已输出: {plan_path}", flush=True)

    # 人类可读摘要
    print("\n===== 摘要 =====")
    print(f"待重命名: {len(rename_map)} 个文件")
    print(f"  - 规则A(去重前缀): {sum(1 for _,v in rename_map.items() if v[1].startswith('A'))}")
    print(f"  - 规则B(去中段nativemodule): {sum(1 for _,v in rename_map.items() if v[1].startswith('B'))}")
    print(f"  - 规则C(a11y): {sum(1 for _,v in rename_map.items() if v[1].startswith('C'))}")
    print(f"  - 规则D-M(其他去重): {sum(1 for _,v in rename_map.items() if v[1][0] in 'DEFGHIJKM')}")
    print(f"无规则匹配(需个案): {len(unmatched)} 个")
    print(f"新名冲突: {len(conflicts)} 个")
    print(f"缩短后仍超阈值: {len(still_long)} 个")
    print(f"链接编辑点: {total_ref_edits} 处（分布于 {referenced_count} 个被引用文件）")

    # 输出前 20 条重命名预览
    print("\n===== 前 20 条重命名预览 =====")
    for item in plan["renames"][:20]:
        print(f"  [{item['old_len']}→{item['new_len']}] {item['rule']}")
        print(f"    原: {item['old_path']}")
        print(f"    新: {item['new_path']}")
        print(f"    引用: {item['ref_count']} 处")

    if unmatched:
        print("\n===== 无规则匹配的前 10 条（需个案）=====")
        for p, b, e in unmatched[:10]:
            print(f"  [{len(b)}] {p}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
