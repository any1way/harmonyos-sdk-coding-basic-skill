---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39
title: 编译报错“Only one default card can be configured in the form_config.json file”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Only one default card can be configured in the form_config.json file”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a9a6eef1895fb58430a2b5ef92038b9a16c56fe585330511c9f7dd651d3d2620
---

**问题现象**

DevEco Studio编译失败。提示：Only one default card can be configured in the form\_config.json file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/1hESj4GrS-qmajiUwbbvjQ/zh-cn_image_0000002229758657.png?HW-CC-KV=V1&HW-CC-Date=20260612T024129Z&HW-CC-Expire=86400&HW-CC-Sign=63EED8C62BC5A7CF17D41618C8BF3153D72950128E70AE46A21A7C193FC2F70B "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
