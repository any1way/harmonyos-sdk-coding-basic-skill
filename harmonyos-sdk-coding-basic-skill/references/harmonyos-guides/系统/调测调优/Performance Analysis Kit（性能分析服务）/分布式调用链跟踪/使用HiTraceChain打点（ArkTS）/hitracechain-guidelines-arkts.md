---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-guidelines-arkts
title: 使用HiTraceChain打点（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 分布式调用链跟踪 > 使用HiTraceChain打点（ArkTS）
category: harmonyos-guides
scraped_at: 2026-06-11T14:52:41+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:ad8046578a545d0603a590fc92d0f3bb4eda31ab71dd381881e0cd9a3427f127
---
## 接口说明

分布式跟踪接口由HiTraceChain模块提供，详细API请参考[@ohos.hiTraceChain (分布式跟踪)](<../../../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiTraceChain (分布式跟踪)/js-apis-hitracechain.md>)。

| 接口名 | 描述 |
| --- | --- |
| hiTraceChain.begin(name: string, flags?: number = HiTraceFlag.DEFAULT): HiTraceId | 开始跟踪，并返回创建的HiTraceId。 |
| hiTraceChain.end(id: HiTraceId): void | 结束跟踪。 |
| hiTraceChain.getId(): HiTraceId | 获取跟踪标识。 |
| hiTraceChain.setId(id: HiTraceId): void | 设置跟踪标识。 |
| hiTraceChain.clearId(): void | 清除跟踪标识。 |
| hiTraceChain.createSpan(): HiTraceId | 创建跟踪分支。创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。 |
| hiTraceChain.isValid(id: HiTraceId): boolean | 判断HiTraceId是否有效。  true：HiTraceId有效；false：HiTraceId无效。 |
| hiTraceChain.isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean | 判断HiTraceId中指定的跟踪标志是否已启用。  true：指定的跟踪标志已启用；false：指定的跟踪标志未启用。 |
| hiTraceChain.enableFlag(id: HiTraceId, flag: HiTraceFlag): void | 启用HiTraceId中指定的跟踪标志。 |
| hiTraceChain.tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void | HiTraceMeter跟踪信息埋点。 |

## 开发步骤

HiTraceChain在ArkTS中的使用方法参考以下示例，开发者可参考[约束与限制](../HiTraceChain介绍/hitracechain-intro.md#约束与限制)，了解常见的支持与不支持HiTraceChain自动传递的机制。

1. 在DevEco Studio中新建工程，选择“Empty Ability”，工程的目录结构如下：

   ```
   1. ├── entry
   2. │   ├── src
   3. │       ├── main
   4. │       │   ├── ets
   5. │       │   │   ├── entryability
   6. │       │   │   │   └── EntryAbility.ets
   7. │       │   │   └── pages
   8. │       │   │       └── Index.ets
   ```
2. 编辑工程中的“entry > src > main > ets > pages > Index.ets”：

   导入所需依赖：

   ```
   1. import { hiTraceChain, hilog } from '@kit.PerformanceAnalysisKit';
   ```

   定义测试方法：

   ```
   1. function initTraceId() {
   2. let traceId = hiTraceChain.getId();
   3. if (!hiTraceChain.isValid(traceId)) {
   4. hilog.info(0x0000, 'testTag', 'HiTraceId is invalid, begin hiTraceChain');
   5. traceId = hiTraceChain.begin('testTag: hiTraceChain begin', hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
   6. } else if (!hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC)) {
   7. hiTraceChain.enableFlag(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
   8. hiTraceChain.setId(traceId);
   9. }
   10. return traceId;
   11. }

   13. async function test(index: number) {
   14. if (index > 0) {
   15. await test(index - 1)
   16. hilog.info(0x0000, 'testTag', `record with traceId at task ${index}`);
   17. }
   18. }

   20. function testHiTraceIdPassedAutomatically() {
   21. let traceId = initTraceId();
   22. hilog.info(0x0000, 'testTag', 'record with traceId at first task');
   23. test(10).then(()=>{
   24. hilog.info(0x0000, 'testTag', 'record with traceId at then function');
   25. })
   26. hiTraceChain.end(traceId);
   27. hilog.info(0x0000, 'testTag', 'hiTraceChain end in main thread');
   28. }

   30. function testHiTraceIdPassedManually() {
   31. let traceId = initTraceId();
   32. hilog.info(0x0000, 'testTag', 'start testHiTraceIdPassedManually async trace');
   33. setTimeout(() => {
   34. // 为异步定时任务设置HiTraceId
   35. hiTraceChain.setId(traceId);
   36. // 为异步定时任务生成分支标识spanId
   37. let traceIdTimeout = hiTraceChain.createSpan();
   38. // 为异步定时任务设置带spanId的HiTraceId
   39. hiTraceChain.setId(traceIdTimeout);
   40. hilog.info(0x0000, 'testTag', 'end testHiTraceIdPassedManually async trace');
   41. }, 100);
   42. hiTraceChain.end(traceId);
   43. hilog.info(0x0000, 'testTag', 'hiTraceChain end in main thread');
   44. }
   ```

   添加按钮以触发接口调用：

   ```
   1. Button("testHiTraceIdPassedAutomatically").backgroundColor('#FFFF00FF')
   2. .onClick(testHiTraceIdPassedAutomatically)

   4. Button("testHiTraceIdPassedManually").backgroundColor('#FFFF00FF')
   5. .onClick(testHiTraceIdPassedManually)
   ```
3. 点击DevEco Studio界面中的运行按钮，运行应用工程，并在hilog日志中过滤“testTag”：

   * HiTraceId支持自动传递场景：

     点击设备上“testHiTraceIdPassedAutomatically”触发业务逻辑可在hilog中看到以下内容：

     ```
     1. 05-28 11:47:20.499   7439-7439     A00000/testTag                  com.examp...racedemo  I     HiTraceId is invalid, begin hiTraceChain
     2. 05-28 11:47:20.500   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 32a835e, 0] record with traceId at first task
     3. 05-28 11:47:20.509   7439-7439     A00000/testTag                  com.examp...racedemo  I     hiTraceChain end in main thread
     4. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 23e9386, 32a835e] record with traceId at task 1
     5. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 38a1eb2, 23e9386] record with traceId at task 2
     6. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 363113e, 38a1eb2] record with traceId at task 3
     7. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 3919396, 363113e] record with traceId at task 4
     8. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 2f5f6d7, 3919396] record with traceId at task 5
     9. 05-28 11:47:20.511   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 3220957, 2f5f6d7] record with traceId at task 6
     10. 05-28 11:47:20.512   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, f3a42b, 3220957] record with traceId at task 7
     11. 05-28 11:47:20.512   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, b293a8, f3a42b] record with traceId at task 8
     12. 05-28 11:47:20.512   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 2090dea, b293a8] record with traceId at task 9
     13. 05-28 11:47:20.512   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 1b63a3e, 1b63a3e] record with traceId at task 10
     14. 05-28 11:47:20.513   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab104a53adf0, 2df6e91, 2df6e91] record with traceId at then function
     ```

     + hilog日志前附加的[chainId spanId parentSpanId]格式的信息即为HiTraceId信息，例如[a92ab104a53adf0 23e9386 32a835e]表示跟踪链标识chainId值为a92ab104a53adf0，分支标识spanId值为23e9386，父分支标识parentSpanId值为32a835e。
     + 示例得到的跟踪链标识chainId值为a92ab104a53adf0，可使用chainId值过滤日志，查看业务完整的调用链hilog日志。
     + promise/then和async/await异步机制都会自动传递HiTraceId，并生成分支标识，例如示例hilog日志中的32a835e、23e9386、38a1eb2等，均为异步任务自动生成的分支标识，且通过parentSpanId信息可以推断该分支标识的生成链路。
     + hiTraceChain.end()和hiTraceChain.clear()都可以结束跟踪，跟踪结束后，hilog日志不再携带HiTraceId信息，例如日志“hiTraceChain end in main thread”不再携带HiTraceId信息。
   * HiTraceId未支持自动传递场景：

     点击设备上“testHiTraceIdPassedManually”按钮触发业务逻辑，可在hilog日志中看到以下内容：

     ```
     1. 05-28 11:49:00.787   7439-7439     A00000/testTag                  com.examp...racedemo  I     HiTraceId is invalid, begin hiTraceChain
     2. 05-28 11:49:00.788   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab4bb2cc0575, 0, 0] start testHiTraceIdPassedManually async trace
     3. 05-28 11:49:00.789   7439-7439     A00000/testTag                  com.examp...racedemo  I     hiTraceChain end in main thread
     4. 05-28 11:49:00.890   7439-7439     A00000/testTag                  com.examp...racedemo  I     [a92ab4bb2cc0575, 3b5f934, 0] end testHiTraceIdPassedManually async trace
     ```
