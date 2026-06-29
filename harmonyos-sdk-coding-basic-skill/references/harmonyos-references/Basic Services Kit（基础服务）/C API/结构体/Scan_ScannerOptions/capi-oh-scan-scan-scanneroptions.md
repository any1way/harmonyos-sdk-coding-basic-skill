---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions
title: Scan_ScannerOptions
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerOptions
category: harmonyos-references
scraped_at: 2026-06-11T16:18:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4150b4959cf2f31aca1d09f90f3fe4c2fc74f64b51d7ce2c113d3264838f838f
---
```
1. typedef struct {...} Scan_ScannerOptions
```

## 概述

PhonePC/2in1Tablet

表示一个扫描仪的所有参数选项

**起始版本：** 12

**相关模块：** [OH\_Scan](../../模块/OH_Scan/capi-oh-scan.md)

**所在头文件：** [ohscan.h](../../头文件/ohscan.h/capi-ohscan-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char\*\* titles | 选项标题 |
| char\*\* descriptions | 选项描述 |
| char\*\* ranges | 选项可设置的范围 |
| int32\_t optionCount | 可设置的参数选项数量 |
