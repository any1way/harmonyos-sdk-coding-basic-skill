---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-settimerparam
title: HiCollie_SetTimerParam
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiCollie_SetTimerParam
category: harmonyos-references
scraped_at: 2026-06-01T16:15:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1055fdf747d36cef917c0567cfbb61bee29bd7093bb374fd22c855b50d94e916
---
```
1. typedef struct HiCollie_SetTimerParam {...} HiCollie_SetTimerParam
```

## 概述

PhonePC/2in1TabletTVWearable

定义OH\_HiCollie\_SetTimer函数的输入参数。

**起始版本：** 18

**相关模块：** [HiCollie](../../模块/HiCollie/capi-hicollie.md)

**所在头文件：** [hicollie.h](../../头文件/hicollie.h/capi-hicollie-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \*name | timer任务名称。 |
| unsigned int timeout | 任务超时时间阈值，单位：s。 |
| [OH\_HiCollie\_Callback](../../头文件/hicollie.h/capi-hicollie-h.md#oh_hicollie_callback) func | 超时发生时执行的回调函数。 |
| void \*arg | 回调函数的参数。 |
| [HiCollie\_Flag](../../头文件/hicollie.h/capi-hicollie-h.md#hicollie_flag) flag | 超时发生时执行的动作，参考[HiCollie\_Flag](../../头文件/hicollie.h/capi-hicollie-h.md#hicollie_flag)。 |
