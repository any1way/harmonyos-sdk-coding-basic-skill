---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent
title: 创建意图框架
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 创建意图框架
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:12+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:d491e1d2f8a1f4a9992d74af2e0c19c28e365d87becb689220582beda12bd683
---

DevEco Studio支持创建意图框架，帮助应用理解用户意图，并提供相应的服务和体验。

## 使用约束

* 支持API 11及以上工程创建意图框架；
* 仅支持在Stage工程的HAP模块中创建意图框架。

## 使用方式

1. 选中模块或模块下的文件，右键单击**New > Insight Intent**，进入意图框架配置界面。
   * **Intent domain**：意图垂域。
   * **Source entry name**：意图框架入口代码文件名。
   * **Intent Settings**：意图配置。以MusicDomain为例：
     + **PlayMusic：**开启/关闭PlayMusic意图能力，实现播放歌曲（指定一首）**。**默认需要关联UIAbility，可在**Ability name**中下拉框选择需要关联的Ability能力。
     + **PlayMusicList**：开启/关闭PlayMusicList意图能力，实现播放歌单（指定一整个歌单）**。**默认需要关联UIAbility，可在**Ability name**下拉框中选择需要关联的Ability能力。

     说明

     PlayMusic和PlayMusicList不支持同时关闭，请至少开启一个意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/jqJ4DykMShKPOfLAJ0XCVA/zh-cn_image_0000002602066653.png?HW-CC-KV=V1&HW-CC-Date=20260611T072211Z&HW-CC-Expire=86400&HW-CC-Sign=FFF623D7AF15F774CF4B0761138F13C00AAD1BE8437019775BE02B9687C563D0)
2. 点击**Finish**，完成意图框架创建。此时将在**entry > src > main > ets > insightintents**目录下生成入口代码文件；在**entry > src > main > resource > base > profile**中，生成**i****nsight\_intent.json**文件，可在该文件查看当前意图框架配置的相关信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Bst-GoTxT-evf71MEZBxNg/zh-cn_image_0000002571387536.png?HW-CC-KV=V1&HW-CC-Date=20260611T072211Z&HW-CC-Expire=86400&HW-CC-Sign=34A17EB86CB23125099801C0EEF6BC2F49F0BF332B5B175C3948FAB0D61FC4CF)
