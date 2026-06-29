---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-expectedraterange
title: OH_NativeXComponent_ExpectedRateRange
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_ExpectedRateRange
category: harmonyos-references
scraped_at: 2026-06-11T15:56:15+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:955b5b8f56e731791cc340f7b8a392d70e220e7a0ddba0bde08692700f7ad4cc
---
```
1. typedef struct {...} OH_NativeXComponent_ExpectedRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

定义期望帧率范围。

**起始版本：** 11

**相关模块：** [OH\_NativeXComponent Native XComponent](<../../模块/OH_NativeXComponent Native XComponent/capi-oh-nativexcomponent-native-xcomponent.md>)

**所在头文件：** [native\_interface\_xcomponent.h](../../头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t min | 期望帧率范围最小值。单位为帧/秒。 |
| int32\_t max | 期望帧率范围最大值。单位为帧/秒。 |
| int32\_t expected | 期望帧率。单位为帧/秒。 |
