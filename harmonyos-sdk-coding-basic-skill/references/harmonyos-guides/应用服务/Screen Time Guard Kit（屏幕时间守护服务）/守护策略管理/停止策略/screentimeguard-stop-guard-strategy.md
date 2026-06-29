---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-stop-guard-strategy
title: 停止策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 停止策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:54+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:4e3b6f92d443d4ff75495627789c39bbe4c6d2fd5aecb8ba771fd5951814e583
---
## 场景介绍

当用户希望停止某个管控规则时，可以调用停止管控策略的接口。根据参数中传入的策略名，应用可以停止对应管控策略。一旦策略被停止，系统将不再根据该规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/TSaGXrwFSAKo_-GhbH1xig/zh-cn_image_0000002622699169.png?HW-CC-KV=V1&HW-CC-Date=20260611T071452Z&HW-CC-Expire=86400&HW-CC-Sign=7F4297263E5B5AE513B75B06F11276A8EA6C15AE641F887F9ABD3993A555FAFA)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Wd3mOPo_TnW-lR2Tribswg/zh-cn_image_0000002592219608.png?HW-CC-KV=V1&HW-CC-Date=20260611T071452Z&HW-CC-Expire=86400&HW-CC-Sign=0C0F5276B75E002EE2A456B536E64B0D930163B094CA01FB84BD4BCF7380F6C5)

流程说明：

1. 应用继承TimeGuardExtensionAbility，实现onStop方法，此步非必需。
2. 应用调用停止管控策略的接口，会拉起健康使用设备查询本应用是否已申请权限、用户是否已给本应用授权。
3. 若没有权限，则抛出相应错误码。若有权限，则解析参数中传入的策略名称，判断策略是否存在。
4. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
5. 若停止策略时正在执行策略，则策略会正常停止，健康使用设备会记录策略停止状态；若停止策略时策略并未执行，该接口将抛出策略未在执行中的错误码。
6. 策略生效期间停止策略，会拉起extension进程，执行TimeGuardExtensionAbility的onStop回调。在非策略生效期间停止策略，不会触发onStop回调。
7. 停止该策略后，若该应用不存在任何启动状态的策略，则该应用被设置为可卸载。
8. 停止该策略后，若设备中不存在任何启动状态的策略，则系统时间设置为可修改。

## 接口说明

停止策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [stopGuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#stopguardstrategy>)(strategyName: string): Promise<void> | 根据策略名称，停止其管控策略。 |
| [onStop](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/TimeGuardExtensionAbility（屏幕时间守护扩展Ability）/screentimeguard-timeguardextensionability.md#onstop>)(strategyName: string): Promise<void> | 在策略结束时执行特定逻辑。 |

## 开发前提

停止管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 停止管控策略

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用stopGuardStrategy，停止管控策略。

   ```
   1. private async stopStrategy(strategyName: string): Promise<void> {
   2. try {
   3. await guardService.stopGuardStrategy(strategyName);
   4. // ...
   5. } catch (error) {
   6. let err: BusinessError = error as BusinessError;
   7. hilog.error(0x0000, 'GuardService',
   8. `stopGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   9. }
   10. }
   ```

## 接收管控策略结束回调（可选）

开发者若需要在策略结束时执行特定逻辑（如发送通知提醒用户），可以通过接收策略结束时的回调来实现。

1. 导入相关模块。

   ```
   1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onStop回调。

   ```
   1. export default class TimeGuardExtAbility extends TimeGuardExtensionAbility {
   2. async onStop(strategyName: string): Promise<void> {
   3. hilog.info(0x0000, 'TimeGuardExtensionAbility', `Strategy-${strategyName} onStop`);
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
