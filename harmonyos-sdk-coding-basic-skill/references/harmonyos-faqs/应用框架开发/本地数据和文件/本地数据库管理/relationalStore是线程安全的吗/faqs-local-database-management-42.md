---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-42
title: relationalStore是线程安全的吗
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > relationalStore是线程安全的吗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:484fb3eb6dbf7e4c3ae95de7da1de53f1c3e4e8115cb2b769e9500215741c08f
---
relationalStore是线程安全的，但由于Worker线程运行在独立上下文环境，与主线程的relationalStore实例存在进程隔离，所以不支持Worker。ArkTS语言基础类库提供了taskPool和worker两种多线程方案，均基于Actor并发模型实现。Actor并发模型通过事件传递数据，避免了锁竞争等复杂问题，确保线程安全且并发度较高。

[@ohos.data.relationalStore (关系型数据库)](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/js-apis-data-relationalstore.md>)
