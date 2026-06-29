---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printdoccallback
title: Print_PrintDocCallback
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrintDocCallback
category: harmonyos-references
scraped_at: 2026-06-11T16:18:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5e868488c0a8b6fb77d517ef0bb6bcdf44017c6b87bf51d856b559a839892269
---
```
1. typedef struct {...} Print_PrintDocCallback
```

## 概述

PhonePC/2in1Tablet

表示打印文档状态回调结构体。

**起始版本：** 13

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_OnStartLayoutWrite](../../头文件/ohprint.h/capi-ohprint-h.md#print_onstartlayoutwrite) startLayoutWriteCb | 打印开始布局回调。 |
| [Print\_OnJobStateChanged](../../头文件/ohprint.h/capi-ohprint-h.md#print_onjobstatechanged) jobStateChangedCb | 打印任务状态回调。 |
