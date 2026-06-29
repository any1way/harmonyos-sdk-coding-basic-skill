---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-datavalue
title: ImageEffect_DataValue
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageEffect_DataValue
category: harmonyos-references
scraped_at: 2026-06-01T16:23:34+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:7b933dc4b36c58a55180cac17c4947cbd2f4cc52396f4871cf2af453ef96b443
---
```
1. typedef union ImageEffect_DataValue {...} ImageEffect_DataValue
```

## 概述

PhonePC/2in1TabletTV

数据值联合体。

**起始版本：** 12

**相关模块：** [ImageEffect](../../模块/ImageEffect/capi-imageeffect.md)

**所在头文件：** [image\_effect\_filter.h](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t int32Value | 整型值，对应[EFFECT\_DATA\_TYPE\_INT32](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| float floatValue | 单精度浮点值，对应[EFFECT\_DATA\_TYPE\_FLOAT](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| double doubleValue | 双精度浮点值，对应[EFFECT\_DATA\_TYPE\_DOUBLE](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| char charValue | 字节值，对应[EFFECT\_DATA\_TYPE\_CHAR](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| long longValue | 长整型值，对应[EFFECT\_DATA\_TYPE\_LONG](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| bool boolValue | 布尔值，对应[EFFECT\_DATA\_TYPE\_BOOL](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
| void \*ptrValue | 指针值，对应[EFFECT\_DATA\_TYPE\_PTR](../../头文件/image_effect_filter.h/capi-image-effect-filter-h.md#imageeffect_datatype)。 |
