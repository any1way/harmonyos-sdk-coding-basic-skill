---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-recorderinfo
title: OH_RecorderInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_RecorderInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:12+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:b6bd8eeae0c95f8af4478831cd76a30cbd89b764f250d6e7fc41e96e3c44a276
---
```
1. typedef struct OH_RecorderInfo {...} OH_RecorderInfo
```

## 概述

PhonePC/2in1TabletTV

录制文件信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| char\* url | 录制文件的URL。 |
| uint32\_t urlLen | 录制文件的URL的长度值。 |
| [OH\_ContainerFormatType](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_containerformattype) fileFormat | 录制文件的格式。 |
