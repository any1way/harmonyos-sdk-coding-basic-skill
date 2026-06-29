---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-419
title: Navigation页面接收参数一般推荐在什么生命周期接收
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation页面接收参数一般推荐在什么生命周期接收
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:52+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:fcc23ea92de4168dbf813a4d0d41845f5a3c6dc45d9260032c88a6964a5cfe57
---
* 页面新创建时，推荐在NavDestination的[onReady](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onready11)生命周期中处理参数。
* API18及以下版本，单实例跳转场景需要开发者自行管理参数。
* 当同时实现onReady和onNewParam时，API version 19及以上版本会优先触发[onNewParam](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onnewparam19)回调。
