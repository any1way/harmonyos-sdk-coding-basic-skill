---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/metadataextractor-oh-avmetadataextractor-frameinfo
title: OH_AVMetadataExtractor_FrameInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVMetadataExtractor_FrameInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44bf6f93958f41d43f7e26b87313ee8c9736625187388a144610dee39f33e364
---
```
1. typedef struct {...} OH_AVMetadataExtractor_FrameInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义从视频中提取出的帧的信息。

**起始版本：** 23

**相关模块：** [AVMetadataExtractor](../../模块/AVMetadataExtractor/capi-avmetadataextractor.md)

**所在头文件：** [avmetadata\_extractor\_base.h](../../头文件/avmetadata_extractor_base.h/capi-avmetadata-extractor-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t requestTimeUs | 用户传入的请求时间。 |
| int64\_t actualTimeUs | 实际提取到的帧的时间；若提取失败，则为-1。 |
| [OH\_PixelmapNative\*](<../../../../Image Kit（图片处理服务）/C API/结构体/OH_PixelmapNative/capi-image-nativemodule-oh-pixelmapnative.md>) image | 从视频中提取出的帧图像；若提取失败，则为空指针。 |
| [OH\_AVMetadataExtractor\_FetchState](../../头文件/avmetadata_extractor_base.h/capi-avmetadata-extractor-base-h.md#oh_avmetadataextractor_fetchstate) result | 本次帧提取操作的结果状态。 |
