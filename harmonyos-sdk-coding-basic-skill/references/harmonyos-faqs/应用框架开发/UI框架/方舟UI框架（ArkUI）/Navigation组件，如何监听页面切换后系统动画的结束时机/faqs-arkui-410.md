---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-410
title: Navigation组件，如何监听页面切换后系统动画的结束时机
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件，如何监听页面切换后系统动画的结束时机
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:40+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:8a697e3c614907aa609aafe5241488b9ee0b72746cbf54248198733e39b28333
---
**问题描述**

业务需要在Navigation的pop动画结束时进行操作，Navigation是否有对应的动画结束时机。

**解决措施**

Navigation进行pop操作时，退场页面会在动画结束时执行onDisappear生命周期，开发者可以在onDisappear()中进行逻辑处理。

**参考链接**

[页面生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面生命周期>)
