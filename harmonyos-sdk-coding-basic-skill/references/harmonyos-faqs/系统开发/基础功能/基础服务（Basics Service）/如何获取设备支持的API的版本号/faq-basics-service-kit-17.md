---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-17
title: 如何获取设备支持的API的版本号
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何获取设备支持的API的版本号
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:16d19fe9e4d7d30c340f9348781faef55f02c582388366a01cea22ac1b58e511
---
可以通过设备信息模块deviceInfo查询，常见的版本号获取方式如下：

* 系统软件API版本：deviceInfo.sdkApiVersion。
* 首个版本系统软件API版本：deviceInfo.firstApiVersion。
* 发行版系统API版本：deviceInfo.distributionOSApiVersion。

**参考链接**

[@ohos.deviceInfo (设备信息)](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)
