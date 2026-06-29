---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo
title: NativeDisplayManager_CutoutInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_CutoutInfo
category: harmonyos-references
scraped_at: 2026-06-11T15:58:36+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:18daa82784cde750dd66a39b9230e1291af05cf3df64fc13dcf4fdfac781ea1c
---
```
1. typedef struct {...} NativeDisplayManager_CutoutInfo
```

## 概述

PhonePC/2in1TabletTVWearable

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](../../模块/OH_DisplayManager/capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](../../头文件/oh_display_info.h/capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t boundingRectsLength | 挖孔屏、刘海屏不可用屏幕区域长度。 |
| [NativeDisplayManager\_Rect](../NativeDisplayManager_Rect/capi-nativedisplaymanager-rect.md)\* boundingRects | 挖孔屏、刘海屏等区域的边界矩形。 |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](../NativeDisplayManager_WaterfallDisplayAreaRects/capi-nativedisp-waterfalldisplayarearects.md) waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
