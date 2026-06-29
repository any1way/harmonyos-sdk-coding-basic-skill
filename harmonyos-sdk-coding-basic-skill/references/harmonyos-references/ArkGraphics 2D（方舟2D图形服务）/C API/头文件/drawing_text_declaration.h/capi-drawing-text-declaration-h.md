---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-declaration-h
title: drawing_text_declaration.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_text_declaration.h
category: harmonyos-references
scraped_at: 2026-06-01T16:28:19+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a7071031d7f57631efecae1727b407e27a042b4bca8eb2a8130976d9e97ab06f
---
## 概述

PhonePC/2in1TabletTVWearable

提供2D绘制文本相关的数据结构声明。

**引用文件：** <native\_drawing/drawing\_text\_declaration.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](../../模块/Drawing/capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_FontCollection](../../结构体/OH_Drawing_FontCollection/capi-drawing-oh-drawing-fontcollection.md) | OH\_Drawing\_FontCollection | 用于加载字体。 |
| [OH\_Drawing\_Typography](../../结构体/OH_Drawing_Typography/capi-drawing-oh-drawing-typography.md) | OH\_Drawing\_Typography | 用于管理排版的布局和显示等。 |
| [OH\_Drawing\_TextStyle](../../结构体/OH_Drawing_TextStyle/capi-drawing-oh-drawing-textstyle.md) | OH\_Drawing\_TextStyle | 用于管理字体颜色、装饰等。 |
| [OH\_Drawing\_TypographyStyle](../../结构体/OH_Drawing_TypographyStyle/capi-drawing-oh-drawing-typographystyle.md) | OH\_Drawing\_TypographyStyle | 用于管理排版风格，如文字方向等。 |
| [OH\_Drawing\_LineTypography](../../结构体/OH_Drawing_LineTypography/capi-drawing-oh-drawing-linetypography.md) | OH\_Drawing\_LineTypography | 用于从一段文字中提取单行数据进行排版。 |
| [OH\_Drawing\_TypographyCreate](../../结构体/OH_Drawing_TypographyCreate/capi-drawing-oh-drawing-typographycreate.md) | OH\_Drawing\_TypographyCreate | 用于创建[OH\_Drawing\_Typography](../../结构体/OH_Drawing_Typography/capi-drawing-oh-drawing-typography.md)。 |
| [OH\_Drawing\_TextBox](../../结构体/OH_Drawing_TextBox/capi-drawing-oh-drawing-textbox.md) | OH\_Drawing\_TextBox | 用于接收文本框的矩形大小、方向和数量大小。 |
| [OH\_Drawing\_PositionAndAffinity](../../结构体/OH_Drawing_PositionAndAffinity/capi-drawing-oh-drawing-positionandaffinity.md) | OH\_Drawing\_PositionAndAffinity | 用于接收字体的位置和亲和性。 |
| [OH\_Drawing\_Range](../../结构体/OH_Drawing_Range/capi-drawing-oh-drawing-range.md) | OH\_Drawing\_Range | 用于接收字体的起始位置和结束位置。 |
| [OH\_Drawing\_TextShadow](../../结构体/OH_Drawing_TextShadow/capi-drawing-oh-drawing-textshadow.md) | OH\_Drawing\_TextShadow | 用于管理文本阴影。 |
| [OH\_Drawing\_FontParser](../../结构体/OH_Drawing_FontParser/capi-drawing-oh-drawing-fontparser.md) | OH\_Drawing\_FontParser | 用来解析系统字体文件。 |
| [OH\_Drawing\_TextTab](../../结构体/OH_Drawing_TextTab/capi-drawing-oh-drawing-texttab.md) | OH\_Drawing\_TextTab | 用于管理文本制表符。 |
| [OH\_Drawing\_TextLine](../../结构体/OH_Drawing_TextLine/capi-drawing-oh-drawing-textline.md) | OH\_Drawing\_TextLine | 用于管理文本行。 |
| [OH\_Drawing\_Run](../../结构体/OH_Drawing_Run/capi-drawing-oh-drawing-run.md) | OH\_Drawing\_Run | 用于管理文本渲染单元。 |
| [OH\_Drawing\_FontFullDescriptor](../../结构体/OH_Drawing_FontFullDescriptor/capi-drawing-oh-drawing-fontfulldescriptor.md) | OH\_Drawing\_FontFullDescriptor | 用于描述字体的详细信息，即字体描述符。 |
| [OH\_Drawing\_FontVariationAxis](../../结构体/OH_Drawing_FontVariationAxis/capi-drawing-oh-drawing-fontvariationaxis.md) | OH\_Drawing\_FontVariationAxis | 用于描述字体可变轴。 |
| [OH\_Drawing\_FontVariationInstance](../../结构体/OH_Drawing_FontVariationInstance/capi-drawing-oh-drawing-fontvariationinstance.md) | OH\_Drawing\_FontVariationInstance | 用于描述字体可变实例，存放预设的可变字体样式信息。 |
