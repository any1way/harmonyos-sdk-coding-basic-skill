---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertydescriptor
title: JSVM_PropertyDescriptor
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_PropertyDescriptor
category: harmonyos-references
scraped_at: 2026-06-11T16:53:10+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:4e482fc93a05afcd7d6f10dd1125568d964946dba07449019cea02913787cb7d
---
```
1. typedef struct {...} JSVM_PropertyDescriptor
```

## 概述

PhonePC/2in1TabletWearable

属性描述符。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| const char\* utf8name | 描述属性键值的可选字符串，UTF-8编码。必须为属性提供utf8name或name之一。 |
| [JSVM\_Value](../JSVM_Value__/capi-jsvm-jsvm-value--8h.md) name | 可选的JSVM\_Value，指向用作属性键的JavaScript字符串或符号。必须为属性提供utf8name或name之一。 |
| [JSVM\_Callback](../JSVM_CallbackStruct/capi-jsvm-jsvm-callbackstruct8h.md) method | 设置此项使属性描述符对象的value属性成为method表示的JavaScript函数。 |
| [JSVM\_Callback](../JSVM_CallbackStruct/capi-jsvm-jsvm-callbackstruct8h.md) getter | 执行对属性的获取访问时调用的函数。 |
| [JSVM\_Callback](../JSVM_CallbackStruct/capi-jsvm-jsvm-callbackstruct8h.md) setter | 执行属性的设置访问时调用的函数。 |
| [JSVM\_Value](../JSVM_Value__/capi-jsvm-jsvm-value--8h.md) value | 如果属性是数据属性，则通过属性的get访问检索到的值。 |
| [JSVM\_PropertyAttributes](../../头文件/jsvm_types.h/capi-jsvm-types-h.md#jsvm_propertyattributes) attributes | 与特定属性关联的属性。 |
