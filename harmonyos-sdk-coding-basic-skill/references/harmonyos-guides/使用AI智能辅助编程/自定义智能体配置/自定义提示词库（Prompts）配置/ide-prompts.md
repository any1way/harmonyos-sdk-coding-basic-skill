---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:42+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:127d9e4b53838867d647d4b8a58ced4775425dae8c929d6efae80afcc96d7987
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/MH7c5UJsRAa9fD2G1Eo_sA/zh-cn_image_0000002602186231.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=53CC5AC330350211E71EB7EAD3EF38880EB6ABF5F57D564722C8CDDCFB053E20)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/pHs8YWUoT--69-m1GXoeJQ/zh-cn_image_0000002602186243.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=9DF7ECEF0E233F012C1366A965BE661E1B4E2B7C7256402BCB8EDA6D48465C4A)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/idQCx2J9SU2lNZZlEmQ5Hw/zh-cn_image_0000002571387076.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=8682720168D4687500D018106CBB42AE99E74146373D189022075EDA8C6600D9)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/UnAMgNDfRUyBH4Z8opMEBQ/zh-cn_image_0000002571387068.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=793959B07240A68D57938C16B6FC4FE90A79143E3B02512821F4D56D8885723C)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/hgoTjk56R6mDWP4i2o32Ig/zh-cn_image_0000002602186235.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=A587398718E5A17E5A4A498690A958368C85CA7F155ACF185C1D1608E8F9E47C)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/rMy2MFggRXi5sXlHCADvVg/zh-cn_image_0000002602066173.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=C11021677A21F9432065997D8C2CA8DDE28369C446207627120A29C53956150A)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/dHtx5I9cQVe96EZdYDcfFQ/zh-cn_image_0000002571387054.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=E55ABF78DE389434E66F9F9E6BC5516CDF9AB67BD9188F21C2710B23438EAA4F)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Eyjc8tLAQEKItTeUWpzK4g/zh-cn_image_0000002571387050.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=D242A975D6B9AF1598204D50DE3B99A16939B3E4EF3225985C2A6D8CBD5328EE)
