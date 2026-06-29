---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo
title: DRM_KeysInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_KeysInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:31:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9981268f16fb37ae9b71697caebe6f96611f29f1050edf038823fcef47ce2a8
---
```
1. typedef struct DRM_KeysInfo {...} DRM_KeysInfo
```

## 概述

PhonePC/2in1TabletTVWearable

媒体密钥信息。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t keysInfoCount | 密钥计数。 |
| uint8\_t keyId[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_ID\_LEN] | 密钥ID集合。 |
| char statusValue[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_STATUS\_VALUE\_LEN] | 密钥状态值。 |
