---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-typetag
title: JSVM_TypeTag
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_TypeTag
category: harmonyos-references
scraped_at: 2026-06-11T16:53:12+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:42823a2e1cfb64419636b0de1d245c34377257d505d3101f09367094fc13079e
---
```
1. typedef struct {...} JSVM_TypeTag
```

## 概述

PhonePC/2in1TabletWearable

类型标记，存储为两个无符号64位整数的128位值。作为一个UUID，通过它，JavaScript对象可以是"tagged"，以确保它们的类型保持不变。

**使用场景：** 在跨语言交互（如C/C++与JavaScript交互）场景中，用于标记和识别JavaScript对象的类型。

**功能特点：** 提供128位唯一标识符，由两个64位整数组成，确保标识的唯一性和准确性。可附加到JavaScript对象上，实现类型标记和验证。

**解决的问题：** 解决JavaScript对象在跨语言交互中的类型识别问题。防止对象类型混淆或被错误识别。

**收益：** 确保JavaScript对象的类型保持一致性，提升跨语言交互的类型安全性。

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
| uint64\_t lower | 低64位 |
| uint64\_t upper | 高64位 |
