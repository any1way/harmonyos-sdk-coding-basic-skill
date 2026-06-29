---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167
title: 编译报错“Duplicate 'Module-Abilities' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'Module-Abilities' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:30d615b4682298e02a7810ea0b2a31144ea9f6ee8eed963130fe8e1e83a5e246
---

**错误描述**

Module-Abilities对象名称重复。

**可能原因**

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/vgOAXpbNTvmiYXAVBWCanQ/zh-cn_image_0000002194158504.png?HW-CC-KV=V1&HW-CC-Date=20260612T024326Z&HW-CC-Expire=86400&HW-CC-Sign=23E72F4D5DF76E6276F49960AD7773AA9EDCEA30EE9F0EE8F4B4A71C6C449DDB)

**解决措施**

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。
