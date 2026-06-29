---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fceda7634532aa7c2c229f9aff1eeab8a523b34e4637860aefa3acc1d29d1f77
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/dNlAGbjwRvK0Cg6wKYUHTQ/zh-cn_image_0000002602065963.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=A9202A0C22C83207EAEBB32BD3CDE10A9A9132296A210C43383EB5A88093CBBC)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/PJKHlOmrTUWQo2CYKsIguQ/zh-cn_image_0000002602186017.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=7570134987AF6CB0770A35EF09CCB3A2E0EA7BE53FA3482FC7F0723A1B29F24F)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/_Wygfy0CSkmyKC3n3mudHg/zh-cn_image_0000002571386852.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=146A1ECF2B79623844735181F247A4D973F5DABC0D5E44F9CB6EBF4EBEF1256F)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/n9RYIq7fRwyKOJku17Qdyg/zh-cn_image_0000002602186023.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=51CA02D0458CD06E4D2137B5DA5E5E890126D81F6BE3F20D5CFD0DF2A6EEE295)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ujdU4TbQSa6xkaChxLo5eA/zh-cn_image_0000002571386858.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=1692B5730ECCF0F615749061543F2930201B767B6E12C01253A472A2C47B5606)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qQXvO5bLS32Cy7Rtb8riOg/zh-cn_image_0000002571546490.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=A9836CA6C540BD2552B58D95493C99B63B8B3380AB687CFC8B36E5812183F501)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/g22_0rfkTe6lrnxv-zBQEQ/zh-cn_image_0000002571546486.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=5EEEAA5F74CD7D99E7D6DC89FECD17253266926AC1CA04A9360BF4D449B74A89)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/iwPQG0XJSqCZrcMXTtT_JA/zh-cn_image_0000002602065967.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=D2C9E7AB7F70999C8AADDA8A159E7A8355364538C086205D4B70E0EED181DCDF)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/wiHWUHjZQM6uZazdTlW7RQ/zh-cn_image_0000002571386856.png?HW-CC-KV=V1&HW-CC-Date=20260611T072910Z&HW-CC-Expire=86400&HW-CC-Sign=78B9D2C5BFD0395A46F6A352375BA639E612B1E4F37046F905826C75E2E52B7B)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

说明

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
