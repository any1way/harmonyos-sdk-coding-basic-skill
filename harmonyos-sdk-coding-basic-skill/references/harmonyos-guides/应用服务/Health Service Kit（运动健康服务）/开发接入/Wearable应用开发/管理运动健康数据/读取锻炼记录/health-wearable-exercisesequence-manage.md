---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-exercisesequence-manage
title: 读取锻炼记录
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Wearable应用开发 > 管理运动健康数据 > 读取锻炼记录
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:22+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:3f676345fd1719ea8a9f3634596f46d82f0af8b39fce88266e0b4f36cee35d72
---
## 场景介绍

读取最新一条锻炼记录。

## 约束与限制

从5.1.1(19) Release版本开始支持。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [readData](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstorereaddata-1>)<T extends [ExerciseSequence](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequence>)>(request: [ExerciseSequenceReadRequest](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#exercisesequencereadrequest>)): Promise<T[]> | 查询最新一条锻炼记录。 |

说明

当前ExerciseSequenceReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据。

## 开发前检查

* 完成[申请运动健康服务](../../../开发准备/申请运动健康服务/health-apply.md)与[配置Client ID](<../../../开发准备/配置Client ID/health-configuration-client-id.md>)。
* 接口首次调用前，需先使用[init](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreinit>)方法进行初始化。
* 需先通过[用户授权](../../../PhoneTablet应用开发/管理用户授权/health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API错误码/errorcode-healthservice.md>)，常见问题请参考[Health Service Kit常见问题](<../../../../Health Service Kit常见问题/health-faqs.md>)。

## 开发步骤

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建查询请求。

   ```
   1. // 查询跑步记录
   2. const sequenceReadRequest:
   3. healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
   4. startTime: 1698040800000,
   5. endTime: 1698042600000,
   6. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
   7. count: 1,
   8. sortOrder: 1,
   9. readOptions: {
   10. withPartialDetails: ['exerciseHeartRate', 'altitude']
   11. }
   12. };
   ```
3. 调用[readData](<../../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstorereaddata-1>)方法执行查询请求，并处理返回结果。

   ```
   1. try {
   2. const runningSequences =
   3. await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
   4. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
   5. runningSequences.forEach((runningSequence) => {
   6. hilog.info(0x0000, 'testTag', `the start time is ${runningSequence.startTime}.`);
   7. hilog.info(0x0000, 'testTag', `the end time is ${runningSequence.endTime}.`);
   8. Object.keys(runningSequence.summaries).forEach((key) => {
   9. Object.keys(runningSequence.summaries[key]).forEach((fieldName) => {
   10. hilog.info(0x0000, 'testTag',
   11. `the summaries of ${key} field ${fieldName} is ${runningSequence.summaries[key][fieldName]}.`);
   12. });
   13. });
   14. });
   15. } catch (err) {
   16. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   17. }
   ```
