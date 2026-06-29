---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-463
title: customDialog里面页面跳转后，页面显示在弹窗下面，怎么调整
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > customDialog里面页面跳转后，页面显示在弹窗下面，怎么调整
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:33+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:7a2672a684eeefff1c08fd926e36f81c1786255a91e2c4fc09de649ca845547b
---
**解决措施**

当前ArkUI弹出框默认为非页面级弹出框。在页面路由跳转时若未主动调用close方法，弹出框将不会自动关闭。若需实现在跳转页面时覆盖弹出框的场景，可以使用组件导航子页面显示类型的弹窗类型（适用于需要保持导航栈关系的场景）或者页面级弹出框（适用于需要全屏模态覆盖的场景）。

**参考链接**

[页面显示类型](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面显示类型>)

[页面级弹出框](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/使用弹窗/弹出框 (Dialog)/页面级弹出框/arkts-embedded-dialog.md>)
