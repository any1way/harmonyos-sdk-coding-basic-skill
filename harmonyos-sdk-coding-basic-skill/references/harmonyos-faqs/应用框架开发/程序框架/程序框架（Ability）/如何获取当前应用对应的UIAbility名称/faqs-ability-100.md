---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-100
title: 如何获取当前应用对应的UIAbility名称
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取当前应用对应的UIAbility名称
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:07+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:e3a5462f843189f67eff3d8fb6e62eefaa68f65c67fe4cc8323828d3dec31472
---
可以通过[bundleManager](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md>)的getBundleInfoForSelf()接口获取当前应用的[AbilityInfo](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/bundleManager/AbilityInfo/js-apis-bundlemanager-abilityinfo.md>)信息，其中参数bundleFlags需要包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ABILITY。AbilityInfo中包含当前应用的Ability名称、Bundle名称等信息。
