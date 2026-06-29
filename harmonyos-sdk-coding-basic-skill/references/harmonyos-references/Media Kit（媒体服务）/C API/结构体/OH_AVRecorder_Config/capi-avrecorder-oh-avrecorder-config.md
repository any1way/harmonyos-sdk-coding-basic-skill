---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-config
title: OH_AVRecorder_Config
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Config
category: harmonyos-references
scraped_at: 2026-06-01T16:25:02+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:65903b0af54b86716aa6398927b388f8bccd5fc49874e4668786e534ac75dc16
---
```
1. typedef struct OH_AVRecorder_Config {...} OH_AVRecorder_Config
```

## 概述

PhonePC/2in1TabletTVWearable

提供媒体AVRecorder的配置定义。

**起始版本：** 18

**相关模块：** [AVRecorder](../../模块/AVRecorder/capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](../../头文件/avrecorder_base.h/capi-avrecorder-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVRecorder\_AudioSourceType](../../头文件/avrecorder_base.h/capi-avrecorder-base-h.md#oh_avrecorder_audiosourcetype) audioSourceType | 录制音频源类型。 |
| [OH\_AVRecorder\_VideoSourceType](../../头文件/avrecorder_base.h/capi-avrecorder-base-h.md#oh_avrecorder_videosourcetype) videoSourceType | 录制视频源类型。 |
| [OH\_AVRecorder\_Profile](../OH_AVRecorder_Profile/capi-avrecorder-oh-avrecorder-profile.md) profile | 包含音频和视频编码配置。 |
| char\* url | 定义文件URL，格式为fd://xx。 |
| [OH\_AVRecorder\_FileGenerationMode](../../头文件/avrecorder_base.h/capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode) fileGenerationMode | 指定录制输出文件的生成模式。 |
| [OH\_AVRecorder\_Metadata](../OH_AVRecorder_Metadata/capi-avrecorder-oh-avrecorder-metadata.md) metadata | 包含录制媒体的附加元数据。 |
| int32\_t maxDuration | 指定录制的最大时长，单位为秒。 |
