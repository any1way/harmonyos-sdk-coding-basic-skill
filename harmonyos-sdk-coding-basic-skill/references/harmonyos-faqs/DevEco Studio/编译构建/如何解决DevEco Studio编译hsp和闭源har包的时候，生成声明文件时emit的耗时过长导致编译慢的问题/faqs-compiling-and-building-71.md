---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-71
title: 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:59+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:f52470fa797c7b4b928dce05dbec63c2e42a4e70d28d00699812ef8e15c3ecfc
---

说明

注：此方法为临时规避方案，后续将修复该问题，建议仅在阻塞时使用。

用于减少编译HSP和闭源HAR包时生成声明文件的耗时。

修改 ets\_checker.js 文件（文件路径：SDK路径\default\base\ets\build-tools\ets-loader\lib\ets\_checker.js），编辑 processBuildHap 函数。

1. 生成 sourceFile，在遍历文件时生成声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Mc7ehFY_Q-ihrPnAZAsq4g/zh-cn_image_0000002229603953.png?HW-CC-KV=V1&HW-CC-Date=20260612T024158Z&HW-CC-Expire=86400&HW-CC-Sign=19EDABBFD14FCEA91B512C0F7B5C852A854131DF71CC63388CE44E32C08C917E "点击放大")
2. 修改 getEmitOutput 函数，将其改为 getFileEmitOutput 函数，以获取声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/JFadiLfBTVOsD3Nv64Ob0g/zh-cn_image_0000002194318168.png?HW-CC-KV=V1&HW-CC-Date=20260612T024158Z&HW-CC-Expire=86400&HW-CC-Sign=6B3596472C3C8C3839B799B74A324F014ABE6D95E8FBC7A201C637BC91F1A3E5 "点击放大")
