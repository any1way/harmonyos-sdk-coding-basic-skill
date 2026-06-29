---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-56
title: 应用免安装的限制、字段解释以及如何自测
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 应用免安装的限制、字段解释以及如何自测
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:301e229b0fd4b211e93db1496a4028efd58349affcd2fe3ce39a7cdef1819fc1
---
* 免安装限制：免安装HAP的总大小限制为10M。10M是指所有HAP的总大小。如果App内有多个HAP，所有HAP的总大小不能超过10M。分包时，每个文件的大小不能超过2M。
* DeliveryWithInstall：配置应用的可选安装功能。具体场景是在应用市场下载安装时，是否跟随应用一起安装。Entry模块的该字段允许设置为false。配置为true的HAP包也会计算在免安装的10M限制内。
* InstallationFree：标识当前Module是否支持免安装特性。如果应用的Entry类型Module的该字段配置为true，Feature类型Module的该字段也必须配置为true。
* 自测：开发者需编写一个服务中心，模拟处理免安装请求。

**参考链接**

[module.json5配置文件](../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)
