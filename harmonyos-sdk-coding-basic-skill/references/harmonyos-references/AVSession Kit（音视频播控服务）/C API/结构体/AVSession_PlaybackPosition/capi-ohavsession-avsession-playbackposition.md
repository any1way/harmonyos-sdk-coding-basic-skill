---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-playbackposition
title: AVSession_PlaybackPosition
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_PlaybackPosition
category: harmonyos-references
scraped_at: 2026-06-01T16:19:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47daa6ab610b8d188db8a0b88219e3a13ca810b49f1f5f5fa4399a99f3f5ec63
---
```
1. typedef struct AVSession_PlaybackPosition {...} AVSession_PlaybackPosition
```

## 概述

PhonePC/2in1TabletTVWearable

媒体播放位置的相关属性。

**起始版本：** 13

**相关模块：** [OHAVSession](../../模块/OHAVSession/capi-ohavsession.md)

**所在头文件：** [native\_avplaybackstate.h](../../头文件/native_avplaybackstate.h/capi-native-avplaybackstate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t elapsedTime | 已用时间，单位毫秒（ms）。 |
| int64\_t updateTime | 更新时间，单位毫秒（ms）。 |
