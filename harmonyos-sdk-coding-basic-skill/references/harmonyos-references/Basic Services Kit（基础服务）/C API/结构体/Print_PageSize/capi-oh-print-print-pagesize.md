---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-pagesize
title: Print_PageSize
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PageSize
category: harmonyos-references
scraped_at: 2026-06-11T16:18:40+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:58855fd389cf20726f4f50ffc67ba538ca5392a9ae644cd7c5d0efbfb5f6634b
---
```
1. typedef struct {...} Print_PageSize
```

## 概述

PhonePC/2in1Tablet

表示纸张尺寸信息。

**起始版本：** 12

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*id | 纸张 ID。 |
| char \*name | 纸张名称。 |
| uint32\_t width | 纸张宽度，单位：毫米。 |
| uint32\_t height | 纸张高度，单位：毫米。 |
