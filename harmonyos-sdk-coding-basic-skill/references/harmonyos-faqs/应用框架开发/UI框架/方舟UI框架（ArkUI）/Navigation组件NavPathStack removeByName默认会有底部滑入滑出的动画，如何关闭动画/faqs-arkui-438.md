---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-438
title: Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:41ed95dbcac7fe618de60124eea5a5d3e5bb41d0cb5b9f3dc0ad7477a281e740
---
开发者可设置NavPathStack上的接口[disableAnimation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#disableanimation11)为true来关闭路由的跳转动画，disableAnimation同时控制removeByName等路由操作的动画开关。示例代码如下：

```
1. this.pageStack.disableAnimation(true);
```
