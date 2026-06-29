---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:13377c8c03bd81e851a6029a5d3da6786e1e0354205d54a93da084b311be108c
---
部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[进程模型](<../../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/进程模型/process-model-stage.md#其他进程类型>)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/K9cP1kidSgOARY5NIeIyPw/zh-cn_image_0000002602066025.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=EFB967BA8815B2F47FFA58E2CA7692863CBEC3F851D8C15C4D2A625613808EA2)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/0f0J5cnGSqK_tBl6ZcQMrA/zh-cn_image_0000002602066023.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=9135C7DA87FB99E8694FDCA47344CF7AC6757752A0FD259C36151F61190C246D "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/3U8j1EX5S72ZwqoPSmVNaA/zh-cn_image_0000002602186073.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=FEBE6DBDD0B6223946679823A99FABD5FE141FA3CF9E108E58DF9E4D45F68476)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ULLCVCHiRVasBszk-XwdEA/zh-cn_image_0000002571386906.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=1571659C0D8BA47D6A8D74B090B73891884117176692401C6C44ECADD5D01FAB)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Cr4wF8WqSBeLw9hd7_xKKw/zh-cn_image_0000002571386908.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=82A0834CDA64A4E42D29BC85F607110330622DB4368A487E2502C74CFE35A472)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/QjfYqxqyRLyLhYft_z3xnw/zh-cn_image_0000002571546542.png?HW-CC-KV=V1&HW-CC-Date=20260611T072901Z&HW-CC-Expire=86400&HW-CC-Sign=C564293D49CB22D3572661AB056171E963EC3238FAA0F96DBF6720AA8D8515A5)
