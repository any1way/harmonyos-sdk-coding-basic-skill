---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-21
title: 编译报错“Failed to generate test project build system”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to generate test project build system”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:65b28e1c23c9b523d73e822e932ed8457889eb526930e3f843f894e21671fec6
---

**问题现象**

执行多模块Native模块构建时，出现“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/AdRPqc4RRuK7N1Xnn0yj-g/zh-cn_image_0000002194158584.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=97F7BAB9DCA232F893EBAB3A47DB065433CBC4FCB9E60E74F094C9F34DDD8CF4)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行Make Module {moduleName}完成单独构建。注意：此方案需避免多模块并行构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/UZwrRdMwQPCYGtdxCw7wZg/zh-cn_image_0000002229758457.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=7730611150304C7884182DC0D0B4A0465F8196E85F2E3A2AAC1F5B381F19F4C0)
