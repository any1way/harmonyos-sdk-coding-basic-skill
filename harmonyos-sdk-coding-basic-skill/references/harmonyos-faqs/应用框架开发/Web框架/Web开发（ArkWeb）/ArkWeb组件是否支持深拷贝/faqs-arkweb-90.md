---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-90
title: ArkWeb组件是否支持深拷贝
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > ArkWeb组件是否支持深拷贝
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3b1295553499023e56fa8c74b7edd65ef7acfff9a388a5fd74562c68bbd145e5
---
**问题描述**

ArkWeb组件支持深拷贝。将ArkWeb组件A深拷贝给ArkWeb组件B后，即使A组件关闭或从路由栈中退出，B仍可继续使用A中的资源。

**解决措施**

当前不支持该功能，只能通过动态创建Web组件的方式，构建一个Web组件池。需要使用时，直接从池中获取组件并挂载到节点树上进行展示。

**参考链接**

[使用Web组件加载页面](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/管理网页加载与浏览记录/使用Web组件加载页面/web-page-loading-with-web-components.md)
