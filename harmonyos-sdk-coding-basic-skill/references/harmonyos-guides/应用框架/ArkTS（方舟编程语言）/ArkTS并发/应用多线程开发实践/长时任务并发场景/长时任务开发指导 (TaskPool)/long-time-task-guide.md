---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-guide
title: 长时任务开发指导 (TaskPool)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 长时任务并发场景 > 长时任务开发指导 (TaskPool)
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:24+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:fbc45f53e769b49daba5c6c4894e7890950522fd8b37049ef87beda4f35a7e28
---

此处提供使用TaskPool进行长时任务的开发指导，以定期采集传感器数据为例。

## 使用TaskPool进行传感器数据监听

1. 导入所需的模块。

   ```
   1. import { sensor } from '@kit.SensorServiceKit';
   2. import { taskpool } from '@kit.ArkTS';
   3. import { BusinessError, emitter } from '@kit.BasicServicesKit';
   ```

   [LongTimeTaskGuide.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/ApplicationMultithreading/entry/src/main/ets/managers/LongTimeTaskGuide.ets#L17-L21)
2. 定义长时任务，内部监听sensor数据，并通过emitter注册销毁通知。

   ```
   1. @Concurrent
   2. async function sensorListener(): Promise<void> {
   3. sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
   4. emitter.emit({ eventId: 0 }, { data: data });
   5. }, { interval: 1000000000 });

   7. emitter.on({ eventId: 1 }, () => {
   8. sensor.off(sensor.SensorId.ACCELEROMETER)
   9. emitter.off(1)
   10. })
   11. }
   ```

   [LongTimeTaskGuide.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/ApplicationMultithreading/entry/src/main/ets/managers/LongTimeTaskGuide.ets#L23-L35)
3. 给sensor添加ohos.permission.ACCELEROMETER权限。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.ACCELEROMETER"
   4. }
   5. ]
   ```
4. 宿主线程定义注册及销毁的行为。

   * 注册：发起长时任务，并通过emitter接收监听数据。
   * 销毁：发送取消传感器监听的事件，并结束长时任务。

   ```
   1. import { sensor } from '@kit.SensorServiceKit';
   2. import { taskpool } from '@kit.ArkTS';
   3. import { BusinessError, emitter } from '@kit.BasicServicesKit';

   5. @Concurrent
   6. async function sensorListener(): Promise<void> {
   7. sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
   8. emitter.emit({ eventId: 0 }, { data: data });
   9. }, { interval: 1000000000 });

   11. emitter.on({ eventId: 1 }, () => {
   12. sensor.off(sensor.SensorId.ACCELEROMETER)
   13. emitter.off(1)
   14. })
   15. }

   17. @Entry
   18. @Component
   19. struct Index {
   20. sensorTask?: taskpool.LongTask
   21. @State addListener: string = 'Add listener';
   22. @State deleteListener: string = 'Delete listener';

   24. build() {
   25. Column() {
   26. Text(this.addListener)
   27. .id('Add listener')
   28. .fontSize(50)
   29. .fontWeight(FontWeight.Bold)
   30. .onClick(() => {
   31. this.sensorTask = new taskpool.LongTask(sensorListener);
   32. emitter.on({ eventId: 0 }, (data) => {
   33. // Do something here
   34. console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}`);
   35. });
   36. taskpool.execute(this.sensorTask).then(() => {
   37. console.info('Add listener of ACCELEROMETER success');
   38. }).catch((e: BusinessError) => {
   39. // Process error
   40. })
   41. this.addListener = 'success';
   42. })
   43. Text(this.deleteListener)
   44. .id('Delete listener')
   45. .fontSize(50)
   46. .fontWeight(FontWeight.Bold)
   47. .onClick(() => {
   48. emitter.emit({ eventId: 1 });
   49. emitter.off(0);
   50. if (this.sensorTask != undefined) {
   51. taskpool.terminateTask(this.sensorTask);
   52. } else {
   53. console.error('sensorTask is undefined.');
   54. }
   55. this.deleteListener = 'success';
   56. })
   57. }
   58. .height('100%')
   59. .width('100%')
   60. }
   61. }
   ```

   [LongTimeTaskGuide.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/ApplicationMultithreading/entry/src/main/ets/managers/LongTimeTaskGuide.ets#L16-L82)
