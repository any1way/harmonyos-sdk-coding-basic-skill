---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist
title: OhosImageSourceSupportedFormatList
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceSupportedFormatList
category: harmonyos-references
scraped_at: 2026-06-01T16:23:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:01e9baa396e70fff057c4128fa2cee60f40068f76a3bd4547ee21ac72658c854
---
```
1. struct OhosImageSourceSupportedFormatList {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源支持的格式字符串列表。由[OH\_ImageSource\_GetSupportedFormats](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)获取。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [OhosImageSourceSupportedFormat](../OhosImageSourceSupportedFormat/capi-image-ohosimagesourcesupportedformat.md)\*\* supportedFormatList = nullptr | 图像源支持的格式字符串列表头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串列表大小。 |
