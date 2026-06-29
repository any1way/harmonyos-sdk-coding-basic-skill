---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid
title: MediaLibrary_RequestId
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 结构体 > MediaLibrary_RequestId
category: harmonyos-references
scraped_at: 2026-06-01T16:26:12+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:c60b293c2d25cf4b43c9be81b3428889febb15891c1ef34ff8a6804c29c533c8
---
```
1. typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

## 概述

PhonePC/2in1TabletTVWearable

定义请求ID。

当请求媒体库资源时，会返回此类型。

请求ID可用于取消请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

**起始版本：** 12

**相关模块：** [MediaAssetManager](../../模块/MediaAssetManager/capi-mediaassetmanager.md)

**所在头文件：** [media\_asset\_base\_capi.h](../../头文件/media_asset_base_capi.h/capi-media-asset-base-capi-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char requestId[UUID\_STR\_MAX\_LENGTH] | 请求ID。 |
