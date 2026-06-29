---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deferred--8h
title: JSVM_Deferred__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_Deferred__*
category: harmonyos-references
scraped_at: 2026-06-11T16:53:28+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:405251a766af9653f56d3b10b997f1868ad810606d0d8d49936b63f366d58954
---
```
1. typedef struct JSVM_Deferred__* JSVM_Deferred
```

## 概述

PhonePC/2in1TabletWearable

表示Promise延迟对象。

**使用场景：** 在JSVM Native模块中需要创建Promise对象并延迟处理异步操作结果时，需要在Native层手动控制Promise的resolve或reject时机的场景，将Native层的异步操作结果封装为Promise返回给JavaScript层。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
