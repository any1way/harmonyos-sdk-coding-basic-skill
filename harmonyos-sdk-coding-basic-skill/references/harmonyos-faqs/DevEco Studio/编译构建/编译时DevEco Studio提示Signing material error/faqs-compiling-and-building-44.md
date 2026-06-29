---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44
title: 编译时DevEco Studio提示Signing material error
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio提示Signing material error
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:74a831d56394522a7877b2721831e7fd66e4cd731cd3be7ed452ea9594eaf518
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Xf61zxyoQCuv5emBF3poqg/zh-cn_image_0000002229604197.png?HW-CC-KV=V1&HW-CC-Date=20260612T024135Z&HW-CC-Expire=86400&HW-CC-Sign=4AE2B7951C8A5C533F36E173D6193BAA8F8D86C429C58D5C27403CF1E00520C5 "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
