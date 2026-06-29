---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:37+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:7232af3d9ba0acc2037f989298567af87f8f3b5d114079b9816d34066f9f9bf1
---

## 功能介绍

模型上下文协议（Model Context Protocol，简称MCP）是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置MCP。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP市场添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/SsbkwNHyQbeM34GwxFAf1A/zh-cn_image_0000002571386958.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=A858B37412DD98AC50FD1A3F07CD110026FAD99CB079877F85B5982030BB0DE9)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/uaw_9e6wRM2-QFjhoYuxzg/zh-cn_image_0000002571386948.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=EB0D8087782CDF962A62BE57C739AA11E13D4F71A80231F2B40ECE65C7B2157E)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/xP4J9G-yQa68n4zoDsJyNg/zh-cn_image_0000002602066081.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=6E6FA3A4C5179ECE5937BA93B577BFA75EACEB86E9CCC0E611804D6B3FE7697F "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/3x16KrqCQfSh99dHH0jHlw/zh-cn_image_0000002602186125.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=784F0DA3A37CCF55F9A55F5C180AA0DBE4534F8459BDF438995F5DCDBBEE11C9)按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP市场添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/WLTKIJNkTUqmsIQQ1og_Tw/zh-cn_image_0000002571386968.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=14BF74B3AF6EEFD112974324AC644C23FB6B304B6FA67A8FBA303557A1EAB021 "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     说明

     MCP Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Zu3CFzsATzCWAd2SiaG5sw/zh-cn_image_0000002602066077.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=8D7471027743901A67A3911B53159C67C097593E36E01774070E8BEB71C182A2 "点击放大")
   * **从MCP市场添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/N9c5caz_RXiZFpLQocpEVA/zh-cn_image_0000002602066067.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=C171A4C537A1660FB9BB9A5DEC79A970FD7AEDA94E0395349FD3E8E50A129D50)按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/FEKTwe2iRRyhK0SkG0xleg/zh-cn_image_0000002571386970.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=11BFE6BA12A063D09DDE2DCBBF55619BFACDCB45999223A46F9549C9B17B3F9D "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/n_gstlfLS2eY9TN4tScmAw/zh-cn_image_0000002602066079.png?HW-CC-KV=V1&HW-CC-Date=20260611T072236Z&HW-CC-Expire=86400&HW-CC-Sign=6423E3070A04B26C18B41DB083A228DA6D140BA9249664135C63C91BF416E5B2 "点击放大")
   * 名称：MCP工具名称，如time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
