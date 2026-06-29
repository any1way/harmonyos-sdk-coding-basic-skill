---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157
title: 编译报错“Unrecognized archive format in parameterFile”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Unrecognized archive format in parameterFile”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:daba996d43ae2def8a63fd17ec4734df14ead740df6710ea6d3b6c14bbc60c0a
---

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/M8wiKoo4QxmQUDhIde2I0g/zh-cn_image_0000002194318392.png?HW-CC-KV=V1&HW-CC-Date=20260612T024316Z&HW-CC-Expire=86400&HW-CC-Sign=C46B3A7B741B44A95153FDF764146BA78F9BBD7779CDF0EAF465B57EF0069E0C)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
