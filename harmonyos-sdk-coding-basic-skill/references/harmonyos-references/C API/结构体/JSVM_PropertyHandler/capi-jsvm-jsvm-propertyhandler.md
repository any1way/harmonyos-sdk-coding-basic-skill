---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandler
title: JSVM_PropertyHandler
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_PropertyHandler
category: harmonyos-references
scraped_at: 2026-06-11T16:53:16+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:b2c2c653aa3617c3960787402e9cac8b761c8caeaf2468e75512213cd8dfb9aa
---
```
1. typedef struct {...} JSVM_PropertyHandler
```

## 概述

PhonePC/2in1TabletWearable

包含将class作为函数进行调用时所触发的回调函数的函数指针，以及访问实例对象属性时触发的回调函数的函数指针集。

**使用场景：** 用于拦截和自定义对象的函数调用行为，用于实现属性访问的自定义逻辑。

**功能特点：** 支持在实例对象作为函数调用时触发自定义回调，支持在访问实例对象属性时触发相应的回调函数。

**能解决的问题：** 实现对象的代理模式，自定义函数调用行为。提供属性访问的拦截机制，增强代码的灵活性和可扩展性。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 18

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_PropertyHandlerCfg](../JSVM_PropertyHandlerConfigurationStruct/capi-jsvm-propertyhandlerconfigurationstruct8h.md) propertyHandlerCfg | 访问实例对象属性触发相应的回调函数。 |
| [JSVM\_Callback](../JSVM_CallbackStruct/capi-jsvm-jsvm-callbackstruct8h.md) callAsFunctionCallback | 实例对象作为函数调用将触发此回调。 |
