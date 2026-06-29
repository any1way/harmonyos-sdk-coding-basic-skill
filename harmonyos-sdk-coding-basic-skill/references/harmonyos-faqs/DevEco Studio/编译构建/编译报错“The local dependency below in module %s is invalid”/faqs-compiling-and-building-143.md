---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143
title: 编译报错“The local dependency below in module %s is invalid”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The local dependency below in module %s is invalid”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0de725a6f2e09caabc8d7acfb30c57c5809bfdb96262bdd06f0406a221d660b6
---

**错误描述**

模块内添加本地依赖项无效。

**可能原因**

当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/HKzPdavrQ0uCGwREzCXcUQ/zh-cn_image_0000002194158324.png?HW-CC-KV=V1&HW-CC-Date=20260612T024303Z&HW-CC-Expire=86400&HW-CC-Sign=1319C708B347F3DAFA660BB117E06C24C463A99E6F6669DECA3F48540769A156)

**解决措施**

设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。
