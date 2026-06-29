---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceinfo
title: OhosImageSourceInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:23:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad1a874e2ed3c5f693f2726c465483d8a479d18c979b20fda080595dccb9d76a
---
```
1. struct OhosImageSourceInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源信息，由[OH\_ImageSource\_GetImageInfo](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_getimageinfo)获取。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t pixelFormat | 图像源像素格式，由[OH\_ImageSource\_CreateFromUri](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromdata)设置。 |
| int32\_t colorSpace | 图像源色彩空间。 |
| int32\_t alphaType | 图像源透明度类型。 |
| int32\_t density | 图像源密度，由[OH\_ImageSource\_CreateFromUri](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromdata)设置。 |
| struct [OhosImageSize](../OhosImageSize/capi-image-ohosimagesize.md) size | 图像源像素宽高的大小。 |
