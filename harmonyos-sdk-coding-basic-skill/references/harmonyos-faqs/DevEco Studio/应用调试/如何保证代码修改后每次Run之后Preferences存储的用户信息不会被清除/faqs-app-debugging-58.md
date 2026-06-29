---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-58
title: 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0c24a06df0043f6abf508d2f2632a5744d7ea2103dac806580e2799bd4a53325
---

如果需要在运行后保留存储在Preferences中的用户信息，可以在DevEco Studio中进行如下设置：点击“Run”->“Edit Configurations...”，进入“Debug Configurations”->“General”->“Installation Options”，勾选“Keep Application Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ogfjEy3PTP-cLf5rN5pUDw/zh-cn_image_0000002229758741.png?HW-CC-KV=V1&HW-CC-Date=20260612T024506Z&HW-CC-Expire=86400&HW-CC-Sign=EF424FE19A21BFAD3271D80BE2F0A8F0F324A208995DDFC9E6083D13A6DB2307)
