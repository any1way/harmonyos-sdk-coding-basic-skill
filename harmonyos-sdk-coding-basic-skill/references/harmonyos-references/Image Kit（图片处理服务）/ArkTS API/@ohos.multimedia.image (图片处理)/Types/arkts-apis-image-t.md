---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-t
title: Types
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Types
category: harmonyos-references
scraped_at: 2026-06-01T16:22:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1faa47e81723338fb345b141dce3bb3a4531c8abf383aa9b24708a17014b4bf5
---
说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## HdrMetadataValue12+

PhonePC/2in1TabletTVWearable

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](../Enums/arkts-apis-image-e.md#hdrmetadatakey12)关键字相对应。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 类型 | 说明 |
| --- | --- |
| [HdrMetadataType](../Enums/arkts-apis-image-e.md#hdrmetadatatype12) | [HdrMetadataKey](../Enums/arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_METADATA\_TYPE关键字对应的元数据值类型。 |
| [HdrStaticMetadata](<../Interfaces (其他)/arkts-apis-image-i.md#hdrstaticmetadata12>) | [HdrMetadataKey](../Enums/arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_STATIC\_METADATA关键字对应的元数据值类型。 |
| ArrayBuffer | [HdrMetadataKey](../Enums/arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_DYNAMIC\_METADATA关键字对应的元数据值类型。 |
| [HdrGainmapMetadata](<../Interfaces (其他)/arkts-apis-image-i.md#hdrgainmapmetadata12>) | [HdrMetadataKey](../Enums/arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_GAINMAP\_METADATA关键字对应的元数据值类型。 |
