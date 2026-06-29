---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-image-nativemodule-oh-pixelmap-hdrgainmapmetadata
title: OH_Pixelmap_HdrGainmapMetadata
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrGainmapMetadata
category: harmonyos-references
scraped_at: 2026-06-01T16:22:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:db6ca7cfeb7df7ce435f174decaa2dba82e196703d18d5ff9940ede39d8d1bfa
---
```
1. typedef struct OH_Pixelmap_HdrGainmapMetadata {...} OH_Pixelmap_HdrGainmapMetadata
```

## 概述

PhonePC/2in1TabletTVWearable

HDR\_GAINMAP\_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](../../模块/Image_NativeModule/capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint16\_t writerVersion | 元数据编写器使用的版本。 |
| uint16\_t miniVersion | 元数据解析需要理解的最小版本。 |
| uint8\_t gainmapChannelNum | Gainmap的颜色通道数，值为3时RGB通道的元数据值不同，值为1时各通道元数据值相同。 |
| bool useBaseColorFlag | 是否使用基础图的色彩空间，参考ISO 21496-1。true表示使用，false表示不使用。 |
| float baseHeadroom | 基础图提亮比，参考ISO 21496-1。 |
| float alternateHeadroom | 提取的可选择图像提亮比，参考ISO 21496-1。 |
| float gainmapMax[3] | 增强图像的最大值，参考ISO 21496-1。 |
| float gainmapMin[3] | 增强图像的最小值，参考ISO 21496-1。 |
| float gamma[3] | gamma值，参考ISO 21496-1。 |
| float baselineOffset[3] | 基础图的偏移，参考ISO 21496-1。 |
| float alternateOffset[3] | 提取的可选择图像偏移量，参考ISO 21496-1。 |
