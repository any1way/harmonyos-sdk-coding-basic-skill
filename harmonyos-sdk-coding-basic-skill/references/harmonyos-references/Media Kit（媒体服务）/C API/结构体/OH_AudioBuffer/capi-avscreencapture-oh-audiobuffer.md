---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer
title: OH_AudioBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioBuffer
category: harmonyos-references
scraped_at: 2026-06-01T16:25:15+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:f2460a087a83aed88942ea5bb59805b27066e41222a2dad46f22787ca6512d83
---
```
1. typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

## 概述

PhonePC/2in1TabletTV

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* buf | 音频buffer内存。 |
| int32\_t size | 音频buffer内存大小。 |
| int64\_t timestamp | 音频buffer时间戳。单位为纳秒（ns）。 |
| [OH\_AudioCaptureSourceType](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频录制源类型。 |
