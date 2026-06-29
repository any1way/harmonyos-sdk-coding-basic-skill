---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-72
title: Web组件是否支持通过URL Scheme协议跳转其它App
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件是否支持通过URL Scheme协议跳转其它App
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a8c62b07c727d523ba3c6de35de975bf8edd2b0363325ee574d9425675b204be
---
Web组件支持通过URL Scheme跳转到其它App。开发者可以通过Web组件的[onLoadIntercept](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/事件/arkts-basic-components-web-events.md#onloadintercept10>)回调拦截默认跳转逻辑，并在其中使用Deep Linking或App Linking的方式自定义跳转逻辑完成应用跳转。

**参考链接**

[使用Deep Linking实现应用间跳转](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/使用Deep Linking实现应用间跳转/deep-linking-startup.md>)

[使用App Linking实现应用间跳转](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/应用间跳转/拉起指定应用/使用App Linking实现应用间跳转/app-linking-startup.md>)
