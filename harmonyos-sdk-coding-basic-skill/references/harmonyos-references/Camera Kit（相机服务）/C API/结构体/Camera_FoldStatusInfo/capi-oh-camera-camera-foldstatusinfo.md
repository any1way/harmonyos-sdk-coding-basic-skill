---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-foldstatusinfo
title: Camera_FoldStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FoldStatusInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ea09755e3fe2fde44d0561b544f7b364cd65979df204a9d5a62e656f81f3bb0
---
```
1. typedef struct Camera_FoldStatusInfo {...} Camera_FoldStatusInfo
```

## 概述

PhonePC/2in1TabletTVWearable

折叠状态信息。

**起始版本：** 13

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_Device](../Camera_Device/capi-oh-camera-camera-device.md)\*\* supportedCameras | 相机实例列表。 |
| uint32\_t cameraSize | 相机列表数量。 |
| [Camera\_FoldStatus](../../头文件/camera.h/capi-camera-h.md#camera_foldstatus) foldStatus | 当前折叠状态。 |
