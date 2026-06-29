---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks
title: MetadataOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > MetadataOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-06-01T16:21:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:88564a773fdf8e0f1dca5efaa244b8b2da1a025b499217e669f38d9029a04a73
---
```
1. typedef struct MetadataOutput_Callbacks {...} MetadataOutput_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

元数据输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](../../模块/OH_Camera/capi-oh-camera.md)

**所在头文件：** [metadata\_output.h](../../头文件/metadata_output.h/capi-metadata-output-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_MetadataOutput\_OnMetadataObjectAvailable](../../头文件/metadata_output.h/capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectavailable) onMetadataObjectAvailable | 此回调将调用元数据输出结果数据。 |
| [OH\_MetadataOutput\_OnError](../../头文件/metadata_output.h/capi-metadata-output-h.md#oh_metadataoutput_onerror) onError | 元数据输出错误事件。 |
