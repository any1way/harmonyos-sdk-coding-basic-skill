---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160
title: 编译报错“CMake task execution failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake task execution failed”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0883a2b8adcdeb06ce62de320890f3c598125d5e88f078f340fd54d5fb07ded9
---

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/p-gsdWOASKugFFrMcjR1MQ/zh-cn_image_0000002229604133.png?HW-CC-KV=V1&HW-CC-Date=20260612T024319Z&HW-CC-Expire=86400&HW-CC-Sign=299C3395063A821B83AF097936E6D6F7718F4F389E40CFC7314CC704443A064B)

**解决措施**

移除arguments字段中的“--version”参数。
