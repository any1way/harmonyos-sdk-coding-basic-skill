---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks
title: VideoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > VideoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-06-01T16:21:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d204f054ecb743f23aea323bcd01c5f5b2934ed8fe57d3e952a383ba02c4fa8c
---
```
1. typedef struct VideoOutput_Callbacks {...} VideoOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

用于录像输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [video\_output.h](../../头文件/video_output.h/capi-video-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoOutput\_OnFrameStart](../../头文件/video_output.h/capi-video-output-h.md#oh_videooutput_onframestart) onFrameStart | 录像输出帧启动事件。 |
| [OH\_VideoOutput\_OnFrameEnd](../../头文件/video_output.h/capi-video-output-h.md#oh_videooutput_onframeend) onFrameEnd | 录像输出帧结束事件。 |
| [OH\_VideoOutput\_OnError](../../头文件/video_output.h/capi-video-output-h.md#oh_videooutput_onerror) onError | 录像输出错误事件。 |
