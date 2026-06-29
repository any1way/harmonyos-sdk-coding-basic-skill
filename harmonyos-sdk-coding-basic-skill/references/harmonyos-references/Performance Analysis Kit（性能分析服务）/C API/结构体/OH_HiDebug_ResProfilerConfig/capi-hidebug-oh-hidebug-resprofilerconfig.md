---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-resprofilerconfig
title: OH_HiDebug_ResProfilerConfig
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiDebug_ResProfilerConfig
category: harmonyos-references
scraped_at: 2026-06-01T16:16:13+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c4940b6ad0f44f49b273be4a2fb45b1f32190b5352eab9e396fa017a652d6714
---
```
1. typedef struct OH_HiDebug_ResProfilerConfig {...} OH_HiDebug_ResProfilerConfig
```

## 概述

PhonePC/2in1TabletTVWearable

定义资源采集配置结构体类型。

**起始版本：** 24

**相关模块：** [HiDebug](../../模块/HiDebug/capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](../../头文件/hidebug_type.h/capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t maxDuration | 最大采集时长，取值范围为 [1, 3600]，单位为秒。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_MAX\_DURATION](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t filterSize | 过滤大小，取值范围为 [1, 4294967295]，单位为字节。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_FILTER\_SIZE](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t maxStackDepth | 最大栈追踪深度，取值范围为 [0, 30]，单位为帧。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_MAX\_STACK\_DEPTH](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t statisticsInterval | 统计间隔，取值范围为 [0, 3600]，单位为秒。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_STATISTICS\_INTERVAL](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
| uint32\_t sampleInterval | 采样大小，取值范围为 [384, 4294967295]，单位为字节。  在采样模式下，如果内存分配大小小于等于采样大小，则概率性采样，否则全量采样。  传入参数超出取值范围，接口将返回错误码[HIDEBUG\_RES\_PROF\_INVALID\_SAMPLE\_INTERVAL](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_errorcode)。  **起始版本：** 24 |
