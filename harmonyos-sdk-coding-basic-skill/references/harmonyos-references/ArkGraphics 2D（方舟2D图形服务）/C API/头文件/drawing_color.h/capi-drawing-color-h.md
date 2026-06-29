---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-h
title: drawing_color.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_color.h
category: harmonyos-references
scraped_at: 2026-06-01T16:27:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:387613e3fa0ed6903aa6f351ed733299653457920baf773db2c05a5a0c00427f
---
## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与颜色相关的功能函数。

**引用文件：** <native\_drawing/drawing\_color.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](../../模块/Drawing/capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [uint32\_t OH\_Drawing\_ColorSetArgb(uint32\_t alpha, uint32\_t red, uint32\_t green, uint32\_t blue)](capi-drawing-color-h.md#oh_drawing_colorsetargb) | 用于将4个变量（分别描述透明度、红色、绿色和蓝色）转化为一个描述颜色的32位（ARGB）变量。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ColorSetArgb()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_ColorSetArgb(uint32_t alpha, uint32_t red, uint32_t green, uint32_t blue)
```

**描述**

用于将4个变量（分别描述透明度、红色、绿色和蓝色）转化为一个描述颜色的32位（ARGB）变量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t alpha | 描述透明度的变量, 变量范围是0x00~0xFF。 |
| uint32\_t red | 描述红色的变量, 变量范围是0x00~0xFF。 |
| uint32\_t green | 描述绿色的变量, 变量范围是0x00~0xFF。 |
| uint32\_t blue | 描述蓝色的变量, 变量范围是0x00~0xFF。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数返回一个描述颜色的32位（ARGB）变量。 |
