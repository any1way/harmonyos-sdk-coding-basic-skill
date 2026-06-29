---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-36
title: 编译报错 “Unknown resource name”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错 “Unknown resource name”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:28+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4d6809c07ad56e54f8e5cde88170d7a146f6d04d6dac90c89034b06469179948
---
**场景一：**

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/FNJ5q538QHOwVE3fHmR2Ew/zh-cn_image_0000002229603765.png?HW-CC-KV=V1&HW-CC-Date=20260612T024127Z&HW-CC-Expire=86400&HW-CC-Sign=A9E912702B57EDEAA5F4314E83C84446C8720CE55CF4ED1C2AF8CCCE85D0D818)

**解决措施**

需要满足以下条件：

1. 资源需放置在模块B目录resource/base路径下，参考链接：[应用资源](../../../../best-practices/一次开发，多端部署/多设备界面开发/多设备资源文件/bpta-multi-device-resource.md#应用资源)。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

**场景二：**

**问题现象**

引用模块的方式不正确，如果引用的是其他模块的代码，也会导致资源未找到的错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/4gGKkun8TKG0ArDsje0DjQ/zh-cn_image_0000002194158372.png?HW-CC-KV=V1&HW-CC-Date=20260612T024127Z&HW-CC-Expire=86400&HW-CC-Sign=3FB3F0A70F486190D71B1B124D970B5CEFEAA662EB83D436E6B4D217ED2D4866)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_VLJZkGPREWKsLRaIRP3-w/zh-cn_image_0000002229603773.png?HW-CC-KV=V1&HW-CC-Date=20260612T024127Z&HW-CC-Expire=86400&HW-CC-Sign=38FF73968A19268C32D3B41B067374451690422CD13F4678EE54DC3E108374E1)

**解决措施**

在oh-package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/LxzScOpWQtSQ5dFnoMVmqw/zh-cn_image_0000002194317992.png?HW-CC-KV=V1&HW-CC-Date=20260612T024127Z&HW-CC-Expire=86400&HW-CC-Sign=CF7F0FC593BD0213448A85D85BD902B4D650FFD336EB86DB3ED36C778F33ED7C)

**场景三：**

**问题现象**

HSP A 申请了某个权限并引用了资源。在构建所有依赖 A 的组件时，报错提示找不到 A 引用的资源。

**解决措施**

在引用方的配置文件中手动添加对应资源可以解决此问题。
