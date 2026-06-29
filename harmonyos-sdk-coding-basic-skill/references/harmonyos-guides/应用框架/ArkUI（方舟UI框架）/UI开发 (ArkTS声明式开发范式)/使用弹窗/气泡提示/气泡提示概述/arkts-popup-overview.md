---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-overview
title: 气泡提示概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 气泡提示 > 气泡提示概述
category: harmonyos-guides
scraped_at: 2026-06-01T11:05:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7e9894198a64daba82b545fa7e64d298e0048d5223e4866fd248f95cd8e6debb
---
气泡提示是一种用于给用户提供提示的弹窗，主要用于屏幕录制、信息弹出提醒等显示状态。

## 使用场景

| 接口 | 使用场景 |
| --- | --- |
| [气泡提示 (Popup)](../气泡提示（Popup）/arkts-popup-and-menu-components-popup.md) | 用于需要给指定的组件提示时，例如点击一个问号图标弹出一段帮助提示等。 |
| [不依赖UI组件的全局气泡提示 (openPopup)](<../不依赖UI组件的全局气泡提示 (openPopup)/arkts-popup-and-menu-components-uicontext-popup.md>) | 用于需要在无法直接访问UI组件的场景中给提示时，例如在事件回调中弹出一段帮助提示等。 |

## 规格约束

* Popup的弹出需要等待页面全部构建完成才能展示，因此[show](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/Popup控制/ts-universal-attributes-popup.md#bindpopup)不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。
* openPopup的弹出需要传入有效的[TargetInfo](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Interfaces (其他)/arkts-apis-uicontext-i.md#targetinfo18>)，否则无法弹出气泡。
* 其他规格约束，具体可参考[Popup控制](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/Popup控制/ts-universal-attributes-popup.md)、[openPopup](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (PromptAction)/arkts-apis-uicontext-promptaction.md#openpopup18>) 说明。
