---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-envscope--8h
title: JSVM_EnvScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_EnvScope__*
category: harmonyos-references
scraped_at: 2026-06-11T16:53:19+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:1320634a9a94ebe1206fc868db941aa4fcc02bb223821f49d41fcf6150dd60f6
---
```
1. typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

## 概述

PhonePC/2in1TabletWearable

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH\_JSVM\_OpenEnvScope进入该环境的JSVM\_EnvScope后，该环境才对线程的虚拟机实例可用。

**使用场景：** 在多线程环境下需要访问和操作JavaScript环境时，用于管理和切换环境作用域。

**解决的问题：** 解决多线程环境下对同一虚拟机实例的环境访问和隔离问题。

**带来的收益：** 为开发者提供线程安全的环境管理机制，确保多线程访问的正确性和隔离性。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

**相关模块：** [JSVM](../../模块/JSVM/capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md)
