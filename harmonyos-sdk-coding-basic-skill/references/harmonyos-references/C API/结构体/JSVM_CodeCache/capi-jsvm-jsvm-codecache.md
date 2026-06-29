---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-codecache
title: JSVM_CodeCache
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CodeCache
category: harmonyos-references
scraped_at: 2026-06-11T16:53:15+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:f8c001286417a918011e7963b90dc864fd78102d88aee48ec841fdf7e8ce1fee
---
```
1. typedef struct {...} JSVM_CodeCache
```

## 概述

PhonePC/2in1TabletWearable

表示当id为JSVM\_COMPILE\_CODE\_CACHE时，content的类型。

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
| uint8\_t\* cache | 缓存地址。 |
| size\_t length | 缓存大小。 |
