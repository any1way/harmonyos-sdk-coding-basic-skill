---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-129
title: 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:49+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:b802b331c5b6e1991de5e7a3e114e6a51fe45e0aee03306ad39d0f32c51c69e7
---

**问题现象**

编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”。常见于图片中两种错误同时出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/sjnOx7x6Rgi0qpngBk4qKQ/zh-cn_image_0000002581587131.png?HW-CC-KV=V1&HW-CC-Date=20260612T024248Z&HW-CC-Expire=86400&HW-CC-Sign=674E4E87ED3E79CBE2751FDF086C6E40D3C4A8990D6D6548B80B027A02CCA131 "点击放大")

**问题****原因**

大小写敏感导致模块无法找到。

**解决方案**

解决引用中的大小写问题。
