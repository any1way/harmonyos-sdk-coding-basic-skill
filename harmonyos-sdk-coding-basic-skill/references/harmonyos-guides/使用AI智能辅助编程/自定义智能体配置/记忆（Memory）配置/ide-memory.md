---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memory
title: 记忆（Memory）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 记忆（Memory）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:42+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:b0f4c17cd8bc2b295d85bc5183664926fac8f2f3be0551684174929c6bbe8a7b
---
## 功能介绍

CodeGenie搭载长期记忆功能，在应用开发过程中，会学习和提取个人偏好、项目细节等有价值的信息，进行主动记忆或自动记忆。伴随开发者的持续使用，逐步形成覆盖开发者信息、项目场景、问题沉淀的全域记忆体系。在长期交互中，记忆也会随时间更新。

依托这一核心能力，CodeGenie能够精准理解和生成符合开发者需求的代码、回答等，与开发者实现更高效的协作。

### 基本概念

* 主动记忆：开发者要求CodeGenie记住输入的内容，CodeGenie会保存这些信息。
* 自动记忆：自动提取对话中有价值的信息，记录任务执行进度，随时间推移学习开发者的编码风格和项目细节等。

### 使用约束

* 当前仅自定义Agent支持长期记忆检索和生成。
* 当CodeGenie记忆与[规则（Rules）](../规则（Rules）配置/ide-agent-rules.md)发生冲突时，以规则为准。
* Mac(64-bit)架构的MacOS操作系统不支持记忆能力。

## 操作步骤

1. 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/WuCWXaMmRuKwv7LheJSDXQ/zh-cn_image_0000002571546642.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=AB85D87393493A4609B43B241A83CA962879F65379802BA9680D5D076C3E7006)按钮，选择**Memory**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/4ukawzDCTYeQcm5GKZFAWg/zh-cn_image_0000002602066127.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=38F8CE39973492612561F1FB8E6E03C39C9E665FD7886122312501C361C99871)
2. 点击Memory后开关，开启和关闭记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Tllj7c4mSsmV6vkUQyQLoQ/zh-cn_image_0000002602186179.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=551168BC2A970F7098B96019EDBD5E86A045B94183C3908AE2D58847EEB10975)
3. 在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/OHSLjjqHR8W-IBMc1HMFHA/zh-cn_image_0000002571387014.png?HW-CC-KV=V1&HW-CC-Date=20260611T072241Z&HW-CC-Expire=86400&HW-CC-Sign=EB0C464C42ED0BBD6A04A9D5DBD6736B81DA22DB7D7869A9209387812695FDC0 "点击放大")
