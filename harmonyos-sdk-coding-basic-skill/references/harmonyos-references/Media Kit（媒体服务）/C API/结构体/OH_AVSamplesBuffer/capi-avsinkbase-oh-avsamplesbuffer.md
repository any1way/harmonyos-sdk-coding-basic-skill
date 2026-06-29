---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase-oh-avsamplesbuffer
title: OH_AVSamplesBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVSamplesBuffer
category: harmonyos-references
scraped_at: 2026-06-01T16:25:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:da4cfc22b300027aca8ebc3a3f8d31dd30821a9094dffc05859de252d1bcf659
---
```
1. typedef struct OH_AVSamplesBuffer OH_AVSamplesBuffer
```

## 概述

PhonePC/2in1Tablet

LowPowerAVSink输入数据的结构体。应用在收到DataNeeded回调后需要将数据打包装进OH\_AVSamplesBuffer实例中送给对应的lowpower\_avsink。

**起始版本：** 20

**相关模块：** [AVSinkBase](../../模块/AVSinkBase/capi-avsinkbase.md)

**所在头文件：** [lowpower\_avsink\_base.h](../../头文件/lowpower_avsink_base.h/capi-lowpower-avsink-base-h.md)
