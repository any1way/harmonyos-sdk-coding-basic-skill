---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo
title: OH_VideoEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_VideoEncInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:10+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:88690881b17814d26c55ecec21b038d719eb5ae06967674037456a65e9a46334
---
```
1. typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```

## 概述

PhonePC/2in1TabletTV

视频编码参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoCodecFormat](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_videocodecformat) videoCodec | 视频采集编码格式。 |
| int32\_t videoBitrate | 视频采集比特率。单位为比特每秒（bit/s）。 |
| int32\_t videoFrameRate | 视频采集帧率。单位为帧率（FPS）。 |
