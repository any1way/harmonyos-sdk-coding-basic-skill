---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-236
title: 如何正确获取刘海区域的高度，topRect中的取值是height、top还是height+top
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何正确获取刘海区域的高度，topRect中的取值是height、top还是height+top
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2d193c9be679f8b6b61e6eafc3cb2726c764f50cb7ce750359c28f03b181377d
---
通过Window.getWindowAvoidArea()方法获取刘海的高度。在topRect中，top表示刘海屏原点（矩形左上角）距离屏幕顶端的像素值，left表示距屏幕左侧的像素值，width和height分别表示刘海屏所在外包矩形的宽度和高度。根据这些值进行计算，并以实际效果为准。

**参考链接**

[getWindowAvoidArea](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getwindowavoidarea9>)

[AvoidArea](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#avoidarea7>)

[Rect](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#rect7>)
