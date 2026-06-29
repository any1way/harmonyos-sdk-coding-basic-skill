---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-update-guard-strategy
title: 修改策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 修改策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:50+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a44486434ac5797d0dd4c2f6bb43bffd6d65df703a8b7391e8429de0fddb30f3
---
## 场景介绍

当用户希望调整现有的屏幕时间守护规则时，可以调用更新管控策略的接口。我们kit支持根据参数中传入的策略名以及修改策略的方案，用户可以修改各种策略，如调整各个应用的停用起止时间。一旦修改完成并保存，系统将根据新的规则对用户的屏幕使用行为进行管控。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/mQZqDN7yT9u1zB8peWFimQ/zh-cn_image_0000002592379538.png?HW-CC-KV=V1&HW-CC-Date=20260611T071449Z&HW-CC-Expire=86400&HW-CC-Sign=C6839599045558A9CC1C3AC85457D227C95FFD2BEABDA55626E414C8C56ACDC2)

流程说明：

1. 应用调用更新管控策略的接口时，会拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则解析参数中传入的策略，并判断策略是否有效、是否存在。
3. 若策略有效，则记录到本地数据库，策略完成修改；否则，抛出相应错误码。

说明

1. 更新管控策略的策略名需和当前已有的策略一致，否则会抛出策略不存在错误。

## 接口说明

修改策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [updateGuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#updateguardstrategy>)(strategyName: string, guardStrategy: [GuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#guardstrategy>)): Promise<void> | 修改屏幕时间管控策略。 |

## 开发前提

修改管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用updateGuardStrategy，修改管控策略。

   ```
   1. private async updateStrategy(strategyName: string, guardStrategy: guardService.GuardStrategy): Promise<void> {
   2. try {
   3. await guardService.updateGuardStrategy(strategyName, guardStrategy);
   4. } catch (error) {
   5. let err: BusinessError = error as BusinessError;
   6. hilog.error(0x0000, 'GuardService',
   7. `updateGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   8. }
   9. }
   ```
