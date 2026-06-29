---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportinformation
title: OH_MIDIPortInformation
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIPortInformation
category: harmonyos-references
scraped_at: 2026-06-01T16:17:55+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:bf12c6a364df942aa7de96b27e999d91d536933a7ca6d9a475cc4ea36e42936b
---
```
1. typedef struct {...} OH_MIDIPortInformation
```

## 概述

PhonePC/2in1Tablet

端口信息结构体。用于枚举端口，包含可显示的端口名称。

**起始版本：** 24

**相关模块：** [OHMIDI](../../模块/OHMIDI/capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](../../头文件/native_midi_base.h/capi-native-midi-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t portIndex | 端口在设备中的索引号。  **起始版本：** 24 |
| int64\_t deviceId | 端口所属的MIDI设备ID。  **起始版本：** 24 |
| [OH\_MIDIPortDirection](../../头文件/native_midi_base.h/capi-native-midi-base-h.md#oh_midiportdirection) direction | 端口方向（输入或输出）。  **起始版本：** 24 |
| char name[64] | 端口名称。  **起始版本：** 24 |
