---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-dataobserver
title: Rdb_DataObserver
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_DataObserver
category: harmonyos-references
scraped_at: 2026-06-01T15:34:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8c990cc58dd4f7d7191a6a6ec2d17184b1bbc74264cdd00974a1df73b65ff873
---
```
1. typedef struct Rdb_DataObserver {...} Rdb_DataObserver
```

## 概述

PhonePC/2in1TabletTVWearable

表示数据观察者。

**起始版本：** 11

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| void\* context | 表示数据观察者的上下文。 |
| [Rdb\_SubscribeCallback](../Rdb_SubscribeCallback/capi-rdb-rdb-subscribecallback.md) callback | 数据观察者的回调。 |
