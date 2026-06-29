---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-76
title: 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:55+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:fa57e2ca091300f067a9be8c4780c5d225c5f3c89988406b3b1037fcba8318fa
---
401错误表示提供的上下文类型不正确，需要使用UIAbility的上下文。获取[UIAbilityContext](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>)的方式如下：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. let uiAbilityContext = this.context;
6. // ...
7. }
8. }
```

[GetUIAbilityContext.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetUIAbilityContext.ets#L21-L28)

**参考链接**

[应用上下文Context](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md>)
