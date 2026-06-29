---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-occlusiondetectionresult
title: Camera_OcclusionDetectionResult
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_OcclusionDetectionResult
category: harmonyos-references
scraped_at: 2026-06-01T16:21:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94a7d8d1117cd5680a800921f80311f7bfccfe45ffce5b7d2c294fd254676c0f
---
```
1. typedef struct {...} Camera_OcclusionDetectionResult
```

## 概述

PhonePC/2in1TabletTVWearable

相机镜头遮挡、脏污检测结果。

**起始版本：** 23

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool isCameraOccluded | 检查相机镜头是否被遮挡。true表示被遮挡，false表示未被遮挡。 |
| bool isCameraLensDirty | 检查相机镜头是否有脏污。true表示有脏污，false表示没有脏污。 |
