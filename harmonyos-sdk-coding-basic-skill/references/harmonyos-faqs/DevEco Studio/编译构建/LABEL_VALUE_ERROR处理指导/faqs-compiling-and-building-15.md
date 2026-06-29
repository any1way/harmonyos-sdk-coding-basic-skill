---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-15
title: LABEL_VALUE_ERROR处理指导
breadcrumb: FAQ > DevEco Studio > 编译构建 > LABEL_VALUE_ERROR处理指导
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d5e6b0ad9f7baed22fdddd24c7ef82caefed785678924498f4bdd91b6f9881f4
---

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/T6qgEY0CTHS1bP-6jFiNHg/zh-cn_image_0000002229758717.png?HW-CC-KV=V1&HW-CC-Date=20260612T024108Z&HW-CC-Expire=86400&HW-CC-Sign=0AA67A97395F8CD3957618FFFBFAA2A151A2D09EDF3281391F3CD850FAF9F0EA)

**解决措施**

该问题由config.json文件的资源引用规则变更引起，需将“label”字段的取值修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/kju85OmmSuWDqMXADV3uBQ/zh-cn_image_0000002194158844.png?HW-CC-KV=V1&HW-CC-Date=20260612T024108Z&HW-CC-Expire=86400&HW-CC-Sign=42238EAE05495A28FAB5883744AF2CB62BD6AE22A806DDBC8C836A3CDF77A8D3)
