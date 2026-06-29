---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-15
title: 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:8365e4e4fe2c6f36d82f6682bf38681ea19c8511a81f26a424cf1c07cbff173b
---

**问题描述**

Windows系统使用DevEco Studio时，SDK卸载失败，提示错误信息。

Unable to rename the file. Cause: Unable to delete D:\\xxx\\default.

**解决方案**

1、启动任务管理器。

2、切换到“性能”选项卡。

3、点击下方“打开资源监视器”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/7B5X6s1KSlCUx6_JpqY88Q/zh-cn_image_0000002194158616.png?HW-CC-KV=V1&HW-CC-Date=20260612T024028Z&HW-CC-Expire=86400&HW-CC-Sign=D465F70417103B5C02938BBA8D2A16CB2A45E9AA0B4B89AE5C72BE482FE2FBCB)

4、将路径 D:\xxx\default 粘贴到关联句柄窗口右侧的搜索栏中，按回车键搜索占用的进程，然后结束该进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/NmFzqA6oSQ2HxBjrds8Qfg/zh-cn_image_0000002229758493.png?HW-CC-KV=V1&HW-CC-Date=20260612T024028Z&HW-CC-Expire=86400&HW-CC-Sign=6E020C8342F5706F292063563941C81B61BC051E1C8097E971A9767C1481F336)
