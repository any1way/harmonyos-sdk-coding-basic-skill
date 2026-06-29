---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo
title: JSVM_VMInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_VMInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:53:09+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:1d36745df066967d3fe027fc343c5b560cde818431c40c86ba1dc05f282ad3c2
---
```
1. typedef struct {...} JSVM_VMInfo
```

## 概述

PhonePC/2in1TabletWearable

JavaScript虚拟机信息。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char\* engine | 实现虚拟机的引擎名称。 |
| const char\* version | 虚拟机的版本。 |
| uint32\_t cachedDataVersionTag | 缓存数据版本标签。 |
