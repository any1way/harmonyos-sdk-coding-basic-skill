---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keydata
title: Rdb_KeyData
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyData
category: harmonyos-references
scraped_at: 2026-06-01T15:34:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f0c6a8ac2dd365da1b6f3d94fe12e671e82c4d08f4eee15949b893792c7af4ea
---
```
1. union Rdb_KeyData { ... }
```

## 概述

PhonePC/2in1TabletTVWearable

存放变化的具体数据。

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint64\_t integer | 存放uint64\_t类型的数据。 |
| double real | 存放double类型的数据。 |
| const char\* text | 存放char类型的数据。 |
