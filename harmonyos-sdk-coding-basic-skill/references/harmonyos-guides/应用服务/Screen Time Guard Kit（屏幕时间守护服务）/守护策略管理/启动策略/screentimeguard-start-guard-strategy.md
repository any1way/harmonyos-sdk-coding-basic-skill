---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-guard-strategy
title: 启动策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 启动策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:53+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:862a63973288555d91fca017b136f66e1449d649798f14cb03c3f6828118374e
---
## 场景介绍

当应用希望启动某个管控规则时，可以调用启动管控策略的接口。根据参数中传入的策略名，应用可以启动对应管控策略。一旦策略被创建并启用，系统将根据规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/zZY0wxR9TT2cxRkHY2Kf4Q/zh-cn_image_0000002592379540.png?HW-CC-KV=V1&HW-CC-Date=20260611T071452Z&HW-CC-Expire=86400&HW-CC-Sign=93E3FA9B7D8ED536C4FB7FEE70352F27F4ADAC4827B2C0A8E2DCB981F03EFF4E)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/JpEARLmTSiy53mxVGE286w/zh-cn_image_0000002622859049.png?HW-CC-KV=V1&HW-CC-Date=20260611T071452Z&HW-CC-Expire=86400&HW-CC-Sign=EA6F01336786DA5740C20D5B3A83094359A51FC5CD95EEFB3D5BB317FD726243)

流程说明：

1. 继承TimeGuardExtensionAbility，实现onStart方法，此步非必需。
2. 调用启动管控策略的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
3. 若开发者没有权限或用户未授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的策略名称，判断策略是否存在。
4. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
5. 若查询的策略未执行，则正常启动策略，并记录启动状态；否则，抛出策略已在执行中的错误码。
6. 策略启动后，系统时间被设置为不可修改，若管控发起应用在[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md#接口说明)时没有设置应用配置信息或应用配置为不可卸载，会被设置为不可卸载。
7. 当到了管控生效的时间，管控开始生效，拉起extension进程，执行TimeGuardExtensionAbility的onStart回调。

## 接口说明

启动策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startGuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#startguardstrategy>)(strategyName: string): Promise<void> | 根据策略名称，启动其管控策略。 |
| [onStart](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/TimeGuardExtensionAbility（屏幕时间守护扩展Ability）/screentimeguard-timeguardextensionability.md#onstart>)(strategyName: string): Promise<void> | 在策略启动时执行特定逻辑。 |

## 开发前提

启动管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 启动管控策略

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用startGuardStrategy，启动管控策略。

   ```
   1. private async startStrategy(strategyName: string): Promise<void> {
   2. try {
   3. await guardService.startGuardStrategy(strategyName);
   4. // ...
   5. } catch (error) {
   6. let err: BusinessError = error as BusinessError;
   7. hilog.error(0x0000, 'GuardService',
   8. `startGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   9. }
   10. }
   ```

## 接收管控策略生效回调（可选）

开发者若需要在策略生效时执行特定逻辑（如发送通知提醒用户），可以通过接收策略生效时的回调来实现。

1. 导入相关模块。

   ```
   1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onStart回调。

   ```
   1. export default class TimeGuardExtAbility extends TimeGuardExtensionAbility {
   2. async onStart(strategyName: string): Promise<void> {
   3. hilog.info(0x0000, 'TimeGuardExtensionAbility', `Strategy-${strategyName} onStart`);
   4. }
   5. }
   ```
3. 在工程中entry模块的module.json5文件中的"extensionAbilities"节点添加如下代码。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "TimeGuardExtAbility",
   4. "type": "screenTimeGuard",
   5. "srcEntry": "./ets/timeguardextability/TimeGuardExtAbility.ets",
   6. "exported": false,
   7. "skills": [
   8. {
   9. "actions": [
   10. "action.ohos.timeGuard.listener"
   11. ]
   12. }
   13. ],
   14. }
   15. ],
   ```
