---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-overview
title: 绑定模态页面概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 绑定模态页面 > 绑定模态页面概述
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a51613468cde0a03d3189d714a6b36290aa04f15b360d7f8e53362147f432096
---
模态页面是一种大面板交互式的弹窗，和其他弹窗组件一样，通常用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作。相比于其他弹窗组件，模态页面的内容都需要开发者通过自定义组件来填充实现，可展示的视图往往也很大。默认需要用户进行交互才能够退出模态页面。ArkUI当前提供了**半模态**和**全模态**两类模态页面组件。

* **​半模态：​**开发者可以利用此模态页面实现多形态效果。支持不同宽度设备显示不同样式的半模态页面。允许用户通过侧滑，点击蒙层，点击关闭按钮，下拉关闭半模态页面。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/7vznIgpUR3y5MZjB1ZNHKw/zh-cn_image_0000002622697881.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063133Z&HW-CC-Expire=86400&HW-CC-Sign=46332ABF399C38046F0D684EDB3EC18AA8591170EB61407BBAA9F454A791647A)
* **全模态：​**开发者可以利用此模态页面实现全屏的模态弹窗效果。默认需要侧滑才能关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1aTrvpLJRFOv8ic_KMJQsQ/zh-cn_image_0000002592218320.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063133Z&HW-CC-Expire=86400&HW-CC-Sign=BA8878BF30571688FA7E00AD4B1DE00B7B9605298DD5A8DF65C97FD77229FDD9)

## 使用场景

| 接口 | 使用场景 |
| --- | --- |
| [bindContentCover](../绑定全模态页面（bindContentCover）/arkts-contentcover-page.md) | 用于自定义全屏的模态展示界面，结合转场动画和共享元素动画可实现复杂转场动画效果，如缩略图片点击后查看大图。 |
| [bindSheet](../绑定半模态页面（bindSheet）/arkts-sheet-page.md) | 用于半模态展示界面，如分享框。 |
| [openBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#openbindsheet12>)/ [updateBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#updatebindsheet12>)/ [closeBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#closebindsheet12>) | 用于不依赖UI组件的场景，如全局拉起、更新、关闭。 |

## 规格约束

* 建议使用UIContext中的弹窗方法。其他规格约束可参考[openBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#openbindsheet12>)、[updateBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#updatebindsheet12>)、[closeBindSheet](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#closebindsheet12>)说明。
