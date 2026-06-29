---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-communicates-with-mainthread
title: Worker和宿主线程的即时消息通信
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > Worker和宿主线程的即时消息通信
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:17+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:702ec401993579709b10fbad737b42edd2cb67b178c0655a07ecb99f69592aee
---
在ArkTS中，Worker相对于Taskpool存在一定的差异性，有数量限制但是可以长时间存在。一个[Worker](../../../多线程并发/Worker简介/worker-introduction.md)中可能会执行多个不同的任务，每个任务的执行时长或返回结果可能都不同，宿主线程需要根据情况调用Worker中的不同方法，Worker则需要及时地将结果返回给宿主线程。

下面以Worker响应"hello world"请求为例说明。

1. 首先，创建一个执行任务的Worker。创建方法可参考[创建Worker的注意事项](../../../多线程并发/Worker简介/worker-introduction.md#创建worker的注意事项)。

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

   3. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   5. workerPort.onmessage = async (e: MessageEvents) => {
   6. // ...
   7. if (e.data === 'hello world') {
   8. workerPort.postMessage('success');
   9. }
   10. }
   ```

   [Worker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationScenario/entry/src/main/ets/workers/Worker.ets#L16-L44)
2. 这里的宿主线程是UI主线程，在宿主线程中创建Worker对象，当点击Button时调用postMessage方法向Worker线程发送消息，Worker线程将通过注册的onmessage回调处理宿主线程发送的消息。

   ```
   1. import { worker } from '@kit.ArkTS';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. function promiseCase() {
   5. let p: Promise<void> = new Promise<void>((resolve: Function, reject: Function) => {
   6. setTimeout(() => {
   7. resolve(1);
   8. }, 100)
   9. }).then(undefined, (error: BusinessError) => {
   10. })
   11. return p;
   12. }

   14. async function postMessageTest() {
   15. let ss = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   16. let res = undefined;
   17. let flag = false;
   18. let isTerminate = false;
   19. ss.onexit = () => {
   20. isTerminate = true;
   21. }
   22. // 接收Worker线程发送的消息
   23. ss.onmessage = (e) => {
   24. res = e.data;
   25. flag = true;
   26. console.info('worker:: res is  ' + res);
   27. }
   28. // 给Worker线程发送消息
   29. ss.postMessage('hello world');
   30. while (!flag) {
   31. await promiseCase();
   32. }

   34. ss.terminate();
   35. while (!isTerminate) {
   36. await promiseCase();
   37. }
   38. }

   40. @Entry
   41. @Component
   42. struct Index {
   43. @State message: string = 'Hello World';

   45. build() {
   46. Row() {
   47. Column() {
   48. Text(this.message)
   49. .fontSize(50)
   50. .fontWeight(FontWeight.Bold)
   51. .onClick(() => {
   52. postMessageTest();
   53. this.message = 'success';
   54. })
   55. }
   56. .width('100%')
   57. }
   58. .height('100%')
   59. }
   60. }
   ```

   [WorkerCommunicatesWithMainthread.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationScenario/entry/src/main/ets/managers/WorkerCommunicatesWithMainthread.ets#L16-L77)

在示例代码中，Worker接收宿主线程的消息，并处理后将结果返回给宿主线程。实现了宿主线程与Worker之间的即时通信，使宿主线程能够方便地使用Worker的运行结果。
