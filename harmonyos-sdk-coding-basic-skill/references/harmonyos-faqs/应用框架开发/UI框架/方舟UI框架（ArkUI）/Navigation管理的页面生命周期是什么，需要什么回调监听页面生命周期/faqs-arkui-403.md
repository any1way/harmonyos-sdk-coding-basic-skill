---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-403
title: Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:32+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:285ee9cf23b5f672ad5d76d81330703d30257a896ed44cc5ac9581beb1501f6e
---
Navigation组件作为路由容器的实现，其生命周期承载在[NavDestination](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md)组件上，以组件事件的形式开放。Navigation管理的页面生命周期包括onAppear（通用生命周期事件）、onShown（NavDestination组件布局显示之后执行）、onActive（NavDestination处于激活态触发）等等，具体可参考下方文档。可以通过[Class (UIObserver)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIObserver)/arkts-apis-uicontext-uiobserver.md>)监听NavDestination组件的生命周期。

**参考链接**

[组件导航(Navigation) (推荐)](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/arkts-navigation-navigation.md>)

[页面生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面生命周期>)
