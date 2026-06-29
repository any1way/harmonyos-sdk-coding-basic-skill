---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturestartinfo
title: Camera_CaptureStartInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_CaptureStartInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d800bafe9dba9cfced573dd753ec75bb8a963b82294df2818717931f54cb71df
---
```
1. typedef struct Camera_CaptureStartInfo {...} Camera_CaptureStartInfo
```

## 概述

PhonePC/2in1TabletTVWearable

拍照开始信息。

**起始版本：** 12

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t captureId | 拍照id。 |
| int64\_t time | 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。 |
