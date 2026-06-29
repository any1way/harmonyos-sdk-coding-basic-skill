---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1
title: 编译报错“JS heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“JS heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:09eac23ee4b10396e868373d99f394a64981d5f388fd8b51371126aa74996322
---

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/e_MxWhq3Sj-oALaWOhWEKQ/zh-cn_image_0000002194158628.png?HW-CC-KV=V1&HW-CC-Date=20260612T024057Z&HW-CC-Expire=86400&HW-CC-Sign=B3823882387BC462FA659879904D545AE319DCD2ACEB5C670BC531B3157395B7)

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用3.1.0及以上版本的hvigor时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/zStQb22fRCusc9vOQwoGBw/zh-cn_image_0000002194318244.png?HW-CC-KV=V1&HW-CC-Date=20260612T024057Z&HW-CC-Expire=86400&HW-CC-Sign=393C37B6DD065AE272D0E2E509272507A8B8BD8D319FD34E7682055285EBED75)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
