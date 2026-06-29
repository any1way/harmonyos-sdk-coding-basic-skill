---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-profilingresult
title: OH_HiDebug_ProfilingResult
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiDebug_ProfilingResult
category: harmonyos-references
scraped_at: 2026-06-01T16:16:13+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:7daa43d14ea994847216482ddc0a7145ac3b60d26320c4148dff6289dd0d44b6
---
```
1. typedef struct OH_HiDebug_ProfilingResult {...} OH_HiDebug_ProfilingResult
```

## 概述

PhonePC/2in1TabletTVWearable

封装单次资源采集的结果。

**起始版本：** 24

**相关模块：** [HiDebug](../../模块/HiDebug/capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](../../头文件/hidebug_type.h/capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_HiDebug\_ResourceType](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#oh_hidebug_resourcetype) resourceType | 资源采集类型。  **起始版本：** 24 |
| const char\* filePath | 资源采集结果文件路径。如果采集失败则为空值。  **起始版本：** 24 |
