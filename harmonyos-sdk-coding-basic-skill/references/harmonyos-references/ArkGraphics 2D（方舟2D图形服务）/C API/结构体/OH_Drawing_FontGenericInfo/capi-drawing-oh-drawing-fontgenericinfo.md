---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo
title: OH_Drawing_FontGenericInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontGenericInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:29:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:434617dd0a1013d007fc169a2128333e86ae9056175ee4f8b2e2542909f2c5ae
---
```
1. typedef struct OH_Drawing_FontGenericInfo {...} OH_Drawing_FontGenericInfo
```

## 概述

PhonePC/2in1TabletTVWearable

系统所支持的通用字体集信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](../../模块/Drawing/capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](../../头文件/drawing_text_typography.h/capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* familyName | 字体家族名。 |
| size\_t aliasInfoSize | 别名字体列表的数量。 |
| size\_t adjustInfoSize | 字重映射列表的数量。 |
| [OH\_Drawing\_FontAliasInfo](../OH_Drawing_FontAliasInfo/capi-drawing-oh-drawing-fontaliasinfo.md)\* aliasInfoSet | 别名字体列表。 |
| [OH\_Drawing\_FontAdjustInfo](../OH_Drawing_FontAdjustInfo/capi-drawing-oh-drawing-fontadjustinfo.md)\* adjustInfoSet | 字重映射列表。 |
