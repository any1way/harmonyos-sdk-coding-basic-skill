---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-75
title: ApplicationContext、UIAbilityContext、Context的区别是什么
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > ApplicationContext、UIAbilityContext、Context的区别是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:54+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:7251c50ca4a3d553ce8cce3a73405c9942cbc9e999544ccd1b7dd7ede7fde432
---
* ApplicationContext 和 UIAbilityContext 都继承自基类 Context，不同的 Context 具有不同的属性和方法。

  ApplicationContext：应用级别的Context，提供了订阅应用组件生命周期变化、系统内存变化和应用系统环境变化的能力。可以在UIAbility、ExtensionAbility、AbilityStage中获取。
* UIAbilityContext：每个UIAbility包含一个Context属性，用于操作应用组件和获取组件配置信息。

**参考链接**

[应用上下文Context](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md>)
