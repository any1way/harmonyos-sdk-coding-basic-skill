---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5
title: 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
breadcrumb: FAQ > DevEco Studio > 应用运行 > 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c02a0e672c26c03432b771f78e8b130aea18e5d4bc0364ad21235523caf76e9b
---

**问题现象**

本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/2NIEgd0MTa-b3Cd7MNHMVw/zh-cn_image_0000002194317932.png?HW-CC-KV=V1&HW-CC-Date=20260612T024406Z&HW-CC-Expire=86400&HW-CC-Sign=0FB162F8E080E38F858E2409B7C0C830D5BAB2AF9852787FC51770D1BDA7EF7E)

**解决措施**

可以通过以下方法重新运行工程：

* 在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
* 打开命令行工具，进入HarmonyOS SDK安装目录下的 `default/base/toolchains` 路径，执行以下命令重启 hdc server：

  ```
  1. ./hdc kill -r
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/gkAszBD2RqOTbv2c_6ggyQ/zh-cn_image_0000002229758185.png?HW-CC-KV=V1&HW-CC-Date=20260612T024406Z&HW-CC-Expire=86400&HW-CC-Sign=993AEE5E31CC3BAC18DDF72387DAB79D09ED816D5A0113DC6F47FE1DBE806DF8)
