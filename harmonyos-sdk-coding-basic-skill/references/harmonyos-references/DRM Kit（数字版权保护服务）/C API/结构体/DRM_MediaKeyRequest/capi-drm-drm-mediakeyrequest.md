---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest
title: DRM_MediaKeyRequest
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyRequest
category: harmonyos-references
scraped_at: 2026-06-11T16:30:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a40f1e0e148e183c4a30df2e44b57ee826dd412849aacd49796c3c02d5b30cc0
---
```
1. typedef struct DRM_MediaKeyRequest {...} DRM_MediaKeyRequest
```

## 概述

PhonePC/2in1TabletTVWearable

媒体密钥请求。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [DRM\_MediaKeyRequestType](../../头文件/native_drm_common.h/capi-native-drm-common-h.md#drm_mediakeyrequesttype) type | 媒体密钥请求类型。 |
| int32\_t dataLen | 媒体密钥请求数据长度。 |
| uint8\_t data[MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN] | 发送到媒体密钥服务器的媒体密钥请求数据。 |
| char defaultUrl[MAX\_DEFAULT\_URL\_LEN] | 媒体密钥服务器URL。 |
