---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-21
title: Hot Reload执行失败原因说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > Hot Reload执行失败原因说明
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:50+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:3fee70b6ffa1c5880cd00f8b47c331a184ef74df919e4cafb48c71f9b9795fb3
---

**问题现象**

热重载执行结果失败，控制台打印蓝色重启链接：“Reloaded 1 files failed. Please reinstall and restart.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/gAmvbIBpT0qfGRJXHPFc_g/zh-cn_image_0000002194318548.png?HW-CC-KV=V1&HW-CC-Date=20260612T024449Z&HW-CC-Expire=86400&HW-CC-Sign=396BF82CE1C199D6E14E4FDD84DAAABA190D63E4B6DC9CC8B8A92B30A5D49A27 "点击放大")

**解决措施**

热重载的最后一步是将补丁包安装到设备并执行quickfix命令。如果quickfix命令执行失败，热重载也会失败。

导致补丁包安装失败的原因可检查以下几个方面：

* 检查工程签名是否正确，热重载需要使用debug签名（不支持release签名），否则热重载将无法执行。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/SHIDnteoQm2Zzn4kmGs01A/zh-cn_image_0000002229604317.png?HW-CC-KV=V1&HW-CC-Date=20260612T024449Z&HW-CC-Expire=86400&HW-CC-Sign=D4C1A0B19DA32E3C260D32BFFC6896A5DF06750EDFFA54A37107B6CEEDC78795 "点击放大")
* 检查工程的Build Mode，热重载不支持release模式，支持debug和<None>。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/QPb8LzG8Q5WKEg_u2CATKQ/zh-cn_image_0000002487886068.png?HW-CC-KV=V1&HW-CC-Date=20260612T024449Z&HW-CC-Expire=86400&HW-CC-Sign=7CA142A497F5E5E88A96CF2FCC8191D88E28C5E5140B9C9794C3EF89AD970D4F)
