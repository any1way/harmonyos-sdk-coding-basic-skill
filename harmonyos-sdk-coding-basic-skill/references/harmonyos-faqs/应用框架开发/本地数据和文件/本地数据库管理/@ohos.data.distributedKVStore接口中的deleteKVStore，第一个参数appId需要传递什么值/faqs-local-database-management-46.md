---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46
title: @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a83874d8f4121aaca13b419245e2aa50a257d609fb9daaaf0a9b07c814b7d02e
---
appId是调用方应用的包名。通过调用[bundleManager.getBundleInfoForSelf()](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself>)获取BundleInfo，然后通过BundleInfo对象的signatureInfo属性获取appId。
