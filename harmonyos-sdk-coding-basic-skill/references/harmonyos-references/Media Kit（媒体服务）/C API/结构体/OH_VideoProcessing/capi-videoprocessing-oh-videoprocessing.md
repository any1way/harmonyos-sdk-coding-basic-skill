---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-oh-videoprocessing
title: OH_VideoProcessing
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_VideoProcessing
category: harmonyos-references
scraped_at: 2026-06-01T16:25:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10b00e795e7593f040091c6847dad33ccfaaf09294f86e8d49b43d812545da38
---
```
1. typedef struct OH_VideoProcessing OH_VideoProcessing
```

## 概述

PhonePC/2in1TabletTV

定义视频处理对象。

定义一个OH\_VideoProcessing空指针，调用[OH\_VideoProcessing\_Create](../../头文件/video_processing.h/capi-video-processing-h.md#oh_videoprocessing_create)创建视频处理实例，该指针在创建实例之前必须为空。用户可以对不同的处理类型创建不同的视频处理实例。

**起始版本：** 12

**相关模块：** [VideoProcessing](../../模块/VideoProcessing/capi-videoprocessing.md)

**所在头文件：** [video\_processing\_types.h](../../头文件/video_processing_types.h/capi-video-processing-types-h.md)
