---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo
title: OH_AudioCaptureInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioCaptureInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:07+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:8eaaa7eeb31bc7e4264b2390d10fdca20bfe7fff9f75f53f98690ed0e05efc00
---
```
1. typedef struct OH_AudioCaptureInfo {...} OH_AudioCaptureInfo
```

## 概述

PhonePC/2in1TabletTV

音频采样信息。

当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t audioSampleRate | 音频采样率，支持列表请查阅Audio Kit的[AudioSamplingRate](<../../../../Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Enums/arkts-apis-audio-e.md#audiosamplingrate8>)。单位为赫兹（Hz）。 |
| int32\_t audioChannels | 音频声道数。 |
| [OH\_AudioCaptureSourceType](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) audioSource | 音频源。 |
