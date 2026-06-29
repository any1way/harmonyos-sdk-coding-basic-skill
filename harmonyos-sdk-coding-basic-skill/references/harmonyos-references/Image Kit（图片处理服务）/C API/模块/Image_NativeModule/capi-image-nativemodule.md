---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule
title: Image_NativeModule
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 模块 > Image_NativeModule
category: harmonyos-references
scraped_at: 2026-06-01T16:22:19+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:704f4f6d275fa53b2507100c361065fce539b0061bbe490e02d73c1cc439cecd
---
## 概述

PhonePC/2in1TabletTVWearable

提供图片处理的相关能力，包括图片编解码、从Native层获取图片数据等。

使用该模块的接口，无需通过JS接口导入，可直接使用NDK完成功能开发。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

* [使用Image\_NativeModule完成图片解码](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片解码/使用Image_NativeModule完成图片解码/image-source-c.md>)
* [使用Image\_NativeModule完成多图对象解码](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片解码/使用Image_NativeModule完成多图对象解码/image-source-picture-c.md>)
* [使用Image\_NativeModule完成图片接收](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片接收/使用Image_NativeModule完成图片接收/image-receiver-c.md>)
* [使用Image\_NativeModule完成位图操作](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用Image_NativeModule完成位图操作/pixelmap-c.md>)
* [使用Image\_NativeModule完成图片编码](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片编码/使用Image_NativeModule完成图片编码/image-packer-c.md>)
* [使用Image\_NativeModule完成多图对象编码](<../../../../../harmonyos-guides/媒体/Image Kit（图片处理服务）/图片开发指导(CC++)/图片编码/使用Image_NativeModule完成多图对象编码/image-packer-picture-c.md>)

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [image\_common.h](../../头文件/image_common.h/capi-image-common-h.md) | 声明图像接口使用的公共枚举和结构体。 |
| [image\_native.h](../../头文件/image_native.h/capi-image-native-h.md) | 声明图像的剪裁矩形、大小和组件数据的接口函数。 |
| [image\_packer\_native.h](../../头文件/image_packer_native.h/capi-image-packer-native-h.md) | 图片编码API。 |
| [image\_receiver\_native.h](../../头文件/image_receiver_native.h/capi-image-receiver-native-h.md) | 声明从native层获取图片数据的方法。 |
| [image\_source\_native.h](../../头文件/image_source_native.h/capi-image-source-native-h.md) | 图片解码API。 |
| [picture\_native.h](../../头文件/picture_native.h/capi-picture-native-h.md) | 提供获取picture数据和信息的API。 |
| [pixelmap\_native.h](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md) | 访问Pixelmap的API。 |
