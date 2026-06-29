---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:38+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:c2de4912a7fb7b149508c433ad77e730e466223e0c43014ff2f348e42b543b9a
---
CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/bwnDqA5kRs2YSVmTvX2Ttg/zh-cn_image_0000002571387144.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=227498766CB08B18FF1C0F4C3352D89351C172D073D1E95EA2BE4A8FF180364E)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5QA3z5BiSC6x0FQ3ynGbdw/zh-cn_image_0000002602066267.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=C77298BFEFA82FF4F60DC86C42698A4212559D5B78E3F4EDE33A8A9BB7399ED3)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/MJPvB6B_QJ-78D_fWcWqwg/zh-cn_image_0000002602186315.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=993244F4A34DB00D64CC53CD107821D7807509252BC2E1BAB5DC4B0693A38FA5 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/sumVVilHQoyU0krir0UHnw/zh-cn_image_0000002571387150.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=02A25FC1504102B5A7B7DF5F339A5DC8DCB7B4FA1D7079C03CD978666F44ED92)按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加，推荐使用Service Provider方式。
   * 通过服务提供商添加。填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。CodeGenie已预置主流模型服务商的配置信息，填写API Key即可快速接入。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/gAn2XF3BRF2OHx7SNlLYvQ/zh-cn_image_0000002602066265.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=93F3062F969BD16575C1DAC3A24B2655C8105BD195F2F5B79581C1964B38F34C "点击放大")

     不同Service Provider的API Key和支持的模型如下：

     | Provider | API Key获取地址 | Model示例 |
     | --- | --- | --- |
     | OpenAI | https://platform.openai.com/api-keys | gpt-5.3-codex、gpt-5.4、gpt-5.5、gpt-5.6 |
     | Gemini | https://aistudio.google.com/apikey | gemini-3-pro-preview、gemini-3-flash-preview、gemini-3-pro-image-preview |
     | Anthropic | https://console.anthropic.com | claude-sonnet-4-5-20250929 |
     | DeepSeek | https://platform.deepseek.com | deepseek-v4-pro |
     | Alibaba Cloud | https://dashscope.console.aliyun.com | qwen3-coder-plus |
     | Z.ai | https://open.bigmodel.cn | glm-5 |
   * 通过URL添加。填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Url**：模型的访问地址。
     + **Protocol**：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/vfzmURVmSFGfSqjh67KClg/zh-cn_image_0000002571387146.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=678E142BC2F0FA39B5BF30BBB44C1DEA4361E4EE386046D77F5DB552F06B43B8 "点击放大")

     说明

     配置说明、URL配置示例等内容请参考[通过URL添加模型](ide-agent-model.md#section1684210554158)。
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/IoDmW3gJSY2GxD3gE5ziKA/zh-cn_image_0000002602066263.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=BE097839BDF3E02886799470E0B3251B8EEDFD7A86245E7D13E5129E357CDDF8 "点击放大")

## 附录

### 通过URL添加模型

**约束与限制**

* 暂不支持开启深度思考（Deep Thinking）功能和多模态图片处理功能。

**配置说明**

* 代理配置：为了避免代理问题造成的请求超时，将内网模型服务域名添加到[HTTP代理的No proxy for](../../../编写与调试应用/附录/配置代理/ide-environment-config.md#section10369436568)中。
* URL：填写URL时，若URL中包含"/chat/completions"后缀，请删除该部分，CodeGenie在请求时会自动拼接。示例如下：
  + 原URL： https://api.deepseek.com/chat/completions
  + 填写为： https://api.deepseek.com
* API Key：填写模型的访问密钥时不需要添加"Bearer"前缀。示例如下：
  + 原API Key：Bearer sk-f9e98c\*\*\*\*\*\*8
  + 填写为：sk-f9e98c\*\*\*\*\*\*8

**配置示例**

* 添加本地Ollama部署的模型

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Z4v_4tznTnuqUSTQDtnRsw/zh-cn_image_0000002583654166.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=B99E5BDA233E925F053632C9444CF4F5F408E74F9E37BB9ED34F427E1B791572)

* 添加DeepSeek模型（OpenAI协议）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/A2wsfs_FSdaRZqJJsdrWDA/zh-cn_image_0000002614013943.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=1A93D9EEF4761F822441D3B866ABF3C69C2454E0EED3208EE810999B92765F2B)
* 添加DeepSeek模型（Anthropic协议）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SmDZfnPIQpKSTOF0_cqSWw/zh-cn_image_0000002613894047.png?HW-CC-KV=V1&HW-CC-Date=20260611T072237Z&HW-CC-Expire=86400&HW-CC-Sign=F212D8552FD5B236BB443DDB52762EF694313D953D4001D3BEA9C12437BE819B)
