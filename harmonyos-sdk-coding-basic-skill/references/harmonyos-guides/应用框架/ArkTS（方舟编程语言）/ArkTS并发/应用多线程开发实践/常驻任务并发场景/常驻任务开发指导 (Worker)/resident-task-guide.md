---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resident-task-guide
title: 常驻任务开发指导 (Worker)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 常驻任务并发场景 > 常驻任务开发指导 (Worker)
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:27+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:18049ba43f19110ff8cbcf41342f86f19de236103cb3ca66c14b7aabb8db5ac0
---
提供使用Worker进行常驻任务的开发指导。Worker将持续执行任务，直到宿主线程发送终止指令。

开发过程和示例如下：

1. DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，单击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建“Worker”为例。

   此外，还支持手动创建Worker文件。具体方式和注意事项请参见[创建Worker的注意事项](../../../多线程并发/Worker简介/worker-introduction.md#创建worker的注意事项)。
2. 首先导入Worker模块，然后在宿主线程中通过调用ThreadWorker的[constructor()](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.worker (启动一个Worker)/js-apis-worker.md#constructor9>)方法创建Worker对象，创建Worker对象的线程为宿主线程。 此处的宿主线程为UI主线程，宿主线程发送'start'以开始执行某个长期运行的任务，并接收子线程返回的相关消息。当不需要执行该任务时，发送'stop'以停止该任务的执行。在此示例中，任务将在10秒后结束。

   ```
   1. import { MessageEvents, worker } from '@kit.ArkTS';

   3. @Entry
   4. @Component
   5. struct Index {
   6. build() {
   7. Column() {
   8. Text('Listener task')
   9. .id('HelloWorld')
   10. .fontSize(50)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   14. workerInstance.onmessage = (event: MessageEvents) => {
   15. console.info('UI主线程收到消息：', event.data);
   16. }
   17. workerInstance.postMessage({type: 'start'})
   18. // 10秒后停止worker
   19. setTimeout(() => {
   20. workerInstance.postMessage({ type: 'stop' });
   21. }, 10000);
   22. })
   23. }
   24. .height('100%')
   25. .width('100%')
   26. }
   27. }
   ```

   [ResidentTaskGuide.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/ApplicationMultithreading/entry/src/main/ets/managers/ResidentTaskGuide.ets#L16-L49)
3. 在Worker线程中，当接收到宿主线程发送的消息为'start'时，开始执行某个长时间不定期运行的任务，并实时向宿主线程返回消息。当接收到的消息为'stop'时，结束该任务的执行并返回相应的消息给宿主线程。

   ```
   1. import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

   3. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   4. let isRunning = false;
   5. workerPort.onmessage = (e: MessageEvents) => {
   6. const type = e.data.type as string;
   7. if (type === 'start') {
   8. if (!isRunning) {
   9. isRunning = true;
   10. // 开始常驻任务
   11. performTask();
   12. }
   13. } else if (type === 'stop') {
   14. isRunning = false;
   15. }
   16. }

   18. // 模拟常驻任务
   19. function performTask() {
   20. if (isRunning) {
   21. // 模拟某个长期运行的任务
   22. workerPort.postMessage('Worker is performing a task');
   23. // 1秒后再次执行任务
   24. setTimeout(performTask, 1000);
   25. } else {
   26. workerPort.postMessage('Worker has stopped performing the task');
   27. workerPort.close();
   28. }
   29. }
   ```

   [Worker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/ApplicationMultithreading/entry/src/main/ets/workers/Worker.ets#L16-L43)
