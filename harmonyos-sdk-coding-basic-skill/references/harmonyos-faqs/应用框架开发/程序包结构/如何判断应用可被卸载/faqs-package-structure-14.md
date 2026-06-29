---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-14
title: 如何判断应用可被卸载
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何判断应用可被卸载
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:01830c3c0d4da89c98e479ae3fdf60239c63f9cadacdcb4ff51f2d36ddcd225c
---
1. 使用bundleManager.getApplicationInfo获取应用程序信息。
2. ApplicationInfo具有removable属性，可用于判断应用是否可卸载。

**参考链接**

[ApplicationInfo](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/bundleManager/ApplicationInfo/js-apis-bundlemanager-applicationinfo.md>)
