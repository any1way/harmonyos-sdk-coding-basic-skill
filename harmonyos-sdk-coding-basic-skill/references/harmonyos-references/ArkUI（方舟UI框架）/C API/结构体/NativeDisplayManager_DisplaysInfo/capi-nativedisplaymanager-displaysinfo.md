---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo
title: NativeDisplayManager_DisplaysInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplaysInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:52:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:15ca80ee1f00684aaf9cd0460ee8aa3062972618dc4631fa383faea128bd4e92
---
```
1. typedef struct {...} NativeDisplayManager_DisplaysInfo
```

## 概述

PhonePC/2in1TabletTVWearable

多显示设备的Display对象。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](../../模块/OH_DisplayManager/capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](../../头文件/oh_display_info.h/capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t displaysLength | 多显示设备Display对象的长度。 |
| [NativeDisplayManager\_DisplayInfo](../NativeDisplayManager_DisplayInfo/capi-nativedisplaymanager-displayinfo.md)\* displaysInfo | 多显示设备Display对象的属性。 |
