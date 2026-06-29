---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-26
title: 如何设置Task优先级
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何设置Task优先级
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9a994f8e3b555c72bdef68a82389e7f6e7a4d35c2505b963a85652a1dee4228d
---
设置任务优先级，示例如下：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function printArgs(args: number): number {
5. console.log("printArgs: " + args);
6. return args;
7. }

9. let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
10. taskpool.execute(task, taskpool.Priority.HIGH).then((res) => {
11. console.log("taskpool result is :" + res);
12. });
```

[SetTaskPriority.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SetTaskPriority.ets#L21-L32)

* HIGH：值为0，表示任务是高优先级。
* MEDIUM：值为1，表示任务是中优先级。
* LOW：值为2，表示任务是低优先级。

**参考链接**

[Priority](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.taskpool (启动任务池)/js-apis-taskpool.md#priority>)
