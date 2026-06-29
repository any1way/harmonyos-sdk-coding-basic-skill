---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autostartupmanager
title: @ohos.app.ability.autoStartupManager (开机自启管理能力)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.autoStartupManager (开机自启管理能力)
category: harmonyos-references
scraped_at: 2026-06-01T15:30:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f436ead48a69ebe4320291e97d79bd550be2782c6d05baaba9a95421af685d8a
---
autoStartupManager模块提供获取自身应用的开机自启状态。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { autoStartupManager } from '@kit.AbilityKit';
```

## autoStartupManager.getAutoStartupStatusForSelf

PhonePC/2in1TabletTVWearable

getAutoStartupStatusForSelf(): Promise<boolean>

获取当前应用的开机自启动状态。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在Phone、PC/2in1、Tablet和Wearable设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前应用已被用户设置为开机自启动，false表示当前应用未被用户设置为开机自启动。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../../../通用错误码/errorcode-universal.md)和[元能力子系统错误码](../../../错误码/元能力子系统错误码/errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |

**示例**：

```
1. import { autoStartupManager, UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. try {
7. autoStartupManager.getAutoStartupStatusForSelf().then((isAutoStartup: boolean) => {
8. console.info(`getAutoStartupStatusForSelf success, isAutoStartup: ${JSON.stringify(isAutoStartup)}.`);
9. }).catch((err: BusinessError) => {
10. console.error(`getAutoStartupStatusForSelf failed, err code: ${err.code}, err msg: ${err.message}.`);
11. });
12. } catch (err) {
13. let code = (err as BusinessError).code;
14. let msg = (err as BusinessError).message;
15. console.error(`getAutoStartupStatusForSelf failed, err code: ${code}, err msg: ${msg}.`);
16. }
17. }
18. }
```
