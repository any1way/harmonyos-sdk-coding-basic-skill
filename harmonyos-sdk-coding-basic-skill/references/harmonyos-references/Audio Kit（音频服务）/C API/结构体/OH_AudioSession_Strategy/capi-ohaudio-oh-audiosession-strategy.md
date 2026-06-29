---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-strategy
title: OH_AudioSession_Strategy
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSession_Strategy
category: harmonyos-references
scraped_at: 2026-06-01T16:17:28+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:2d59eb1a069f3db381b43e4bb37c3af863d5ced2fb0a2581c829e1aae90b8443
---
```
1. typedef struct OH_AudioSession_Strategy {...} OH_AudioSession_Strategy
```

## 概述

PhonePC/2in1TabletTVWearable

音频会话策略。

从API version 24开始，此结构体由native\_audio\_session\_manager.h移动至native\_audio\_session\_base.h文件。

在API version 24之前，使用该结构体请引用native\_audio\_session\_manager.h头文件；从API version 24开始，引用native\_audio\_session\_manager.h或native\_audio\_session\_base.h均可正常使用该结构体。

**起始版本：** 12

**相关模块：** [OHAudio](../../模块/OHAudio/capi-ohaudio.md)

**所在头文件：** [native\_audio\_session\_base.h](../../头文件/native_audio_session_base.h/capi-native-audio-session-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioSession\_ConcurrencyMode](../../头文件/native_audio_session_base.h/capi-native-audio-session-base-h.md#oh_audiosession_concurrencymode) concurrencyMode | 音频并发模式。 |
