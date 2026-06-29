---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat
title: OhosImageSourceSupportedFormat
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceSupportedFormat
category: harmonyos-references
scraped_at: 2026-06-01T16:23:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c9715e8c6c110747fe489fd964dfc7f3b6f90d3f9f449151775c980ca65a10e2
---
```
1. struct OhosImageSourceSupportedFormat {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](../OhosImageSourceSupportedFormatList/capi-image-ohosimagesourcesupportedformatlist.md)和[OH\_ImageSource\_GetSupportedFormats](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)接口使用。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* format = nullptr | 图像源支持的格式字符串头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串大小。 |
