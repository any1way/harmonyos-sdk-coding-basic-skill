---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray
title: Hid_EventTypeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventTypeArray
category: harmonyos-references
scraped_at: 2026-06-11T16:23:01+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:76ffd2063bf0deef77d8b4b11c7966292f79b6f7ef81ff6b98b7cf675db6718f
---
```
1. typedef struct Hid_EventTypeArray {...} Hid_EventTypeArray
```

## 概述

PC/2in1

事件类型编码数组。

**起始版本：** 11

**相关模块：** [HidDdk](../../模块/HidDdk/capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/hid_ddk_types.h/capi-hid-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [Hid\_EventType](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/hid_ddk_types.h/capi-hid-ddk-types-h.md#hid_eventtype>)\* hidEventType | 事件类型编码 |
| uint16\_t length | 数组的有效长度 |
