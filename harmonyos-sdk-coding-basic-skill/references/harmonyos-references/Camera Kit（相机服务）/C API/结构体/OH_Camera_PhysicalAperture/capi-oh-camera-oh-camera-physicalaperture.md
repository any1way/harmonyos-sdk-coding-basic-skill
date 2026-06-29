---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-physicalaperture
title: OH_Camera_PhysicalAperture
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > OH_Camera_PhysicalAperture
category: harmonyos-references
scraped_at: 2026-06-01T16:21:28+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:015bc6b7090e2e86c868f37ac58c6be2283800e0c26901d638adb0dda330e697
---
```
1. typedef struct OH_Camera_PhysicalAperture {...} OH_Camera_PhysicalAperture
```

## 概述

PhonePC/2in1TabletTVWearable

物理光圈配置。

**起始版本：** 24

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Camera\_ZoomRange](../OH_Camera_ZoomRange/capi-oh-camera-oh-camera-zoomrange.md) zoomRange | 变焦范围。 |
| float\* apertures | 支持的光圈值数组。 |
| size\_t apertureCount | 光圈值数量。 |
