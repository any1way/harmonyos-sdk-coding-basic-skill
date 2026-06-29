---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-5
title: 如何理解connection.getDefaultNet返回对象netHandle中的netId
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何理解connection.getDefaultNet返回对象netHandle中的netId
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1bc4afe6bd0e8f212258a91a888fda0b9b938c58b09e8c43a0e1b8debd19a974
---
**问题现象**

netId的值0表示未联网，100表示已联网。

**解决措施**

在正常情况下，netHandle中的netId为0表示未连接网络，大于等于100表示已连接网络。

**参考链接**

[NetHandle](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#nethandle>)
