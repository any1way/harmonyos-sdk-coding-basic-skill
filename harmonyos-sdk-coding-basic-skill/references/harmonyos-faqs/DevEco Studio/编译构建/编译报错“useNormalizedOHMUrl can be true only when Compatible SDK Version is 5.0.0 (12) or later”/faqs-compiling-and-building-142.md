---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-142
title: 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8d9965b1d2b665a0ccc74b517a2d6739414d403cf33c351502c2b13c11e23c99
---
**错误描述**

仅当兼容SDK版本为5.0.0(12)及以上版本时，useNormalizedOHMUrl才可以设置为true。

**可能原因**

当compatibleSdkVersion为5.0.0(12)以下版本时，设置useNormalizedOHMUrl为true导致。

**解决措施**

检查工程级build-profile.json5文件中的compatibleSdkVersion配置。如果compatibleSdkVersion为 4.1.0(11) 及之前版本，请将[useNormalizedOHMUrl](../../../../harmonyos-guides/构建应用/配置文件/工程级build-profile.json5文件/ide-hvigor-build-profile-app.md#section13181758123312)设置为false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/vKySfa_aS7Ku-nV9qe89Pg/zh-cn_image_0000002363676020.png?HW-CC-KV=V1&HW-CC-Date=20260612T024303Z&HW-CC-Expire=86400&HW-CC-Sign=FF4FC10711EB9F4825EE56D6856A7394265BB4612926BAD262D9D71DA1114841)
