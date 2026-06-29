---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/age-nativemodule-oh-pixelmap-initializationoptions
title: OH_Pixelmap_InitializationOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_InitializationOptions
category: harmonyos-references
scraped_at: 2026-06-01T16:22:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7b9f274f3087a0657538cbb9ffc9e12e5845c7abfd9a7a8f25a5e8cd1379b834
---
```
1. struct OH_Pixelmap_InitializationOptions
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_Pixelmap\_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。

创建OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Create](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_create)函数。

释放OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Release](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_release)函数。

OH\_Pixelmap\_InitializationOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽 | [OH\_PixelmapInitializationOptions\_GetWidth](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getwidth) | 获取图片宽。 |
| uint32\_t | width | 图片宽 | [OH\_PixelmapInitializationOptions\_SetWidth](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setwidth) | 设置图片宽。 |
| uint32\_t | height | 图片高 | [OH\_PixelmapInitializationOptions\_GetHeight](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getheight) | 获取图片高。 |
| uint32\_t | height | 图片高 | [OH\_PixelmapInitializationOptions\_SetHeight](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setheight) | 设置图片高。 |
| int32\_t | pixelFormat | 像素格式 | [OH\_PixelmapInitializationOptions\_GetPixelFormat](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getpixelformat) | 获取像素格式。 |
| int32\_t | pixelFormat | 像素格式 | [OH\_PixelmapInitializationOptions\_SetPixelFormat](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setpixelformat) | 设置像素格式。 |
| int32\_t | alphaType | 透明度类型 | [OH\_PixelmapInitializationOptions\_GetAlphaType](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getalphatype) | 获取透明度类型。 |
| int32\_t | alphaType | 透明度类型 | [OH\_PixelmapInitializationOptions\_SetAlphaType](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setalphatype) | 设置透明度类型。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](../../模块/Image_NativeModule/capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md)
