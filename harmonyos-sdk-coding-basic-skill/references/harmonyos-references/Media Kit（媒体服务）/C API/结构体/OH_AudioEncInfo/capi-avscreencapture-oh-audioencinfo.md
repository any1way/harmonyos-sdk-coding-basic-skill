---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioencinfo
title: OH_AudioEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioEncInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:07+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:8414904ac989701c77b52d4aba5581c6597e76d42ed20aae0b25bac0a059b9ce
---
```
1. typedef struct OH_AudioEncInfo {...} OH_AudioEncInfo
```

## 概述

PhonePC/2in1TabletTV

音频编码信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t audioBitrate | 音频编码比特率。单位为比特每秒（bit/s）。 |
| [OH\_AudioCodecFormat](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_audiocodecformat) audioCodecformat | 音频编码格式。 |
