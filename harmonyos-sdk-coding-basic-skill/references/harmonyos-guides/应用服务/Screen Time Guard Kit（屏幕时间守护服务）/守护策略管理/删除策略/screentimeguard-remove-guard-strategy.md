---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-remove-guard-strategy
title: 删除策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 删除策略
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:51+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c04ba24c41e45fb47209876253452888a41154ca1fea224712cde398f48e4b15
---
## 场景介绍

当应用希望删除现有的屏幕时间守护规则时，可以调用删除管控策略的接口。根据参数中传入的策略名删除对应的策略。一旦策略被删除，系统将不再根据该规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/JXjipocbRoSPDXo_tI8yjw/zh-cn_image_0000002622699167.png?HW-CC-KV=V1&HW-CC-Date=20260611T071450Z&HW-CC-Expire=86400&HW-CC-Sign=0D347AC9E844C3C3ECE1D30D9E6895B9601F2A1FD12C4F7593D4C136DF27ACCB)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Hmzp_XuaQhu5_fijPi3Rog/zh-cn_image_0000002592219606.png?HW-CC-KV=V1&HW-CC-Date=20260611T071450Z&HW-CC-Expire=86400&HW-CC-Sign=496104678261932BF045F8639168F5BC6B2CB1EFBAE563905A6B5A41469BC292)

流程说明：

1. 应用调用删除管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码。若有权限，则解析参数中传入的策略名称，判断策略是否存在。
3. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
4. 若策略在执行，则会先停止管控策略再删除。

## 接口说明

删除策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [removeGuardStrategy](<../../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#removeguardstrategy>)(strategyName: string): Promise<void> | 删除管控策略。 |

## 开发前提

删除管控策略需要申请用户授权，请先参考[请求用户授权](../../用户授权管理/请求用户授权/screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用removeGuardStrategy，删除管控策略。

   ```
   1. private async removeStrategy(strategyName: string): Promise<void> {
   2. try {
   3. await guardService.removeGuardStrategy(strategyName);
   4. } catch (error) {
   5. let err: BusinessError = error as BusinessError;
   6. hilog.error(0x0000, 'GuardService',
   7. `removeGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
   8. }
   9. }
   ```
