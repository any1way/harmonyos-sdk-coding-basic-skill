---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matrix-programming-operator
title: 矩阵编程算子实现
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 矩阵编程（高阶API） > 矩阵编程算子实现
category: harmonyos-guides
scraped_at: 2026-06-11T15:16:56+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:b73c0ae4ae457ced1036bd36868e6537ea620423c6afd95bcf92e1bb575aa10b
---
## 实现流程

上文介绍了Matmul矩阵乘的数据切分方案和数据流。AscendC提供一组Matmul高阶API，封装了这些常用的切分和数据搬运、计算的算法逻辑，方便开发者快速实现Matmul矩阵乘法的运算操作。开发者在host侧通过调用API自动获取Tiling参数，该参数传递到kernel侧后，在初始化操作时传入，通过几个简单的API即可完成矩阵乘操作。以下代码仅包含Matmul的关键步骤，不能直接运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/RxSOADlPQ_uD4o3BHCr5lA/zh-cn_image_0000002622699241.png?HW-CC-KV=V1&HW-CC-Date=20260611T071655Z&HW-CC-Expire=86400&HW-CC-Sign=9A2A822C3DBC357C2C0B30F2247B81388D7674EFC7AD9254D469461BD63C53EE)

**host侧自动获取Tiling参数的关键步骤介绍如下。**

1. 创建Tiling对象。

   ```
   1. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
   2. matmul_tiling::MatmulApiTiling cubeTiling(ascendcPlatform);
   ```

   创建对象时需要传入硬件平台信息，硬件平台信息可以通过[GetPlatformInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplatforminfo)获取。
2. 设置A、B、Bias的数据类型和格式。

   ```
   1. cubeTiling.SetAType(AscendC::TPosition::GM, CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
   2. cubeTiling.SetBType(AscendC::TPosition::GM, CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
   3. cubeTiling.SetCType(AscendC::TPosition::GM, CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
   4. cubeTiling.SetBiasType(AscendC::TPosition::GM, CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
   ```
3. 设置矩阵shape信息。

   ```
   1. cubeTiling.SetShape(M, N, K);
   2. cubeTiling.SetOrgShape(M, N, K);
   ```
4. 设置可用空间大小信息。

   ```
   1. cubeTiling.SetBufferSpace(-1, -1, -1);
   ```
5. 按需设置其他参数，比如设置bias参与计算。

   ```
   1. cubeTiling.SetBias(true);
   ```
6. 获取Tiling参数。

   ```
   1. MatmulCustomTilingData tiling;
   2. if (cubeTiling.GetTiling(tiling.cubeTilingData) == -1){
   3. return ge::GRAPH_FAILED;
   4. }
   ```
7. Tiling参数的序列化保存等其他操作。

**kernel侧使用Matmul API矩阵乘运算的具体步骤如下。**

1. 创建Matmul对象。示例如下。

   ```
   1. #include "lib/matmul_intf.h"
   2. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
   3. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
   4. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
   5. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
   6. matmul::Matmul<aType, bType, cType, biasType> mm;
   ```

   创建对象时需要传入A、B、C、Bias的参数类型信息， 类型信息通过MatmulType来定义，包括：内存逻辑位置、数据格式、数据类型。
2. 初始化操作。

   ```
   1. mm.Init(&tiling.cubeTilingData, &pipe); // 初始化
   ```
3. 设置左矩阵A、右矩阵B、Bias。

   ```
   1. mm.SetTensorA(gm_a); // 设置左矩阵A
   2. mm.SetTensorB(gm_b); // 设置右矩阵B
   3. mm.SetBias(gm_bias); // 设置Bias
   ```
4. 完成矩阵乘操作。

   * 调用Iterate完成单次迭代计算，叠加while循环完成单核全量数据的计算。Iterate方式，可以自行控制迭代次数，完成所需数据量的计算，方式比较灵活。

     ```
     1. while (mm.Iterate()) {
     2. mm.GetTensorC(gm_c);
     3. }
     ```
   * 调用IterateAll完成单核上所有数据的计算。IterateAll方式，无需循环迭代，使用比较简单。

     ```
     1. mm.IterateAll(gm_c);
     ```
5. 结束矩阵乘操作。

   ```
   1. mm.End();
   ```

## 设置format格式

创建Matmul对象时需要传入A、B、C、Bias的参数类型信息， 类型信息通过MatmulType来定义，包括：内存逻辑位置、数据格式、数据类型。示例如下。

```
1. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
2. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
3. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
4. typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
5. matmul::Matmul<aType, bType, cType, biasType> mm;
```

针对数据格式，包括CubeFormat::ND, CubeFormat::NZ, CubeFormat::ND\_ALIGN三种，ND和NZ格式在[数据格式](../基础知识/cannkit-basic-knowledge.md#数据格式)章节已经介绍。

ND\_ALIGN用于配置输出矩阵时按照一定的补齐规则进行输出。ND–>ND\_ALIGN变换过程下图所示，矩阵数据类型为uint32\_t，假设输出矩阵输出到UB，原矩阵N方向没有32字节对齐，设置ND\_ALIGN则在其后补0，将其对齐到32字节。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/1qsTtnhDRX-qNh8wqi8F5A/zh-cn_image_0000002592219680.png?HW-CC-KV=V1&HW-CC-Date=20260611T071655Z&HW-CC-Expire=86400&HW-CC-Sign=6BE59A74CCF8F551BBC8984BF10E2514712296088BEB0CC4FF6717BCD00F1DE5)

## 设置Shape信息

Host Tiling时可以设置Shape信息，用于Tiling计算；kernel侧运行时也可以修改部分shape信息，用于尾块设置、Matmul复用（多个Matmul计算复用一个Matmul对象）等场景。本节对涉及到的Shape概念进行介绍，并给出host侧和kernel侧设置Tiling信息的指导。

* orgShape：M、N、K
* singleCoreShape：singleCoreM、singleCoreN、singleCoreK
* singleShape：singleM、singleN、singleK
* baseShape：baseM、baseN、baseK

通过[数据分块(Tiling)](../基础知识/cannkit-basic-knowledge.md#数据分块tiling)的介绍我们已经了解了orgShape(M、N、K)，singleCoreShape(singleCoreM、singleCoreN、singleCoreK)，baseShape(baseM、baseN、baseK)的概念，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wd8gv7UOQ929UbnZY_F3Ng/zh-cn_image_0000002592379614.png?HW-CC-KV=V1&HW-CC-Date=20260611T071655Z&HW-CC-Expire=86400&HW-CC-Sign=E394188E7629534DFD3AC1A556050B4365D6030B499E6A4ABAE362319A5421EE)

除此之外，单核的Matmul Tiling时，实际参与Matmul计算的shape可以是原始shape中的一部分，singleM, singleN, singleK用于表达实际参与Matmul计算的shape，如下图所示。在单核的情况下，singleM, singleN, singleK会透传给singleCoreM, singleCoreN, singleCoreK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/IASHvVRqSYeB0Mnn4UHySA/zh-cn_image_0000002622859123.png?HW-CC-KV=V1&HW-CC-Date=20260611T071655Z&HW-CC-Expire=86400&HW-CC-Sign=996B71C38770F240B986D94195D7E71FD3B73C1CB9664A0AA43C6CB84972C850)
