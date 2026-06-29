---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-47
title: 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed2474e14383cdaedb0e769de63be324d68866324e7ff98d29b793f12a3f16c9
---
查询数据库可以使用[@ohos.data.relationalStore](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/js-apis-data-relationalstore.md>)模块提供的[query](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#query10>)方法，该方法是异步方法，因此对于查询数据库操作，不需要开子线程。
