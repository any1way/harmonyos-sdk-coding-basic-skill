---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-optimization
title: 异构
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 异构
category: harmonyos-guides
scraped_at: 2026-06-11T15:16:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19de5fe461adb8602266e1364491192f8644e08d41c2f86afa18aa954d1a564e
---
## 概述

异构是CANN Kit提供的异构计算能力，能够使开发者App在华为平台上充分享受到硬件平台的计算加速性能，同时提供非华为硬件平台的模型计算兼容性和计算加速，使开发者App开发过程归一化，不再需要为不同硬件平台适配不同模型或者计算框架，减少App开发及维护的难度。

异构的原理如下图所示，指定OP1、OP2、OP5~OPn在CPU上进行推理，OP3、OP4在NPU上进行推理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/wxjVakQrRO-Pr4tzbL9ygQ/zh-cn_image_0000002622699217.png?HW-CC-KV=V1&HW-CC-Date=20260611T071635Z&HW-CC-Expire=86400&HW-CC-Sign=6DA32BA0200F4B26566D9179BFDA7FE9C2BD191406D81567417F8A6B9BEFA6C0)

实现异构可以通过在线调优方式，以下为在线调优参数设置接口，接口使用见[在线调优开发步骤](cannkit-optimization.md#在线调优开发步骤)。如要使用更丰富的设置和查询接口，请参见[API参考](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md>)。

**表1** 在线调优接口及功能介绍

| 接口名 | 描述 |
| --- | --- |
| OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningMode(OH\_NNCompilation\* compilation, HiAI\_TuningMode tuningMode); | 芯片调优模式配置。 |
| OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningCacheDir(OH\_NNCompilation\* compilation, const char\* cacheDir); | 芯片调优缓存目录配置。 |

## 在线调优开发步骤

1. 设置芯片调优模式。

   * 调用[OH\_NNCompilation\_ConstructWithOfflineModelFile](<../../../../../harmonyos-references/Neural Network Runtime Kit（Neural Network运行时服务）/C API/头文件/neural_network_core.h/capi-neural-network-core-h.md#oh_nncompilation_constructwithofflinemodelfile>)，读取模型buffer，创建模型编译实例。
   * 调用[HMS\_HiAIOptions\_SetTuningMode](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md#hms_hiaioptions_settuningmode>)向模型编译实例中设置芯片调优模式调优选项。
2. 调用[HMS\_HiAIOptions\_SetTuningCacheDir](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md#hms_hiaioptions_settuningcachedir>)向模型编译实例中设置芯片调优缓存目录调优选项。
3. 执行模型编译。

   设置好所需调优选项参数后，通过调用[OH\_NNCompilation\_Build](<../../../../../harmonyos-references/Neural Network Runtime Kit（Neural Network运行时服务）/C API/头文件/neural_network_core.h/capi-neural-network-core-h.md#oh_nncompilation_build>)，传入创建模型编译实例，即可执行模型编译，编译成功则返回编译后的模型指针。后续流程同[模型推理](../模型推理/cannkit-model-inference.md)。

## 在线调优示例说明

以下示例代码设置调优参数SetTuningMode及SetTuningCacheDir，实现在线调优。

```
1. #include "neural_network_runtime/neural_network_core.h"
2. #include "CANNKit/hiai_options.h"
3. // 基于离线模型文件创建编译实例
4. OH_NNCompilation* compilation = OH_NNCompilation_ConstructWithOfflineModelFile("test.om");
5. if (compilation == nullptr) {
6. return;
7. }
8. // 选择辅助调优模式
9. OH_NN_ReturnCode ret = HMS_HiAIOptions_SetTuningMode(compilation, HIAI_TUNING_MODE_HETER);
10. if (ret != OH_NN_SUCCESS ) {
11. return;
12. }
13. // 设置辅助调优的缓存目录
14. const char* cacheDir = "/data/local/tmp";
15. ret = HMS_HiAIOptions_SetTuningCacheDir(compilation, cacheDir);
16. if (ret != OH_NN_SUCCESS ) {
17. return;
18. }
19. // 编译模型
20. ret = OH_NNCompilation_Build(compilation);
21. if (ret != OH_NN_SUCCESS ) {
22. return;
23. }
```
