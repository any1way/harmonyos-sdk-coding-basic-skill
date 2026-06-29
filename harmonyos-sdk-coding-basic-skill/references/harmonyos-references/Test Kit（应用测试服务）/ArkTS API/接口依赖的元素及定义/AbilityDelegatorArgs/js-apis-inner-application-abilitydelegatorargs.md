---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs
title: AbilityDelegatorArgs
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 接口依赖的元素及定义 > AbilityDelegatorArgs
category: harmonyos-references
scraped_at: 2026-06-11T16:25:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:98668bd95f1ffac9437f592bda4d11c0b126eb18583338cba563c87e6f7f0ea0
---
AbilityDelegatorArgs模块提供在应用程序执行测试用例期间，获取测试用例参数AbilityDelegatorArgs对象的能力。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../../../../../harmonyos-guides/应用测试/单元测试和UI测试/自动化测试框架使用指导/单元测试框架使用指导/unittest-guidelines.md)中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

通过AbilityDelegatorRegistry中[getArguments](<../../@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)/js-apis-app-ability-abilitydelegatorregistry.md#abilitydelegatorregistrygetarguments>)方法获取。

## AbilityDelegatorArgs

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 当前被测试应用的包名。 |
| parameters | Record<string, string> | 否 | 否 | 当前启动单元测试的参数。 |
| testCaseNames | string | 否 | 否 | 测试用例名称。 |
| testRunnerClassName | string | 否 | 否 | 执行测试用例的测试执行器名称。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let args: abilityDelegatorRegistry.AbilityDelegatorArgs = abilityDelegatorRegistry.getArguments();
```
