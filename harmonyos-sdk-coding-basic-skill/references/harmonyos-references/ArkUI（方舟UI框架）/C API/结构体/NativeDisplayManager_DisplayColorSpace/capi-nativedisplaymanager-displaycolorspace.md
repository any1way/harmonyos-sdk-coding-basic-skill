---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace
title: NativeDisplayManager_DisplayColorSpace
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayColorSpace
category: harmonyos-references
scraped_at: 2026-06-01T15:52:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42e355d055118b6009409695013a56683679c437dbee2a72060e88c58b34ae03
---
```
1. typedef struct {...} NativeDisplayManager_DisplayColorSpace
```

## 概述

PhonePC/2in1TabletTVWearable

显示设备支持的所有色域类型。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](../../模块/OH_DisplayManager/capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](../../头文件/oh_display_info.h/capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t colorSpaceLength | 显示设备的色域长度。 |
| uint32\_t\* colorSpaces | 显示设备的色域数据。 |
