---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe
title: HiDebug_StackFrame
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_StackFrame
category: harmonyos-references
scraped_at: 2026-06-01T16:16:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f6bd9e3dea3310ddb7ce9b60f75b4dcf985b5b62a840216d4290209789c013c1
---
```
1. typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```

## 概述

PhonePC/2in1TabletTVWearable

栈帧内容的定义。

**起始版本：** 20

**相关模块：** [HiDebug](../../模块/HiDebug/capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](../../头文件/hidebug_type.h/capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [HiDebug\_StackFrameType](../../头文件/hidebug_type.h/capi-hidebug-type-h.md#hidebug_stackframetype) type | 当前栈的类型。 |
| struct [HiDebug\_JsStackFrame](../HiDebug_JsStackFrame/capi-hidebug-hidebug-jsstackframe.md) js | 由[HiDebug\_JsStackFrame](../HiDebug_JsStackFrame/capi-hidebug-hidebug-jsstackframe.md)定义的js栈帧内容。 |
| struct [HiDebug\_NativeStackFrame](../HiDebug_NativeStackFrame/capi-hidebug-hidebug-nativestackframe.md) native | 由[HiDebug\_NativeStackFrame](../HiDebug_NativeStackFrame/capi-hidebug-hidebug-nativestackframe.md)定义的native栈帧内容。 |
