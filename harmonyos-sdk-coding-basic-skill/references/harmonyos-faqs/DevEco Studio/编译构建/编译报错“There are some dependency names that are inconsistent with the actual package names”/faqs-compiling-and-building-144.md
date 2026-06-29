---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144
title: 编译报错“There are some dependency names that are inconsistent with the actual package names”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“There are some dependency names that are inconsistent with the actual package names”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:efe6a16305d4efd84f7abb11dfce67d4e629a65ffa90b9c6dfd8db14bfdb5ec4
---

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/vDi25lJ7SkS2lfUfaYy7hw/zh-cn_image_0000002229758445.png?HW-CC-KV=V1&HW-CC-Date=20260612T024305Z&HW-CC-Expire=86400&HW-CC-Sign=38BFF7D9BF0F4DA89DBB86BC5A119068F318D9762BC6382993DBDF9006BE765D)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
