---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-58
title: 如何在编译过程中添加自定义任务
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在编译过程中添加自定义任务
category: harmonyos-faqs
scraped_at: 2026-06-01T17:06:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0cf34c955ddf1df0576b3a1730d8b1fe3e1ebbec9f7540fbb129da88cfbb1f79
---
1. 打开模块级的hvigorfile.ts文件。
2. 使用 pluginContext的registerTask方法注册自定义任务，开发者在run方法内编写自定义任务。

   ```
   1. import { hapTasks } from '@ohos/hvigor-ohos-plugin';
   2. import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

   5. const node = getNode(__filename);
   6. node.registerTask({
   7. name: 'customTask',
   8. run() {
   9. console.log('this is Task');
   10. }});
   ```

   [hvigorfile.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/hvigorfile.ts#L3-L12)
3. 在终端中输入以下代码执行任务。

   ```
   1. ./hvigorw customTask
   ```

**参考链接**

[开发hvigor任务](../../../../harmonyos-guides/构建应用/扩展构建能力/开发Hvigor任务/ide-hvigor-task.md)
