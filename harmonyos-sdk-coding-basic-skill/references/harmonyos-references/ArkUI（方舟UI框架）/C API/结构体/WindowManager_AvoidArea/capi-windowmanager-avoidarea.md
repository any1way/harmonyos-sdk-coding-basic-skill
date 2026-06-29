---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-avoidarea
title: WindowManager_AvoidArea
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_AvoidArea
category: harmonyos-references
scraped_at: 2026-06-01T15:52:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:862c100a965ac394bb763a0a6e61495b9b5c85f6246da4e75d6f716fb057e137
---
```
1. typedef struct {...} WindowManager_AvoidArea
```

## 概述

PhonePC/2in1TabletTVWearable

定义避让区域结构体。

**起始版本：** 15

**相关模块：** [WindowManager](../../模块/WindowManager/capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](../../头文件/oh_window_comm.h/capi-oh-window-comm-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [WindowManager\_Rect](../WindowManager_Rect/capi-windowmanager-rect.md) topRect | 避让区域的顶部矩形。 |
| [WindowManager\_Rect](../WindowManager_Rect/capi-windowmanager-rect.md) leftRect | 避让区域的左侧矩形。 |
| [WindowManager\_Rect](../WindowManager_Rect/capi-windowmanager-rect.md) rightRect | 避让区域的右侧矩形。 |
| [WindowManager\_Rect](../WindowManager_Rect/capi-windowmanager-rect.md) bottomRect | 避让区域的底部矩形。 |
