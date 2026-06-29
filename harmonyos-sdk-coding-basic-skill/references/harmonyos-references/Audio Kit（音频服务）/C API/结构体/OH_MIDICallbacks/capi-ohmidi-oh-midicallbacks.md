---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midicallbacks
title: OH_MIDICallbacks
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDICallbacks
category: harmonyos-references
scraped_at: 2026-06-01T16:17:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3a1500f8bcd82797e90687ef6c92588d90adf6889c47475509be3dea622d53e8
---
```
1. typedef struct {...} OH_MIDICallbacks
```

## 概述

PhonePC/2in1Tablet

客户端回调结构体，包含设备变化和错误处理的回调函数。

**起始版本：** 24

**相关模块：** [OHMIDI](../../模块/OHMIDI/capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](../../头文件/native_midi_base.h/capi-native-midi-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_MIDICallback\_OnDeviceChange](../../头文件/native_midi_base.h/capi-native-midi-base-h.md#oh_midicallback_ondevicechange) onDeviceChange | 处理设备热插拔事件的回调。  **起始版本：** 24 |
| [OH\_MIDICallback\_OnError](../../头文件/native_midi_base.h/capi-native-midi-base-h.md#oh_midicallback_onerror) onError | 处理关键服务错误的回调。  **起始版本：** 24 |
