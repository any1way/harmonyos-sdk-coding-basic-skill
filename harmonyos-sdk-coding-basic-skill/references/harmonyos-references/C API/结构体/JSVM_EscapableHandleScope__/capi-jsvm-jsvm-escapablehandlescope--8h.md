---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-escapablehandlescope--8h
title: JSVM_EscapableHandleScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_EscapableHandleScope__*
category: harmonyos-references
scraped_at: 2026-06-11T16:53:26+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:b01d5aa882b0bbf508af73b6febf30062ed721fa66ac69355d06839d54784c1d
---
```
1. typedef struct JSVM_EscapableHandleScope__* JSVM_EscapableHandleScope
```

## 概述

PhonePC/2in1TabletWearable

表示一种特殊类型的handle scope，用于将在特定handle scope内创建的值返回到父作用域。

**使用场景：** 当需要在子函数中创建JS对象并将其返回给父函数或更上层作用域时使用，在JSVM API开发中，需要将局部创建的JS值传递出当前作用域的场景。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
