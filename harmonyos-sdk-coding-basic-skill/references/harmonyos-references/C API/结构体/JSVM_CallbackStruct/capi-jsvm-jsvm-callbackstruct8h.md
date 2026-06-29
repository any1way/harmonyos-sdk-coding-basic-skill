---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct8h
title: JSVM_CallbackStruct*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CallbackStruct*
category: harmonyos-references
scraped_at: 2026-06-11T16:53:28+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:a1c5ef42bfbd63ac211727821e35835a66c91b9357b83f035407f12bee37acc8
---
```
1. typedef JSVM_CallbackStruct* JSVM_Callback
```

## 概述

PhonePC/2in1TabletWearable

用户提供的native函数的函数指针类型，这些函数通过JSVM-API接口暴露给JavaScript。

**使用场景：** 在Native层实现JavaScript可调用的函数时使用，适用于JSVM扩展开发场景。

**解决的问题：** 定义标准化的函数指针类型，便于将C/C++函数暴露给JavaScript环境。

**功能特点：** 提供类型安全的函数指针定义，支持Native与JavaScript的交互。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
