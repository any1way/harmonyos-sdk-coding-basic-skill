---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-417
title: NavDestinationMode.DIALOG模式下，如何针对弹窗内容或者背景遮罩做转场动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > NavDestinationMode.DIALOG模式下，如何针对弹窗内容或者背景遮罩做转场动效
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0250a68b94dcb405c2391dd9b5051fb63cdffc01141905ca2f04ea782aadc9a9
---
**问题背景**

开发者对默认dialog动画不满意或需自定义转场动画。

**解决措施**

* 如对默认dialog动画不满意，开发者可以为NavDestination页面设置[systemTransition](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#systemtransition14)属性为SLIDE\_RIGHT（从右侧划入）、SLIDE\_BOTTOM（从底部划入）等转场效果。
* 如需自定义动画可以为NavDestination页面设置[customTransition](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#customtransition15)属性。

**参考链接**

[示例2（设置NavDestination自定义转场）](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#示例2设置navdestination自定义转场)

[示例3（设置指定的NavDestination系统转场）](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#示例3设置指定的navdestination系统转场)
