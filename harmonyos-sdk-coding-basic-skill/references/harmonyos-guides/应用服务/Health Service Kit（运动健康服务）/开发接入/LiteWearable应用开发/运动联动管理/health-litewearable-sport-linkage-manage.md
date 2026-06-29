---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-sport-linkage-manage
title: 运动联动管理
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > LiteWearable应用开发 > 运动联动管理
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:27+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:0d5216932120e1a5045f6c607ad1f8a2211d06f35422eaca5a5a955509b96e89
---
## 场景介绍

运动联动管理，包含运动联动的配置、开启、暂停、恢复、停止，数据订阅、解订阅、下发，锻炼记录的读写。

## 约束与限制

从6.1.1(24) 版本开始，Lite Wearable设备新增支持health Service Kit特性。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [config](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutconfig>)(workoutConfig: WorkoutConfig): void | 运动联动配置。 |
| [start](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutstart>)(): StartResult | 开启运动联动。 |
| [pause](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutpause>)(): void | 暂停运动联动。 |
| [resume](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutresume>)(): void | 恢复运动联动。 |
| [stop](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutstop>)(): void | 停止运动联动。 |
| [onData](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutondata>)(dataType: undefined, listener: Callback<[SampleReal](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#samplereal>)[]>): void | 订阅数据。 |
| [offData](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutoffdata>)(dataType: undefined, listener?: Callback<[SampleReal](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#samplereal>)[]>): void | 解订阅数据。 |
| [sendData](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#workoutsenddata>)(sampleReal: [SampleReal](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthService (运动健康联动服务)(Lite)/health-api-healthservice-lite.md#samplereal>)[]): void | 下发融合数据。 |
| [readData](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#healthstorereaddata>)<T extends ExerciseSequence>(request: exercisesequencereadrequest, callback: Callback<T[]>): void | 查询最新一条锻炼记录。 |
| [saveData](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)(Lite)/health-api-healthstore-lite.md#healthstoresavedata>)(exerciseSequence: ExerciseSequence): void | 保存锻炼记录。 |

## 开发前检查

* 完成[申请运动健康服务](../../开发准备/申请运动健康服务/health-apply.md)。
* 需先通过[用户授权](../管理用户授权/health-litewearable-add-permissions.md)接口引导用户授权，用户授权应根据[权限说明](../../数据类型/权限说明/health-permission-description.md#lite-wearable)中要求来打开锻炼记录读/写和联动接口控制权限，。
* 常见问题请参考[Health Service Kit常见问题](<../../../Health Service Kit常见问题/health-faqs.md>)。

## 开发步骤

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import healthService from '@hms.health.service';
   2. import healthStore from '@hms.health.store';
   ```
2. 配置联动。

   ```
   1. function config() {
   2. let workoutOptions = {
   3. linkageType: healthService.workout.LinkageType.ACTIVITY_LINK,
   4. sportType: healthStore.exerciseSequenceHelper.badminton.EXERCISE_TYPE.id,
   5. activityGoals: [
   6. {
   7. type: healthService.workout.TargetType.CALORIE,
   8. value: 100
   9. }
   10. ]
   11. };
   12. try {
   13. healthService.workout.config(workoutOptions);
   14. } catch (err) {
   15. // 异常场景处理
   16. }
   17. }
   ```
3. 开启联动。

   ```
   1. function start() {
   2. try {
   3. let startResult = healthService.workout.start();
   4. } catch (err) {
   5. // 异常场景处理
   6. }
   7. }
   ```
4. 暂停/恢复联动。

   ```
   1. function pause() { // 暂停联动
   2. try {
   3. healthService.workout.pause();
   4. } catch (err) {
   5. // 异常场景处理
   6. }
   7. }

   9. function resume() { // 恢复联动
   10. try {
   11. healthService.workout.resume();
   12. } catch (err) {
   13. // 异常场景处理
   14. }
   15. }
   ```
5. 订阅数据，可以实时获取运动数据，并对获取的运动数据进行处理。

   ```
   1. function onData() {
   2. const callback = (sampleReals) => {
   3. // 运动数据回调处理流程
   4. };

   6. try {
   7. healthService.workout.onData(undefined, callback);
   8. } catch (e) {
   9. if (e.code === 1009104001) { // 联动已开启其他应用已调用start开启联动
   10. // 回到准备界面
   11. } else if (e.code === 1009104003) { // 在当前状态下，指令非法。请先开启运动联动
   12. // 回到准备界面
   13. }
   14. }
   15. }
   ```
6. 解订阅数据（根据需求调整调用时机）。

   ```
   1. function offData() {
   2. const callback = (sampleReals) => {
   3. // 运动数据回调处理流程
   4. };

   6. try {
   7. healthService.workout.offData(undefined, callback);
   8. } catch (e) {
   9. // 异常场景处理
   10. }
   11. }
   ```
7. 保存锻炼记录。

   ```
   1. function saveData() {
   2. let healthSequence = {
   3. dataType: healthStore.healthDataTypes.WORKOUT_REALTIME,
   4. // insertDataSource插入数据源接口返回的DataSourceId
   5. dataSourceId: 'xxx',
   6. localDate: '09/26/2023',
   7. startTime: 1695740400000,  // 2023-10-23 14:00:00
   8. endTime: 1695769200000,   // 2023-10-23 14:30:00
   9. timeZone: '+0800',
   10. modifiedTime: 1695769200000,
   11. exerciseType: healthStore.exerciseSequenceHelper.badminton.EXERCISE_TYPE,
   12. duration: 1800000,
   13. summaries: {
   14. avgShotSpeed: 25.5,
   15. maxShotSpeed: 32.8,
   16. shots: 125,
   17. maxContinuousRally: 7,
   18. forehandStroke: 45,
   19. backhandStroke: 32,
   20. overhandStroke: 18,
   21. underhandStroke: 10,
   22. smash: 23,
   23. highClear: 15
   24. }
   25. }

   27. try {
   28. healthStore.saveData(healthSequence);
   29. } catch (err) {
   30. // 异常处理流程
   31. }
   32. }
   ```
8. 读取锻炼记录。

   ```
   1. function readData() {
   2. const startTime = 1698040800000; // 2023-10-23 14:00:00
   3. const endTime = 1698042600000; // 2023-10-23 14:30:00

   5. const sequenceReadRequest = {
   6. startTime: startTime,
   7. endTime: endTime,
   8. exerciseType: healthStore.exerciseSequenceHelper.badminton.EXERCISE_TYPE,
   9. count: 1,
   10. sortOrder: healthStore.SortOrder.DESC,
   11. readOptions: {
   12. withPartialDetails: ['exerciseHeartRate']
   13. }
   14. };

   16. const callback = (samplePoints) => {
   17. // 锻炼记录数据回调处理流程
   18. };

   20. try {
   21. healthStore.readData(sequenceReadRequest, callback);
   22. } catch (err) {
   23. // 异常处理流程
   24. }
   25. }
   ```
9. 停止联动。

   ```
   1. function stop() {
   2. try {
   3. healthService.workout.stop();
   4. } catch (err) {
   5. // 异常场景处理
   6. }
   7. }
   ```
