---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avcodecbufferattr
title: OH_AVCodecBufferAttr
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVCodecBufferAttr
category: harmonyos-references
scraped_at: 2026-06-01T16:18:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1c1ae9b778f7790166fa7a7b0d16c45d7efb344183e4360c4403cc5f595f7315
---
```
1. typedef struct OH_AVCodecBufferAttr {...} OH_AVCodecBufferAttr
```

## 概述

PhonePC/2in1TabletTVWearable

定义OH\_AVCodec的缓冲区描述信息。

**起始版本：** 9

**相关模块：** [Core](../../模块/Core/capi-core.md)

**所在头文件：** [native\_avbuffer\_info.h](../../头文件/native_avbuffer_info.h/capi-native-avbuffer-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t pts | 此缓冲区的显示时间戳（以微秒为单位）。 |
| int32\_t size | 缓冲区中包含的数据的大小（以字节为单位）。 |
| int32\_t offset | 此缓冲区中有效数据的起始偏移量。 |
| uint32\_t flags | 此缓冲区具有的标志，请参阅[OH\_AVCodecBufferFlags](../../头文件/native_avbuffer_info.h/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)。 |
