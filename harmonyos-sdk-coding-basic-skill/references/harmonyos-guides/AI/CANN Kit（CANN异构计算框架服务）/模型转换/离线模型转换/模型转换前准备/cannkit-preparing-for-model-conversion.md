---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparing-for-model-conversion
title: 模型转换前准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > 离线模型转换 > 模型转换前准备
category: harmonyos-guides
scraped_at: 2026-06-01T15:12:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f972742f24596765489bc06995b755279486ca6b846c35984d3b9a316758d081
---
CANN Kit当前仅支持Caffe、TensorFlow、ONNX和MindSpore模型转换为离线模型，其他格式的模型需要开发者自行转换为CANN Kit支持的模型格式。

1. 准备训练好的Caffe、TensorFlow、ONNX等模型。例如：[Caffe SqueezeNet V1.0](https://github.com/forresti/SqueezeNet)模型。
2. 下载[Tools](../../../开发准备/cannkit-preparations.md#tools下载)，解压使用Tools下的OMG工具，将TensorFlow或Caffe模型转换为IR模型，使用方式请参见[模型转换示例](../模型转换示例/cannkit-model-conversion-example.md)。

说明

若TensorFlow或Caffe模型过大，可以在OMG转换之前使用[Tools下载](../../../开发准备/cannkit-preparations.md#tools下载)的轻量化工具，使用方式请参见[模型轻量化](../../../模型优化/模型轻量化/概述/cannkit-lightweight-tool-overview.md)。
