---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-query-guard-strategies
title: 查询策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 查询策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:51+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:4e2ecf3ac702f1ac0743eeb1a7d707d74173b245f3e9621bd85b73241361b0c5
---
## 场景介绍

当用户希望查看现有的屏幕时间守护规则时，可以调用查询管控策略的接口。通过成功调用查询策略接口，用户可以浏览已创建的所有管控策略，如查看各个应用的停用起止时间或可使用时长。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/F2w-lNaRQV-MURGQyaVkwA/zh-cn_image_0000002622859047.png?HW-CC-KV=V1&HW-CC-Date=20260611T071450Z&HW-CC-Expire=86400&HW-CC-Sign=605BD9D7116EC3833533ACEADAB1354C1D5350881F594655E2B5DAB100CB0001)

流程说明：

1. 应用调用查询管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则返回对应应用下的所有管控策略。

## 接口说明

查询策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [queryGuardStrategies](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#queryguardstrategies>)(): Promise<[GuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#guardstrategy>)[]> | 查询该应用下的所有管控策略。 |

## 开发前提

查询管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用queryGuardStrategy，查询对应应用下的所有管控策略。

   ```
   1. private async isStrategyExist(strategyName: string): Promise<boolean> {
   2. try {
   3. let guardStrategies: guardService.GuardStrategy[] = await guardService.queryGuardStrategies();
   4. for (let i = 0; i < guardStrategies.length; i++) {
   5. if (guardStrategies[i].name === strategyName) {
   6. return true;
   7. }
   8. }
   9. } catch (error) {
   10. let err: BusinessError = error as BusinessError;
   11. hilog.error(0x0000, 'GuardService',
   12. `queryGuardStrategies failed, errCode is ${err.code}, errMessage is ${err.message}`);
   13. }
   14. return false;
   15. }
   ```
