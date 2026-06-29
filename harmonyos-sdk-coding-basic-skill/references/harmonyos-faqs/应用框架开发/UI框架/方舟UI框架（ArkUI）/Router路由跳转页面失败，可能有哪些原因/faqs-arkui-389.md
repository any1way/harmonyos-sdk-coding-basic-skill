---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-389
title: Router路由跳转页面失败，可能有哪些原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Router路由跳转页面失败，可能有哪些原因
category: harmonyos-faqs
scraped_at: 2026-06-12T10:32:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6d6c2e44bf153cf6cc75acf34422d7541ac266f81bcb95d4bc719f8a68c7fd4e
---
**1.har包中的page，未使用命名路由跳转**

HAR包中不支持在配置文件中声明pages页面，但是可以包含page并通过命名路由跳转，可参考：[命名路由](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/页面路由 (@ohos.router)(不推荐)/arkts-routing.md#命名路由>)。

**2.import导入问题**

检查是否正确import目标页面，可以参考[命名路由](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/页面路由 (@ohos.router)(不推荐)/arkts-routing.md#命名路由>)的配置进行排查。
