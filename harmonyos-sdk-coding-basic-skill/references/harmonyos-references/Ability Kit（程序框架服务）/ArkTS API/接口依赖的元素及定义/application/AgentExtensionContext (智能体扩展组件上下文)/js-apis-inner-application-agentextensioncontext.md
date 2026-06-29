---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentextensioncontext
title: AgentExtensionContext (智能体扩展组件上下文)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AgentExtensionContext (智能体扩展组件上下文)
category: harmonyos-references
scraped_at: 2026-06-01T15:31:05+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9dd3770c20ac9384cc85e0d711f3658f766bd6efd6962ba53d340e1f29fa3d95
---
AgentExtensionContext模块是[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)的上下文环境，继承自[ExtensionContext](../ExtensionContext/js-apis-inner-application-extensioncontext.md)。

AgentExtensionContext为开发者提供访问当前[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)智能体所配置的[AgentCard](../AgentCard/js-apis-inner-application-agentcard.md)信息的能力。

说明

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 在本文档的示例中，通过this.context来获取AgentExtensionContext，其中this代表继承自AgentExtensionAbility的实例。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## AgentExtensionContext

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| agentCard | [AgentCard](../AgentCard/js-apis-inner-application-agentcard.md) | 否 | 否 | 当前[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)所配置的[AgentCard](../AgentCard/js-apis-inner-application-agentcard.md#agentcard-1)信息。 |

**示例：**

```
1. import { AgentExtensionAbility, common } from '@kit.AbilityKit';

3. export default class AgentExtension extends AgentExtensionAbility {
4. onCreate(): void {
5. let tmpContext: common.AgentExtensionContext = this.context; // 获取AgentExtensionContext
6. console.info(`agentCard info data: ${JSON.stringify(tmpContext.agentCard)}.`);
7. }
8. }
```
