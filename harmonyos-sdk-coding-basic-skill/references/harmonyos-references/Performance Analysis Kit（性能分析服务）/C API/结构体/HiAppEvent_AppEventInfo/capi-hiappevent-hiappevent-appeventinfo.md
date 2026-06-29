---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventinfo
title: HiAppEvent_AppEventInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:15:53+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:bd4f8cb38dfa2ccfc64f1bd8dcae4d50a5cf87487e6fa662de7139ddc8b2bb02
---
```
1. typedef struct HiAppEvent_AppEventInfo {...} HiAppEvent_AppEventInfo
```

## 概述

PhonePC/2in1TabletTVWearable

单个事件信息，包含事件领域、事件名称、事件类型和事件携带的用json格式字符串表示的自定义参数列表。

**起始版本：** 12

**相关模块：** [HiAppEvent](../../模块/HiAppEvent/capi-hiappevent.md)

**所在头文件：** [hiappevent.h](../../头文件/hiappevent.h/capi-hiappevent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* domain | 事件领域。 |
| const char\* name | 事件名称。 |
| enum [EventType](../../头文件/hiappevent.h/capi-hiappevent-h.md#eventtype) type | 事件类型。 |
| const char\* params | json格式字符串类型的事件参数列表。 |
