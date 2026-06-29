---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52
title: 如何给新增的module在线签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何给新增的module在线签名
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:42+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:273c0b04d3c0785d7c044f4c1e151b16edc87bfde662bb14a3b03c2b23659896
---
操作步骤：

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../../../../harmonyos-guides/编写与调试应用/使用本地真机运行应用/ide-run-device.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/KjCHOgshRj-acdc7XzGlHg/zh-cn_image_0000002229604037.png?HW-CC-KV=V1&HW-CC-Date=20260612T024141Z&HW-CC-Expire=86400&HW-CC-Sign=9AA47BF906676BC576E7A1C2C0BC1A899C745E69C5A5A008966C9AAD0992B84C)
2. 进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/xUepqhIRRpekX6-VqMpPug/zh-cn_image_0000002229758513.png?HW-CC-KV=V1&HW-CC-Date=20260612T024141Z&HW-CC-Expire=86400&HW-CC-Sign=01FBCFE045D88F618544F365FB8BAB0D5B3C17AC79F1B5096D902EE6B5724873 "点击放大")

   签名完成后，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/mDNXiKDgSh-qsAQMKuQWTA/zh-cn_image_0000002194318264.png?HW-CC-KV=V1&HW-CC-Date=20260612T024141Z&HW-CC-Expire=86400&HW-CC-Sign=B66F55F0751E784279AAA66D3CDBE1508A0D1F89B73E8E238BEE2508CD9BB648 "点击放大")
