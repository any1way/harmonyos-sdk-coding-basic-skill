---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-use
title: 自定义智能体（Agent）配置和调用
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 自定义智能体（Agent）配置和调用
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:36+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:99e62d4e2a461aed81b6c5244dbe0ac11781a1d412e392767c580c02991d25c4
---
从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Beta1开始，自定义Agent配置时支持添加DevEco Studio内置的工具Built-in Tools、Auto Run和Blocklist。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始，DevEco Studio内置工具新增To Do工具，以及支持Agent智能体切换模型和配置三方模型。

从DevEco Studio 6.1.0 Beta2开始，DevEco Studio内置工具新增Web Rag工具；Blocklist变更为AllowList，在调用命令行工具执行命令时，白名单中的命令会自动执行。

从DevEco Studio 6.1.0 Release（6.1.0.830）版本开始，DevEco Studio内置工具新增Skill工具。

## Agent配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/WjCSm9YPTg2el0IFpfwL9g/zh-cn_image_0000002571546788.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=12B34FA545D778751CCC95467D169099B9793822E9E3F7D9BDE1606C7122BDCE)按钮；或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/SmovUEdTRo-PYUfiZCNs2A/zh-cn_image_0000002602186313.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=05A61A08487E15695944C72FA97EB9C7689E69AD95BFEC2E0A8E23E48AA62CDA)按钮，选择**Agent**；或者在输入框左下角下拉框选择**Create Agent**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/GWNQh8LQSom1ZRn2m1LkOg/zh-cn_image_0000002602186319.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=1AE2BB365A1E963DF7455B11F354238C019DC1401379E15B6EE8E3758BE7C022 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/gV0r5qVUTOSQZhMxEtlR3w/zh-cn_image_0000002602066271.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=8BB33731B512DAC3D8D59C29E53BB7369E0FB475C157C46AD30C0B11A9C63D58)按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。
   * **Name**：必填，自定义Agent的名称。
   * **Prompt Description**：可选，自定义Agent的提示词。
   * **MCP Tools**：可选，添加MCP工具，具体请参考[MCP配置](../模型上下文协议（MCP）配置/ide-agent-mcp.md)。
   * **Built-in Tools**：可选，开启或关闭File Manager、Terminal、Compile and Build、Web Rag、To Do、Skill，默认开启。
     + File Manager开启后，支持读写本地的代码文件。
     + Terminal开启后，在CodeGenie对话框执行命令时可自动拉起Terminal终端。
     + Compile and Build开启后，支持编译与构建项目。
     + Web Rag开启后，支持在问答过程中检索鸿蒙相关的资料，提升答复准确性。
     + To Do开启后，支持把一个复杂任务拆解成多步执行，帮助CodeGenie聚焦任务，避免遗忘任务，提升答复准确性。
     + Skill开启后，支持在自定义智能体中使用配置的Skill。
   * **Select Model**：必填，选择需要使用的模型，具体请参考[模型（Model）配置](../模型（Model）配置/ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/o8hoLoUtQhqJ-6x5YMtGWQ/zh-cn_image_0000002602066281.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=D38AF46E1853BC371A24F21D2EDE688F5CF23D27ECCA9AF5E6F071294F9C7DF3 "点击放大")
3. 在**All Agents**下展示所有智能体。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/zJgGt4ezS9y4Epqv3CHkSA/zh-cn_image_0000002602186339.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=C6A6B43EF9BC10E05E4F77D096A293845F3C6DE7E846C91FAE504E48C4CE9E60)
4. 设置自动执行开关和白名单列表。
   * **Auto Run**：内置工具（命令行工具除外）和MCP工具被调用过程中，自动执行的开启开关。开启时，工具被调用可自动执行和输出内容；关闭时，工具被调用需开发者授权。默认关闭。
   * **AllowList**：白名单列表，开启Auto Run后，白名单中的命令同样会自动执行。点击**Enter Command**中输入命令，点击**Add**可将命令添加至白名单列表；点击命令后×，可将命令从白名单列表中删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/6EcUcj68QeqzaGM0SIViUQ/zh-cn_image_0000002571546774.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=D48699D35C95E0282568B1EE1EDAA86E78A1CBD36B893EBEAE04DA8265EE7F2E "点击放大")
5. 选择自定义智能体后，开发者可以切换模型，包括内置模型/默认模型（deepseek-v3.2、glm-5）和三方模型（如deepseek）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ob1HOUXESfO1tvM7DOD7ug/zh-cn_image_0000002571546782.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=B09D90F93DE34FCC47A41986DC743CA494BA12A0B4D8C31378AAF5809A433848)
6. 点击置灰的三方模型会跳转到Service Provider配置界面（如**deepseek-chat**），填写**API Key**字段即可添加模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/yrGvjGf6Sie_sWiGgy11qQ/zh-cn_image_0000002602186311.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=661020D98EFEEF5A81767CF501FAEC7182282C5ACE1A78C54FE1D281D092E512 "点击放大")

## Agent调用

1. Agent配置完成后，可以通过如下两种方式开启调用：
   * 在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。从DevEco Studio 6.1.0 Beta2开始不支持。
   * 在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/R9SKE_SiRqmHjAYcnX8jJQ/zh-cn_image_0000002571546790.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=5EA9DDAF19E207B44391173C1531F7DC90D726AA285B48FF1D66718E3552BD68)
2. 选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/7LBUYq4ESt2oh5ETfRTh6A/zh-cn_image_0000002602186329.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=51DC11AA9C04778B46414D2B271B85018CD61B477C67BC30FF996D1B69BBC531 "点击放大")
3. 根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Ouzjlt3yTc-PLc0k69yhOA/zh-cn_image_0000002571387162.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=5B1D49E3DF875AEF6647CED3CF25129F2790C8C75845790AC3A5486BC252B4A5 "点击放大")
