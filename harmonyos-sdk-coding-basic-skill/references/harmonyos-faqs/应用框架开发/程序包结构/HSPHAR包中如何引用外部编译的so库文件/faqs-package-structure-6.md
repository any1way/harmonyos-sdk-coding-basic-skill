---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6
title: HSP/HAR包中如何引用外部编译的so库文件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HSP/HAR包中如何引用外部编译的so库文件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:20:24+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:d0b2013a04f645c202f5f27a78165869f27f5ae2204460d14fa21a76085c1bed
---

1. libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86\_64。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/OxXgu4-jR9CA7hTBE_daPA/zh-cn_image_0000002194158696.png?HW-CC-KV=V1&HW-CC-Date=20260612T022023Z&HW-CC-Expire=86400&HW-CC-Sign=AAEC88610963123A7B2B9A81B18C8AD5B52F5462119BA0F3A56D99ADF876F231 "点击放大")
2. 在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target\_link\_libraries(entry PUBLIC libxxx)
