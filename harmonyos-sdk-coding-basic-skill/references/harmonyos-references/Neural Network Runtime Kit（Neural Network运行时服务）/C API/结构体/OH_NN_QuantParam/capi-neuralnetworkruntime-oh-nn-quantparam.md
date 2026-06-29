---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-06-11T16:52:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:127f79275462a817c25056bb07ee083caad4f708da64ae5ffdb250894badf9e5
---
```
1. typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

PhonePC/2in1TabletTV

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/hCL5KpyQTKmn23_Ekm6fqQ/zh-cn_image_0000002592221384.png?HW-CC-KV=V1&HW-CC-Date=20260611T085215Z&HW-CC-Expire=86400&HW-CC-Sign=7E24397691BBD4C96F3A8A466DC178A73C550650BB2769531B1C02E9AB13AEC9)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xPjdv_FLR1-TQ7MRnHwq8Q/zh-cn_image_0000002592381316.png?HW-CC-KV=V1&HW-CC-Date=20260611T085215Z&HW-CC-Expire=86400&HW-CC-Sign=BAD5A3CCFD0B92D4673045AA86DCF6EC59F43EDDF19F61723B57D7CB0EDD21B9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/OBfMCp8PT-u8Pz1JUGGU6w/zh-cn_image_0000002622860827.png?HW-CC-KV=V1&HW-CC-Date=20260611T085215Z&HW-CC-Expire=86400&HW-CC-Sign=E458277CDD71CD82B24602681C6E7633EDB085347BC88BE71EAC150623D11EA9)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/EmOXaVYGS-e7_D7w0eg2zQ/zh-cn_image_0000002622700945.png?HW-CC-KV=V1&HW-CC-Date=20260611T085215Z&HW-CC-Expire=86400&HW-CC-Sign=AEE74CB57FFFC37DD8FB35CC1D8ECD7DB75B39AFAD5938B735F71CCE946D69BB)

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_QuantParam](../NN_QuantParam/capi-neuralnetworkruntime-nn-quantparam.md)

**相关模块：** [NeuralNetworkRuntime](../../模块/NeuralNetworkRuntime/capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](../../头文件/neural_network_runtime_type.h/capi-neural-network-runtime-type-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint32\_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32\_t \*numBits | 量化位数。 |
| const double \*scale | 指向量化公式中scale数据的指针。 |
| const int32\_t \*zeroPoint | 指向量化公式中zero point数据的指针。 |
