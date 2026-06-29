---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressdetails
title: Rdb_ProgressDetails
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ProgressDetails
category: harmonyos-references
scraped_at: 2026-06-01T15:34:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9fb75778edb1463ddf0d33b05840bf72ca6f65557e95432b030082cdcb473afc
---
```
1. typedef struct Rdb_ProgressDetails {...} Rdb_ProgressDetails
```

## 概述

PhonePC/2in1TabletTVWearable

描述数据库整体执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：** [RDB](../../模块/RDB/capi-rdb.md)

**所在头文件：** [relational\_store.h](../../头文件/relational_store.h/capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识OH\_TableDetails结构的版本。 |
| int schedule | 表示端云同步过程。 |
| int code | 表示端云同步过程的状态。 |
| int32\_t tableLength | 表示端云同步的表的数量。 |
