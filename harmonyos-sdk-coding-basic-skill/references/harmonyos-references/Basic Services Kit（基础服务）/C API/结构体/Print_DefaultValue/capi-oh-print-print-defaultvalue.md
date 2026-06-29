---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-defaultvalue
title: Print_DefaultValue
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_DefaultValue
category: harmonyos-references
scraped_at: 2026-06-11T16:18:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:31ce6c0460186b657c6b35471b274fbb159ce6687653bb6a8854283c0b2166ed
---
```
1. typedef struct {...} Print_DefaultValue
```

## 概述

PhonePC/2in1Tablet

表示当前属性。

**起始版本：** 12

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_ColorMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_colormode) defaultColorMode | 默认色彩模式。 |
| [Print\_DuplexMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_duplexmode) defaultDuplexMode | 默认双面模式。 |
| char \*defaultMediaType | 默认介质类型。 |
| char \*defaultPageSizeId | 默认纸张尺寸 ID。 |
| [Print\_Margin](../Print_Margin/capi-oh-print-print-margin.md) defaultMargin | 默认边距。 |
| char \*defaultPaperSource | 默认纸张来源。 |
| [Print\_Quality](../../头文件/ohprint.h/capi-ohprint-h.md#print_quality) defaultPrintQuality | 默认打印质量。 |
| uint32\_t defaultCopies | 默认份数。 |
| [Print\_Resolution](../Print_Resolution/capi-oh-print-print-resolution.md) defaultResolution | 默认打印机分辨率。 |
| [Print\_OrientationMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_orientationmode) defaultOrientation | 默认方向。 |
| char \*otherDefaultValues | JSON 格式的其他默认值。 |
