---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-propertylist
title: Print_PropertyList
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PropertyList
category: harmonyos-references
scraped_at: 2026-06-11T16:18:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6cfd8fba60f7b80fe7793b13013c3248fe2eb8ffff5a401e43f0eb6bf0159319
---
```
1. typedef struct {...} Print_PropertyList
```

## 概述

PhonePC/2in1Tablet

打印机属性列表。

**起始版本：** 12

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 属性数量。 |
| [Print\_Property](../Print_Property/capi-oh-print-print-property.md) \*list | 属性指针数组。 |
