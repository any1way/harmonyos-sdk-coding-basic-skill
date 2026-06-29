---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-9
title: 系统设置只展示应用申请过的权限
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 系统设置只展示应用申请过的权限
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8ab7edc5967897fd53c97e410ad2de5f0cd36f462f9eb742328fad8e91c62a27
---
应用的权限设置中只展示应用申请过的权限，该特性是系统规格，只有在调用[requestPermissionsFromUser](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.abilityAccessCtrl (程序访问控制管理)/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9>)这个接口，并且用户选择是否授予权限之后，才会在应用详情页显示该权限开关。该设计特性考量：这个可以让用户看到一个更干净的权限管理页面，一个用户从来没有打开过的应用，进入应用详情页面却有众多权限，用户也会不理解。
