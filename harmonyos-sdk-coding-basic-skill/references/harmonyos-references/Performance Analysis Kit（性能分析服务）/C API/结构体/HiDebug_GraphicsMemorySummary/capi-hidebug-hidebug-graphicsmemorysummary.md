---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-graphicsmemorysummary
title: HiDebug_GraphicsMemorySummary
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_GraphicsMemorySummary
category: harmonyos-references
scraped_at: 2026-06-01T16:16:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:db12e4fca17045b372503f7318bf646f7dfaeb8b9153568796350c636f492143
---
```
1. typedef struct HiDebug_GraphicsMemorySummary {...} HiDebug_GraphicsMemorySummary
```

## 概述

PhonePC/2in1TabletTVWearable

应用图形显存占用详情的结构定义。

**起始版本：** 21

**相关模块：** [HiDebug](../../模块/HiDebug/capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](../../头文件/hidebug_type.h/capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t gl | gl内存大小，RenderService渲染进程加载所需资源占用的内存，例如图片、纹理等，以KB为单位。 |
| uint32\_t graph | graph内存大小，进程统计的DMA内存占用，包括直接通过接口申请的DMA buffer和通过allocator\_host申请的DMA buffer，以KB为单位。 |
