---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-modify
title: 代码修改
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码修改
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e021375924827ed5819ba7fee26f154975fd2be99f82e31a68291677cb13e759
---
CodeGenie提供代码修改能力，在**对话框内**输入需求描述，生成符合要求的代码，提升代码质量与开发效率。

在DevEco Studio 6.0.1 Beta1和Release版本，生成的代码与原文件代码可快速对比和采纳。

从DevEco Studio 6.0.2 Beta1开始，生成的内容直接被应用到代码文件中。

从DevEco Studio 6.0.2 Release开始，代码修改使用的是HarmonyOS Act智能体。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Beta1版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框中输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，选择需要修改的代码文件，或在对话框输入文件路径指定需要修改的代码文件，或修改当前代码文件。
2. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/24Ao3D_mREGPcNOE1WLKyg/zh-cn_image_0000002602186353.png?HW-CC-KV=V1&HW-CC-Date=20260611T072223Z&HW-CC-Expire=86400&HW-CC-Sign=FBA6862654D44DE24F7361E4AEDAE4569BFF827E7779C6CF37CA655BF4A18083)发送。
3. 在问答区域的**Changed Files**可以查看被修改的文件；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ay4lyUhiSPCyz1j7QqCJKQ/zh-cn_image_0000002602066295.png?HW-CC-KV=V1&HW-CC-Date=20260611T072223Z&HW-CC-Expire=86400&HW-CC-Sign=D19B11D506C5C1D3EC2D723377FC6B7A5C1E79BD81D9E37121835A6F16CBC468)可接受或拒绝该文件的修改。
4. 点击问答区域中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](../../自定义智能体配置/自定义智能体（Agent）配置和调用/ide-agent-use.md#section2075893021715)。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/0NGV9X6kR_uncm9B0XlXNA/zh-cn_image_0000002571387176.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072223Z&HW-CC-Expire=86400&HW-CC-Sign=81CE1C5AC9530FB602A1E2E1810BCB024A2688AEB347EB6B2E99EB5E5587A424 "点击放大")

**DevEco Studio 6.0.1 Beta1**

**操作步骤**

1. 点击**@Add Context >** **Files**选择需要修改的文件，在对话框输入代码修改描述。
2. 在对话问答区域，点击文件路径，打开代码对比页面。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/dlYwJFnbSWesbPtIfcEDUg/zh-cn_image_0000002602066297.png?HW-CC-KV=V1&HW-CC-Date=20260611T072223Z&HW-CC-Expire=86400&HW-CC-Sign=88413BCD3F36EFF4938546E9E765E018A1A93ED11B0AF77174EBF285491E6FB3)，快速采纳修改后的代码。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/AimaCVIBTpiJ257HCPeDdA/zh-cn_image_0000002571546814.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072223Z&HW-CC-Expire=86400&HW-CC-Sign=1C8838B4721AD129A1152D4047954C27A61B60017EA89AF3B4B08672C21829D5 "点击放大")
