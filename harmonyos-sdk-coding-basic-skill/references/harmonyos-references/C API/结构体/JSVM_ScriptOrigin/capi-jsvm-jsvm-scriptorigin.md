---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-scriptorigin
title: JSVM_ScriptOrigin
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ScriptOrigin
category: harmonyos-references
scraped_at: 2026-06-11T16:53:14+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:d7d84d60a167d3be34e848e66d328abc103d8dd99c6e7fdbfc565644c30bcff9
---
```
1. typedef struct {...} JSVM_ScriptOrigin
```

## 概述

PhonePC/2in1TabletWearable

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| const char\* sourceMapUrl | Sourcemap 路径。 |
| const char\* resourceName | 源文件名。 |
| size\_t resourceLineOffset | 这段代码在源文件中的起始行号。 |
| size\_t resourceColumnOffset | 这段代码在源文件中的起始列号。 |
