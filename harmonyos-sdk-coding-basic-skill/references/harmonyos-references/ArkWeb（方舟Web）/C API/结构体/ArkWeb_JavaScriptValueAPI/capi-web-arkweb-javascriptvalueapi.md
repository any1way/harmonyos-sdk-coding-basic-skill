---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalueapi
title: ArkWeb_JavaScriptValueAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptValueAPI
category: harmonyos-references
scraped_at: 2026-06-01T15:56:15+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:aa24c8a8201a8e0ee16518152dbe1bb169ff8a14474a35864d84742fd00153ac
---
```
1. typedef struct {...} ArkWeb_JavaScriptValueAPI
```

## 概述

PhonePC/2in1TabletTVWearable

定义了ArkWeb的JavaScriptValue接口。在调用接口之前，建议使用[ARKWEB\_MEMBER\_MISSING](../../头文件/arkweb_type.h/capi-arkweb-type-h.md#宏定义)检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。

**起始版本：** 18

**相关模块：** [Web](../../模块/Web/capi-web.md)

**所在头文件：** [arkweb\_type.h](../../头文件/arkweb_type.h/capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| size\_t size | 结构体的大小。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkWeb\_JavaScriptValuePtr (\*createJavaScriptValue)(ArkWeb\_JavaScriptValueType type, void\* data, size\_t dataLength)](capi-web-arkweb-javascriptvalueapi.md#createjavascriptvalue) | 创建一个JavaScript值，用于返回给HTML。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### createJavaScriptValue()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_JavaScriptValuePtr (*createJavaScriptValue)(ArkWeb_JavaScriptValueType type, void* data, size_t dataLength)
```

**描述：**

创建一个JavaScript值，用于返回给HTML。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkWeb\_JavaScriptValueType type | JavaScript值的类型。 |
| void\* data | JavaScript值的数据缓冲区。 |
| size\_t dataLength | JavaScript值的缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_JavaScriptValuePtr](../ArkWeb_JavaScriptValue/capi-web-arkweb-javascriptvalue8h.md) | 创建出来的JavaScript值。当输入参数无效或内存分配失败时，返回NULL。 |
