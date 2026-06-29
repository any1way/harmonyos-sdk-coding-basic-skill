---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-104
title: 如何在构建任务中执行shell脚本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在构建任务中执行shell脚本
category: harmonyos-faqs
scraped_at: 2026-06-01T17:06:57+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:ecbe9dd62a962d44f9be355ff3ba6f3c1d5a81091e4be85a425b540e3e5759b5
---

在hvigorfile.ts文件中执行如下示例：

```
1. import { harTasks } from '@ohos/hvigor-ohos-plugin';
2. import { exec } from 'node:child_process';
3. import util from 'node:util';

5. const scriptPath = 'xxxx.bat';

7. export function customPluginFunction1(str?: string) {
8. return {
9. pluginId: 'CustomPluginID1',
10. apply(pluginContext) {
11. pluginContext.registerTask({
12. // Write a custom task
13. name: 'customTask1',
14. run: (taskContext) => {
15. console.log('run into: ');
16. const execPromise = util.promisify(exec)
17. execPromise(scriptPath).then(res => {
18. console.log(res, 'res');
19. }).catch(err => {
20. console.log(err, 'err');
21. })
22. },
23. // Confirm custom task insertion position
24. dependencies: ['default@BuildJS'],
25. postDependencies: ['default@CompileArkTS']
26. })
27. }
28. }
29. }

31. export default {
32. system: harTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
33. plugins: [customPluginFunction1()] /* Custom plugin to extend the functionality of Hvigor. */
34. }
```

[hvigorfile.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library3/hvigorfile.ts#L3-L36)

说明

需要特别注意system字段的取值，不同的模块需要使用不同的值：

1. 在项目的hvigorfile.ts中，需要使用system: appTasks。
2. 在har模块的hvigorfile.ts中，需要使用system: harTasks。
3. 在hsp模块的hvigorfile.ts中，需要使用system: hspTasks。
4. 在hap模块的hvigorfile.ts中，需要使用system: hapTasks。
