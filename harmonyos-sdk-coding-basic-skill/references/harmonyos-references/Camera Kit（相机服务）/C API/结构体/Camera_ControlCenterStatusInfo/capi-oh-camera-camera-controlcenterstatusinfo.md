---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-controlcenterstatusinfo
title: Camera_ControlCenterStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_ControlCenterStatusInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a576f8fd7fcfffc55aa7fdc81abd1d462b4355d4d973835763073f48d3722b7
---
```
1. typedef struct Camera_ControlCenterStatusInfo {...} Camera_ControlCenterStatusInfo
```

## 概述

PhonePC/2in1TabletTVWearable

控制器效果激活状态信息。

**起始版本：** 20

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_ControlCenterEffectType](../../头文件/camera.h/capi-camera-h.md#camera_controlcentereffecttype) effectType | 控制器效果类型。 |
| bool isActive | 控制器是否激活。true表示激活，false表示未激活。 |
