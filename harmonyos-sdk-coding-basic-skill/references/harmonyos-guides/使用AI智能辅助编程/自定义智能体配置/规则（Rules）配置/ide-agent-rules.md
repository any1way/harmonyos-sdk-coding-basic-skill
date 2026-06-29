---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:38+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:2b25071614664dc82aa51dac6a2e047cd5c706b62b8673751e585da23b0864f2
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

* **Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。
* **Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

说明

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/iq4IBXSnQ4GE6HRPLSTKCQ/zh-cn_image_0000002571386850.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=1897C452ADF68752A111AAEDA6741A31A7E39778DB7613240615D3FD3E877BF9)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/WvtrtabeQiGu2p9tBGZIEQ/zh-cn_image_0000002571546474.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=3C368D31678A6A74A9147E49E5C9D332B5DC2171DA63BBD15FE6B7FC80F9476E)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/PX8BpbMtTiW2sQRBt1mM8A/zh-cn_image_0000002571386840.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=2E208FB91E265CE2CD652718030FB7B7143A5E1415BD186C559950E10694EBFB)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/oRdZo_5URDiZmoV4u9TUWA/zh-cn_image_0000002602185997.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=23A9FB3B00872239FB33340A40B57B54E643566C877186E3C365CFA2A2433D7A)
3. 以有网络为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/KLV_emjHRTqlPFvGD4DBSA/zh-cn_image_0000002602065969.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=E27DE19F1ED369FB940378611B314F9E9818825898C25C51948C54AAACBB3422)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/y4yZLiXLSAeMvhiQ1V4sjA/zh-cn_image_0000002571386846.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=D42F3DE2AE7B068BE53E266BCE7B8B834FA243529A1B2CBB8FA1AEAB32B5D9FA)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/uZC1vbkBQ-Sxm1QX4H-Vaw/zh-cn_image_0000002602186003.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=DB9D6A4FB3B9EF9F36EE20F07686DC0E39C68A5C50A3FCF20D71932329C3F958)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/B0f-v3kWTiiHnEGlrIaXZQ/zh-cn_image_0000002602065973.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=CACA990F8A4A69A120FBFD1197DABB2645B96E6022EDF013B6E1FD7E198BEC2F)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/9WGpzPH7S9qRhIIJfYw0pw/zh-cn_image_0000002571386830.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=AF29A34E418BD457FCF667EC900FC8CD203AE7A8511E0B1AACB7D61FC8006754)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/vSSIIDcTRiy__9SLYmQeMA/zh-cn_image_0000002571546478.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=A268F773B6E23915B2230450DEA49457BA25F08AFE0764477DDA07CB04AC904C)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/6HwcIx5eTLO0LN1KqpA2FA/zh-cn_image_0000002602065941.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=C04141C06EE803444AC5AFFFDC492C29DB1BFF1C2448AAD11479BB28FF549682)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ojXhwzxjTAm4EStKOHMULQ/zh-cn_image_0000002602186013.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=A4FEBD2C1B6D443274FC5C03B66E7FE007E9100EC3C712E95D397671B74641DF)
