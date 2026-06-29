---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-systemmeminfo
title: HiDebug_SystemMemInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_SystemMemInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:16:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6e4bbc8541544217120d75b103ef87bb860c1961744d3b2805cfea957f513ee5
---
```
1. typedef struct HiDebug_SystemMemInfo {...} HiDebug_SystemMemInfo
```

## 概述

PhonePC/2in1TabletTVWearable

系统内存信息结构类型定义。

**起始版本：** 12

**相关模块：** [HiDebug](../../模块/HiDebug/capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](../../头文件/hidebug_type.h/capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t totalMem | 系统总的内存，以KB为单位。 |
| uint32\_t freeMem | 系统空闲的内存，以KB为单位。 |
| uint32\_t availableMem | 系统可用的内存，以KB为单位。 |
