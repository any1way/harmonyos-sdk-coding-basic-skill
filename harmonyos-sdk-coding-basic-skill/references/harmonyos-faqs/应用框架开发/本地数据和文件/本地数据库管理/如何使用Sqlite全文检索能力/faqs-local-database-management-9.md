---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-9
title: 如何使用Sqlite全文检索能力
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何使用Sqlite全文检索能力
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ccaddfe356d0b0848c63d82a9e339ea54bca6b7d9fa5ecd49d95265da8e2133
---
**解决措施**

没有提供直接的接口，需要执行SQL语句CREATE VIRTUAL TABLE语句建立FTS表，再使用MATCH操作符实现检索。

[executeSql](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#executesql10>)：执行包含指定参数但不返回值的SQL语句。

[querySql](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#querysql10>)：根据指定的SQL语句查询数据库中的数据。
