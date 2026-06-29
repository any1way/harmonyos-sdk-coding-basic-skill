---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-30
title: 如何实现同步方式调用数据库接口
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何实现同步方式调用数据库接口
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4611990949f862c49f2a931f831ed26b50c9206ed3ba75bb669a5df45d7a8c60
---
使用getRdbStore打开数据库时，推荐封装成async/await语法，对于性能敏感场景可直接使用同步接口，异步封装适用于需要避免UI阻塞的情况。

关于数据库的增删改查，已提供同步接口，具体可查看[API文档](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#insertsync12>)。
