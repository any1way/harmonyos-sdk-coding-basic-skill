---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo
title: Camera_ConcurrentInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_ConcurrentInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42a2cb7d645c4609ea3dd8cf054f71e50d7d3ec3c526a6a94288d0f9d1b33e5a
---
```
1. typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```

## 概述

PhonePC/2in1TabletTVWearable

相机并发能力信息。

**起始版本：** 18

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_Device](../Camera_Device/capi-oh-camera-camera-device.md) camera | 相机实例。 |
| [Camera\_ConcurrentType](../../头文件/camera.h/capi-camera-h.md#camera_concurrenttype) type | 相机并发状态。 |
| [Camera\_SceneMode](../../头文件/camera.h/capi-camera-h.md#camera_scenemode)\* sceneModes | 相机并发支持的模式。 |
| [Camera\_OutputCapability](../Camera_OutputCapability/capi-oh-camera-camera-outputcapability.md)\* outputCapabilities | 相机输出能力集。 |
| uint32\_t modeAndCapabilitySize | 相机输出能力集大小。 |
