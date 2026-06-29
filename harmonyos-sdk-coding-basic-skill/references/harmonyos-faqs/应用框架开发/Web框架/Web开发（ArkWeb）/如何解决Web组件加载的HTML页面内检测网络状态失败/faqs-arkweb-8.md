---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-8
title: 如何解决Web组件加载的HTML页面内检测网络状态失败
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件加载的HTML页面内检测网络状态失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5e693a2de7027bf490c11592daced20d34b5b78b0d0a64e5ad40aa4b25df58bb
---
**问题现象**

在HTML页面中，使用window.navigator.onLine获取网络状态，在联网/断网情况下返回值均为false。

**解决措施**

配置应用以获取网络信息权限：ohos.permission.GET\_NETWORK\_INFO

**参考链接**

[ohos.permission.GET\_NETWORK\_INFO](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/应用权限列表/开放权限（系统授权）/permissions-for-all.md#ohospermissionget_network_info)
