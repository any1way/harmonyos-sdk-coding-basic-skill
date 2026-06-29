---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-positionarea
title: Image_PositionArea
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_PositionArea
category: harmonyos-references
scraped_at: 2026-06-01T16:23:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3fe4c199d8029a3c83bcd206bc428518f33adc3a978ff7d49bbaa48a998b1f4c
---
```
1. typedef struct Image_PositionArea {...} Image_PositionArea
```

## 概述

PhonePC/2in1TabletTVWearable

要读取或写入的图像像素区域。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](../../模块/Image_NativeModule/capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](../../头文件/image_common.h/capi-image-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*pixels | 读取或写入的图像像素数据。仅支持BRGA\_8888格式的数据。 |
| size\_t pixelsSize | 图像像素数据的长度（单位：字节）。 |
| uint32\_t offset | 数据读取或写入的偏移量（单位：字节）。 |
| uint32\_t stride | 区域的跨距，即区域中每行像素所占的空间（单位：字节）。stride >= region.size.width \* 4。 |
| [Image\_Region](../Image_Region/capi-image-nativemodule-image-region.md) region | 读取或写入的区域。区域宽度加X坐标不能大于原图的宽度，区域高度加Y坐标不能大于原图的高度。 |
