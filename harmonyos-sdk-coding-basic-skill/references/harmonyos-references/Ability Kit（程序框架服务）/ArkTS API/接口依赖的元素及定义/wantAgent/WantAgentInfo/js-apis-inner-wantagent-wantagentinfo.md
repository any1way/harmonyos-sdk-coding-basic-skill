---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo
title: WantAgentInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > wantAgent > WantAgentInfo
category: harmonyos-references
scraped_at: 2026-06-01T15:31:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5ec7d8f3db8b2bcc28f05d241ead16619f73ed39a8feb85b4ef7ea01549243c5
---
定义触发WantAgent所需要的信息。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { wantAgent as abilityWantAgent } from '@kit.AbilityKit';
```

## WantAgentInfo

PhonePC/2in1TabletTVWearable

定义触发WantAgent所需要的信息，可以作为[getWantAgent](<../../../通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md#wantagentgetwantagent>)的入参创建指定的WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wants | Array<[Want](<../../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)> | 否 | 否 | 将被执行的动作列表。wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| operationType(deprecated) | [wantAgent.OperationType](<../../../已停止维护的接口/@ohos.wantAgent (WantAgent模块)/js-apis-wantagent.md#operationtype>) | 否 | 是 | 动作类型。  从API version 7 开始支持，从API version 11 开始废弃，建议使用actionType11+替代。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| actionType11+ | [abilityWantAgent.OperationType](<../../../通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md#operationtype>) | 否 | 是 | 动作类型。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| requestCode | number | 否 | 否 | 开发者自定义的请求码，用于标识将被执行的动作。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| wantAgentFlags(deprecated) | Array<[wantAgent.WantAgentFlags](<../../../已停止维护的接口/@ohos.wantAgent (WantAgent模块)/js-apis-wantagent.md#wantagentflags>)> | 否 | 是 | 动作执行属性。  从API version 7 开始支持，从API version 11 开始废弃，建议使用actionFlags11+替代。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| actionFlags11+ | Array<[abilityWantAgent.WantAgentFlags](<../../../通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md#wantagentflags>)> | 否 | 是 | 动作执行属性。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
