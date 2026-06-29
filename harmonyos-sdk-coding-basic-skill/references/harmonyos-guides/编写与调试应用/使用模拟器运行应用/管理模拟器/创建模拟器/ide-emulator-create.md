---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:37+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:8f0b696e9dbb36c926e8210098c7aa70676be480a5a3ad207afec3f1c9d63412
---
有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](../../离线部署模拟器/ide-emulator-no-network.md)。

说明

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[macOS上活动监视器中显示模拟器内存偏高](<../../../../../harmonyos-faqs/DevEco Studio/应用运行/macOS上活动监视器中显示模拟器内存偏高/faqs-app-running-23.md>)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

说明

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/n5JW9wqOQeyUHS0QspS_bA/zh-cn_image_0000002602184865.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=535DB9A6FA33E554A887CE3ABFB24869FDEB6719C801ACE8333099D0D1AAF78E)

在设备选择框中，选择预置的模拟器并点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/FBtE2_xmRwanUivg1FkTLA/zh-cn_image_0000002602184855.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=3E99E4FB861979426284A6EEAADDDEE0BC1DD3B5DB3B79349AA4C8D4318754C1)后，根据界面提示下载镜像，或点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/QbtAvjVZQlOQg98IZLYoIQ/zh-cn_image_0000002571545316.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=7C218B24551A62FE66FBAE8EA2F49532CA8BE72AA5B70A5A5F9F1E406D1C956A)下载镜像后，即可快捷使用模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/7aZxB7NnRva8eVxL6jO8iA/zh-cn_image_0000002571385686.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=7D74AA35231D755E9DCC623B2C2809A1187B442532A26327A2F8CE813BE86CD2)

## 创建新的模拟器

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/PD5VTvufTcSX0w2zkz9Heg/zh-cn_image_0000002602184863.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=E2B0E689B4958F1A2B1749B65C087C956F62955109D7BEF587FDE9C4F3741B68 "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时请点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/40Dyb_zzQOG0Ff_UmWusbQ/zh-cn_image_0000002571545304.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=0EF877DD842FE0B20EEFEC47F7729D199A5B884391250BE21A17604A79B520CE)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   说明

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/-n6hvZhRQH6bCHMydPUm7A/zh-cn_image_0000002571545328.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=5A4E11B36E014BEF77AE19B54B77DFC965131166198F54361FA00BE2138CE2EA)
3. 单击**Next**，设置设备相关的参数。
   * **Name**：设置模拟器的名称。
   * **Screen Profile**：从DevEco Studio 6.0.0 Beta1版本开始，部分设备支持选择预置的机型配置或自定义屏幕配置，具体支持的设备请参考[自定义屏幕配置](../../修改模拟器/自定义屏幕配置/ide-emulator-customize-screen-configuration.md)。可点击下拉框选择预置的机型配置，也可点击**Customize**自定义配置，在自定义配置的情况下可以对屏幕尺寸、分辨率和DPI进行修改，取值范围参考界面提示。
     + **Screen size：**屏幕的对角线长度，单位为inch。
     + **Resolution**：分辨率，包括宽度和高度，单位为px。
     + **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
   * **Boot options**：模拟器启动方式。从DevEco Studio 6.1.0 Beta1版本开始支持。
     + **Cold boot**：以开机启动的方式重新启动。
     + **Quick boot**：启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。
   * **Memory**：设置模拟器的内存。
   * **Storage**：设置模拟器的存储空间。

   确认所有参数后，点击**Finish**创建模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/z1IlQgDNTYuk6lEp6_M_sQ/zh-cn_image_0000002602184861.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=0145B502137F4C9B04118010B5F70E219C772724159171FB5D6E746AE1142D77)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/tQiIiDkiRvGD35JlVI8Q5w/zh-cn_image_0000002571545332.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=B02C0200792D036AF87972D5663B607FACB9BB0A6034C7BC068806FA26CDB5E0)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KXBV9KiXR16UaE2beCB7ew/zh-cn_image_0000002602184849.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=CE961A2E1BE9FA5BCDEAADA3024360030978AE47760BAE75D17B0C998F466458)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/hcHpgM2zRK66y3IHmH533A/zh-cn_image_0000002571545330.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=AF508BECD397E08280DBE25602160E1D01E2F9D68348862521597D49E792AE06)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Z2HLjhuKQ3anbXyGPz_wzA/zh-cn_image_0000002571545326.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=16E0AD8B64CC0F9E382FE43DF9BCA81230AF344C2B02F2222E13D19AA0B470EF "点击放大")
5. 单击DevEco Studio的**Run > Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/zaojua9PTQGBgeQd61vuEg/zh-cn_image_0000002571385678.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=D83F405B95E5B7CDAF3BAA476BAD1A7BDABA0CACDB88ECEFF9FAF1E98121CB45)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/N88KTvbXTOStwhHO3emdmw/zh-cn_image_0000002602184867.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=33E7B28956AED592D10226D82315A6D8C48BA38E70926B655B3D324D3205FAAF)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/gNLk_h_8TheqHPasoTgLLg/zh-cn_image_0000002602184841.png?HW-CC-KV=V1&HW-CC-Date=20260611T072836Z&HW-CC-Expire=86400&HW-CC-Sign=8EDD85EEDB8E01D067A02118AEDBC1F4F6CBB6979E640B4C4D8C0FB336E729C0)
