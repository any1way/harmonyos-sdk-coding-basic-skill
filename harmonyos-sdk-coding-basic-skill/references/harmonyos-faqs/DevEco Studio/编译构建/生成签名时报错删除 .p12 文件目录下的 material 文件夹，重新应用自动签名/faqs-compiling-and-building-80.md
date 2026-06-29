---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-80
title: 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5f5565cce708ee80a731fc8e2e2977c7f06cdd5dc1ed68cc40946e87e271b5eb
---

**问题描述**

点击生成签名时出现错误：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/M694S7gIQ8aVWid2Qv7Buw/zh-cn_image_0000002229604377.png?HW-CC-KV=V1&HW-CC-Date=20260612T024205Z&HW-CC-Expire=86400&HW-CC-Sign=6999392CD5C055946F5578D0493326C981384F417D124AE708AC886EDEDAB700)**解决方案：**

可以通过签名界面提供的profile文件（\*.p7b）或Certpath文件（\*.cer）对应的签名文件路径，删除本地的material文件夹，然后重新启动DevEco Studio进行签名。
