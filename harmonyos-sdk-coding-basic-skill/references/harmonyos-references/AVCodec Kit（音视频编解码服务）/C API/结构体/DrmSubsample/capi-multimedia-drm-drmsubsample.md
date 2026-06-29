---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm-drmsubsample
title: DrmSubsample
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > DrmSubsample
category: harmonyos-references
scraped_at: 2026-06-01T16:18:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5253ffaedefc03cadc7015f792c96270909b88c00f7d390679518da9f1764929
---
```
1. typedef struct DrmSubsample {...} DrmSubsample
```

## 概述

PhonePC/2in1TabletTVWearable

Subsample结构类型定义。

**起始版本：** 12

**相关模块：** [Multimedia\_Drm](../../模块/Multimedia_Drm/capi-multimedia-drm.md)

**所在头文件：** [native\_cencinfo.h](../../头文件/native_cencinfo.h/capi-native-cencinfo-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t clearHeaderLen | 头部清流数据的长度。 |
| uint32\_t payLoadLen | 加密数据的长度。 |
