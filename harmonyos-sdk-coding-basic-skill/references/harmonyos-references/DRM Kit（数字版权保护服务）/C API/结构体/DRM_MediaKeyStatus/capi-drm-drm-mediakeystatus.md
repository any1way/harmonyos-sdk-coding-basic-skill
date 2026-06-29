---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus
title: DRM_MediaKeyStatus
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyStatus
category: harmonyos-references
scraped_at: 2026-06-11T16:31:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:683b053c8c182ea53352c3c00e1c22dc2a422e5b6ec3014db1e0d1e0d4fbcdf4
---
```
1. typedef struct DRM_MediaKeyStatus {...} DRM_MediaKeyStatus
```

## 概述

PhonePC/2in1TabletTVWearable

媒体密钥状态。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t statusCount | 状态计数。 |
| char statusName[MAX\_MEDIA\_KEY\_STATUS\_COUNT][MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN] | 状态名数组。 |
| char statusValue[MAX\_MEDIA\_KEY\_STATUS\_COUNT][MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN] | 状态值数组。 |
