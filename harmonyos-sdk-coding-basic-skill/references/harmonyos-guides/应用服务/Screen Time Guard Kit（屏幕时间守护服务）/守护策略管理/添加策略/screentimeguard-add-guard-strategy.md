---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-add-guard-strategy
title: 添加策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 添加策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:49+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:8b37c97b9af3e5dab3e89567c886ab7635a2c9ce680c7b856376d78cf356965d
---
## 场景介绍

当用户希望创建新的屏幕时间守护规则时，可以调用添加管控策略的接口。根据参数中传入的策略，用户可以添加各种策略，如设置各个应用的停用起止时间。一旦策略被创建并启用，系统将根据规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/OadH0Qb6RQKJPcUeuqqkLg/zh-cn_image_0000002622699165.png?HW-CC-KV=V1&HW-CC-Date=20260611T071448Z&HW-CC-Expire=86400&HW-CC-Sign=4C94F4869E31ABB268E185EA38DE1808341858C4539BEB3C160A362778A0813C)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/3d8xO2Q4R7W4NgJZfIgdjA/zh-cn_image_0000002592219604.png?HW-CC-KV=V1&HW-CC-Date=20260611T071448Z&HW-CC-Expire=86400&HW-CC-Sign=3925D8869B586A4BB95EA348A0686B684595B9B137BE01238F939CE12E0E5D85)

流程说明：

1. 应用调用添加管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否已给本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则解析参数中传入的策略，判断策略是否有效、是否重复、数量是否超限。
3. 若策略正常，则记录到本地数据库；否则，抛出相应错误码。

说明

1. 管控策略可以设置为起止时间策略，表示策略在一天内配置的起始时间和结束时间内生效；也可以设置为总时长策略类型，表示一天内策略生效的总时长；也可以设置为共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额。具体可参考[TimeStrategyType](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#timestrategytype>) 。
2. 管控策略可以设置限制类型，按允许清单做限制表示对传入的应用之外的应用进行管控，按禁止清单做限制表示对传入的应用进行限制。具体可参考[RestrictionType](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#restrictiontype>) 。
3. 管控策略可以设置一周内重复执行时间，支持填写含有1-7数字的number数组，表示在周一到周日的某些天重复执行。具体可参考[TimeStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#timestrategy>) 。

## 接口说明

添加策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [addGuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#addguardstrategy>)(guardStrategy: [GuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#guardstrategy>)): Promise<void> | 添加屏幕时间管控策略。 |

## 开发前提

添加管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义屏幕时间管理策略。

   ```
   1. guardStrategy: guardService.GuardStrategy = {
   2. name: 'GuardStrategy',
   3. timeStrategy: {
   4. type: guardService.TimeStrategyType.START_END_TIME_TYPE,
   5. startTime: '19:00',
   6. endTime: '21:00',
   7. repeat: [1, 2, 3, 4, 5, 6, 7]
   8. },
   9. appInfo: { appTokens: [] }, // 可通过startAppPicker接口获取
   10. appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
   11. };
   ```
3. 调用addGuardStrategy，添加屏幕时间管控策略。

   ```
   1. private async addStrategy(guardStrategy: guardService.GuardStrategy): Promise<void> {
   2. try {
   3. await guardService.addGuardStrategy(guardStrategy);
   4. } catch (error) {
   5. let err: BusinessError = error as BusinessError;
   6. hilog.error(0x0000, 'GuardService',
   7. `addGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   8. }
   9. }
   ```
