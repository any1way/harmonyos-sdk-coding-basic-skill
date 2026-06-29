---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo
title: OH_Drawing_FontConfigInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontConfigInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:29:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:88de9984464c216c452015dfbfd8d2cc4c938bda8c4c92274e2320d48dc68997
---
```
1. typedef struct OH_Drawing_FontConfigInfo {...} OH_Drawing_FontConfigInfo
```

## 概述

PhonePC/2in1TabletTVWearable

系统字体配置信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](../../模块/Drawing/capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](../../头文件/drawing_text_typography.h/capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| size\_t fontDirSize | 系统字体文件路径数量。 |
| size\_t fontGenericInfoSize | 通用字体集列表数量。 |
| size\_t fallbackGroupSize | 备用字体集列表数量。 |
| char\*\* fontDirSet | 系统字体文件路径列表。 |
| [OH\_Drawing\_FontGenericInfo](../OH_Drawing_FontGenericInfo/capi-drawing-oh-drawing-fontgenericinfo.md)\* fontGenericInfoSet | 通用字体集列表。 |
| [OH\_Drawing\_FontFallbackGroup](../OH_Drawing_FontFallbackGroup/capi-drawing-oh-drawing-fontfallbackgroup.md)\* fallbackGroupSet | 备用字体集列表。 |
