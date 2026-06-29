---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07a3f5d11171c690035b097a39e6f2b6246d198298ab3687f8ad25e56106969f
---
CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/iLF6IbLITyOgBlGnXNcHxg/zh-cn_image_0000002602186161.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=E6C47F023B3D1D8CC70001380A97CD5118B745E2245FB84E7A18C93809D11B67)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/J5cQMEPnQ2aYZzCQk1A0VA/zh-cn_image_0000002602186155.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=0FBEEB83DCBB14D60D24FC8615D0585DC967C4F66EEBB4C0F07F82B9834604B3)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ZB69V34jQBijOn0zqKITBQ/zh-cn_image_0000002571546622.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=A5319959B911655DADC403CAB04647BE809DAE6514F77D5F54748327ABBE1AE2)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原；以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Release版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WR2eeQFrRIu_bD3w8zxUHQ/zh-cn_image_0000002571386994.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=C99CEAC2B6B906A370CECE1CEC03E64D85CD48C0384E41A98A0C1DF2E2BE08F6)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/keRkzMAaTjy-wuqKclr_wg/zh-cn_image_0000002602066099.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=42CBD3522934A8DBBC4ACFCAA1352DCC89C610CEC79D977D54851D549C33A775)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](../../自定义智能体配置/自定义智能体（Agent）配置和调用/ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/kQR2dRedTW21XXV-nEEEqA/zh-cn_image_0000002602186159.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=4F59D983B6B56717B945D6EC3128B36268A56EF90918539ABDABE35CA3BB5C80 "点击放大")

**DevEco Studio 6.0.1 Release****版本**

**操作步骤**

在对话区域输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/wLHup2uNRBqL6_AEors67g/zh-cn_image_0000002602066105.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=3085F0146BF214F97EBCF745DBD6E7E64FBA41477CFC4FF4E7811BD0B62EA0CB)发送，将自动生成符合要求的代码段，将代码段一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Wq97MZjESgm0VdowcExQLw/zh-cn_image_0000002571386984.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=6F5C0EE02737BE11F088BA9AEECB30D4842D0D69F51850B3803415BBD434B190)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1AT_85H3Sl2KOMeLf0V0jw/zh-cn_image_0000002602186163.png?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=72CA69AA77705829A66D42F4550140131C1682F348F7E7A58B8CD77EEAE297C9)至编辑区当前光标位置。

**示例**

使用ArkTs语言写一段代码，在页面中间部分插入Swiper组件，其中有3个Image组件，其图片资源名分别为app.media.phone，app.media.watch，app.media.glasses。这些Image组件的宽度撑满父布局，高度为600，图片缩放类型为保持图片宽高比不变，将图片完全显示在边界内。 Swiper组件设置为自动播放，播放时间间隔为2秒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/k7YATkz4QQ-DPNq7Cc1ncQ/zh-cn_image_0000002602186157.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072222Z&HW-CC-Expire=86400&HW-CC-Sign=2632E679EA7D1C413B1F7F276D7C652E735AB613D2BEA9B5CCA378FEFE9AD2DA "点击放大")
