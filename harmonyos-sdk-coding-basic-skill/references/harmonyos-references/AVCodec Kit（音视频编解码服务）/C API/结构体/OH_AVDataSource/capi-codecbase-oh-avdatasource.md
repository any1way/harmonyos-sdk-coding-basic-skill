---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasource
title: OH_AVDataSource
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVDataSource
category: harmonyos-references
scraped_at: 2026-06-01T16:18:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c379316ab0a36b0b656f7e48cf27ee857978c12d2d5b9b1023e6bc18617fe7e5
---
```
1. typedef struct OH_AVDataSource {...} OH_AVDataSource
```

## 概述

PhonePC/2in1TabletTVWearable

用户自定义数据源。

**起始版本：** 12

**相关模块：** [CodecBase](../../模块/CodecBase/capi-codecbase.md)

**所在头文件：** [native\_avcodec\_base.h](../../头文件/native_avcodec_base.h/capi-native-avcodec-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t size | 数据源的总大小。 |
| [OH\_AVDataSourceReadAt](../../头文件/native_avcodec_base.h/capi-native-avcodec-base-h.md#oh_avdatasourcereadat) readAt | 数据源的数据回调。 |
