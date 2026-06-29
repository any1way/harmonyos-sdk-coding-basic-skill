---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-33
title: 启动模拟器，提示镜像文件缺失
breadcrumb: FAQ > DevEco Studio > 应用运行 > 启动模拟器，提示镜像文件缺失
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8b35b7707d4a390dafa4148837f3cca944253451d97b7103f82b61f0cf20146b
---

**问题现象**

启动模拟器失败，提示“system-image文件缺失”或“The system-image file is missing.”，原因是模拟器镜像文件缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/mXlA9Gu1QhCXaCieysgEjA/zh-cn_image_0000002229758805.png?HW-CC-KV=V1&HW-CC-Date=20260612T024427Z&HW-CC-Expire=86400&HW-CC-Sign=91086382ACB00F9A10B1A180E1302492842EB8B448CF87EF01C3B65EADB4CDFA "点击放大")

**解决措施**

请通过以下两种方式解决：

* 单击菜单栏的Tools > Device Manager。在Local Emulator页签，单击右下角的New Emulator按钮。在虚拟设备配置界面，更新模拟器的镜像。
* 删除已创建的模拟器，然后重新创建。
