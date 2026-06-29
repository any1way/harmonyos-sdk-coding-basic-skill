---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-135
title: 编译报错“The service widget file contains one or more references to HSPs”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The service widget file contains one or more references to HSPs”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2442df8bb546fbcc2a856f8a8d835635cf4af039e7c62fa906ad4b08eaafdc7c
---

**错误描述**

服务卡片文件包含一个或多个HSP模块的引用。

**可能原因**

服务卡片文件中引用了HSP模块类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6zGvLbY1SzaTWmYESM1giw/zh-cn_image_0000002229758293.png?HW-CC-KV=V1&HW-CC-Date=20260612T024255Z&HW-CC-Expire=86400&HW-CC-Sign=C9BF4B7CAC3B84F3BB66E7B6CB6AE17009E5C661C5347F47E0B92961139EE4AA)

**解决措施**

在服务卡片文件中，移除关于HSP类型模块的引用。
