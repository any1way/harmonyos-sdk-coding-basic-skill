---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-94
title: 如果有多个UIAbility，如何判断应用进入后台
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如果有多个UIAbility，如何判断应用进入后台
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:03+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:489978c0d5b38ca6e9841141a87a11b42330fc4534732e74275066ee721f495c
---
在多UIAbility情况下，只有当所有UIAbility均在后台时，应用才处于后台状态。

可以使用[ApplicationContext.on('abilityLifecycle')](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ApplicationContext (应用上下文)/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle>)接口，该方法第一个参数为'abilityLifecycle'类型，表示应用内UIAbility的生命周期，第二个参数为一个回调函数，可以监听应用前后台切换状态。
