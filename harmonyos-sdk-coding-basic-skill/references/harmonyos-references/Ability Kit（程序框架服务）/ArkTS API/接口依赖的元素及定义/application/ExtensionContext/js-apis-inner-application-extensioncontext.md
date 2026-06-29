---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext
title: ExtensionContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ExtensionContext
category: harmonyos-references
scraped_at: 2026-06-01T15:31:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ee8653264e8a1f3336f296ea51e2f64e0a9b8c7c3e801810e55816b9b9cac791
---
ExtensionContext是[ExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)的上下文环境，继承自[Context](<../Context (Stage模型的上下文基类)/js-apis-inner-application-context.md#context>)。

ExtensionContext模块提供访问特定[ExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)的资源的能力。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentHapModuleInfo | [HapModuleInfo](../../bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | 所属Hap包的信息。 |
| config | [Configuration](<../../../通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md>) | 否 | 否 | 所属Module的配置信息。 |
| extensionAbilityInfo | [ExtensionAbilityInfo](../../bundleManager/ExtensionAbilityInfo/js-apis-bundlemanager-extensionabilityinfo.md) | 否 | 否 | 所属[ExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)的信息。 |

## 使用场景

PhonePC/2in1TabletTVWearable

ExtensionContext主要用于查询所属ExtensionAbility的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

**示例：**

在扩展的[FormExtensionAbility](<../../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)中获取上下文，查询该扩展的FormExtensionAbility所属HAP包等信息。

```
1. import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onAddForm(want: Want) {
6. console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
7. let extensionContext = this.context;
8. let hapInfo = extensionContext.currentHapModuleInfo;
9. console.info(`HAP name is: ${hapInfo.name}`);
10. let dataObj1: Record<string, string> = {
11. 'temperature': '11c',
12. 'time': '11:00'
13. };
14. let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
15. return obj1;
16. }
17. };
```
