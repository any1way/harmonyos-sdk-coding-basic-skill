---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-14
title: 用sqlite开发时，怎么保证数据库同一时间只能支持一个写操作？怎么创建索引
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 用sqlite开发时，怎么保证数据库同一时间只能支持一个写操作？怎么创建索引
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2fa8a8b53eedd145e5c1062a6ba8adcf6f9673d10397565b7339ce06faa86b76
---
可以使用事务来确保数据库在同一时间只支持一个写操作。创建索引时，请参考SQLite的官方文档中的索引创建语法规范。。

1.定义SQL语句的常量

const SQL\_CREATE\_TABLE = 'CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,salary REAL)';

const CREATE\_INDEX = 'CREATE INDEX idx\_name ON employee (name)';

2.使用executeSql执行包含指定参数的 SQL 语句，但不返回值。

this.rdbStore.executeSql(SQL\_CREATE\_TABLE);

this.rdbStore.executeSql(CREATE\_INDEX);

**参考链接**

[beginTransaction](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#begintransaction>)
