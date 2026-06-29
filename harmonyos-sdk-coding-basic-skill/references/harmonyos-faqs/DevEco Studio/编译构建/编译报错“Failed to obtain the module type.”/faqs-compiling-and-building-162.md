---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162
title: 编译报错“Failed to obtain the module type.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to obtain the module type.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1a5e40106e6d786561b9d0af0472f6868156956d526bd9fc6d248550a1d921f2
---

**错误描述**

未找到指定的模块类型。

**可能原因**

在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/lYLHMGb2S9mUtEQrLcwekg/zh-cn_image_0000002229604177.png?HW-CC-KV=V1&HW-CC-Date=20260612T024321Z&HW-CC-Expire=86400&HW-CC-Sign=212B94639870A87CFD11929F9CE02862A9EE3FD665C56FA8E832EFCC54DABBE3)

**解决措施**

确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
