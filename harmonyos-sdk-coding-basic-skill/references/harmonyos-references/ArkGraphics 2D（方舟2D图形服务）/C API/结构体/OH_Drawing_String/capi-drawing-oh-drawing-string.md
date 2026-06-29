---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-string
title: OH_Drawing_String
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_String
category: harmonyos-references
scraped_at: 2026-06-01T16:29:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d5ad4efb8c50bc0b485ff3f1c1ac57a0beaf903134d8f8fa948502e2e85f378
---
```
1. typedef struct {...} OH_Drawing_String
```

## 概述

PhonePC/2in1TabletTVWearable

采用UTF-16编码的字符串信息结构体。

**起始版本：** 14

**相关模块：** [Drawing](../../模块/Drawing/capi-drawing.md)

**所在头文件：** [drawing\_types.h](../../头文件/drawing_types.h/capi-drawing-types-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* strData | 指向包含UTF-16编码的字节数组的指针。 |
| uint32\_t strLen | strData指向的字符串的实际长度，单位为字节。 |
