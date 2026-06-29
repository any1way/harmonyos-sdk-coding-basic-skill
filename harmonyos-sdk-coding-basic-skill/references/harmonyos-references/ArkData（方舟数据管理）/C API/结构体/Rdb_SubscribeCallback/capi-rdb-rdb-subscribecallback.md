---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback
title: Rdb_SubscribeCallback
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_SubscribeCallback
category: harmonyos-references
scraped_at: 2026-06-01T15:34:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9caaeb918c8296b2fc70cfff18ded48e55e1e68794119d04ee47986a1e9283dc
---
```
1. typedef union Rdb_SubscribeCallback {...} Rdb_SubscribeCallback
```

## 概述

PhonePC/2in1TabletTVWearable

表示回调函数。

**起始版本：** 11

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rdb\_DetailsObserver](../../头文件/relational_store.h/capi-relational-store-h.md#rdb_detailsobserver) detailsObserver | 端云数据更改事件的细节的回调函数。 |
| [Rdb\_BriefObserver](../../头文件/relational_store.h/capi-relational-store-h.md#rdb_briefobserver) briefObserver | 端云数据更改事件的回调函数。 |
