---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-lowpowervideosink-oh-lowpowervideosinkcallback
title: OH_LowPowerVideoSinkCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_LowPowerVideoSinkCallback
category: harmonyos-references
scraped_at: 2026-06-01T16:25:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf8786adfbf2159cea533e4b6a41af5059e1f97f142cace3655c4c1e61ec732d
---
```
1. typedef struct OH_LowPowerVideoSinkCallback OH_LowPowerVideoSinkCallback
```

## 概述

PhonePC/2in1Tablet

包含了LowPowerVideoSink回调函数指针的集合。

应用需注册此实例结构体到[OH\_LowPowerVideoSink](../OH_LowPowerVideoSink/capi-lowpowervideosink-oh-lowpowervideosink.md)实例中，并对回调上报的信息进行处理，保证LowPowerVideoSink的正常运行。

**起始版本：** 20

**相关模块：** [LowPowerVideoSink](../../模块/LowPowerVideoSink/capi-lowpowervideosink.md)

**所在头文件：** [lowpower\_video\_sink\_base.h](../../头文件/lowpower_video_sink_base.h/capi-lowpower-video-sink-base-h.md)
