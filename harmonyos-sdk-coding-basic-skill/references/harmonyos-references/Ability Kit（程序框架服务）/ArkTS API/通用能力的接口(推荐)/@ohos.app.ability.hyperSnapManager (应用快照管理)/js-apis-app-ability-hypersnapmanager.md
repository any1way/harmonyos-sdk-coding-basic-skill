---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-hypersnapmanager
title: @ohos.app.ability.hyperSnapManager (应用快照管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.hyperSnapManager (应用快照管理)
category: harmonyos-references
scraped_at: 2026-06-11T15:35:18+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1b250390cfdfca44287bbd840d6c9544596015a3e965ef3baa2a0ffae3c3422b
---
应用启动过程中的初始化流程可以提前制作成应用快照，从快照启动的应用不再重复执行初始化流程，从而起到加速启动的作用。hyperSnapManager模块提供应用快照管理的能力，包括启用或禁用应用的快照功能、请求重建应用快照等。

说明

本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 实现原理

PhonePC/2in1TabletTVWearable

应用快照只会制作一次，从应用快照启动可以省去应用初始化和AbilityStage创建所需的时间。

**图1** 快照启动流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/z5docE7pR32fnCLxnZM6xg/zh-cn_image_0000002622699421.png?HW-CC-KV=V1&HW-CC-Date=20260611T073517Z&HW-CC-Expire=86400&HW-CC-Sign=75C5FE67986AB67DEA0388DB9A60675C027015F908B2C23ADEDFC28802587315)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { hyperSnapManager } from '@kit.AbilityKit';
```

## hyperSnapManager.setHyperSnapEnabled

PhonePC/2in1TabletTVWearable

setHyperSnapEnabled(enableFlag: boolean): void

启用或禁用应用的快照功能。

说明

* 当通过本接口启用应用快照功能时，系统最终会根据应用兼容性、资源可用性和系统策略来决定是否创建或使用快照。当通过本接口禁用快照功能时，可以保证系统不会创建快照。
* 设置的值会在重启后保持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enableFlag | boolean | 是 | 表示快照功能开关标志。  - true：表示启用快照功能（系统将最终决策是否创建快照）。  - false：禁用应用快照功能。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../../../通用错误码/errorcode-universal.md)和[元能力子系统错误码](../../../错误码/元能力子系统错误码/errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000150 | Failed to send request to system service. |

**示例：**

```
1. import { hyperSnapManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 启用应用快照功能
6. hyperSnapManager.setHyperSnapEnabled(true);
7. console.info('Hyper Snap enabled successfully.');
8. } catch (err) {
9. let code = (err as BusinessError).code;
10. let message = (err as BusinessError).message;
11. console.error(`Failed to enable Hyper Snap. Code: ${code}, Message: ${message}`);
12. }
```

## hyperSnapManager.requestRebuildHyperSnap

PhonePC/2in1TabletTVWearable

requestRebuildHyperSnap(): void

请求重建应用的快照。

此方法会销毁当前进程对应的快照，系统将在合适的时机生成新的快照。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../../../通用错误码/errorcode-universal.md)和[元能力子系统错误码](../../../错误码/元能力子系统错误码/errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000150 | Failed to send request to system service. |

**示例：**

```
1. import { hyperSnapManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 请求重建应用快照
6. hyperSnapManager.requestRebuildHyperSnap();
7. console.info('Requested to rebuild Hyper Snap successfully.');
8. } catch (err) {
9. let code = (err as BusinessError).code;
10. let message = (err as BusinessError).message;
11. console.error(`Failed to request Hyper Snap rebuild. Code: ${code}, Message: ${message}`);
12. }
```
