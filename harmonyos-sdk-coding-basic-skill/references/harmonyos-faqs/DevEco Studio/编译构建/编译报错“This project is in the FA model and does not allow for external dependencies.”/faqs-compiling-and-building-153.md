---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-153
title: 编译报错“This project is in the FA model and does not allow for external dependencies.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“This project is in the FA model and does not allow for external dependencies.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c23a46f24e53fb80ce5ff76d42ffd62845b24be71009389b2f005d23fa16a1d8
---

**错误描述**

FA模型项目不得依赖外部项目模块。

**可能原因**

在FA模型项目中，build-profile.json5文件的srcPath字段引用了外部项目模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sV7puRCSRbKqGc0WewTGNg/zh-cn_image_0000002194318412.png?HW-CC-KV=V1&HW-CC-Date=20260612T024313Z&HW-CC-Expire=86400&HW-CC-Sign=31BC77213C2FACD87B9BB2F01B9967BDD28512808C27DF55D215F3E65A693065)

**解决措施**

在项目根目录的build-profile.json5文件中，移除srcPath字段依赖的外部项目模块。
