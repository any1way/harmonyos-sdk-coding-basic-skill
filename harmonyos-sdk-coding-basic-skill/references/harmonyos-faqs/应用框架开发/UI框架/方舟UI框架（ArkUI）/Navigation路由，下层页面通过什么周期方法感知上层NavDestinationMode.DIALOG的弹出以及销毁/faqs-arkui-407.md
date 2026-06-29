---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-407
title: Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2e8580674fe8e2b7ca9b2aa3ea34e110fee330672eb91b213ef315237cc55d18
---
开发者可以使用observer对navDestination的生命周期进行统一管理，可参考：[on('navDestinationUpdate')](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIObserver)/arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11>)。

从API17开始，新增[onActive](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onactive17)、[onInactive](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#oninactive17)生命周期，dialog销毁、弹出时会分别触发下层页面的onActive、onInactive生命周期。
