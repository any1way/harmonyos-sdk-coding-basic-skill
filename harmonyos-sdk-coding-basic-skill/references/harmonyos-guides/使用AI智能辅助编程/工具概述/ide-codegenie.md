---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
title: 工具概述
breadcrumb: 指南 > 使用AI智能辅助编程 > 工具概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:15+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:a886388ea8d6f0d54e1dbf6ffb37803424395d2a10287c6dc3c16bab113afde8
---
DevEco CodeGenie是DevEco Studio AI辅助编程工具，支持智能问答、代码生成、页面生成、万能卡片生成、单元测试用例生成、代码智能解读、编译报错智能分析、智慧调优、应用UI生成、意图装饰器生成、小艺智能体创建、自定义Agent等能力，帮助开发者更高效地开发应用。

## 使用方式

在DevEco Studio右侧边栏点击**CodeGenie**或通过快捷键**Alt/Option+U**，进入或隐藏CodeGenie。点击**Sign in** ，跳转至华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功后点击**Agree**，同意隐私安全政策及使用条款后开始体验。

若需使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#zh-cn_topic_0000002166808440_section18337533718)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ZcYscvj8RkqwtoVNYIBnpQ/zh-cn_image_0000002571387554.png?HW-CC-KV=V1&HW-CC-Date=20260611T071920Z&HW-CC-Expire=86400&HW-CC-Sign=2CFC01DCF3C09783FCC3AC3BF1C6BBE446C31F638E9A0BDD3F928C1278BD5EC3)

## 插件获取及安装

若在历史版本的DevEco Studio中使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取最新的CodeGenie插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

下载完成后，插件安装包**无需解压**，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/eBBab9JGQmCo7U9GPUUXNA/zh-cn_image_0000002571547186.png?HW-CC-KV=V1&HW-CC-Date=20260611T071920Z&HW-CC-Expire=86400&HW-CC-Sign=F13FC486B73770ECFFF0F157F54C81B99548E98E97AAF419BEE838D59AE4FAF7) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Nve2ievYTz2OnjrO7M1bfg/zh-cn_image_0000002571387552.png?HW-CC-KV=V1&HW-CC-Date=20260611T071920Z&HW-CC-Expire=86400&HW-CC-Sign=DF13A023D64CBED8333D2FE7652BBD15E468D2205B1429D5CE289554A1BFD760)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/oHc8F2RMRVm3GgYAg3Uwmw/zh-cn_image_0000002602066669.png?HW-CC-KV=V1&HW-CC-Date=20260611T071920Z&HW-CC-Expire=86400&HW-CC-Sign=6806004316D02FFDCDFEF3D7F9464FF69E65CDF495CA7D3F44E21C6A0721184F)
3. 点击**Restart IDE**，重新启动DevEco Studio。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/xLgVl92HRv-a7Fyce4mPTQ/zh-cn_image_0000002602186721.png?HW-CC-KV=V1&HW-CC-Date=20260611T071920Z&HW-CC-Expire=86400&HW-CC-Sign=B375FCB9D6CC16AF07B85A0AEE07FBDFE847B6EF118881D618E2281D8CA0270A)
4. 在DevEco Studio右侧边栏点击**CodeGenie**，完成登录并开始体验。

说明

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；不勾选时会有弹框提示用户手动升级。若管理台配置的插件不支持静默升级，均有弹框提示用户手动升级。
