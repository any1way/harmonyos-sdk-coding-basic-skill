---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress
title: Scan_PictureScanProgress
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_PictureScanProgress
category: harmonyos-references
scraped_at: 2026-06-11T16:18:55+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:483cfd145dd2474b4f323644bb01ac0a874960e0ad4a191c9e533b622f7d4b0e
---
```
1. typedef struct {...} Scan_PictureScanProgress
```

## 概述

PhonePC/2in1Tablet

表示扫描仪扫描图片的进度

**起始版本：** 12

**相关模块：** [OH\_Scan](../../模块/OH_Scan/capi-oh-scan.md)

**所在头文件：** [ohscan.h](../../头文件/ohscan.h/capi-ohscan-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t progress | 图片的扫描进度，从0到100，单位：百分比。 |
| int32\_t fd | 扫描仪文件句柄 |
| bool isFinal | 指示该图像是否为最后扫描的图像。true表示该图像是最后扫描的图像，false表示该图像不是最后扫描的图像。 |
