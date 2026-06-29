---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common
title: @ohos.app.ability.common (Ability公共模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.common (Ability公共模块)
category: harmonyos-references
scraped_at: 2026-06-11T15:34:16+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:013b2d4d258b19bd9be792c297b31179df9a1fca47a4156968ee92709d9500d0
---
本模块提供Ability Kit中常用公共能力的纯类型定义，包含各类上下文对象、回调接口和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIAbilityContext

PhonePC/2in1TabletTVWearable

type UIAbilityContext = \_UIAbilityContext.default

[UIAbility](<../@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md>)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIAbilityContext.default](../../接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md) | UIAbilityContext组件上下文。 |

## AbilityStageContext

PhonePC/2in1TabletTVWearable

type AbilityStageContext = \_AbilityStageContext.default

[AbilityStage](<../@ohos.app.ability.AbilityStage (AbilityStage组件管理器)/js-apis-app-ability-abilitystage.md>)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStageContext.default](../../接口依赖的元素及定义/application/AbilityStageContext/js-apis-inner-application-abilitystagecontext.md) | AbilityStage组件上下文。 |

## ApplicationContext

PhonePC/2in1TabletTVWearable

type ApplicationContext = \_ApplicationContext.default

应用上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ApplicationContext.default](<../../接口依赖的元素及定义/application/ApplicationContext (应用上下文)/js-apis-inner-application-applicationcontext.md>) | 应用上下文。 |

## BaseContext

PhonePC/2in1TabletTVWearable

type BaseContext = \_BaseContext.default

所有Context类型的父类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_BaseContext.default](../../接口依赖的元素及定义/application/BaseContext/js-apis-inner-application-basecontext.md) | 所有Context的父类。 |

## Context

PhonePC/2in1TabletTVWearable

type Context = \_Context.default

[Stage模型](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Ability Kit术语/ability-terminology.md#stage模型>)的上下文基类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_Context.default](<../../接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>) | Stage模型的上下文基类。 |

## ExtensionContext

PhonePC/2in1TabletTVWearable

type ExtensionContext = \_ExtensionContext.default

[ExtensionAbility](<../@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ExtensionContext.default](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md) | ExtensionAbility组件上下文。 |

## FormExtensionContext

PhonePC/2in1TabletTVWearable

type FormExtensionContext = \_FormExtensionContext.default

[FormExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)组件上下文，继承自[ExtensionContext](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormExtensionContext.default](<../../../../Form Kit（卡片开发服务）/ArkTS API/application/FormExtensionContext/js-apis-inner-application-formextensioncontext.md>) | FormExtensionAbility组件上下文。 |

## VpnExtensionContext11+

PhonePC/2in1TabletTVWearable

type VpnExtensionContext = \_VpnExtensionContext.default

[VpnExtensionAbility](<../../../../网络/Network Kit（网络服务）/ArkTS API/@ohos.app.ability.VpnExtensionAbility (三方VPN能力)/js-apis-vpnextensionability.md>)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_VpnExtensionContext.default](<../../../../网络/Network Kit（网络服务）/ArkTS API/VpnExtensionContext/js-apis-inner-application-vpnextensioncontext.md>) | VpnExtensionAbility组件上下文。 |

## EventHub

PhonePC/2in1TabletTVWearable

type EventHub = \_EventHub.default

EventHub是系统提供的基于发布-订阅模式实现的事件通信机制。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EventHub.default](../../接口依赖的元素及定义/application/EventHub/js-apis-inner-application-eventhub.md) | 系统提供的基于发布-订阅模式实现的事件通信机制。 |

## PacMap

PhonePC/2in1TabletTVWearable

type PacMap = \_PacMap

存储基础数据类型的容器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_PacMap](../../接口依赖的元素及定义/ability/DataAbilityHelper/js-apis-inner-ability-dataabilityhelper.md#pacmap) | 存储基础数据类型的容器。 |

## AbilityResult

PhonePC/2in1TabletTVWearable

type AbilityResult = \_AbilityResult

定义Ability被拉起并退出后返回的结果码和数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityResult](../../接口依赖的元素及定义/ability/AbilityResult/js-apis-inner-ability-abilityresult.md) | 定义Ability被拉起并退出后返回的结果码和数据。 |

## AbilityStartCallback11+

PhonePC/2in1TabletTVWearable

type AbilityStartCallback = \_AbilityStartCallback

定义了拉起UIExtensionAbility的回调结果，通常作为[UIAbilityContext.startAbilityByType](../../接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)/[UIExtensionContext.startAbilityByType](<../@ohos.app.ability.UIExtensionContentSession (带界面扩展能力的界面操作类)/js-apis-app-ability_18888586.md#startabilitybytype11>)的入参传入。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStartCallback](../../接口依赖的元素及定义/application/AbilityStartCallback/js-apis-inner-application-abilitystartcallback.md) | 定义拉起UIExtensionAbility的回调结果。 |

## ConnectOptions

PhonePC/2in1TabletTVWearable

type ConnectOptions = \_ConnectOptions

在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ConnectOptions](../../接口依赖的元素及定义/ability/ConnectOptions/js-apis-inner-ability-connectoptions.md) | 在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。 |

## UIExtensionContext10+

PhonePC/2in1TabletTVWearable

type UIExtensionContext = \_UIExtensionContext.default

[UIExtensionAbility](<../@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)/js-apis-app-abili_64670486.md>)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIExtensionContext.default](../../接口依赖的元素及定义/application/UIExtensionContext/js-apis-inner-application-uiextensioncontext.md) | UIExtensionAbility组件上下文。 |

## EmbeddableUIAbilityContext12+

PhonePC/2in1TabletTVWearable

type EmbeddableUIAbilityContext = \_EmbeddableUIAbilityContext.default

[EmbeddableUIAbility](<../@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)/js-apis-app-ability-embeddableuiability.md>)组件上下文，继承自Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EmbeddableUIAbilityContext.default](../../接口依赖的元素及定义/application/EmbeddableUIAbilityContext/js-apis-app-embeddableuiabilitycontext.md) | EmbeddableUIAbility组件上下文。 |

## PhotoEditorExtensionContext12+

PhonePC/2in1TabletTV

type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default

[PhotoEditorExtensionAbility](<../@ohos.app.ability.PhotoEditorExtensionAbility (支持图片编辑能力的ExtensionAbility组件)/js-apis_76813348.md>)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AppExtension.PhotoEditorExtension

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PhotoEditorExtensionContext.default](../../接口依赖的元素及定义/application/PhotoEditorExtensionContext/js-apis-app-ability-photoeditorextensioncontext.md) | PhotoEditorExtensionAbility组件上下文。 |

## UIServiceProxy14+

PhonePC/2in1TabletTVWearable

type UIServiceProxy = \_UIServiceProxy.default

UIServiceProxy提供了与UIServiceExtensionAbility服务端数据通信的能力。UIServiceExtensionAbility是一类特殊的ExtensionAbility组件，这类组件由系统提供，通常用于提供浮窗组件相关扩展能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceProxy.default](../../接口依赖的元素及定义/application/UIServiceProxy/js-apis-inner-application-uiserviceproxy.md) | 提供与UIServiceExtensionAbility服务端数据通信的能力。 |

## UIServiceExtensionConnectCallback14+

PhonePC/2in1TabletTVWearable

type UIServiceExtensionConnectCallback = \_UIServiceExtensionConnectCallback.default

在连接指定的UIServiceExtensionAbility服务时作为入参，用于提供UIServiceExtensionAbility连接回调数据能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceExtensionConnectCallback.default](../../接口依赖的元素及定义/application/UIServiceExtensionConnectCallback/js-apis-inner-application-uiservice_20803489.md) | 提供UIServiceExtensionAbility连接回调数据能力。 |

## AppServiceExtensionContext20+

PhonePC/2in1TabletTVWearable

type AppServiceExtensionContext = \_AppServiceExtensionContext.default

[AppServiceExtensionAbility](<../@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)/js-apis-app-ability-a_17903419.md>)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AppServiceExtensionContext.default](<../../接口依赖的元素及定义/application/AppServiceExtensionContext (应用后台服务扩展组件上下文)/js-apis-inner-application-_79664473.md>) | AppServiceExtensionAbility组件上下文。 |

## FormEditExtensionContext22+

PhonePC/2in1TabletTVWearable

type FormEditExtensionContext = \_FormEditExtensionContext.default

[FormEditExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)/js-apis-app-form-formeditextensionability.md>)组件上下文，继承自[UIExtensionContext](../../接口依赖的元素及定义/application/UIExtensionContext/js-apis-inner-application-uiextensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormEditExtensionContext.default](<../../../../Form Kit（卡片开发服务）/ArkTS API/application/FormEditExtensionContext/js-apis-inner-application-formeditextensioncontext.md>) | FormEditExtensionAbility组件上下文。 |

## LiveFormExtensionContext22+

PhonePC/2in1TabletTVWearable

type LiveFormExtensionContext = \_LiveFormExtensionContext.default

[LiveFormExtensionAbility](<../../../../Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)/js-apis-app-form-liveformextensionability.md>)组件上下文，继承自[ExtensionContext](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_LiveFormExtensionContext.default](<../../../../Form Kit（卡片开发服务）/ArkTS API/application/LiveFormExtensionContext/js-apis-application-liveformextensioncontext.md>) | LiveFormExtensionAbility组件上下文。 |

## AgentCard24+

PhonePC/2in1TabletTVWearable

type AgentCard = \_AgentCard

[AgentCard](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md)相当于Agent(智能体)的"名片"，用于描述Agent的能力和技能，由开发者在Agent的配置文件agent\_config.json中配置。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentCard](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md) | Agent(智能体)的"名片"，用于描述Agent的能力和技能。 |

## AgentProvider24+

PhonePC/2in1TabletTVWearable

type AgentProvider = \_AgentProvider

[AgentProvider](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentprovider)表示Agent的服务提供商。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentProvider](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentprovider) | Agent的服务提供商。 |

## AgentCapabilities24+

PhonePC/2in1TabletTVWearable

type AgentCapabilities = \_AgentCapabilities

[AgentCapabilities](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentcapabilities)用来定义Agent支持的可选能力。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentCapabilities](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentcapabilities) | 定义Agent支持的可选能力。 |

## AgentSkill24+

PhonePC/2in1TabletTVWearable

type AgentSkill = \_AgentSkill

[AgentSkill](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentskill)表示Agent可以执行的不同能力或功能。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentSkill](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentskill) | 表示Agent可以执行的不同能力或功能。 |

## AgentAppInfo24+

PhonePC/2in1TabletTVWearable

type AgentAppInfo = \_AgentAppInfo

[AgentAppInfo](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentappinfo)表示Agent所属的应用信息。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentAppInfo](../../接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md#agentappinfo) | Agent所属的应用信息。 |

## AgentHostProxy24+

PhonePC/2in1TabletTVWearable

type AgentHostProxy = \_AgentHostProxy

[AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md)用于从[AgentExtensionAbility](<../@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)服务端向客户端发送数据或安全认证请求。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md) | 用于从[AgentExtensionAbility](<../@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)服务端向客户端发送数据或安全认证请求。 |

## AgentExtensionContext24+

PhonePC/2in1TabletTVWearable

type AgentExtensionContext = \_AgentExtensionContext

[AgentExtensionContext](<../../接口依赖的元素及定义/application/AgentExtensionContext (智能体扩展组件上下文)/js-apis-inner-application-agentextensioncontext.md>)是[AgentExtensionAbility](<../@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)的上下文环境，继承自[ExtensionContext](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentExtensionContext](<../../接口依赖的元素及定义/application/AgentExtensionContext (智能体扩展组件上下文)/js-apis-inner-application-agentextensioncontext.md>) | [AgentExtensionAbility](<../@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)的上下文环境，继承自[ExtensionContext](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md)。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. let uiAbilityContext: common.UIAbilityContext;
4. let abilityStageContext: common.AbilityStageContext;
5. let applicationContext: common.ApplicationContext;
6. let baseContext: common.BaseContext;
7. let context: common.Context;
8. let uiExtensionContext: common.UIExtensionContext;
9. let extensionContext: common.ExtensionContext;
10. let formExtensionContext: common.FormExtensionContext;
11. let vpnExtensionContext: common.VpnExtensionContext;
12. let eventHub: common.EventHub;
13. let pacMap: common.PacMap;
14. let abilityResult: common.AbilityResult;
15. let abilityStartCallback: common.AbilityStartCallback;
16. let connectOptions: common.ConnectOptions;
17. let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
18. let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
19. let uiServiceProxy : common.UIServiceProxy;
20. let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
21. let appServiceExtensionContext : common.AppServiceExtensionContext;
22. let formEditExtensionContext : common.FormEditExtensionContext;
23. let liveFormExtensionContext : common.LiveFormExtensionContext;
24. let agentCard: common.AgentCard;
25. let agentProvider: common.AgentProvider;
26. let agentCapabilities: common.AgentCapabilities;
27. let agentSkill: common.AgentSkill;
28. let agentAppInfo: common.AgentAppInfo;
29. let agentHostProxy: common.AgentHostProxy;
30. let agentExtensionContext: common.AgentExtensionContext;
```
