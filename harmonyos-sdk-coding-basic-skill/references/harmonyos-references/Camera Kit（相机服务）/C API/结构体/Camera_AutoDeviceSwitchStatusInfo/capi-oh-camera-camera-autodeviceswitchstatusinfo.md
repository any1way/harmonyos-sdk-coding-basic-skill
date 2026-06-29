---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-autodeviceswitchstatusinfo
title: Camera_AutoDeviceSwitchStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_AutoDeviceSwitchStatusInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:960f8f2e799ac3145ef69389c1983ecc89fbc38213ff19443ad198319cf5315d
---
```
1. typedef struct Camera_AutoDeviceSwitchStatusInfo {...} Camera_AutoDeviceSwitchStatusInfo
```

## 概述

PhonePC/2in1TabletTVWearable

自动设备切换状态信息。

**起始版本：** 13

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool isDeviceSwitched | 设备是否已切换，true表示已切换，false表示未切换。 |
| bool isDeviceCapabilityChanged | 设备功能是否改变，true表示已改变，false表示未改变。 |
