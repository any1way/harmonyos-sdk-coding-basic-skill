---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-statistics
title: DRM_Statistics
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_Statistics
category: harmonyos-references
scraped_at: 2026-06-11T16:30:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4556c0ec1d93541fd3290f1cdb4bca1d84b7a56651c1912d32a232f20ed88a4b
---
```
1. typedef struct DRM_Statistics {...} DRM_Statistics
```

## 概述

PhonePC/2in1TabletTVWearable

MediaKeySystem的度量信息。

**起始版本：** 11

**相关模块：** [Drm](../../模块/Drm/capi-drm.md)

**所在头文件：** [native\_drm\_common.h](../../头文件/native_drm_common.h/capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t statisticsCount | 度量计数。 |
| char statisticsName[MAX\_STATISTICS\_COUNT][MAX\_STATISTICS\_NAME\_LEN] | 度量信息名称集合。 |
| char statisticsDescription[MAX\_STATISTICS\_COUNT][MAX\_STATISTICS\_BUFFER\_LEN] | 度量信息描述集合。 |
