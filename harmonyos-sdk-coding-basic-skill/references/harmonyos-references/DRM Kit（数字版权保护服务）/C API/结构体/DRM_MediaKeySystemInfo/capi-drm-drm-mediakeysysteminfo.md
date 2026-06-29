---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo
title: DRM_MediaKeySystemInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeySystemInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:31:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14e3786a0065b6135d63d30b65431e0a0dad8d7dcc2d12dca16e888c44b73e62
---
```
1. typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```

## 概述

PhonePC/2in1TabletTVWearable

加密媒体内容的DRM信息。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t psshCount | PSSH计数。 |
| [DRM\_PsshInfo](../DRM_PsshInfo/capi-drm-drm-psshinfo.md) psshInfo[MAX\_PSSH\_INFO\_COUNT] | PSSH信息。 |
