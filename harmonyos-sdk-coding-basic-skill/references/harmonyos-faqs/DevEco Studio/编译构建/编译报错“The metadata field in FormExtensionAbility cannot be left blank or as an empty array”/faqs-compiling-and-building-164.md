---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-164
title: 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:63f13ffc02894a14e32abffc082fd5f9fa41540b92ce9c4147a9b7c86d6003c8
---
**错误描述**

FormExtensionAbility中的metadata字段必须非空且不为数组。

**可能原因**

在module.json5文件中，当ExtensionAbility的type为form时，metadata字段可以是空对象或空数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/mQdOkcbcT0iJH6JHxXXgyw/zh-cn_image_0000002194158712.png?HW-CC-KV=V1&HW-CC-Date=20260612T024323Z&HW-CC-Expire=86400&HW-CC-Sign=C5DE55BF865E199DBECAFCF5BC66CBC8F9C3A997213A2E2B976823391F0935B9)

**解决措施**

在module.json5中type为form的ExtensionAbility中配置metadata字段，具体配置方式参考[配置ArkTS卡片的配置文件](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md>)。
