---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup
title: HiAppEvent_AppEventGroup
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventGroup
category: harmonyos-references
scraped_at: 2026-06-01T16:15:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a4c50c5f22138844d4a401437541ca93aa657747ca4466e5904801719bb93793
---
```
1. typedef struct HiAppEvent_AppEventGroup {...} HiAppEvent_AppEventGroup
```

## 概述

PhonePC/2in1TabletTVWearable

一组事件信息，包含事件组的名称，按名称分组的单个事件信息数组，事件数组的长度。

**起始版本：** 12

**相关模块：** [HiAppEvent](../../模块/HiAppEvent/capi-hiappevent.md)

**所在头文件：** [hiappevent.h](../../头文件/hiappevent.h/capi-hiappevent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* name | 事件数组中相同的事件名称。 |
| const struct HiAppEvent\_AppEventInfo\* appEventInfos | 具有相同事件名称的事件数组。 |
| uint32\_t infoLen | 具有相同事件名称的事件数组的长度。 |
