---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange
title: ArkUI_ExpectedFrameRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ExpectedFrameRateRange
category: harmonyos-references
scraped_at: 2026-06-01T15:50:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:000f7b1addeaecc542454bdd4ec06efd1b4167434f5a7e3408d5518c63e9cabc
---
```
1. typedef struct {...} ArkUI_ExpectedFrameRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

设置动画的期望帧率。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](../../头文件/native_animate.h/capi-native-animate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t min | 期望的最小帧率，单位为帧/秒（fps）。 |
| uint32\_t max | 期望的最大帧率，单位为帧/秒（fps）。 |
| uint32\_t expected | 期望的最优帧率，单位为帧/秒（fps）。 |
