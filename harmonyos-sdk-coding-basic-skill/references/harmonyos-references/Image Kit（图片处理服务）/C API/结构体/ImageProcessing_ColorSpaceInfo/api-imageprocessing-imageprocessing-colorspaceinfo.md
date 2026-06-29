---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-imageprocessing-imageprocessing-colorspaceinfo
title: ImageProcessing_ColorSpaceInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageProcessing_ColorSpaceInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:23:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d476e1e72014b3f2225423805037d8047c74e8fa0539763c784e3ca1e4048326
---
```
1. typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```

## 概述

PhonePC/2in1TabletTV

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH\_ImageProcessing\_IsColorSpaceConversionSupported](../../头文件/image_processing.h/capi-image-processing-h.md#oh_imageprocessing_iscolorspaceconversionsupported), [OH\_ImageProcessing\_IsCompositionSupported](../../头文件/image_processing.h/capi-image-processing-h.md#oh_imageprocessing_iscompositionsupported), [OH\_ImageProcessing\_IsDecompositionSupported](../../头文件/image_processing.h/capi-image-processing-h.md#oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：** [ImageProcessing](../../模块/ImageProcessing/capi-imageprocessing.md)

**所在头文件：** [image\_processing\_types.h](../../头文件/image_processing_types.h/capi-image-processing-types-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t metadataType | 定义元数据类型，参考[OH\_Pixelmap\_HdrMetadataKey](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)。 |
| int32\_t colorSpace | 定义色彩空间，参考[ColorSpaceName](<../../../../ArkGraphics 2D（方舟2D图形服务）/C API/头文件/native_color_space_manager.h/capi-native-color-space-manager-h.md#colorspacename>)。 |
| int32\_t pixelFormat | 定义像素格式，参考[PIXEL\_FORMAT](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#pixel_format)。 |
