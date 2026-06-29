---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8
title: 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:494fe373e9c499dee845e2a3fb597a2701e0f5b47938d98c9507e8895675b907
---

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/QPc85PxFT5e_PDP_ulcf0A/zh-cn_image_0000002229758241.png?HW-CC-KV=V1&HW-CC-Date=20260612T024103Z&HW-CC-Expire=86400&HW-CC-Sign=10614DEDB44904E940182D665266B00696845EAA2CEAD883277666595FE59B31)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sP3Q6WtNQwOI8BI8c_PBdg/zh-cn_image_0000002194158380.png?HW-CC-KV=V1&HW-CC-Date=20260612T024103Z&HW-CC-Expire=86400&HW-CC-Sign=C20986320D27E9F5E2E95A3DBA8C50D94FA89081907221979544ECF0A5847305)
