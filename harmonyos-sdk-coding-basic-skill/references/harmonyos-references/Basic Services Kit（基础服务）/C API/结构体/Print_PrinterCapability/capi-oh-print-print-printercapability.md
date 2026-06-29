---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printercapability
title: Print_PrinterCapability
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrinterCapability
category: harmonyos-references
scraped_at: 2026-06-11T16:18:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8e1540be6ea882416e51fb0867b3107deb28101f32b77186b130c47147735863
---
```
1. typedef struct {...} Print_PrinterCapability
```

## 概述

PhonePC/2in1Tablet

表示打印机能力。

**起始版本：** 12

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_ColorMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_colormode) \*supportedColorModes | 支持的色彩模式数组。 |
| uint32\_t supportedColorModesCount | 支持的色彩模式数量。 |
| [Print\_DuplexMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_duplexmode) \*supportedDuplexModes | 支持的双面打印模式数组。 |
| uint32\_t supportedDuplexModesCount | 支持的双面打印模式数量。 |
| [Print\_PageSize](../Print_PageSize/capi-oh-print-print-pagesize.md) \*supportedPageSizes | 支持的打印纸张尺寸数组。 |
| uint32\_t supportedPageSizesCount | 支持的打印纸张尺寸数量。 |
| char \*supportedMediaTypes | JSON 字符串数组格式的支持的打印介质类型。 |
| [Print\_Quality](../../头文件/ohprint.h/capi-ohprint-h.md#print_quality) \*supportedQualities | 支持的打印质量数组。 |
| uint32\_t supportedQualitiesCount | 支持的打印质量数量。 |
| char \*supportedPaperSources | JSON 字符串数组格式的支持的纸张来源。 |
| uint32\_t supportedCopies | 支持的份数。 |
| [Print\_Resolution](../Print_Resolution/capi-oh-print-print-resolution.md) \*supportedResolutions | 支持的打印机分辨率数组。 |
| uint32\_t supportedResolutionsCount | 支持的打印机分辨率数量。 |
| [Print\_OrientationMode](../../头文件/ohprint.h/capi-ohprint-h.md#print_orientationmode) \*supportedOrientations | 支持的方向数组。 |
| uint32\_t supportedOrientationsCount | 支持的方向数量。 |
| char \*advancedCapability | JSON 格式的高级能力。 |
