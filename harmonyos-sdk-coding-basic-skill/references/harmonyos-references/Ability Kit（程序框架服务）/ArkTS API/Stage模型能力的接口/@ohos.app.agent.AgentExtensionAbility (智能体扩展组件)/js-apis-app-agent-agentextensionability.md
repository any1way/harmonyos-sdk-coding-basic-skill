---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability
title: @ohos.app.agent.AgentExtensionAbility (智能体扩展组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.agent.AgentExtensionAbility (智能体扩展组件)
category: harmonyos-references
scraped_at: 2026-06-11T15:34:48+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:39b390dae23dc2e306605d75fb1c596f410876442eaeb6853c3e513146a7ba5e
---
AgentExtensionAbility继承自[ExtensionAbility](<../@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)，提供智能体扩展能力，包括智能体服务的创建、销毁、连接、断开的生命周期回调接口，以及接收客户端所发送数据和安全认证的回调接口。

本文将AgentExtensionAbility组件提供方称为服务端，将AgentExtensionAbility组件使用方称为客户端。

说明

本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口不支持在[har](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)包中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AgentExtensionAbility } from '@kit.AbilityKit';
```

## 生命周期

PhonePC/2in1TabletTVWearable

**图1** AgentExtensionAbility生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/2dSYpC1aRXSL6txah3N88w/zh-cn_image_0000002622699419.png?HW-CC-KV=V1&HW-CC-Date=20260611T073447Z&HW-CC-Expire=86400&HW-CC-Sign=94F24D47A0B60CC6DF7D4A27E65A9CFD9FB7907DF82DA7D6DB1CB8F274A66BA1)

* **onCreate**

  当AgentExtensionAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。
* **onConnect**

  当客户端连接AgentExtensionAbility成功后，系统会触发该回调。
* **onDisconnect**

  当客户端与AgentExtensionAbility断开连接时，系统会触发该回调。
* **onDestroy**

  当AgentExtensionAbility被销毁时，系统会触发该回调。

## AgentExtensionAbility

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 24开始，该属性支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [AgentExtensionContext](<../../接口依赖的元素及定义/application/AgentExtensionContext (智能体扩展组件上下文)/js-apis-inner-application-agentextensioncontext.md>) | 否 | 否 | AgentExtensionAbility的上下文环境，继承自[ExtensionContext](../../接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md)。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

当AgentExtensionAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 当前AgentExtensionAbility相关的[Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)类型信息，包括Ability名称、Bundle名称等。 |

**示例：**

```
1. import { AgentExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AppServiceExtAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. // 创建AgentExtensionAbility
8. onCreate(want: Want) {
9. hilog.info(0x0000, TAG, `onCreate, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
10. }
11. }
```

### onConnect

PhonePC/2in1TabletTVWearable

onConnect(want: Want, proxy: AgentHostProxy): void

当客户端连接AgentExtensionAbility成功后，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 当前AgentExtensionAbility相关的[Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)类型信息，包括Ability名称、Bundle名称等。 |
| proxy | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md) | 是 | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md)对象，用于与客户端进行通信。 |

**示例：**

```
1. import { AgentExtensionAbility, Want, common} from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AgentExtensionAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. onConnect(want: Want, proxy: common.AgentHostProxy){
8. hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
9. }
10. }
```

### onDisconnect

PhonePC/2in1TabletTVWearable

onDisconnect(want: Want, proxy: AgentHostProxy): void

当客户端与AgentExtensionAbility断开连接时，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 当前AgentExtensionAbility相关的[Want](<../../通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)类型信息，包括Ability名称、Bundle名称等。 |
| proxy | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md) | 是 | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md)对象，用于与客户端进行通信。 |

**示例：**

```
1. import { AgentExtensionAbility, Want, common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AgentExtensionAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. onDisconnect(want: Want, proxy: common.AgentHostProxy) {
8. hilog.info(0x0000, TAG, `onDisconnect, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
9. }
10. }
```

### onData

PhonePC/2in1TabletTVWearable

onData(proxy: AgentHostProxy, data: string): void

当AgentExtensionAbility接收到客户端发送的数据时，系统会触发该回调。服务端可以在此回调中通过[AgentHostProxy.senddata](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md#senddata)向客户端发送数据。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md) | 是 | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md)对象，用于与客户端进行通信。 |
| data | string | 是 | 表示接收到的数据。 |

**示例：**

```
1. import { AgentExtensionAbility, common} from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AgentExtensionAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. onData(proxy : common.AgentHostProxy, data : string ){
8. hilog.info(0x0000, TAG, `onData, data: ${data}`);
9. }
10. }
```

### onAuth

PhonePC/2in1TabletTVWearable

onAuth(proxy: AgentHostProxy, handshakeData: string): void

当AgentExtensionAbility接收到客户端发送的安全认证请求时，系统会触发该回调。服务端可以在此回调中处理接收到的安全认证请求，并通过[AgentHostProxy.authorize](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md#authorize)向客户端发送安全认证请求。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md) | 是 | [AgentHostProxy](../../接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md)对象，用于向客户端发送安全认证请求。 |
| handshakeData | string | 是 | 表示接收到的安全认证数据。 |

**示例：**

```
1. import { AgentExtensionAbility, common} from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AgentExtensionAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. onAuth(proxy : common.AgentHostProxy, handshakeData : string ){
8. hilog.info(0x0000, TAG, `onAuth, handshakeData: ${handshakeData}`);
9. }
10. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

当AgentExtensionAbility被销毁时，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**示例：**

```
1. import { AgentExtensionAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AgentExtensionAbility]';

6. export default class AgentExt extends AgentExtensionAbility {
7. onDestroy() {
8. hilog.info(0x0000, TAG, `onDestroy`);
9. }
10. }
```
