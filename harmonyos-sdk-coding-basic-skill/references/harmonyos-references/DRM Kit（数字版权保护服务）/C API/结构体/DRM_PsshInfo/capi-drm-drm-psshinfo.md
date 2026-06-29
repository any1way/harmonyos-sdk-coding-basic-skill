---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo
title: DRM_PsshInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_PsshInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:31:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aed9e2c73cc141382ee0f722de79072349ee328a691be3827af10f74c618fffa
---
```
1. typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```

## 概述

PhonePC/2in1TabletTVWearable

DRM内容保护系统专用头（Protection System Specific Header）信息。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t uuid[DRM\_UUID\_LEN] | UUID的PSSH信息。 |
| int32\_t dataLen | PSSH数据长度。 |
| uint8\_t data[MAX\_PSSH\_DATA\_LEN] | PSSH数据。 |
