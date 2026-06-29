---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3c30cd6b308ae22e80caba4083846abbd3b2a2123312c3eef4b7149492ee3da2
---
CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型进行生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Y8WZxjM8TD2UFCgE9Hf_Nw/zh-cn_image_0000002571546902.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=6BE62D73C73B43B10197BBCB1A7062066C15C1838A4B549943514B3C4F734999)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框。

     在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。

     从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Suggestion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Suggestion & Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/kUBhdK-5RIeWaIts3Pa4OQ/zh-cn_image_0000002571387262.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=9A88732F591B08E2FB1B80FBB07081C681862D9FC99B3142EB2CFD36F196B6BC)
2. 选择在CodeGenie中已配置的三方模型，或者使用默认模型。三方模型配置具体请参考[模型（Model）配置](../../自定义智能体配置/模型（Model）配置/ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/e8itjD5jRouEi50G5E4urg/zh-cn_image_0000002571546904.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=5D365207CAE472856CD4224A742C038CDD549AEE53EF5C4686E37BC283CB95CE "点击放大")
3. 若选择默认模型，在对话框中输入所需要的代码功能描述，在键盘输入回车或点击发送，开始生成代码。点击**Stop Generation**，中断本轮代码生成过程。

   若选择三方模型，支持分析当前代码文件和生成分析报告，以及进行参数校验（**Parameter Validation**）、代码注释（**Code Explanation**）、代码优化（**Code Optimization**），分析报告和参数校验等结果跟模型有关，具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/G9VkYvMmSPCPq0ZF3wRsAQ/zh-cn_image_0000002602186437.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=46AEB0B6C6927C9219D19D56349173323F6BE03EF31574B4657B97FE4EAE772F)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**/**Code Explanation**/**Code Optimization**，可输入或不输入所需的功能描述，在键盘输入回车或点击发送后开始生成。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/cuJHswPcRdObDDu4oIMesA/zh-cn_image_0000002571546900.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=929F2830CEBB70B6D8A0F54D4AA54B14212A34A72C505357E5CA1FE41270E9AD)
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/CoUwxnczRFq5kecSP20WrQ/zh-cn_image_0000002602186439.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=FA45BB805C01F93A5297D0EDF279CD317423D639C1BF16F28BEAC23F801DC6C1)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/M_15fnHTQMG4AxDZ6fVn8Q/zh-cn_image_0000002571546906.png?HW-CC-KV=V1&HW-CC-Date=20260611T072225Z&HW-CC-Expire=86400&HW-CC-Sign=D0DC12C4DDEE3DC321465BDC68CD7FB05CB200F29A13F3F0098096E487952F50)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
