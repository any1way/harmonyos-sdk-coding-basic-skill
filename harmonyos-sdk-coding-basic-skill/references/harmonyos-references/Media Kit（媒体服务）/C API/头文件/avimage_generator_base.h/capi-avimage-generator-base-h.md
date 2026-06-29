---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimage-generator-base-h
title: avimage_generator_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avimage_generator_base.h
category: harmonyos-references
scraped_at: 2026-06-01T16:24:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b319f2bd2bad9b51e0d14cf0d11775b75aebe673bfa4e8fcc85ccb383a0b10c3
---
## 概述

PhonePC/2in1TabletTVWearable

定义AVImageGenerator的枚举。

**引用文件：** <multimedia/player\_framework/avimage\_generator\_base.h>

**库：** libavimage\_generator.so

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**相关模块：** [AVImageGenerator](../../模块/AVImageGenerator/capi-avimagegenerator.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVImageGenerator\_QueryOptions](capi-avimage-generator-base-h.md#oh_avimagegenerator_queryoptions) | OH\_AVImageGenerator\_QueryOptions | 指定时间点与视频帧对应关系的枚举类型。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVImageGenerator\_QueryOptions

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVImageGenerator_QueryOptions
```

**描述**

指定时间点与视频帧对应关系的枚举类型。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_NEXT\_SYNC = 0 | 此选项用于选取传入时间点或之后的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_PREVIOUS\_SYNC = 1 | 此选项用于选取传入时间点或之前的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST\_SYNC = 2 | 此选项用于选取离传入时间点最近的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST = 3 | 此选项用于选取离传入时间点最近的帧，该帧不一定是关键帧。 |
