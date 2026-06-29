---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-10
title: 在Windows电脑上启动模拟器，提示未开启Hyper-V
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在Windows电脑上启动模拟器，提示未开启Hyper-V
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3fe5b2d59755c8536e6fbc50a1bc054a251f94309103b291453b4724c52af79a
---
**问题现象**一

启动模拟器时，如果未开启Hyper-V，或在虚拟环境中使用模拟器，会弹窗提示“Hyper-V not enabled”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/9B7AJbGBRYCdrOdYhjFs-w/zh-cn_image_0000002194158596.png?HW-CC-KV=V1&HW-CC-Date=20260612T024410Z&HW-CC-Expire=86400&HW-CC-Sign=118B54F753980F58CF295C5CEC6586E6A87B3BDD30C67E87CF23CF840A5F0B9A)

**解决措施**

1. 请确保模拟器的[使用环境](../../../../harmonyos-guides/编写与调试应用/使用模拟器运行应用/概述/使用环境/ide-emulator-requirements.md)符合要求。
2. 如果CPU支持虚拟化，打开控制面板 > 程序 > 程序与功能 > 启动或关闭Windows功能（对于Windows 11系统，需打开系统 > 可选功能，在相关设置中点击更多Windows功能），找到并勾选“Hyper-V”、“Windows虚拟机监控程序平台”和“虚拟机平台”，点击确定并重启电脑。若勾选后启动模拟器仍提示错误，需以管理员权限打开命令行窗口，执行 `bcdedit /set hypervisorlaunchtype auto`，然后重启电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/duECpFALRr6j3nFQ4VFwXA/zh-cn_image_0000002273550542.png?HW-CC-KV=V1&HW-CC-Date=20260612T024410Z&HW-CC-Expire=86400&HW-CC-Sign=834BCDC72FEE9F39A9FDD4699E088A8156B5F406A6FCF74CA1821D974C5000A7)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/AXwOmMUOTsaGR0dR_4a1vw/zh-cn_image_0000002308080257.png?HW-CC-KV=V1&HW-CC-Date=20260612T024410Z&HW-CC-Expire=86400&HW-CC-Sign=EBF949C528424106344AD5D52265C577B0DE6A04CA25435609CAB209DCD24C48)
3. 若勾选后启动模拟器仍然提示该错误，需要以管理员权限打开命令行窗口执行以下命令，并重启电脑。

   ```
   1. bcdedit /set hypervisorlaunchtype auto
   ```
4. 如果上述步骤无法解决问题，打开任务管理器，切换到“性能”选项卡。如果显示虚拟化已禁用或未开启，说明BIOS中虚拟化功能未开启。请根据计算机主板型号，进入 BIOS 设置界面，开启虚拟化功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/uH1IVqSmQc6K-byV_ss6wQ/zh-cn_image_0000002307967181.png?HW-CC-KV=V1&HW-CC-Date=20260612T024410Z&HW-CC-Expire=86400&HW-CC-Sign=409B495A6A2578809FCB55772801146CA18B83E4BA6F100957CC309E10A70BA7)

如果安装和开启Hyper-V的过程遇到其他问题，请根据系统版本查阅相关文档。更多关于Hyper-V安装请参考[安装 Hyper-V](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v?f=255&MSPPError=-2147217396)，[Windows 和 Windows Server 上的 Hyper-V 的系统要求](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/hyper-v-requirements)。
