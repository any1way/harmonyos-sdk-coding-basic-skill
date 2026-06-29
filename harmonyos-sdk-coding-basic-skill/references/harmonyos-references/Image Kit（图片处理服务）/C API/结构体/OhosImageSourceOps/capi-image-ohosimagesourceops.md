---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceops
title: OhosImageSourceOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceOps
category: harmonyos-references
scraped_at: 2026-06-01T16:23:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:83377bec138cc1994f4f1a50c6b9abedfa929be4c59113e3065b549c7e10387d
---
```
1. struct OhosImageSourceOps {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源选项信息。此选项给[OH\_ImageSource\_CreateFromUri](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromfd)、[OH\_ImageSource\_CreateFromData](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createfromdata)和[OH\_ImageSource\_CreateIncremental](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createincremental)接口使用。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t density | 图像源像素密度。 |
| int32\_t pixelFormat | 图像源像素格式，通常用于描述YUV缓冲区。 |
| struct [OhosImageSize](../OhosImageSize/capi-image-ohosimagesize.md) size | 图像源像素宽高的大小。 |
