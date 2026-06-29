---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-ref--8h
title: JSVM_Ref__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_Ref__*
category: harmonyos-references
scraped_at: 2026-06-11T16:53:24+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:fdd9e1b4878caaa78841312925921f8609a4ceaa555eeb56ed53ad9d264a8dad
---
```
1. typedef struct JSVM_Ref__* JSVM_Ref
```

## 概述

PhonePC/2in1TabletWearable

表示JavaScript值的引用。

**使用场景：** 在Native与JavaScript交互场景中，需要持有JavaScript对象引用时使用。

**功能特点：** 提供对JavaScript值的稳定引用，防止被垃圾回收。支持跨函数、跨作用域传递JavaScript值。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
