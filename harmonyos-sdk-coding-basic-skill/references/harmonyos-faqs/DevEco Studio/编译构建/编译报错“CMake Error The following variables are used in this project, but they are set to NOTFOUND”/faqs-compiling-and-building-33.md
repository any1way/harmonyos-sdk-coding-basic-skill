---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-33
title: 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:daa55dc6455734c440ca6037752a2f889979d8e8944fade17eb460280331264d
---

**问题现象**

Native工程使用find\_path时出现报错。因find\_path未在CMAKE\_SYSROOT限定路径中找到目标文件而触发该报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/G3qd-djUTTGBS-FPFZchBA/zh-cn_image_0000002229603961.png?HW-CC-KV=V1&HW-CC-Date=20260612T024122Z&HW-CC-Expire=86400&HW-CC-Sign=F07A3102805435CE830B16D5843B426D4531E0213C7773A365984382DBD8A965 "点击放大")

**解决措施**

OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将“D:/demo”添加至搜索路径：

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

添加后，即可使用find\_path查找“D:/demo”目录下的文件。
