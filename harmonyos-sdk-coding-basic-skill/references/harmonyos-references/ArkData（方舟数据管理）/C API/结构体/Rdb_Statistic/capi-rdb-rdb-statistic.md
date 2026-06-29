---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-statistic
title: Rdb_Statistic
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_Statistic
category: harmonyos-references
scraped_at: 2026-06-01T15:34:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8be41c024f4987a543c79c573b3507a301fec1250fe11f3eeb5467ac83785a50
---
```
1. typedef struct Rdb_Statistic {...} Rdb_Statistic
```

## 概述

PhonePC/2in1TabletTVWearable

描述数据库表的端云同步过程的统计信息。

**起始版本：** 11

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int total | 表示数据库表中需要端云同步的总行数。 |
| int successful | 表示数据库表中端云同步成功的行数。 |
| int failed | 表示数据库表中端云同步失败的行数。 |
| int remained | 表示数据库表中端云同步剩余未执行的行数。 |
