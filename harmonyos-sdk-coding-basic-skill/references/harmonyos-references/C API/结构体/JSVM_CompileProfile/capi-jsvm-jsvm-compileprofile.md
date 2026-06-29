---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile
title: JSVM_CompileProfile
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CompileProfile
category: harmonyos-references
scraped_at: 2026-06-11T16:53:31+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:ae5195f90f4e2df5f547f414109bdb128047a46492d1f10119762da86a035ed4
---
```
1. typedef const struct {...} JSVM_CompileProfile
```

## 概述

PhonePC/2in1TabletWearable

与JSVM\_COMPILE\_COMPILE\_PROFILE一起传递的编译采样文件。

**使用场景：** 用于应用二次启动时的预编译优化，可提升应用启动速度和运行性能。适用于需要优化启动性能的应用场景。

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
| int \*profile | 编译采样文件的指针。 |
| size\_t length | 编译采样文件的大小。 |
