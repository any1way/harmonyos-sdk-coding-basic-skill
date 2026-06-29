---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t
title: Types
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Types
category: harmonyos-references
scraped_at: 2026-06-01T16:20:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b7ad7cf46a67940447ea3af1b27c01924af093c0bc6f00a89e557bfc70fba82
---
说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ImageType

PhonePC/2in1TabletTVWearable

type ImageType = image.Image | image.Picture

图片容器类型，用于获取全质量图和未压缩图(YUV)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 类型 | 说明 |
| --- | --- |
| [image.Image](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Image)/arkts-apis-image-image.md>) | 图片容器类型，用于获取全质量图。 |
| [image.Picture](<../../../../Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md>) | 图片容器类型，用于获取未压缩图(YUV)。 |
