---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm
title: JSVM
breadcrumb: API参考 > 公共基础能力 > C API > 模块 > JSVM
category: harmonyos-references
scraped_at: 2026-06-11T16:52:45+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:5789f204823f1cc4bb381f70e89263bc939691e0f84e5d1aced3e528df1002f3
---
## 概述

PhonePC/2in1TabletWearable

提供标准的JavaScript引擎能力。功能概述：标准JS引擎是严格遵守ECMAScript规范的JavaScript代码执行引擎。支持[ECMAScript规范](https://ecma262.com/)定义的标准库，提供完备的[C++交互JS的native API](../../../../harmonyos-guides/NDK开发/代码开发/使用JSVM-API实现JS与CC++语言交互/JSVM-API简介/jsvm-introduction.md)。通过JIT编译加速代码执行，为应用提供安全、高效的JS执行能力。标准JS引擎的能力通过一套稳定的ABI（Application Binary Interface，应用程序二进制接口），即JSVM-API（JavaScript Virtual Machine API）提供。JSVM-API支持动态链接到不同版本的JS引擎库，从而为开发者屏蔽掉不同引擎接口的差异。JSVM-API提供引擎生命周期管理、JS context管理、JS代码执行、JS/C++互操作、执行环境快照、code cache等能力。

使用平台：arm64平台。

使用方法：链接SDK中的libjsvm.so，并在C++代码中包含ark\_runtime/jsvm.h头文件。

**使用场景：** 需要实现C++与JavaScript的跨语言调用。

**解决的问题：** 提供标准的JavaScript执行环境，确保代码兼容性。

**带来的收益：** 严格遵守ECMAScript规范，确保JavaScript代码的标准化执行。JIT编译加速代码执行，提升应用性能。提供稳定的ABI接口，降低引擎升级成本。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。

## 文件汇总

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [jsvm.h](../../头文件/jsvm.h/capi-jsvm-h.md) | 提供JSVM-API接口定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。 |
| [jsvm\_types.h](../../头文件/jsvm_types.h/capi-jsvm-types-h.md) | 提供JSVM-API类型定义。通过API接口为开发者提供独立、标准、完整的JavaScript引擎能力，包括管理引擎生命周期、编译运行JS代码、实现JS/C++跨语言调用、拍摄快照等。 |
