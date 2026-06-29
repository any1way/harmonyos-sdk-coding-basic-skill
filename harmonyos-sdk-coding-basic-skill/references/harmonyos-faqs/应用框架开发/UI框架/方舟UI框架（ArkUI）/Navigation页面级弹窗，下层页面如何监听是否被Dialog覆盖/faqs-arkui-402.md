---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-402
title: Navigation页面级弹窗，下层页面如何监听是否被Dialog覆盖
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation页面级弹窗，下层页面如何监听是否被Dialog覆盖
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:30+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:c4f19ac1d074309f8a8f71f3ece48ecec1c94beba5c6579618bf6e73e51ad7d9
---
可以通过[Class (UIObserver)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIObserver)/arkts-apis-uicontext-uiobserver.md>)监听[NavDestination](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md)组件的生命周期。生命周期可以参考下方文档。从API17开始，新增onActive、onInactive生命周期，在Dialog弹出、销毁时会分别触发下层页面的onInactive、onActive生命周期。

**参考链接**

[页面生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面生命周期>)
