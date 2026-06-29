---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-distributedconfig
title: Rdb_DistributedConfig
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_DistributedConfig
category: harmonyos-references
scraped_at: 2026-06-01T15:34:29+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:59f818ecf181a2e142c01d783293b393dff153aa2204f6fb3ae343acbb8149fa
---
```
1. typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```

## 概述

PhonePC/2in1TabletTVWearable

记录表的分布式配置信息。

**起始版本：** 11

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb\_DistributedConfig结构的版本。 |
| bool isAutoSync | 表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用[OH\_Rdb\_CloudSync](../../头文件/relational_store.h/capi-relational-store-h.md#oh_rdb_cloudsync)接口触发端云同步。 |
