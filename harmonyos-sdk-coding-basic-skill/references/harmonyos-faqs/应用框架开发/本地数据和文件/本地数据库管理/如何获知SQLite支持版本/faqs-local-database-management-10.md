---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-10
title: 如何获知SQLite支持版本
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何获知SQLite支持版本
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:18+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:aa6e3e765a2e6cda595129b24010fd9a55c4e584bf989884d4ab17ae3009988a
---
当前SQLite版本号："3.40.1"，SQLite的版本是HarmonyOS系统内置好的，有封装好的RDB接口，不能随意引用最新版本。

虽然系统内置SQLite，但推荐使用更高层级的RDB接口进行封装操作，[@ohos.data.relationalStore](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/js-apis-data-relationalstore.md>)基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。
