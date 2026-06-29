---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-140
title: 编译报错“Cannot resolved import statement”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot resolved import statement”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2b6b19981f26009da99bb161d92c4fc780ea17d2fe08ada255510df20907cac8
---

**错误描述**

在编译过程中，提示“Cannot resolved import statement”错误信息。

**可能原因**

导入文件时，大小写不一致会导致问题（导入到单个文件夹时，默认寻址小写 “index.ets”文件，但该文件夹下仅存在大写“index.ets”文件）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/N8epnOMjQwmKVoxPeAtHGg/zh-cn_image_0000002194318384.png?HW-CC-KV=V1&HW-CC-Date=20260612T024301Z&HW-CC-Expire=86400&HW-CC-Sign=4E3AAEF9602D5BDAEDB002173C3FE1FBD476D2B649D65EE5033149B93F60A4E8)

**解决措施**

检查import文件的大小写。
