---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext
title: AbilityStageContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityStageContext
category: harmonyos-references
scraped_at: 2026-06-01T15:31:01+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:47d42e31cf5327728253c54c2ad5ee5de33e15a4b2623b13b2455ecb56a0902b
---
AbilityStageContext是AbilityStage的上下文环境，继承自[Context](<../Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>)。

AbilityStageContext提供允许访问特定于abilityStage的资源的能力，包括获取AbilityStage对应的ModuleInfo对象、环境变化对象。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

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
| currentHapModuleInfo | [HapModuleInfo](../../bundleManager/HapModuleInfo/js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | AbilityStage对应的ModuleInfo对象。 |
| config | [Configuration](<../../../通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md>) | 否 | 否 | 环境变量。 |
| launchElement24+ | [ElementName](../../bundleManager/ElementName/js-apis-bundlemanager-elementname.md) | 否 | 是 | 创建AbilityStage时的ElementName。  **元服务API**：从API version 24开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { AbilityStage } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyAbilityStage extends AbilityStage {
5. onCreate() {
6. let abilityStageContext = this.context;
7. // 获取当前模块名
8. let name = abilityStageContext.currentHapModuleInfo.name;
9. // 获取当前模块语言
10. let language = abilityStageContext.config.language;
11. // 获取创建AbilityStage时的ElementName
12. let elementName = abilityStageContext.launchElement;
13. if (elementName) {
14. hilog.info(0x0000, 'testTag', 'bundleName: %{public}s', elementName.bundleName);
15. hilog.info(0x0000, 'testTag', 'moduleName: %{public}s', elementName.moduleName);
16. hilog.info(0x0000, 'testTag', 'abilityName: %{public}s', elementName.abilityName);
17. }
18. }
19. }
```
