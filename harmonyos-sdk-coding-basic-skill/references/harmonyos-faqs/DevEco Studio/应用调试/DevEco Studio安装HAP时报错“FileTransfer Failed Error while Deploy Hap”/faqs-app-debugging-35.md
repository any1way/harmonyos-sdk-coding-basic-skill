---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35
title: DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5abd8f1d66073f58d217a58faa1311e92c2bc054601234c85a05ac20a467ac7
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/OppeXGuWRHCLHkEfU9-Xuw/zh-cn_image_0000002215508376.png?HW-CC-KV=V1&HW-CC-Date=20260612T024458Z&HW-CC-Expire=86400&HW-CC-Sign=86F53E4B8C0E09332EA7E57961274CCE28A98FC0D4D9D5E7AEBC48940534A791)

**解决措施**

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

* 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
* 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
