---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midievent
title: OH_MIDIEvent
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIEvent
category: harmonyos-references
scraped_at: 2026-06-01T16:17:53+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3f16578619fa4ca4a359bf37a783515b9092e16f508e4325d334b1df75e4c783
---
```
1. typedef struct {...} OH_MIDIEvent
```

## 概述

PhonePC/2in1Tablet

MIDI事件结构体（通用）。适用于原始字节流（MIDI 1.0）和UMP（Universal MIDI Packet）两种数据格式。

**起始版本：** 24

**相关模块：** [OHMIDI](../../模块/OHMIDI/capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](../../头文件/native_midi_base.h/capi-native-midi-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint64\_t timestamp | 时间戳，单位为纳秒。  通过clock\_gettime(CLOCK\_MONOTONIC, &time)获取基准时间。值为0表示立即发送。  **起始版本：** 24 |
| size\_t length | UMP数据包中的32位字（word）数量。  例如：Type 2/4消息占1个字（64位消息占2个字）。  此字段表示UMP数据中uint32\_t字的数量，而非字节数。  **起始版本：** 24 |
| uint32\_t \*data | 指向UMP数据的指针，包含原始UMP字（uint32\_t）。  此指针必须指向4字节对齐的内存地址，以满足UMP规范对32位边界对齐的要求。  **起始版本：** 24 |
