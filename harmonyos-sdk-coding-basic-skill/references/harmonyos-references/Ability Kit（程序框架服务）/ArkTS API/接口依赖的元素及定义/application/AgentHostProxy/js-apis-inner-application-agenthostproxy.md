---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agenthostproxy
title: AgentHostProxy
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AgentHostProxy
category: harmonyos-references
scraped_at: 2026-06-01T15:31:07+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:6a8f2d5ae86fbdeb930a323bc82e7f3b1b3ae1a1730aa42e8602b24acb3f636a
---
AgentHostProxy用于从[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)服务端向客户端发送数据或安全认证请求。

说明

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不支持在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## AgentHostProxy

PhonePC/2in1TabletTVWearable

### sendData

PhonePC/2in1TabletTVWearable

sendData(data: string): void

从[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)服务端给客户端发送数据。

**元服务API**：从 API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 待发送到[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)客户端的数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../../../../通用错误码/errorcode-universal.md)和[元能力子系统错误码](../../../../错误码/元能力子系统错误码/errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 35600002 | Failed to send the IPC message. |

**示例：**

```
1. import { common, AgentExtensionAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[AgentExtensionAbility] ';

6. export default class MyAgentExtensionAbility extends AgentExtensionAbility {
7. // 数据发送处理
8. onData(proxy: common.AgentHostProxy, data: string) {
9. console.info(TAG + `onData ${data}`);
10. try {
11. // 发送数据到AgentExtensionAbility的客户端
12. proxy.sendData('Hello Client');
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let msg = (err as BusinessError).message;
16. console.error(`${TAG} sendData failed, err code: ${code}, err msg: ${msg}.`);
17. }
18. }
19. }
```

### authorize

PhonePC/2in1TabletTVWearable

authorize(handshakeData: string): void

从[AgentExtensionAbility](<../../../Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)服务端给客户端发送安全认证请求。

**元服务API**：从 API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handshakeData | string | 是 | 待发送到客户端的安全认证数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../../../../通用错误码/errorcode-universal.md)和[元能力子系统错误码](../../../../错误码/元能力子系统错误码/errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 35600002 | Failed to send the IPC message. |

**示例：**

```
1. import { common, AgentExtensionAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[AgentExtensionAbility] ';

6. export default class MyAgentExtensionAbility extends AgentExtensionAbility {
7. // 数据发送处理
8. onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
9. console.info(TAG + `onAuth ${handshakeData}`);
10. try {
11. // 发送认证数据到AgentExtensionAbility的客户端
12. proxy.authorize('handshake_token');
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let msg = (err as BusinessError).message;
16. console.error(`${TAG} authorize failed, err code: ${code}, err msg: ${msg}.`);
17. }
18. }
19. }
```
