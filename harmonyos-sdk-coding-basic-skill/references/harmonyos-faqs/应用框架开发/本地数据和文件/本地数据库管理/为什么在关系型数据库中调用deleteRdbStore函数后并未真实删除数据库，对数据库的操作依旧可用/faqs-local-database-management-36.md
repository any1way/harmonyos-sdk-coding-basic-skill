---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-36
title: 为什么在关系型数据库中调用deleteRdbStore函数后并未真实删除数据库，对数据库的操作依旧可用
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 为什么在关系型数据库中调用deleteRdbStore函数后并未真实删除数据库，对数据库的操作依旧可用
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:92f067c6333128d24a2d9508ee5d70dcd127e20ce0723c1d027eadac967b3f5f
---
建立数据库时，如果在 StoreConfig 中配置了自定义路径，调用 relationalStore.deleteRdbStore 接口删除数据库将无效，必须使用[deleteRdbStore10+](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Functions/arkts-apis-data-relationalstore-f.md#relationalstoredeleterdbstore10>)接口。数据库删除成功后，建议将数据库对象置为null以避免内存泄漏。

**参考链接**

[关系型数据库](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/js-apis-data-relationalstore.md>)
