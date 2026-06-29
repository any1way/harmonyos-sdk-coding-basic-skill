---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-240
title: 创建subwindow默认是否铺满全屏，铺满全屏时如何隐藏状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 创建subwindow默认是否铺满全屏，铺满全屏时如何隐藏状态栏
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:89ffe02573e4c5a076722de4ddcabb8aa8cf2dffa16585aeae7536d879157de9
---
子窗口默认不铺满全屏。要设置窗口全屏模式时状态栏的可见模式，需调用setWindowSystemBarEnable方法，此方法必须由主窗口调用。

**参考链接**

[setWindowSystemBarEnable](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowsystembarenable9>)
