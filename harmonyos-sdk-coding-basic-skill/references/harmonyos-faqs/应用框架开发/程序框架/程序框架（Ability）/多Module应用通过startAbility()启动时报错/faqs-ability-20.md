---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20
title: 多Module应用通过startAbility()启动时报错
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多Module应用通过startAbility()启动时报错
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:31+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:550641822137d11d1b6b9db538a8062771048df3f884ab0dd90bbd1722ce44c5
---
**原因**

在同一个工程和设备中存在多个模块，并且这些模块之间存在调用关系，但并非所有HAP包都已安装到设备中。

**解决措施**

单击Run > Edit Configurations，在Deploy Multi Hap/Hsp中，勾选Deploy Multi Hap/Hsp Packaqes，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RQhIFthxRRKq8c_mUtl2Kg/zh-cn_image_0000002589944296.png?HW-CC-KV=V1&HW-CC-Date=20260612T022128Z&HW-CC-Expire=86400&HW-CC-Sign=7DF83DA6996237E7EA290896A647C2E9E4D4D5B400853EE83E2B978961D030DD)

**参考链接**

[设置HAP安装方式](../../../../../harmonyos-guides/编写与调试应用/应用调试/自定义运行调试配置/ide-run-debug-configurations.md#section531811771410)

[module.json5配置文件](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)
