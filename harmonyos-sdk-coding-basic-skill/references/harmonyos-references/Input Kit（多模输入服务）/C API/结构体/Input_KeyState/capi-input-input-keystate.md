---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate
title: Input_KeyState
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_KeyState
category: harmonyos-references
scraped_at: 2026-06-11T16:20:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b097bb27e57404f609614322ea4963f719bd482336d5a2fefb17645c22a63b56
---
```
1. typedef struct Input_KeyState Input_KeyState
```

## 概述

PhonePC/2in1TabletTVWearable

定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。

**起始版本：** 12

**相关模块：** [input](../../模块/input/capi-input.md)

**所在头文件：** [oh\_input\_manager.h](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateKeyState](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_createkeystate) | 创建按键状态的枚举对象。通过调用[OH\_Input\_DestroyKeyState](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_destroykeystate)销毁按键状态的枚举对象。 |
| [OH\_Input\_DestroyKeyState](../../头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_destroykeystate) | 销毁按键状态的枚举对象。 |
