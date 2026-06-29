---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-extension-ability
title: 使用AgentExtensionAbility组件实现智能体服务
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 端侧A2A框架开发指导 > 开发端侧智能体 > 使用AgentExtensionAbility组件实现智能体服务
category: harmonyos-guides
scraped_at: 2026-06-11T14:24:37+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:4e1ae30075d3a13f1555d381c208efca58907bf722636b50ae27ec88f1029bc4
---
## 概述

在跨应用协作场景下，开发者经常需要从系统应用调用其他应用提供的智能体服务，但缺少标准化的通信机制，导致集成成本高、安全认证复杂。从API version 24开始，支持开发者使用[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)类型的组件提供智能体服务。系统应用可以连接其他应用实现的[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)组件，并使用相应的智能体服务。通过使用该组件，可降低跨应用对接成本，保障通信安全，同时支持双向数据通道实时交互。

说明

本文描述中称被连接的[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)为服务端，称连接[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)的组件为客户端。

## 实现AgentExtensionAbility组件

在DevEco Studio工程中手动新建一个[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择"New > Directory"，新建一个目录并命名为agentextability。
2. 在AgentExtAbility目录，右键选择"New > ArkTS File"，新建一个文件并命名为AgentExtAbility.ets。

   ```
   1. ├── ets
   2. │ ├── agentextability
   3. │ │   ├── AgentExtAbility.ets
   ```
3. 在AgentExtAbility.ets文件中，补充[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)的导入模块，自定义类AgentExtAbility继承[AgentExtensionAbility](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md>)并实现生命周期回调。

   ```
   1. import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. export default class AgentExtAbility extends AgentExtensionAbility {
   5. private comProxy: common.AgentHostProxy | null = null;
   6. // 创建AgentExtensionAbility
   7. onCreate(want: Want) {
   8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   9. }

   11. // 连接
   12. onConnect(want: Want, proxy: common.AgentHostProxy) {
   13. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onConnect');
   14. this.comProxy = proxy;
   15. }

   17. // 断开连接
   18. onDisconnect(want: Want, proxy: common.AgentHostProxy) {
   19. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDisconnect');
   20. this.comProxy = null;
   21. }
   22. // 接收数据
   23. onData(proxy: common.AgentHostProxy, data: string) {
   24. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onData');
   25. try {
   26. let replyData = 'reply message';
   27. proxy.sendData(replyData);
   28. } catch (err) {
   29. let code = (err as BusinessError).code;
   30. let msg = (err as BusinessError).message;
   31. console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
   32. }
   33. }
   34. // 认证
   35. onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
   36. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onAuth');
   37. try {
   38. // 处理认证逻辑
   39. let authResult = 'auth success';
   40. proxy.authorize(authResult);
   41. } catch (err) {
   42. let code = (err as BusinessError).code;
   43. let msg = (err as BusinessError).message;
   44. console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
   45. }
   46. }
   47. // 销毁
   48. onDestroy() {
   49. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
   50. }
   51. }
   ```

   [AgentExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Ability/AgentExtensionAbility/entry/src/main/ets/agentextability/AgentExtAbility.ets#L15-L79)
4. 在工程Module对应的[module.json5配置文件](../../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中注册AgentExtensionAbility，type标签需要设置为"agent"，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. "extensionAbilities": [
   4. {
   5. "name": "AgentExtAbility",
   6. "icon": "$media:icon",
   7. "description": "agent",
   8. "type": "agent",
   9. "exported": true,
   10. "srcEntry": "./ets/agentextability/AgentExtAbility.ets",
   11. "metadata": [
   12. {
   13. "name": "ohos.extension.agent",
   14. "resource": "$profile:agent_config",
   15. }
   16. ]
   17. }
   18. ]
   19. }
   20. }
   ```
5. 在工程Module的resources/base/profile/目录下新建agent\_config.json文件，然后在其中配置[AgentCard](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentCard/js-apis-inner-application-agentcard.md>)信息，详细操作步骤请参考[Agent配置文件说明](../AgentExtensionAbility配置文件说明/agent-extension-configuration.md)。

## 使用AgentExtensionAbility组件收发数据

应用可以在服务端AgentExtensionAbility组件的[onData()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md#ondata>)方法中接收客户端传递的数据和[AgentHostProxy](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md>)对象，并且可以通过调用[AgentHostProxy](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md>)对象的[sendData()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md#senddata>)方法将数据发送给客户端。

```
1. import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class AgentExtAbility extends AgentExtensionAbility {
5. // ...
6. // 接收数据
7. onData(proxy: common.AgentHostProxy, data: string) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onData');
9. try {
10. let replyData = 'reply message';
11. proxy.sendData(replyData);
12. } catch (err) {
13. let code = (err as BusinessError).code;
14. let msg = (err as BusinessError).message;
15. console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
16. }
17. }
18. // ...
19. }
```

[AgentExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Ability/AgentExtensionAbility/entry/src/main/ets/agentextability/AgentExtAbility.ets#L16-L78)

## 使用AgentExtensionAbility组件接收和发送安全认证请求

应用可以在服务端AgentExtensionAbility组件的[onAuth()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)/js-apis-app-agent-agentextensionability.md#onauth>)方法中接收客户端的安全认证请求以及[AgentHostProxy](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md>)对象，并且可以通过[AgentHostProxy](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md>)的[authorize()](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AgentHostProxy/js-apis-inner-application-agenthostproxy.md#authorize>)方法向客户端发送安全认证请求。

```
1. import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class AgentExtAbility extends AgentExtensionAbility {
5. // ...
6. // 认证
7. onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onAuth');
9. try {
10. // 处理认证逻辑
11. let authResult = 'auth success';
12. proxy.authorize(authResult);
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let msg = (err as BusinessError).message;
16. console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
17. }
18. }
19. // ...
20. }
```

[AgentExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Ability/AgentExtensionAbility/entry/src/main/ets/agentextability/AgentExtAbility.ets#L17-L77)
