---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-keycodearray
title: Hid_KeyCodeArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_KeyCodeArray
category: harmonyos-references
scraped_at: 2026-06-11T16:23:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e08410a413b4eecf6b9353e344e08c5d039b8c8537a1895d45c6b4312ec081ed
---
```
1. typedef struct Hid_KeyCodeArray {...} Hid_KeyCodeArray
```

## 概述

PC/2in1

键值属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](../../模块/HidDdk/capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/hid_ddk_types.h/capi-hid-ddk-types-h.md>)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [Hid\_KeyCode](<../../../../硬件/Driver Development Kit（驱动开发服务）/C API/头文件/hid_ddk_types.h/capi-hid-ddk-types-h.md#hid_keycode>)\* hidKeyCode | 键值编码 |
| uint16\_t length | 数组的有效长度 |
