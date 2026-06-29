---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-23
title: 如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:175de95d1b068c97b35004deed09879c5144967257512525ee837844c40cecfc
---
应用所在设备的信息，可以通过@kit.BasicServicesKit的deviceInfo模块获取：

* SDK版本：deviceInfo.sdkApiVersion。
* 产品版本：deviceInfo.displayVersion。
* 设备类型（平板、手机）：deviceInfo.deviceType。
* build版本：deviceInfo.buildVersion。

更多请参见[@ohos.deviceInfo (设备信息)](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)。
