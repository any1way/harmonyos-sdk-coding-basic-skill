---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime
title: NeuralNetworkRuntime
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 模块 > NeuralNetworkRuntime
category: harmonyos-references
scraped_at: 2026-06-01T16:41:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:354a28af4347aeecd51dbff47d351bea934591abf55973d73c60b6bef2508999
---
## 概述

PhonePC/2in1TabletTV

提供Neural Network Runtime加速模型推理的相关接口。

**起始版本：** 9

## 文件汇总

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [neural\_network\_core.h](../../头文件/neural_network_core.h/capi-neural-network-core-h.md) | Neural Network Core模块接口定义，AI推理框架使用Neural Network Core提供的Native接口，完成模型编译，并在加速硬件上执行推理和计算。  部分接口定义从neural\_network\_runtime.h移动至此头文件统一呈现，对于此类接口，API version 11 版本之前即支持使用，各版本均可正常使用。  Neural Network Core的接口目前均不支持多线程并发调用。 |
| [neural\_network\_runtime.h](../../头文件/neural_network_runtime.h/capi-neural-network-runtime-h.md) | Neural Network Runtime模块接口定义，AI推理框架使用Neural Network Runtime提供的Native接口，完成模型构建。  Neural Network Runtime的接口目前均不支持多线程并发调用。 |
| [neural\_network\_runtime\_type.h](../../头文件/neural_network_runtime_type.h/capi-neural-network-runtime-type-h.md) | Neural Network Runtime定义的结构体和枚举值。 |
