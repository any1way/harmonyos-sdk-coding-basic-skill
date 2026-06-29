---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagedecodingops
title: OhosImageDecodingOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageDecodingOps
category: harmonyos-references
scraped_at: 2026-06-01T16:23:26+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:f1b2bfbb30e7c0a2188db34a2b3a0bd8f46cc21529eae044fcc0471f6f05951b
---
```
1. struct OhosImageDecodingOps {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源解码选项。此选项给[OH\_ImageSource\_CreatePixelMap](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createpixelmap)和[OH\_ImageSource\_CreatePixelMapList](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md#oh_imagesource_createpixelmaplist)接口使用。

**起始版本：** 10

**相关模块：** [Image](../../模块/Image/capi-image.md)

**所在头文件：** [image\_source\_mdk.h](../../头文件/image_source_mdk.h/capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int8\_t editable | 定义输出的像素位图是否可编辑。 |
| int32\_t pixelFormat | 定义输出的像素格式。 |
| int32\_t fitDensity | 定义解码目标的像素密度。 |
| uint32\_t index | 定义ImageSource解码索引。 |
| uint32\_t sampleSize | 定义解码样本大小选项。 |
| uint32\_t rotate | 定义解码旋转选项。 |
| struct [OhosImageSize](../OhosImageSize/capi-image-ohosimagesize.md) size | 定义解码目标像素宽高的大小。 |
| struct [OhosImageRegion](../OhosImageRegion/capi-image-ohosimageregion.md) region | 定义ImageSource解码的像素范围。 |
