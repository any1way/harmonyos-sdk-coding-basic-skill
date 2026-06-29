---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue
title: OH_Pixelmap_HdrMetadataValue
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrMetadataValue
category: harmonyos-references
scraped_at: 2026-06-11T16:32:22+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:f0a374fe6fa738ea7eee73f22488050f936e2abdd268859d2c88b254121209ea
---
```
1. typedef struct OH_Pixelmap_HdrMetadataValue {...} OH_Pixelmap_HdrMetadataValue
```

## 概述

PhonePC/2in1TabletTVWearable

Pixelmap使用的HDR元数据值，和OH\_Pixelmap\_HdrMetadataKey关键字相对应。用于[OH\_PixelmapNative\_SetMetadata](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)，有相应[OH\_Pixelmap\_HdrMetadataKey](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](../../模块/Image_NativeModule/capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_HdrMetadataType](../../头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) type | HDR\_METADATA\_TYPE关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrStaticMetadata](../OH_Pixelmap_HdrStaticMetadata/capi-image-oh-pixelmap-hdrstaticmetadata.md) staticMetadata | HDR\_STATIC\_METADATA关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrDynamicMetadata](../OH_Pixelmap_HdrDynamicMetadata/capi-image-oh-pixelmap-hdrdynamicmetadata.md) dynamicMetadata | HDR\_DYNAMIC\_METADATA关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrGainmapMetadata](../OH_Pixelmap_HdrGainmapMetadata/capi-image-oh-pixelmap-hdrgainmapmetadata.md) gainmapMetadata | HDR\_GAINMAP\_METADATA关键字对应的具体值。 |
