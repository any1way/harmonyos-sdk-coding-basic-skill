---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks
title: PhotoOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > PhotoOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-06-01T16:21:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73cbc0b0c3af7ee3de53a0c6e5e9bd089de025c7d4c77b5e7c87461df79a401d
---
```
1. typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

拍照输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [photo\_output.h](../../头文件/photo_output.h/capi-photo-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_PhotoOutput\_OnFrameStart](../../头文件/photo_output.h/capi-photo-output-h.md#oh_photooutput_onframestart) onFrameStart | 拍照输出帧启动事件。 |
| [OH\_PhotoOutput\_OnFrameShutter](../../头文件/photo_output.h/capi-photo-output-h.md#oh_photooutput_onframeshutter) onFrameShutter | 拍照输出帧快门事件。 |
| [OH\_PhotoOutput\_OnFrameEnd](../../头文件/photo_output.h/capi-photo-output-h.md#oh_photooutput_onframeend) onFrameEnd | 拍照输出帧结束事件。 |
| [OH\_PhotoOutput\_OnError](../../头文件/photo_output.h/capi-photo-output-h.md#oh_photooutput_onerror) onError | 拍照输出错误事件。 |
