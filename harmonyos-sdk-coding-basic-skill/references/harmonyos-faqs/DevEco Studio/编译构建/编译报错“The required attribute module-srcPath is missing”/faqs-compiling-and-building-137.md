---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137
title: 编译报错“The required attribute module-srcPath is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute module-srcPath is missing”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:968c891b71dd156bc6af4c736297a785e08c91697dcbb03da64df54a16bb9dbd
---

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/zaE1UwBVTEGs5zNvU_76mw/zh-cn_image_0000002229758669.png?HW-CC-KV=V1&HW-CC-Date=20260612T024257Z&HW-CC-Expire=86400&HW-CC-Sign=C84096FB4EC370170F17B719BED90D243DB2F3A60CBA45F7D3EC761282CD2C53)

**解决措施**

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
