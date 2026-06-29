---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo
title: OH_AudioInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:926b2da833b9372b01137cd99c383a2ae584d96e30464df2b06ea22d90185367
---
```
1. typedef struct OH_AudioInfo {...} OH_AudioInfo
```

## 概述

PhonePC/2in1TabletTV

音频信息。

同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioCaptureInfo](../OH_AudioCaptureInfo/capi-avscreencapture-oh-audiocaptureinfo.md) micCapInfo | 音频麦克风采样信息。 |
| [OH\_AudioCaptureInfo](../OH_AudioCaptureInfo/capi-avscreencapture-oh-audiocaptureinfo.md) innerCapInfo | 音频内录采样信息。 |
| [OH\_AudioEncInfo](../OH_AudioEncInfo/capi-avscreencapture-oh-audioencinfo.md) audioEncInfo | 音频编码信息，原始码流时不需要设置。 |
