---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:220857a384c232cc427deff04780b0625ed95a1fe6a9d01040a5a7e9321f293d
---
在本地真机中运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

说明

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 确保设备系统版本升级到[HarmonyOS NEXT Developer Beta1](<../../../harmonyos-releases/历史版本/HarmonyOS 5.0.0(12)/版本概览/overview-500.md#section849861583816>)或以上。
* 在真机设备上查看**设置 > 系统**中开发者选项是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在设备运行应用/元服务需要根据[配置调试签名](../配置调试签名/ide-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与PC端进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/WiGaz-1_QOWPmJNfXTFOnA/zh-cn_image_0000002571387482.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=E95F82BC9AC5595A2FCC86825F138C99FF8496655F20DB32D70EF5BC31753E69)
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/zsNC_XHCQeW558sQXFrsbQ/zh-cn_image_0000002571547118.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=9FAADF39F4BC008DD559B381F4E003C9FB7D72B3CB37073B7FAC22EE54168222)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/25_cEhcjSyaQ1NNnTfFCJg/zh-cn_image_0000002571547128.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=E2C1CB7E6552BB4B85DC4E4F25F693B70CB90019B8F519C82E66BE2AE3D3B279)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示“No Devices”，可使用设备连接助手来排查问题。点击设备下拉框，并点击**Troubleshoot Device Connections**打开该功能，分为三个步骤，每个步骤排查完后点击**Next**排查下一个。

1. **通过USB连接设备：**根据界面提示，使用USB连接设备后，点击**Rescan Devices**按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
2. **启用USB调试：**根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
3. **重启HDC服务：**如果DevEco Studio仍然无法识别设备，点击**Restart hdc Service**按钮重启HDC服务，重启后HDC会重新识别设备。如果重启后仍识别不到设备，请参考[设备连接后，无法识别设备的处理指导](<../../../harmonyos-faqs/DevEco Studio/应用调试/真机设备连接后，在DevEco Studio中无法识别设备/faqs-app-debugging-3.md>)或[如何解决设备无法识别问题](<../../../harmonyos-faqs/DevEco Studio/应用调试/真机设备连接后，执行“hdc list targets”命令结果为“[Empty]”/faqs-performance-analysis-kit-32.md>)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/IjjMwO-CQHmFN-cI5Qq7uQ/zh-cn_image_0000002571387488.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=7643CBCE56956A756CFCD7D86BA5DA812F327CF5CB2FC8C0C5F6EEBE25C50238 "点击放大")
3. 连接设备，有两种方式。
   * 在DevEco Studio菜单栏中，单击**Tools > IP Connection**，输入连接设备的IP地址和端口号，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/iF2SZGDUR0Otgy--J1kbvw/zh-cn_image_0000002571387480.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=7EDFA0834C6A28F80463EEFF8375A75AA240B3007C4A83DCDB1CE5CDF6293F6F)，连接正常后，设备状态为**online**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-5U--wEyTmaajB5HMNqQuQ/zh-cn_image_0000002602066605.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=694B1C131AA1309B751111CD2B6CECFB71DAC794B376EABAC4FDFBFEEE4C6384)
   * 执行hdc命令，关于hdc工具的使用指导请参考[hdc](../../系统/调测调优/调试命令/hdc/hdc.md)。

     ```
     1. hdc tconn 设备IP地址:端口号
     ```
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/s5ivw8o7TMiReePCDpSKXA/zh-cn_image_0000002571547120.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=B405903D7C79C9EA749D7612E04F9E0A24F437F4D1262F10B967D4EF562D5350)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/wg-v9ZZCRXOV7XqB0OZrcg/zh-cn_image_0000002602066601.png?HW-CC-KV=V1&HW-CC-Date=20260611T072830Z&HW-CC-Expire=86400&HW-CC-Sign=4FCC9CB9F482B8E538E8B053983CD2444E4E1C70F457BC1F132617CBCFBC3505)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
