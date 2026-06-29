---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-colorspaceinfo
title: VideoProcessing_ColorSpaceInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > VideoProcessing_ColorSpaceInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:34:56+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:8ccef51c7887e5d94e619de4035f73a540d66216497b4ac435758cd197665214
---
```
1. typedef struct VideoProcessing_ColorSpaceInfo {...} VideoProcessing_ColorSpaceInfo
```

## 概述

PhonePC/2in1TabletTV

视频颜色空间信息数据结构。

**参考：** [OH\_VideoProcessing\_IsColorSpaceConversionSupported](../../头文件/video_processing.h/capi-video-processing-h.md#oh_videoprocessing_iscolorspaceconversionsupported)

**起始版本：** 12

**相关模块：** [VideoProcessing](../../模块/VideoProcessing/capi-videoprocessing.md)

**所在头文件：** [video\_processing\_types.h](../../头文件/video_processing_types.h/capi-video-processing-types-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t metadataType | 视频元数据类型，参考[OH\_NativeBuffer\_MetadataType](<../../../../ArkGraphics 2D（方舟2D图形服务）/C API/头文件/buffer_common.h/capi-buffer-common-h.md#oh_nativebuffer_metadatatype>)。 |
| int32\_t colorSpace | 视频颜色空间类型，参考[OH\_NativeBuffer\_ColorSpace](<../../../../ArkGraphics 2D（方舟2D图形服务）/C API/头文件/buffer_common.h/capi-buffer-common-h.md#oh_nativebuffer_colorspace>)。 |
| int32\_t pixelFormat | 视频像素格式，参考[OH\_NativeBuffer\_Format](<../../../../ArkGraphics 2D（方舟2D图形服务）/C API/头文件/buffer_common.h/capi-buffer-common-h.md#oh_nativebuffer_format>)。 |
