---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem
title: ArkUI_AttributeItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AttributeItem
category: harmonyos-references
scraped_at: 2026-06-01T15:51:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ebaa06124fc3b14150aa47bfc0beab9f2278d1f797ec4f5dd0f1bd28db9d3201
---
```
1. typedef struct {...} ArkUI_AttributeItem
```

## 概述

PhonePC/2in1TabletTVWearable

定义[setAttribute](../ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)函数通用入参结构。各个属性设置接口可选择使用其中的成员变量来存储特定类型的参数数据。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](../../头文件/native_node.h/capi-native-node-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const [ArkUI\_NumberValue](../ArkUI_NumberValue/capi-arkui-nativemodule-arkui-numbervalue.md)\* value | 数字类型数组，用于存储数字数组类型的参数。 |
| int32\_t size | 数字类型数组大小，配合变量value使用，value数组的长度。 |
| const char\* string | 字符串类型，用于存储字符串类型的参数。 |
| void\* object | 对象类型，用于存储对象类型的参数。 |
