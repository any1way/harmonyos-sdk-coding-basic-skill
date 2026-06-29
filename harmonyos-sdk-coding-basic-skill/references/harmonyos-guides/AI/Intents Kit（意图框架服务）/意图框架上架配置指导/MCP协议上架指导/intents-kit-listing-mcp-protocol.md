---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:07+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:2438e95a6f71817545b7a16ebb527a8b13d25edab4c16b3bad80f8ad29ac52be
---

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“[华为开发者联盟](https://developer.huawei.com/consumer/cn/) > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口。发布渠道为“智能体/小艺对话”只能使用与应用上架相同的账号登录，若发布渠道为“插件市场”则无特殊账号要求。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/ERs6FYJvQTmuHIx_Q0QAXw/zh-cn_image_0000002622859225.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=176494F28AFF30406B96DB0BEBA3C680178826771340ADC4A1CE0BAF6FE4CC61)
   2. 点击“立即体验”即可进入意图注册入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/HvnfEWjoTPiRdOb5k8Mv8w/zh-cn_image_0000002622699345.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=5054DAB2EB89AA48A371A1D311D71B494C79860F2364F56978C50980BC03BB49)
2. 注册意图集

   1. 如图，点击“注册意图”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/FOgf_GpXT_uWyH7jK1a-rQ/zh-cn_image_0000002592219784.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=E954FD51C33366D531CE753EEFC5F4949C15DF9191E2F25D256FE7129A90F92B)
   2. 选择“MCP协议”并填写基本信息创建意图集。

      1. 意图集（插件）名称：需唯一标识。
      2. 意图集（插件）描述：开发者自定义插件描述信息。
      3. 分类：按业务场景选择。
      4. MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      5. 认证信息配置：对应鉴权信息（注意放在Header/Query）。
      6. 协议类型：根据情况选择，提供SSE/Streamable两种。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/DFx14c85QmeRE4U68tA8ag/zh-cn_image_0000002592379718.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=0B3556409229902F56BFFFF9C84FD81D59225DB273A4CD2D16DF78839E3914F5)
3. 编辑：创建后自动进入”插件编辑“页面。

   1. 编辑基本信息：

      1. 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      2. 图标：192\*192。
      3. 使用描述：需使用Markdown格式。（需对server的功能概述、apikey申请方式表达准确清晰）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/FwutvZQCQzeHYeuNGL2gGw/zh-cn_image_0000002622859227.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=EE37D799D3B6DC826B7176B6018043D22680AC48CC056535345BCE164D179450)
4. 工具检查：保存后切换至"工具"页签。若基本信息配置无误，工具列表中会根据基本信息内容自动生成1条/多条信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ljRLZKe5QHKTs0y1RMtphQ/zh-cn_image_0000002622699347.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=C5ADCF3894A6115B6E73451F0C132C00D92B5E216BF46488B67B38F17BDEA8EB)

   1. 出现工具列表：请检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/U1uRfDGUR92CvQj0b7YGsQ/zh-cn_image_0000002592219786.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=87B6CF0D172BCF0809EA12B5892D87FD86B7E924671E82823DC5CD4E8E0FA27D)
   2. 未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。多次尝试后仍未解决，请通过邮箱联系华为意图框架同学（hagservice@huawei.com） 。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。
      1. 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。
      2. 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺APP主对话调用（当前暂不支持开发者独立在小艺主对话上线该能力，需联系华为意图框架同学）。
      3. 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供平台上其他开发者开发智能体时调用（回到开发者源头平台去开服）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/4etii-vyRRuATvtRTyd7qA/zh-cn_image_0000002592379720.png?HW-CC-KV=V1&HW-CC-Date=20260611T071905Z&HW-CC-Expire=86400&HW-CC-Sign=83E57C5BD60749089630CB066B6A75FDC852076B1CCCBD1E7DAFD972AB0FA251)
   2. 提交审核后，请耐心等待平台相关审核流程完成；完成后即可在“[华为开发者联盟](https://developer.huawei.com/consumer/cn/) > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架 > 小艺插件市场”中找到您的工具。
