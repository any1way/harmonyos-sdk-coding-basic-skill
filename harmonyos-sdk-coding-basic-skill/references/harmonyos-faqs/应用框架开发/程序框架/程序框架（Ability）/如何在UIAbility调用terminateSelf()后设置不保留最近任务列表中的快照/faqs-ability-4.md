---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-4
title: 如何在UIAbility调用terminateSelf()后设置不保留最近任务列表中的快照
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在UIAbility调用terminateSelf()后设置不保留最近任务列表中的快照
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:02b3849bf85d1279300f7bfa6061005129462ca8f6aaa60f6b96a5c7b064ffc4
---
在HarmonyOS应用开发中，UIAbilityContext的[terminateSelf()](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#terminateself-1>)方法被用来结束当前的UIAbility实例。

如果希望在调用terminateSelf()后，让应用在最近任务列表中不保留快照，可以通过在[module.json5配置文件](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中配置removeMissionAfterTerminate为true来实现。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. // ...
7. "removeMissionAfterTerminate": true,
8. }
9. ],
10. // ...
11. }
12. }
```

[module\_remove.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/module_remove.json5#L5-L63)

说明

* removeMissionAfterTerminate字段的默认值为false，表示默认情况下应用会在最近任务列表中保留快照。

* 仅当removeMissionAfterTerminate设置为true时，调用terminateSelf()后应用不会在最近任务列表中保留快照。
