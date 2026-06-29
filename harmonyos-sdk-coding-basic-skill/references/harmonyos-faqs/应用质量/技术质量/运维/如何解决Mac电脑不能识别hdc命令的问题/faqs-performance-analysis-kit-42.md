---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-42
title: 如何解决Mac电脑不能识别hdc命令的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决Mac电脑不能识别hdc命令的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:42+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c290a8077dc40218476cd351d96a5881a937e7b00c246eaed3cf5aa3609af99f
---
1. 环境变量因素的解决方法参考如下：
   1. 点击屏幕左上角的苹果图标，转到系统设置中的“用户与群组”。
   2. 按住Ctrl键，点击左侧窗格中的用户账户名称，然后选择“高级选项”。
   3. 点击"Login Shell"下拉框，然后选择"/bin/bash"以将Bash作为默认shell。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GQdDxsQMTVyEW3Gz78VK-w/zh-cn_image_0000002194318532.png?HW-CC-KV=V1&HW-CC-Date=20260612T021941Z&HW-CC-Expire=86400&HW-CC-Sign=A57E2D8BCB0BD34CA689761473E99B4402DB423526D6B01E9EDCE2509BFB3446 "点击放大")
2. 非环境变量因素的解决方法参见：
   1. 打开终端，输入 cd ~。
   2. 使用 sudo vim .bash\_profile 命令编辑文件。
   3. 在文档底部输入：

      export PATH=${PATH}:Sdk/default/base/toolchains

      按下Esc键退出，然后在下方输入:wq保存并退出。
   4. 运行 source .bash\_profile 命令以加载环境变量。
   5. 输入 hdc -v，显示版本信息即表示可用。

   **参考链接：**

   [常见问题](../../../../../harmonyos-guides/系统/调测调优/调试命令/hdc/hdc.md#常见问题)
