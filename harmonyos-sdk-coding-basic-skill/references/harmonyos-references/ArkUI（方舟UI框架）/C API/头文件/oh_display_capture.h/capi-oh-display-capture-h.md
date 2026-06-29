---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-capture-h
title: oh_display_capture.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_display_capture.h
category: harmonyos-references
scraped_at: 2026-06-01T15:49:48+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:aec3c0c146746f8a08d3d4c77527b3ae46d86dd955e70e4cb8a00150dabb2b75
---
## 概述

PhonePC/2in1TabletTVWearable

提供屏幕截屏的能力。

**引用文件：** <window\_manager/oh\_display\_capture.h>

**库：** libnative\_display\_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](../../模块/OH_DisplayManager/capi-oh-displaymanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CaptureScreenPixelmap(uint32\_t displayId,OH\_PixelmapNative \*\*pixelMap)](capi-oh-display-capture-h.md#oh_nativedisplaymanager_capturescreenpixelmap) | 获取屏幕全屏截图，可以通过设置不同的屏幕id号截取不同屏幕的截图。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeDisplayManager\_CaptureScreenPixelmap()

PhonePC/2in1TabletTVWearable

```
1. NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CaptureScreenPixelmap(uint32_t displayId,OH_PixelmapNative **pixelMap)
```

**描述**

获取屏幕全屏截图，可以通过设置不同的屏幕id号截取不同屏幕的截图。

**需要权限：**

* API版本22+：ohos.permission.CUSTOM\_SCREEN\_CAPTURE or ohos.permission.CUSTOM\_SCREEN\_RECORDING
* API版本14-21：ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**起始版本：** 14

**设备行为差异：** 在API version 21之前，该接口在2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。从API version 21开始，该接口在Phone设备、2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t displayId | 需要截屏的屏幕id号，该值为非负整数。 |
| [OH\_PixelmapNative](<../../../../Image Kit（图片处理服务）/C API/结构体/OH_PixelmapNative/capi-image-nativemodule-oh-pixelmapnative.md>) \*\*pixelMap | 创建指定屏幕id的OH\_PixelmapNative对象，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeDisplayManager\_ErrorCode](../oh_display_info.h/capi-oh-display-info-h.md#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](../oh_display_info.h/capi-oh-display-info-h.md#nativedisplaymanager_errorcode)。 |
