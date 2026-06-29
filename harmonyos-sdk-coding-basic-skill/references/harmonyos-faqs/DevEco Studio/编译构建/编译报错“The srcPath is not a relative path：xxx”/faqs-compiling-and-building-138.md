---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-138
title: 编译报错“The srcPath is not a relative path：xxx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The srcPath is not a relative path：xxx”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed4c2b06f314cdffbc8ef0283a0ea3deb4a6e2c17c8f63b896bff7c64a9508df
---
**错误描述**

srcPath字段配置值必须为相对路径。

**可能原因**

开发者在hvigorconfig.ts文件中使用includeNode方法时，srcPath必须是相对路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/MzU9RvupQ22hXRKLgVoRaA/zh-cn_image_0000002229604333.png?HW-CC-KV=V1&HW-CC-Date=20260612T024259Z&HW-CC-Expire=86400&HW-CC-Sign=612EC7C94FC589D9C0DEF0281CB5EE33659062CC3A90A1ABFC9834C1BE40A49F)

**解决措施**

确保项目的hvigorconfig.ts文件中使用includeNode时的传参srcPath为相对路径。

**参考链接**

[Hvigor脚本文件](../../../../harmonyos-guides/构建应用/概述/构建系统生命周期/ide-hvigor-life-cycle.md#section810245135914)
