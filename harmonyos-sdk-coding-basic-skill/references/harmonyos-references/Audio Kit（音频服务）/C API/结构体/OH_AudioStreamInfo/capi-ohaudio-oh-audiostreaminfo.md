---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo
title: OH_AudioStreamInfo
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioStreamInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:17:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:611c84306ae3e1bc5d08cee627fb8221b2aae2cb55df86f35cbcc68efdd31584
---
```
1. typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义音频流信息，用于描述基本音频格式。

**起始版本：** 19

**相关模块：** [OHAudio](../../模块/OHAudio/capi-ohaudio.md)

**所在头文件：** [native\_audiostream\_base.h](../../头文件/native_audiostream_base.h/capi-native-audiostream-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t samplingRate | 音频流采样率。 |
| [OH\_AudioChannelLayout](<../../../../AVCodec Kit（音视频编解码服务）/C API/头文件/native_audio_channel_layout.h/capi-native-audio-channel-layout-h.md#oh_audiochannellayout>) channelLayout | 音频流声道布局。 |
| [OH\_AudioStream\_EncodingType](../../头文件/native_audiostream_base.h/capi-native-audiostream-base-h.md#oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |
| [OH\_AudioStream\_SampleFormat](../../头文件/native_audiostream_base.h/capi-native-audiostream-base-h.md#oh_audiostream_sampleformat) sampleFormat | 音频流采样格式。 |
