---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-487
title: 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8307f6c1b415aee7123b1cc9ce1ca0335865a5bf411c9804e07b7f5454993c1f
---
**问题原理**

vp与px转换公式：px = vp \* 显示设备逻辑像素的密度。

ArkTS页面组件的尺寸单位通常会使用vp，当拖拽悬浮窗至扩展显示器时，组件的实际显示大小px会因为显示设备逻辑像素密度的改变而变化，此时如果不同步调整窗口大小，会导致悬浮窗布局出现异常。

**解决措施**

使用[on('densityUpdate')](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIObserver)/arkts-apis-uicontext-uiobserver.md#ondensityupdate12>)监听悬浮窗所处屏幕逻辑像素密度的变化，当其改变时，根据窗口原有vp，通过[resize](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#resize9>)接口调整悬浮窗实际大小（px），确保悬浮窗布局不出现异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/y48V3Gw5RPiLcqpbGvSXoQ/zh-cn_image_0000002533911659.png?HW-CC-KV=V1&HW-CC-Date=20260612T023403Z&HW-CC-Expire=86400&HW-CC-Sign=89F11FB056A66ED83ECF609CAE85DF14E52621F18432285D538EEB5FFDE00956 "点击放大")
