---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videocaptureinfo
title: OH_VideoCaptureInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_VideoCaptureInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b4e25824feb6e8d1b1a8110a02c95d545e8ee99d431d14f248775ca07d3ba7e5
---
```
1. typedef struct OH_VideoCaptureInfo {...} OH_VideoCaptureInfo
```

## 概述

PhonePC/2in1TabletTV

视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint64\_t displayId | 录制物理屏id，使用该参数需要在capturemode为CAPTURE\_SPECIFIED\_SCREEN模式下使用。 |
| int32\_t\* missionIDs | 指定窗口id列表，使用该参数需要在capturemode为CAPTURE\_SPECIFIED\_WINDOW模式下使用。 |
| int32\_t missionIDsLen | 指定窗口ID长度，使用该参数需要在capturemode为CAPTURE\_SPECIFIED\_WINDOW模式下使用。 |
| int32\_t videoFrameWidth | 采集视频的宽度设置，单位px。 |
| int32\_t videoFrameHeight | 采集视频的高度设置，单位px。 |
| [OH\_VideoSourceType](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_videosourcetype) videoSource | 视频采集格式设置，目前仅支持RGBA格式。 |
