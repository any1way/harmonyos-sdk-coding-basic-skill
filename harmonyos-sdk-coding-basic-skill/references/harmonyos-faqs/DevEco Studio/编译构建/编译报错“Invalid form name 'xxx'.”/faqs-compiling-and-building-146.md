---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146
title: 编译报错“Invalid form name 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid form name 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:40f3d9f9ae289d0c42cba33a561ecc9522898ece849c0776f570fe9f38bc334f
---

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/kNKmQWzWSE2mcGeoSnhEnA/zh-cn_image_0000002194158436.png?HW-CC-KV=V1&HW-CC-Date=20260612T024307Z&HW-CC-Expire=86400&HW-CC-Sign=731C561577D7B763F7488E3530DA8712CF023A14865441D4AABB4E3A334322A3 "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
