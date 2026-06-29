---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-30
title: 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c488874a6d160d441c8cc7df050dd6a59973f31edb31b0fed2d18557b1df120e
---
**问题现象**

工程构建时，出现ArkTS语法告警提示，详情请参见FAQ。

报错信息：

1. ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2. ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ZQJPJVjERf-EgNQIhutGVQ/zh-cn_image_0000002429325678.png?HW-CC-KV=V1&HW-CC-Date=20260612T024120Z&HW-CC-Expire=86400&HW-CC-Sign=C249776F56A9864B9088C4C327D85A76F16B6503CF6CD1FD1B754A484A272FF6)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/F7ZnxRd0Snem9QE8lJJdsg/zh-cn_image_0000002429485750.png?HW-CC-KV=V1&HW-CC-Date=20260612T024120Z&HW-CC-Expire=86400&HW-CC-Sign=3E998CAC72E5E2F09831794AC0CC594B47F35DD902967554E8E223C81C475EC7)

**解决措施**

该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/arkts.md)
