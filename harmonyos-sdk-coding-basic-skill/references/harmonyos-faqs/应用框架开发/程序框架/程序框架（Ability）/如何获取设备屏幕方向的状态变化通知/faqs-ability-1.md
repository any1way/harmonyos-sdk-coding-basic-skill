---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-1
title: 如何获取设备屏幕方向的状态变化通知
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取设备屏幕方向的状态变化通知
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:21+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:5bb7e84519cf2e562a2034b59428286711c5ecbaa9637ae7a2a7020bf759874f
---
可以通过以下方式实现订阅系统环境变量的变化：

* 使用ApplicationContext订阅回调。
* 在AbilityStage组件容器中订阅回调。
* 在UIAbility组件中订阅回调。
* 在ExtensionAbility组件中订阅回调。

在onConfigurationUpdate回调方法中订阅或监听系统环境变量的变化，包括语言、颜色模式和屏幕方向。

详细请参见[获取/设置环境变量](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/获取设置环境变量/subscribe-system-environment-variable-changes.md>)。
