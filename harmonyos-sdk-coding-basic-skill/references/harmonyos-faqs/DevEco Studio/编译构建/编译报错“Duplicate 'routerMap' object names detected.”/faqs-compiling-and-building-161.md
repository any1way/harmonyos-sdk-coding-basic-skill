---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161
title: 编译报错“Duplicate 'routerMap' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'routerMap' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d0d9e2ab0fb7e247a64b243bba8fb9b56f034df832bd0e3d78130f79b849f666
---

**错误描述**

routerMap配置中存在重复名称。

**可能原因**

当前模块的router\_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/9PBos0TvRf6FBPXO3G6AqA/zh-cn_image_0000002229603813.png?HW-CC-KV=V1&HW-CC-Date=20260612T024320Z&HW-CC-Expire=86400&HW-CC-Sign=845D688AA6FB0A8C0F074055D33686C377A0EEE632C2D29C9B9B565CC5A4C24D)

**解决措施**

修改router\_map.json文件中的name字段，确保其值唯一。
