---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-26
title: 如何使用DevEco Studio进行C/C++代码断点调试
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何使用DevEco Studio进行C/C++代码断点调试
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a07a297ca0472004d95f0fe619f09b777431841a4c867781cbcaf5d686a55ae9
---

**问题现象**

在DevEco Studio上的C/C++代码处打断点，调试运行时断点不生效。

**可能原因**

DevEco Studio进行ArkTS/JS + Native混合调试时需要配置DevEco Studio的调试模式。

**解决措施**

选择配置项：Run/Debug Configurations > Debugger > Dual(ArkTS/JS + Native)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/wq08DyYZQhyho6TGCRzAQA/zh-cn_image_0000002229604041.png?HW-CC-KV=V1&HW-CC-Date=20260612T024451Z&HW-CC-Expire=86400&HW-CC-Sign=BC6674CB2EB92D2ED8519AA4482DE484D01D4CE8E6D50D1A4EA9C29AF1085680 "点击放大")
