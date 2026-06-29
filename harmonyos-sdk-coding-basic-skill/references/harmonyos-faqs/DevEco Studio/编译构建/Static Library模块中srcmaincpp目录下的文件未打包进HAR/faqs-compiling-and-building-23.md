---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-23
title: Static Library模块中src/main/cpp目录下的文件未打包进HAR
breadcrumb: FAQ > DevEco Studio > 编译构建 > Static Library模块中src/main/cpp目录下的文件未打包进HAR
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d44cca98f4681130306bcca0c10d65a30b4737342bf0d68644a46e02bd9e42de
---

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/35SnhpMLRQmdaVxELTMBSg/zh-cn_image_0000002229758217.png?HW-CC-KV=V1&HW-CC-Date=20260612T024116Z&HW-CC-Expire=86400&HW-CC-Sign=C76F3CB4E4EADB580D9B90AE67795B011873409D0716C6E53B105DE2080DFD1E)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，仅会将dependencies内处于本模块路径下的本地依赖打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中，然后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/xek5AU89RdO7lz97bMQWfA/zh-cn_image_0000002229603749.png?HW-CC-KV=V1&HW-CC-Date=20260612T024116Z&HW-CC-Expire=86400&HW-CC-Sign=C15B024E8F898E93EC5D22E69CBB305A41D1927A86E212F8C3126A8227904B0E)
