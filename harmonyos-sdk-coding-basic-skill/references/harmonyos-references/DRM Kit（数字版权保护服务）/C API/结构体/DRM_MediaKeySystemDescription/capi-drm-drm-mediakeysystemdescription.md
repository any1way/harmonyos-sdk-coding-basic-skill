---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysystemdescription
title: DRM_MediaKeySystemDescription
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeySystemDescription
category: harmonyos-references
scraped_at: 2026-06-11T16:31:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:768b77abbecd9869c7e82e05a698d561b7fb9db143a00290de761eba6d963f8b
---
```
1. typedef struct DRM_MediaKeySystemDescription {...} DRM_MediaKeySystemDescription
```

## 概述

PhonePC/2in1TabletTVWearable

DRM解决方案名称及其UUID的列表。

**起始版本：** 12

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char name[MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN] | DRM插件的名称。 |
| uint8\_t uuid[DRM\_UUID\_LEN] | UUID。 |
