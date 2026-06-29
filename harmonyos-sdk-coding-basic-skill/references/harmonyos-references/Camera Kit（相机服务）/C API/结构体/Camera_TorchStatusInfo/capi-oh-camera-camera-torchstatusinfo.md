---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-torchstatusinfo
title: Camera_TorchStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_TorchStatusInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:21:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7623130ed09c2134a18c7ef067777fd90802975a6870fa3a4e28151a0d2b0f1
---
```
1. typedef struct Camera_TorchStatusInfo {...} Camera_TorchStatusInfo
```

## 概述

PhonePC/2in1TabletTVWearable

手电筒状态信息。

**起始版本：** 12

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [camera.h](../../头文件/camera.h/capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool isTorchAvailable | 手电筒是否可用，true表示可用，false表示不可用。 |
| bool isTorchActive | 手电筒是否激活，true表示激活，false表示未激活。 |
| float torchLevel | 手电筒亮度等级。取值范围为[0,1]，越靠近1，亮度越大。 |
