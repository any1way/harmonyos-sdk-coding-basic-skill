---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensionability
title: TimeGuardExtensionAbility（屏幕时间守护扩展Ability）
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > TimeGuardExtensionAbility（屏幕时间守护扩展Ability）
category: harmonyos-references
scraped_at: 2026-06-11T16:50:34+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:79e4d169d7e8ff640a0065fa0f0a4033b68adf9521a836c72dfd3c464161859d
---
TimeGuardExtensionAbility是屏幕时间守护扩展Ability，提供extension回调，支持开发者在策略管控生效和策略停止时执行特定逻辑，以及支持开发者用户授予应用权限和取消应用授权时执行特定逻辑。TimeGuardExtensionAbility继承自[ExtensionAbility](<../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

## 导入模块

PhoneTablet

```
1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
```

## 属性

PhoneTablet

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [TimeGuardExtensionContext](../TimeGuardExtensionContext（屏幕时间守护扩展Context）/screentimeguard-timeguardextensioncontext.md) | 否 | 否 | [TimeGuardExtensionContext](../TimeGuardExtensionContext（屏幕时间守护扩展Context）/screentimeguard-timeguardextensioncontext.md)上下文环境，继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。 |

## onStart

PhoneTablet

onStart(strategyName: string): Promise<void>

当管控应用启动的策略管控生效时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 生效的时间管控策略名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

3. let index = 0; // 用于自增操作

5. function asyncIncrement(): Promise<void> {
6. // index自增的异步操作
7. return new Promise<void>((resolve) => {
8. index++;
9. resolve();
10. });
11. }

13. export default class EntryAbility extends TimeGuardExtensionAbility {
14. async onStart(strategyName: string): Promise<void> {
15. // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
16. await asyncIncrement();
17. console.info('test --- onStart:', strategyName, index);
18. }
19. }
```

## onStop

PhoneTablet

onStop(strategyName: string): Promise<void>

当管控应用启动的策略管控结束时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 结束的时间管控策略名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

3. let index = 0; // 用于自增操作

5. function asyncIncrement(): Promise<void> {
6. // index自增的异步操作
7. return new Promise<void>((resolve) => {
8. index++;
9. resolve();
10. });
11. }

13. export default class EntryAbility extends TimeGuardExtensionAbility {
14. async onStop(strategyName: string): Promise<void> {
15. // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
16. await asyncIncrement();
17. console.info('test --- onStop:', strategyName, index);
18. }
19. }
```

## onUserAuthSwitchOn

PhoneTablet

onUserAuthSwitchOn(): Promise<void>

当用户在“健康使用设备”中授予管控应用权限时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

3. let index = 0; // 用于自增操作

5. function asyncIncrement(): Promise<void> {
6. // index自增的异步操作
7. return new Promise<void>((resolve) => {
8. index++;
9. resolve();
10. });
11. }

13. export default class EntryAbility extends TimeGuardExtensionAbility {
14. async onUserAuthSwitchOn(): Promise<void> {
15. // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
16. await asyncIncrement();
17. console.info('test --- onUserAuthSwitchOn:', index);
18. }
19. }
```

## onUserAuthSwitchOff

PhoneTablet

onUserAuthSwitchOff(): Promise<void>

当用户在“健康使用设备”中授予管控应用权限时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

3. let index = 0; // 用于自增操作

5. function asyncIncrement(): Promise<void> {
6. // index自增的异步操作
7. return new Promise<void>((resolve) => {
8. index++;
9. resolve();
10. });
11. }

13. export default class EntryAbility extends TimeGuardExtensionAbility {
14. async onUserAuthSwitchOff(): Promise<void> {
15. // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
16. await asyncIncrement();
17. console.info('test --- onUserAuthSwitchOff:', index);
18. }
19. }
```
