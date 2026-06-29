---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-invoke-mainthread-interface
title: Worker同步调用宿主线程的接口
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > Worker同步调用宿主线程的接口
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:19+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:bf6ae914739f0c16700502c9b901ba1b9f4a9f2ec8da161df80e613eb8c73549
---
如果一个接口已在宿主线程中实现，Worker可以通过以下方式调用该接口。

以下示例展示了Worker同步调用宿主线程接口的方法，创建Worker的方法可参考[创建Worker的注意事项](../../../多线程并发/Worker简介/worker-introduction.md#创建worker的注意事项)。

1. 首先，在宿主线程实现需要调用的接口，并创建Worker对象，在Worker对象上注册需要调用的对象。

   ```
   1. import { MessageEvents, worker } from '@kit.ArkTS';

   3. class TestObj {
   4. public getMessage(): string {
   5. return 'this is a message from TestObj';
   6. }

   8. public static testObj: TestObj = new TestObj();
   9. }

   11. @Entry
   12. @Component
   13. struct Index {
   14. @State message: string = 'Hello World';

   16. build() {
   17. Row() {
   18. Column() {
   19. Text(this.message)
   20. .fontSize(50)
   21. .fontWeight(FontWeight.Bold)
   22. .onClick(() => {
   23. // 创建Worker对象
   24. const workerInstance: worker.ThreadWorker = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
   25. // 在Worker上注册需要调用的对象
   26. workerInstance.registerGlobalCallObject('testObj', TestObj.testObj);
   27. workerInstance.onmessage = (e: MessageEvents): void => {
   28. // 接收Worker子线程的结果
   29. console.info('mainThread: ' + e.data);
   30. // 销毁Worker
   31. workerInstance.terminate();
   32. }
   33. workerInstance.postMessage('start');
   34. })
   35. }
   36. .width('100%')
   37. }
   38. .height('100%')
   39. }
   40. }
   ```

   [WorkerCallGlobalUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationScenario/entry/src/main/ets/managers/WorkerCallGlobalUsage.ets#L16-L57)
2. 然后，在Worker中通过[callGlobalCallObjectMethod](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.worker (启动一个Worker)/js-apis-worker.md#callglobalcallobjectmethod11>)接口可以调用宿主线程中的getMessage()方法。

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

   3. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   5. workerPort.onmessage = async (e: MessageEvents) => {
   6. if (e.data === 'start') {
   7. try {
   8. // 调用方法
   9. let res: string = workerPort.callGlobalCallObjectMethod('testObj', 'getMessage', 0) as string;
   10. if (res === 'this is a message from TestObj') {
   11. workerPort.postMessage('run function success.');
   12. }
   13. } catch (error) {
   14. // 异常处理
   15. console.error('worker: error code is ' + error.code + ' error message is ' + error.message);
   16. }
   17. }

   19. // ...
   20. }
   ```

   [Worker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationScenario/entry/src/main/ets/workers/Worker.ets#L17-L45)
