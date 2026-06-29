---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audioformat
title: OH_AudioFormat
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioFormat
category: harmonyos-references
scraped_at: 2026-06-01T16:17:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6646d073a033c2f2ebe7470467601555cfb1b1bbd72b9ba97a0d1798e7ddf0fb
---
```
1. typedef struct {...} OH_AudioFormat
```

## 概述

PhonePC/2in1Tablet

定义音频编创的音频流信息，用于描述基本音频格式。

**起始版本：** 22

**相关模块：** [OHAudioSuite](../../模块/OHAudioSuite/capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](../../头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_Audio\_SampleRate](../../头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audio_samplerate) samplingRate | 音频流采样率。 |
| OH\_AudioChannelLayout channelLayout | 音频流声道布局，当前只支持CH\_LAYOUT\_MONO 和 CH\_LAYOUT\_STEREO。 |
| uint32\_t channelCount | 音频流声道个数，当前只支持1声道和2声道。 |
| [OH\_Audio\_EncodingType](../../头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audio_encodingtype) encodingType | 音频流编码类型。 |
| [OH\_Audio\_SampleFormat](../../头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audio_sampleformat) sampleFormat | 音频流采样格式。 |
