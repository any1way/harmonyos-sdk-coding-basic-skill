---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-259
title: 为什么vp2px、px2vp返回的结果不正确
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 为什么vp2px、px2vp返回的结果不正确
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:824b3e729a7b18b4b7f071df979d3917f389a47ce02609e31fa5486950159568
---
1. [vp2px](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#vp2px12>)、[px2vp](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#px2vp12>)是ArkUI的全局接口，该接口已被标记为废弃，不推荐使用。在应用启动阶段或非UI线程调用时，UI实例不明确，使用默认屏幕的虚拟像素比进行转换，可能导致转换后结果与预期不一致的情况。
2. UIContext的[vp2px](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#vp2px12>)、[px2vp](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#px2vp12>)为推荐的替代接口，能保证调用时UI实例已经创建，并返回正确的结果。

**参考链接**

[像素单位](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/像素单位/ts-pixel-units.md)
