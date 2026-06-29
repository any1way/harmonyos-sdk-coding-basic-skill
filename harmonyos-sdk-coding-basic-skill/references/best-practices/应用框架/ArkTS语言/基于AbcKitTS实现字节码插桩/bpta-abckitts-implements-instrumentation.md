---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-abckitts-implements-instrumentation
title: 基于AbcKitTS实现字节码插桩
breadcrumb: 最佳实践 > 应用框架 > ArkTS语言 > 基于AbcKitTS实现字节码插桩
category: best-practices
scraped_at: 2026-06-11T16:57:08+08:00
doc_updated_at: 2026-05-11
content_hash: sha256:b586ac72e6d69f83a9255672fa2bfdf0e14a62555115415cab78b22abb0cb6d2
---
## 概述

AbcKitTS是一款专为方舟字节码设计的TypeScript字节码分析与修改工具库。它提供了简洁而强大的字节码操作API，让开发者能够精确定位目标方法、拦截API调用、注入回调逻辑，并支持灵活的字节码指令创建与修改，从而实现高效的切面编程。本文将从实际业务场景出发，深入剖析AbcKitTS在切面编程中的高频应用模式，分享最佳实践与实现技巧。

同时，针对轻量化的业务需求，可以参考基于装饰器配置的[基于Aspect插件库实现切面编程](../基于Aspect插件库实现切面编程/bpta-aspect-implements-aop.md)——它完全封装了底层的字节码技术，让开发者以声明式的方式快速实现切面功能，真正做到"零侵入"式开发。

## 实现原理

在深入实践之前，建议先通过官方文档了解[方舟字节码](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS编译工具链/方舟字节码/arkts-bytecode.md)的基本原理，并掌握[Disassembler反汇编工具](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS编译工具链/Disassembler反汇编工具/tool-disassembler.md)的基础技能，这将有助于更好地理解后续内容。

### 底层架构

AbcKitTS是基于C++版[libabckit](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit)方舟字节码工具库的TypeScript封装，旨在提升开发者的字节码插桩效率。通过提供易用的API接口，它将底层复杂的字节码操作抽象为简洁的开发体验。

### 核心设计：扁平化的元数据模型

AbcKitTS通过AbcManager统一管理字节码文件，并提供链式查询API供开发者快速定位目标方法。其元数据模型在设计上独具匠心：底层虽然遵循源程序的"树形结构"，但对外提供了扁平化的查询视图，极大地简化了数据检索过程。

说明

AbcManager是字节码操作统一管理器，其核心功能包括加载、查询和修改字节码。

以namespace a { namespace b { ... } }的嵌套结构为例，在AbcModule的AbcNamespace[]列表中会保存为两条独立的命名空间数据，开发者无需进行嵌套遍历即可直接访问。

元数据结构详解：

| 节点类型 | 对应关系 | 设计特点 |
| --- | --- | --- |
| AbcModule | ets/ts源文件 | 包含文件内所有命名空间、类、顶层函数（包括匿名回调函数）；  持有特殊的func\_main\_0入口函数，记录文件顶层的语句执行及声明。 |
| AbcNamespace | 命名空间 | 采用扁平化设计，仅持有该命名空间内的顶层函数，其内部的类统一由AbcModule持有。 |
| AbcClass | 类定义 | 持有类方法，但不包含方法内部定义的匿名回调函数，后者被保存在AbcModule中。 |
| AbcFunction | 函数/方法 | 可遍历Block块，也可直接遍历指令。底层解析时，实际是从外层Block到内层Instruction的顺序逐层解析。 |
| Block | 代码块 | 函数体由多个Block构成（至少3个：startBlock、endBlock及startBlock的后继块）；  支持代码分支语句（如if-else、try-catch）构建，常用于入参校验、返回值校验、异常捕捉等代码结构改造场景。 |
| Instruction | 指令序列 | 字节码的基本执行单元，绝大多数插桩功能通过创建或修改指令完成。 |

### 指令操作：IsaKit的设计要点

IsaKit是AbcKitTS提供的核心指令操作工具，用于操作方法的Block及Instruction。

注意

使用时需要特别注意：

* 作用域限定：IsaKit必须通过AbcFunction实例获取，不同方法拥有独立的IsaKit实例。
* 避免混淆：在回调函数分析等场景中，切勿跨方法混用IsaKit，否则可能导致指令操作错乱。

本文主要内容如下：

* [开发流程](bpta-abckitts-implements-instrumentation.md#section1179862361313)：介绍所有场景通用的开发流程。
* [场景示例](bpta-abckitts-implements-instrumentation.md#section21172491410)：通过实际开发中的场景，介绍基于AbcKitTS的基本使用方法。
  + 生命周期函数打点
  + 函数耗时统计
  + 隐私API监控
  + 方法调用点替换
  + 关键属性修改
  + 事件监听埋点
  + 方法入参校验
* [示例代码](bpta-abckitts-implements-instrumentation.md#section129251397148)：本文引用的工程代码。

## 开发流程

开发者要使用AbckitTS对HarmonyOS工程进行插桩，需要完成两个步骤：**编写插桩代码**和**注册插件**。其中，插桩代码的编写会根据具体业务逻辑而有所不同，本文将在[场景示例](bpta-abckitts-implements-instrumentation.md#section21172491410)中根据不同业务场景详细介绍实现方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/cME7t7HAR_OJi399BpN0xQ/zh-cn_image_0000002568136792.png?HW-CC-KV=V1&HW-CC-Date=20260611T085706Z&HW-CC-Expire=86400&HW-CC-Sign=2AE5892721E744779186EAB5351548BB2D1CC3649920742BBA9F9A9A5E5587E9 "点击放大")

### 编写插桩代码

编写TypeScript插桩代码时，可以在项目根目录下新建TS子工程，用于开发插桩逻辑代码。

```
1. .
2. ├──entry/src/main/ets                 // entry module
3. ├──abckitTask                         // abckitTask directory
4. │  └──src
5. │  │  ├──task
6. │  │  │  └──CallReplaceTask.ts        // instrumentation code
7. │  │  └──index.ts                     // instrumentation Entry Point
8. │  └──package.json                    // Node.js configuration
9. │  └──tsconfig.json                   // TypeScript project connfiguration
10. ├──hvigorfile.ts                      // registering a Plug-in
11. ├──...
12. └──README.md
```

1. 初始化插桩任务工程，配置package.json。

   ```
   1. {
   2. "name": "abckit-ts-task",
   3. "version": "1.0.0",
   4. "description": "",
   5. "main": "index.js",
   6. "scripts": {
   7. "test": "echo \"Error: no test specified\" && exit 1"
   8. },
   9. "author": "",
   10. "license": "ISC",
   11. "devDependencies": {
   12. "@types/node": "^25.5.0",
   13. "typescript": "^5.9.3"
   14. },
   15. "dependencies": {
   16. "@hadss/abckit-ts": "1.0.0-rc.0"
   17. }
   18. }
   ```

   配置tsconfig.json。

   ```
   1. {
   2. "compilerOptions": {
   3. "target": "ES6",
   4. "moduleResolution": "node",
   5. "module": "commonjs",
   6. "esModuleInterop": true,
   7. "allowSyntheticDefaultImports": true,
   8. "outDir": "./dist",
   9. "rootDir": "./src",
   10. "strict": true
   11. },
   12. "include": [
   13. "src/**/*"
   14. ],
   15. "exclude": [
   16. "node_modules"
   17. ]
   18. }
   ```

   安装依赖：

   ```
   1. npm install
   ```
2. 编写插桩任务。
3. 编写入口脚本。

   这里推荐使用worker\_threads子线程方式执行插桩任务，可以避免DevEco Studio、Hvigor、Native跨环境调用可能产生的内存访问异常的问题。

   ```
   1. import { CallReplaceTask } from './task/CallReplaceTask';
   2. import { DurationTask } from './task/DurationTask';
   3. import { EventCbTask } from './task/EventCbTask';
   4. import { KeyAttributeModifyTask } from './task/KeyAttributeModifyTask';
   5. import { LifeCycleTask } from './task/LifeCycleTask';
   6. import { MethodParameterValidateTask } from './task/MethodParameterValidateTask';
   7. import { PrivacyApiScanTask } from './task/PrivacyApiScanTask';
   8. import { AbcManager } from '@hadss/abckit-ts';

   10. const fs = require('fs');
   11. const abcPath = process.argv[2]
   12. const outPath = `${abcPath}.bak`

   14. export function runTest(abcPath: string, outPath: string): void {
   15. const abcManger = new AbcManager(abcPath);
   16. new DurationTask(abcManger).run();
   17. new EventCbTask(abcManger).run();
   18. new CallReplaceTask(abcManger).run();
   19. new KeyAttributeModifyTask(abcManger).run();
   20. new LifeCycleTask(abcManger).run();
   21. new MethodParameterValidateTask(abcManger).run();
   22. new PrivacyApiScanTask(abcManger).run();
   23. abcManger.writeAbc(outPath);
   24. fs.renameSync(outPath, abcPath);
   25. }

   27. try {
   28. runTest(abcPath, outPath);

   30. process.exit(0)
   31. } catch (err) {
   32. console.error('error: ', err instanceof Error ? err.message : err)
   33. process.exit(1)
   34. }
   ```

   [index.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/index.ts#L16-L49)
4. 编译构建abckitTask工程。

   ```
   1. cd abckitTask && npx tsc
   ```

   至此，Hvigor Plugin准备好了插桩任务调用入口dist/index.js。

### 注册插件

AbcKitTS插桩接口基于Hvigor插件开发，具体流程可参考[《开发Hvigor插件》](../../../../harmonyos-guides/构建应用/扩展构建能力/开发Hvigor插件/ide-hvigor-plugin.md)文档。

本最佳实践基于hvigorfile脚本开发，在hvigorfile.ts中定义aspectPlugin()函数。

```
1. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
2. import { appTasks, OhosPluginId, OhosHapContext, OhosHspContext, OhosHarContext } from '@ohos/hvigor-ohos-plugin';

4. const { spawnSync } = require('child_process');

6. type OhosContext = OhosHapContext | OhosHspContext | OhosHarContext;

8. export default {
9. system: appTasks,
10. plugins: [
11. aspectPlugin(),
12. ],
13. };

15. function aspectPlugin(): HvigorPlugin {
16. return {
17. pluginId: 'aspectPlugin',
18. apply(node: HvigorNode) : void {
19. hvigor.nodesEvaluated(async () => {
20. const hotReload = hvigor.getParameter().getExtParam('hotReload');
21. if (hotReload) {
22. return;
23. }
24. node.subNodes(subNode => {
25. const context = (
26. subNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) ??
27. subNode.getContext(OhosPluginId.OHOS_HSP_PLUGIN) ??
28. subNode.getContext(OhosPluginId.OHOS_HAR_PLUGIN)
29. ) as OhosContext | undefined;
30. if (!context) {
31. return;
32. }
33. context.transformAbc(async (abcPath: string, config: any) => {
34. console.log("[Final] Abckit Task Start! ");
35. const child = spawnSync('node', ['./abckitTask/dist/index.js', abcPath]);
36. if (child.status !== 3221225477 && child.status !== 0) {
37. throw new Error(child.status);
38. }
39. console.log("[Final] Abckit Task Completed! ABC File generated.");
40. });
41. });
42. });
43. },
44. };
45. }
```

[hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/hvigorfile.ts#L17-L61)

说明

1. AbcKitTS不支持HotReload模式。

2. OHOS\_HAR\_PLUGIN、OHOS\_HSP\_PLUGIN和OHOS\_HAP\_PLUGIN分别对应har、hsp和hap三种包类型。

3. transformAbc API基于Hvigor框架，用于处理abc文件路径。

4. 为避免DevEco Studio、Hvigor和Native环境调用时可能出现的内存访问异常，建议使用worker\_threads子线程执行插桩任务。

## 场景示例

**场景一：生命周期函数打点**

**场景描述：**

在开发过程中，精准定位组件行为往往需要对其生命周期进行监控。通过在关键生命周期函数中打点，开发者可以有效追踪组件行为，从而快速定位问题。

以下示例以组件CompA为例，在aboutToAppear生命周期函数中进行插桩。

ArkTS源码如下所示：

```
1. aboutToAppear(): void {
2. // Insert here: Set message to `Module[path: &entry/src/main/ets/pages/scene/LifeCycle&] - struct[name: ComponentA]
3. // - aboutToAppear is executed.`
4. }
```

[LifeCycle.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/LifeCycle.ets#L74-L77)

**实现步骤：**

1. 初始化AbcManager实例。
2. 定位目标函数。
3. 执行前置插桩操作。
4. 输出abc文件。

   代码如下：

   ```
   1. class Context {
   2. static readonly PROJECT_MODULE: string = 'entry';
   3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/LifeCycle';
   4. static readonly QUERY_CLASS_NAME: string = 'ComponentA';
   5. static readonly QUERY_FUNCTION_NAME: string = 'aboutToAppear';
   6. static readonly ATTRIBUTE_NAME: string = 'message';
   7. static apiCallLog(moduleName: string, className: string): string {
   8. return `Module[path: ${moduleName}] - struct[name: ${className}] - aboutToAppear is executed.`;
   9. }
   10. }

   12. export class LifeCycleTask {
   13. manager: AbcManager;
   14. targetFunc: AbcFunction | null = null;

   16. /**
   17. * step1. init AbcManager
   18. *
   19. * @param manager AbcManager
   20. */
   21. constructor(manager: AbcManager) {
   22. this.manager = manager;
   23. }

   25. run(): void {
   26. this.getTargetFunction();
   27. this.transform();
   28. this.manager.flush();
   29. }

   31. /**
   32. * step2. Position objective function
   33. */
   34. getTargetFunction(): void {
   35. const functions = this.manager.query()
   36. .projectModule(Context.PROJECT_MODULE)
   37. .path(Context.QUERY_PATH)
   38. .className(Context.QUERY_CLASS_NAME)
   39. .functionName(Context.QUERY_FUNCTION_NAME)
   40. .getFunction();
   41. if (functions.length === 0) {
   42. throw new Error('LifeCycle Task function not found');
   43. }
   44. this.targetFunc = functions[0];
   45. }

   47. /**
   48. * step3. Perform pre-instrumentation.
   49. */
   50. transform(): void {
   51. if (!this.targetFunc) {
   52. return;
   53. }
   54. const isaKit = this.targetFunc.getIsaKit();
   55. const instructions: Instruction[] = [];
   56. const params = this.targetFunc.getParameters();
   57. const moduleName = this.targetFunc.getParentModule().getName();
   58. const className = this.targetFunc.getParentClass() == null ? '' : this.targetFunc.getParentClass().getName();
   59. const loadStringInst = isaKit.createLdaString(Context.apiCallLog(moduleName, className));
   60. const stobjbynameInst = isaKit.createStObjByName(loadStringInst, Context.ATTRIBUTE_NAME, params[params.length - 1]);
   61. instructions.push(loadStringInst);
   62. instructions.push(stobjbynameInst);
   63. this.targetFunc.insertBefore(instructions);
   64. this.targetFunc.apply();
   65. }
   66. }
   ```

   [LifeCycleTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/LifeCycleTask.ts#L18-L83)

**场景二：函数耗时统计**

**场景描述：**

开发者可以通过对函数定义点进行环绕插桩，定位源码中的性能问题。

以下示例将对组件CompA中的aboutToAppear方法进行环绕插桩， 统计方法运行耗时。

ArkTS源码如下所示：

```
1. async aboutToAppear(): Promise<void> {
2. // Insert here
3. // Assign startTime with Date.now()
4. await this.pseudoSyncOperation();
5. // Assign endTime with Date.now()
6. // Set message to `durations(ms): ${endTime}-${startTime}`
7. }
```

[FunctionDuration.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/FunctionDuration.ets#L85-L91)

**实现步骤：**

1. 初始化AbcManager实例。
2. 定位目标函数。
3. 执行环绕插桩操作。
4. 输出abc文件。

代码如下：

```
1. class Context {
2. static readonly PROJECT_MODULE: string = 'entry';
3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/FunctionDuration';
4. static readonly QUERY_CLASS_NAME: string = 'CompA';
5. static readonly QUERY_FUNCTION_NAME: string = 'aboutToAppear';
6. static readonly API_IMPORT_NAME: string = 'geoLocationManager';
7. static readonly API_FUNCTION_NAME: string = 'getCurrentLocation';
8. static readonly REPLACE_MESSAGE: string = 'duration(ms): ';
9. static readonly ATTRIBUTE_NAME: string = 'message';
10. static readonly REPLACE_IMPORT_NAME: string = 'Date';
11. static readonly REPLACE_FUNCTION_NAME: string = 'now';
12. }

14. export class DurationTask {
15. manager: AbcManager;
16. targetFunc: AbcFunction | null = null;

18. /**
19. * step1. init AbcManager
20. *
21. * @param manager AbcManager
22. */
23. constructor(manager: AbcManager) {
24. this.manager = manager;
25. }

27. run(): void {
28. this.getTargetFunction();
29. this.doTransform();
30. this.manager.flush();
31. }

33. /**
34. * step3. Perform the wraparound instrumentation operation.
35. */
36. doTransform(): void {
37. const startTimeInst = this.doInsertBefore();
38. this.doInsertAfter(startTimeInst);
39. this.targetFunc?.apply();
40. }

42. doInsertAfter(startTimeInst: Instruction): void {
43. if (!this.targetFunc) {
44. return;
45. }
46. const isaKit = this.targetFunc.getIsaKit();
47. for (const inst of this.targetFunc.getInstructions()) {
48. const isReturn = isaKit.iGetOpcode(inst) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_RETURN ||
49. isaKit.iGetOpcode(inst) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_RETURNUNDEFINED;
50. if (isReturn) {
51. const afterInsts = this.createAfterInsts(startTimeInst, isaKit);
52. isaKit.iInsertBefore(inst, afterInsts);
53. }
54. }
55. }

57. createAfterInsts(startTimeInst: Instruction, isaKit: IsaKit): Instruction[] {
58. const instructions: Instruction[] = [];
59. if (!this.targetFunc) {
60. return instructions;
61. }

63. const endTimeInsts = this.createTimeInstructions();
64. const subInst = isaKit.createSub2(startTimeInst, endTimeInsts[endTimeInsts.length - 1]);

66. const durationStrInst = isaKit.createLdaString(Context.REPLACE_MESSAGE);
67. const addInst = isaKit.createAdd2(subInst, durationStrInst);

69. const params = this.targetFunc.getParameters();
70. const stobjbynameInst = isaKit.createStObjByName(addInst, Context.ATTRIBUTE_NAME, params[params.length - 1]);

72. instructions.push(...endTimeInsts);
73. instructions.push(...[subInst, durationStrInst, addInst, stobjbynameInst]);
74. return instructions;
75. }

77. doInsertBefore(): Instruction {
78. const startTimeInsts = this.createTimeInstructions();
79. this.targetFunc?.insertBefore(startTimeInsts);
80. return startTimeInsts[startTimeInsts.length - 1];
81. }

83. createTimeInstructions(): Instruction[] {
84. const instructions: Instruction[] = [];
85. if (!this.targetFunc) {
86. return instructions;
87. }
88. const isaKit = this.targetFunc.getIsaKit();
89. const tryldglobalbyname = isaKit.createTryLdGlobalByName(Context.REPLACE_IMPORT_NAME);
90. const ldobjbyname = isaKit.createLdObjByName(tryldglobalbyname, Context.REPLACE_FUNCTION_NAME);
91. const callthis0 = isaKit.createCallThis0(ldobjbyname, tryldglobalbyname);

93. instructions.push(tryldglobalbyname);
94. instructions.push(ldobjbyname);
95. instructions.push(callthis0);

97. return instructions;
98. }

100. /**
101. * step2. Position objective function
102. */
103. getTargetFunction(): void {
104. const functions = this.manager.query()
105. .projectModule(Context.PROJECT_MODULE)
106. .path(Context.QUERY_PATH)
107. .className(Context.QUERY_CLASS_NAME)
108. .functionName(Context.QUERY_FUNCTION_NAME)
109. .getFunction();
110. if (functions.length === 0) {
111. throw new Error('Duration Task function not found.');
112. }
113. this.targetFunc = functions[0];
114. }
115. }
```

[DurationTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/DurationTask.ts#L18-L132)

**场景三：隐私API监控**

**场景描述：**

开发者可以通过对调用点位置进行分析埋点，实现对重点API接口的调用监控。

以下示例对地理位置获取操作进行调用监控，对geoLocationManager.getCurrentLocation()方法调用进行前置插桩。

ArkTS源码如下所示：

```
1. getLocation(): void {
2. const request: geoLocationManager.SingleLocationRequest = {
3. locatingPriority: geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
4. locatingTimeoutMs: CommonConstants.LOCATING_TIMEOUT_MS
5. };
6. // Insert here: Set message to `Module[path: &entry/src/main/ets/pages/scene/PrivacyApi&]
7. // - struct[name: getLocation] - getCurrentLocation is executed.`
8. geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
9. this.longitude = location.longitude;
10. this.latitude = location.latitude;
11. }).catch((err: BusinessError) => {
12. Logger.error(TAG, `getLocation failed, code: ${err.code}, message: ${err.message}`);
13. LocationErrorUtil.locationFailedAlert(this.getUIContext(), err.code);
14. });
15. }
```

[PrivacyApi.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/PrivacyApi.ets#L83-L97)

**实现步骤：**

1. 初始化AbcManager实例。
2. 收集目标函数。
3. 扫描函数指令，定位API调用点。
4. 执行前置插桩操作。
5. 输出abc文件。

   代码如下：

   ```
   1. class Context {
   2. static readonly PROJECT_MODULE: string = 'entry';
   3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/PrivacyApi';
   4. static readonly QUERY_CLASS_NAME: string = 'PrivacyApiPage';
   5. static readonly QUERY_FUNCTION_NAME: string = 'getLocation';
   6. static readonly API_IMPORT_NAME: string = 'geoLocationManager';
   7. static readonly API_FUNCTION_NAME: string = 'getCurrentLocation';
   8. static readonly ATTRIBUTE_NAME: string = 'message';
   9. static apiCallLog(moduleName: string, className: string): string {
   10. return `Module[path: ${moduleName}] - struct[name: ${className}] - getCurrentLocation is executed.`;
   11. }
   12. }

   14. export class PrivacyApiScanTask {
   15. manager: AbcManager;
   16. targetFunc: AbcFunction | null = null;

   18. /**
   19. * step1. init AbcManager
   20. *
   21. * @param manager AbcManager
   22. */
   23. constructor(manager: AbcManager) {
   24. this.manager = manager;
   25. }

   27. run(): void {
   28. this.getTargetFunction();
   29. this.transform();
   30. this.manager.flush();
   31. }

   33. /**
   34. * step2. Collect objective functions
   35. */
   36. getTargetFunction(): void {
   37. const functions = this.manager.query()
   38. .projectModule(Context.PROJECT_MODULE)
   39. .path(Context.QUERY_PATH)
   40. .className(Context.QUERY_CLASS_NAME)
   41. .functionName(Context.QUERY_FUNCTION_NAME)
   42. .getFunction();
   43. if (functions.length === 0) {
   44. throw new Error('PrivacyApiScan Task function not found');
   45. }
   46. this.targetFunc = functions[0];
   47. }

   49. isTargetApiCall(callInst: Instruction, params: { importName: string; functionName: string }): boolean {
   50. if (!this.targetFunc) {
   51. return false;
   52. }
   53. if (!this.targetFunc.getIsaKit().iIsCall(callInst)) {
   54. return false;
   55. }

   57. const input0 = this.targetFunc.getIsaKit().iGetInput(callInst, 0);
   58. const isTargetFunction = input0 && this.targetFunc.getIsaKit().iGetOpcode(input0) ===
   59. IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_LDOBJBYNAME &&
   60. this.targetFunc.getIsaKit().iGetString(input0) === params.functionName;
   61. if (!isTargetFunction) {
   62. return false;
   63. }

   65. const input1 = this.targetFunc.getIsaKit().iGetInput(callInst, 1);
   66. if (!input1) {
   67. return false;
   68. }
   69. const isTargetImport = this.targetFunc.getIsaKit().iGetOpcode(input1) ===
   70. IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_LDEXTERNALMODULEVAR &&
   71. this.targetFunc.getIsaKit().iGetImportDescriptor(input1).getAlias() === params.importName;
   72. return isTargetImport;
   73. }

   75. /**
   76. * step3. Scans function instructions to locate API call points.
   77. * step4. Perform pre-instrumentation operations.
   78. */
   79. transform(): void {
   80. const instructions = this.targetFunc?.getInstructions();
   81. if (!instructions || !this.targetFunc) {
   82. return;
   83. }

   85. for (const inst of instructions) {
   86. if (!this.isTargetApiCall(inst, { importName: Context.API_IMPORT_NAME, functionName: Context.API_FUNCTION_NAME })) {
   87. continue;
   88. }

   90. const isaKit = this.targetFunc.getIsaKit();
   91. const instructionsInsert: Instruction[] = [];
   92. const params = this.targetFunc.getParameters();
   93. const moduleName = this.targetFunc.getParentModule().getName();
   94. const loadStringInst = isaKit.createLdaString(Context.apiCallLog(moduleName, this.targetFunc.getName()));
   95. const stobjbynameInst = isaKit.createStObjByName(loadStringInst, Context.ATTRIBUTE_NAME, params[params.length - 1]);
   96. instructionsInsert.push(loadStringInst);
   97. instructionsInsert.push(stobjbynameInst);

   99. isaKit.iInsertBefore(inst, instructionsInsert);
   100. }
   101. this.targetFunc?.apply();
   102. }
   103. }
   ```

   [PrivacyApiScanTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/PrivacyApiScanTask.ts#L19-L121)

说明

调用点分析通常不确定调用点位置，因此需要对范围内的方法进行全量指令扫描，范围限定越精确，定位调用点耗时越少。

**场景四：方法调用点替换**

**场景描述：**

业务逻辑开发过程中，源码或三方库可能需要紧急修复异常，开发者可以通过调用点替换来增强API功能。

以下示例将系统API geoLocationManager.getCurrentLocation()调用替换为自定义的GeoUtils.getLocation()方法。

ArkTS源码如下所示：

geoLocationManager.getCurrentLocation()为待替换API。

```
1. getLocation(): void {
2. const request: geoLocationManager.SingleLocationRequest = {
3. locatingPriority: geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
4. locatingTimeoutMs: CommonConstants.LOCATING_TIMEOUT_MS
5. };
6. // Replace here: Replace geoLocationManager.getCurrentLocation with GeoUtils.getLocation
7. geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
8. this.longitude = location.longitude;
9. this.latitude = location.latitude;
10. this.message = TimeUtil.getNowWithHMS() + Context.MESSAGE_INFO;
11. }).catch((err: BusinessError) => {
12. Logger.error(TAG, `getLocationAddress failed, code: ${err.code}, message: ${err.message}`);

14. if (err.message === CommonConstants.CALL_TOO_FAST) {
15. this.message = TimeUtil.getNowWithHMS() + ': ' + err.message;
16. } else {
17. LocationErrorUtil.locationFailedAlert(this.getUIContext(), err.code);
18. }
19. });
20. }
```

[CallReplace.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/CallReplace.ets#L94-L113)

GeoUtils.getLocation()为替换API。

```
1. export class GeoUtils {
2. private static lastInvokeTime: number = PageConstants.CONSTANT_VALUE_ZERO;
3. private static readonly MIN_INTERVAL: number = PageConstants.MINI_INTERVAL;

5. static async getLocation(
6. request?: geoLocationManager.CurrentLocationRequest | geoLocationManager.SingleLocationRequest
7. ): Promise<geoLocationManager.Location> {
8. const now = new Date().getTime();
9. if (now - GeoUtils.lastInvokeTime < GeoUtils.MIN_INTERVAL) {
10. return Promise.reject(new Error(CommonConstants.CALL_TOO_FAST));
11. }

13. GeoUtils.lastInvokeTime = now;
14. try {
15. return await geoLocationManager.getCurrentLocation(request);
16. } catch (error) {
17. throw new Error('Location retrieval failed');
18. }
19. }

21. static getLastInvokeTime(): number {
22. return GeoUtils.lastInvokeTime;
23. }

25. static resetLastInvokeTime(): void {
26. GeoUtils.lastInvokeTime = PageConstants.CONSTANT_VALUE_ZERO;
27. }

29. static init(): void {
30. }
31. }
```

[GeoUtils.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/common/GeoUtils.ets#L21-L51)

**实现步骤：**

1. 初始化AbcManager实例。
2. 定位目标函数。
3. 扫描函数指令，定位API调用点。
4. 引入外部替换API模块。
5. 执行替换插桩操作。
6. 输出abc文件。

代码如下：

```
1. class Context {
2. static readonly PROJECT_MODULE: string = 'entry';
3. static readonly ASPECT_PATH: string = 'src/main/ets/common/GeoUtils';
4. static readonly ASPECT_FUNCTION_NAME: string = 'getLocation';
5. static readonly ASPECT_IMPORT_NAME: string = 'GeoUtils';
6. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/CallReplace';
7. static readonly QUERY_FUNCTION_NAME: string = 'getLocation';
8. static readonly API_IMPORT_NAME: string = 'geoLocationManager';
9. static readonly API_FUNCTION_NAME: string = 'getCurrentLocation';
10. static readonly REPLACE_IMPORT_NAME: string = 'GeoUtils';
11. }

13. export class CallReplaceTask {
14. manager: AbcManager;
15. targetFunc: AbcFunction | null = null;
16. aspectFunc: AbcFunction | null = null;
17. importDescriptor: ImportDescriptor | null = null;

19. /**
20. * step1. init AbcManager
21. *
22. * @param manager AbcManager
23. */
24. constructor(manager: AbcManager) {
25. this.manager = manager;
26. }

28. run(): void {
29. this.getTargetFunction();
30. this.getAspectFunction();
31. this.getImportDescriptor();
32. this.doTransform();
33. this.manager.flush();
34. }

36. /**
37. * step4. Scans function instructions to locate API call points.
38. * step5. Perform the replacement and instrumentation operation.
39. */
40. doTransform(): void {
41. if (!this.targetFunc || !this.importDescriptor || !this.aspectFunc) {
42. return;
43. }

45. const isaKit = this.targetFunc.getIsaKit();
46. const insts = this.targetFunc.getInstructions();

48. if (!insts) {
49. return;
50. }

52. for (const inst of insts) {
53. if (!this.isTargetApiCall(inst,
54. { importName: Context.API_IMPORT_NAME, functionName: Context.API_FUNCTION_NAME })) {
55. continue;
56. }
57. const importDesc = isaKit.createLdExternalModuleVar(this.importDescriptor);
58. const parentClass = this.aspectFunc.getParentClass();

60. if (!parentClass) {
61. continue;
62. }

64. const myAspect =
65. isaKit.createThrowUndefinedIfHoleWithName(importDesc, parentClass.getName());
66. const replaceAdd = isaKit.createLdObjByName(myAspect, this.aspectFunc.getName());
67. isaKit.iInsertBefore(inst, [importDesc, myAspect, replaceAdd]);
68. isaKit.iSetInput(inst, 0, replaceAdd);
69. isaKit.iSetInput(inst, 1, importDesc);
70. }
71. this.targetFunc.apply();
72. }

74. isTargetApiCall(callInst: Instruction, params: { importName: string; functionName: string }): boolean {
75. if (!this.targetFunc) {
76. return false;
77. }
78. const isaKit = this.targetFunc.getIsaKit();
79. if (!isaKit.iIsCall(callInst)) {
80. return false;
81. }

83. const input0 = isaKit.iGetInput(callInst, 0);
84. const isTargetFunction =
85. input0 && isaKit.iGetOpcode(input0) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_LDOBJBYNAME &&
86. isaKit.iGetString(input0) === params.functionName;
87. if (!isTargetFunction) {
88. return false;
89. }

91. const input1 = isaKit.iGetInput(callInst, 1);
92. if (!input1) {
93. return false;
94. }
95. const isTargetImport =
96. isaKit.iGetOpcode(input1) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_LDEXTERNALMODULEVAR &&
97. isaKit.iGetImportDescriptor(input1).getAlias() === params.importName;

99. return isTargetImport;
100. }

102. getImportDescriptor(): void {
103. if (!this.targetFunc || !this.aspectFunc) {
104. return;
105. }
106. const isa = this.targetFunc.getIsaKit();
107. this.importDescriptor =
108. isa.getOrAddImportDescriptor(this.targetFunc.getParentModule(), this.aspectFunc.getParentModule(),
109. Context.REPLACE_IMPORT_NAME,
110. Context.REPLACE_IMPORT_NAME);
111. }

113. /**
114. * step3. Introduce an external API replacement module
115. */
116. getAspectFunction(): void {
117. const functions = this.manager.query()
118. .projectModule(Context.PROJECT_MODULE)
119. .path(Context.ASPECT_PATH)
120. .functionName(Context.ASPECT_FUNCTION_NAME)
121. .getFunction();
122. if (functions.length === 0) {
123. throw new Error('aspect function not found');
124. }
125. this.aspectFunc = functions[0];
126. }

128. /**
129. * step2. Position objective function
130. */
131. getTargetFunction(): void {
132. const functions = this.manager.query()
133. .projectModule(Context.PROJECT_MODULE)
134. .path(Context.QUERY_PATH)
135. .functionName(Context.QUERY_FUNCTION_NAME)
136. .getFunction();
137. if (functions.length === 0) {
138. throw new Error('CallReplace Task function not found.');
139. }
140. this.targetFunc = functions[0];
141. }
142. }
```

[CallReplaceTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/CallReplaceTask.ts#L19-L160)

**场景五：关键属性修改**

**场景描述：**

当三方框架出现运行时缺陷，某些属性的配置不符合预期，开发者可以通过对字节码指令的修改，修复相关问题。

以下示例通过对字节码指令的编辑，实现对message属性的修改。

ArkTS源码如下所示：

```
1. changeMessage(): void {
2. this.logInfo = Context.MESSAGE_INFO;
3. // Insert here: Set this.message to "This is New Title"
4. }
```

[KeyAttribute.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/KeyAttribute.ets#L40-L43)

**实现步骤：**

1. 初始化AbcManager实例。
2. 定位目标函数。
3. 执行指令编辑操作。
4. 输出abc文件。

   代码如下：

   ```
   1. class Context {
   2. static readonly PROJECT_MODULE: string = 'entry';
   3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/KeyAttribute';
   4. static readonly QUERY_CLASS_NAME: string = 'KeyAttributePage';
   5. static readonly QUERY_FUNCTION_NAME: string = 'changeMessage';
   6. static readonly REPLACE_MESSAGE: string = 'This is New Title!';
   7. static readonly ATTRIBUTE_NAME: string = 'message';
   8. }

   10. export class KeyAttributeModifyTask {
   11. manager: AbcManager;
   12. targetFunc: AbcFunction | null = null;

   14. /**
   15. * step1. init AbcManager
   16. *
   17. * @param manager AbcManager
   18. */
   19. constructor(manager: AbcManager) {
   20. this.manager = manager;
   21. }

   23. run(): void {
   24. this.getTargetFunction();
   25. this.transform();
   26. this.manager.flush();
   27. }

   29. /**
   30. * step2. Position objective function
   31. */
   32. getTargetFunction(): void {
   33. const functions = this.manager.query()
   34. .projectModule(Context.PROJECT_MODULE)
   35. .path(Context.QUERY_PATH)
   36. .className(Context.QUERY_CLASS_NAME)
   37. .functionName(Context.QUERY_FUNCTION_NAME)
   38. .getFunction();
   39. if (functions.length === 0) {
   40. throw new Error('KeyAttributeModify Task function not found');
   41. }
   42. this.targetFunc = functions[0];
   43. }

   45. /**
   46. * step3. Perform the instruction editing operation.
   47. */
   48. transform(): void {
   49. if (!this.targetFunc) {
   50. return;
   51. }
   52. const isaKit = this.targetFunc.getIsaKit();
   53. const instructions: Instruction[] = [];
   54. const params = this.targetFunc.getParameters();
   55. const loadStringInst = isaKit.createLdaString(Context.REPLACE_MESSAGE);
   56. const stobjbynameInst = isaKit.createStObjByName(loadStringInst, Context.ATTRIBUTE_NAME, params[params.length - 1]);
   57. instructions.push(loadStringInst);
   58. instructions.push(stobjbynameInst);
   59. this.targetFunc.insertBefore(instructions);
   60. this.targetFunc.apply();
   61. }
   62. }
   ```

   [KeyAttributeModifyTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/KeyAttributeModifyTask.ts#L19-L80)

**场景六：点击事件埋点**

**场景描述：**

开发者可通过在点击事件回调函数中插桩，对用户点击行为进行监控和统计，实现用户行为数据的自动采集。

以下示例对Button组件的onClick()事件回调函数进行前置插桩。

ArkTS源码如下所示：

```
1. Button($r('app.string.event_onclick'))
2. .attributeModifier(new ButtonStyles())
3. .onClick(() => {
4. // Insert here: Set message to `Module[path: &entry/src/main/ets/pages/scene/EventCallbackBeforeTs&]
5. // -onclick event is triggered.`
6. });
```

[EventCallbackBeforeTs.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/EventCallbackBeforeTs.ets#L49-L54)

**实现步骤：**

1. 初始化AbcManager实例。
2. 收集目标函数。
3. 扫描函数指令，定位回调函数。
4. 执行前置插桩操作。
5. 输出abc文件。

代码如下：

```
1. class Context {
2. static readonly PROJECT_MODULE: string = 'entry';
3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/EventCallbackBeforeTs';
4. static readonly QUERY_FUNCTION_NAME: string = 'initialRender';
5. static readonly API_IMPORT_NAME: string = 'Button';
6. static readonly API_FUNCTION_NAME: string = 'onClick';
7. static readonly ATTRIBUTE_NAME: string = 'message';

9. static apiCallLog(moduleName: string): string {
10. return `Module[path: ${moduleName}] - onclick event is triggered.`;
11. }
12. }

14. export class EventCbTask {
15. manager: AbcManager;
16. targetFuncs: AbcFunction[] = [];

18. /**
19. * step1. init AbcManager
20. *
21. * @param manager AbcManager
22. */
23. constructor(manager: AbcManager) {
24. this.manager = manager;
25. }

27. run(): void {
28. this.getTargetFunction();
29. const targetCbFuncs: AbcFunction[] = [];
30. for (const func of this.targetFuncs) {
31. this.collectCallBackFuncs(func, targetCbFuncs);
32. }

34. for (const cbFunc of targetCbFuncs) {
35. this.doTransform(cbFunc);
36. }
37. this.manager.flush();
38. }

40. /**
41. * step4. Perform pre-instrumentation operations.
42. *
43. * @param cbFunc AbcFunction
44. */
45. doTransform(cbFunc: AbcFunction): void {
46. const moduleName = cbFunc.getParentModule().getName();
47. const isaKit = cbFunc.getIsaKit();
48. for (const inst of cbFunc.getInstructions()) {
49. const isReturn = isaKit.iGetOpcode(inst) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_RETURN ||
50. isaKit.iGetOpcode(inst) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_RETURNUNDEFINED;
51. if (isReturn) {
52. const ldlexvarInst = isaKit.createLdLexVar(0, 0);
53. const loadStringInst = isaKit.createLdaString(Context.apiCallLog(moduleName));
54. const stobjbynameInst = isaKit.createStObjByName(loadStringInst, Context.ATTRIBUTE_NAME, ldlexvarInst);
55. const instructions: Instruction[] = [];
56. instructions.push(ldlexvarInst);
57. instructions.push(loadStringInst);
58. instructions.push(stobjbynameInst);
59. isaKit.iInsertBefore(inst, instructions);
60. }
61. }

63. cbFunc.apply();
64. }

66. /**
67. * step3. Scans function instructions to locate the callback function.
68. *
69. * @param targetFunc AbcFunction
70. * @param targetCbFuncs AbcFunction[]
71. */
72. collectCallBackFuncs(targetFunc: AbcFunction, targetCbFuncs: AbcFunction[]): void {
73. const instructions = targetFunc.getInstructions();
74. const isaKit = targetFunc.getIsaKit();
75. for (const inst of instructions) {
76. if (!this.isTargetApiCall(targetFunc, inst, { importName: Context.API_IMPORT_NAME, functionName: Context.API_FUNCTION_NAME })) {
77. continue;
78. }
79. const cbFunc = this.getCbFunc(inst, isaKit);
80. if (!cbFunc) {
81. throw new Error('Failed to get callback function');
82. }
83. targetCbFuncs.push(cbFunc);
84. }
85. }

87. isTargetApiCall(targetFunc: AbcFunction, callInst: Instruction,
88. params: { importName: string; functionName: string }): boolean {
89. const isaKit = targetFunc.getIsaKit();
90. if (!isaKit.iIsCall(callInst)) {
91. return false;
92. }

94. const input0 = isaKit.iGetInput(callInst, 0);
95. if (!input0) {
96. return false;
97. }
98. const isTargetFunction = input0 && isaKit.iGetOpcode(input0) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_LDOBJBYNAME &&
99. isaKit.iGetString(input0) === params.functionName;
100. if (!isTargetFunction) {
101. return false;
102. }
103. const input1 = isaKit.iGetInput(callInst, 1);
104. if (!input1) {
105. return false;
106. }
107. const isTargetImport = isaKit.iGetOpcode(input1) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_TRYLDGLOBALBYNAME &&
108. isaKit.iGetString(input1) === params.importName;
109. return isTargetImport;
110. }

112. getCbFunc(callInst: Instruction, isaKit: IsaKit): AbcFunction | undefined {
113. const inputs = isaKit.iGetInputs(callInst);
114. for (const input of inputs) {
115. if (isaKit.iGetOpcode(input) === IsaApiDynamicOpcode.ABCKIT_ISA_API_DYNAMIC_OPCODE_DEFINEFUNC) {
116. return isaKit.iGetFunction(input) ?? undefined;
117. }
118. }
119. return undefined;
120. }

122. /**
123. * step2. Collect the objective function.
124. */
125. getTargetFunction(): void {
126. const functions = this.manager.query()
127. .projectModule(Context.PROJECT_MODULE)
128. .path(Context.QUERY_PATH)
129. .functionName(Context.QUERY_FUNCTION_NAME)
130. .getFunction();
131. if (functions.length === 0) {
132. throw new Error('EventCb Task function not found');
133. }
134. const children = functions[0].getNestedAnonymousCallbacks();
135. if (children.length === 0) {
136. throw new Error('EventCb Task initialRender function has no nested anonymous callback');
137. }
138. this.targetFuncs.push(...children);
139. }
140. }
```

[EventCbTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/EventCbTask.ts#L19-L158)

说明

**initialRender**函数是鸿蒙应用页面级渲染的入口函数，onClick回调通常以匿名函数形式嵌套在其中。

**场景七：方法入参校验**

**场景描述：**

在开发过程中，方法入参的合法性校验是保证程序健壮性的重要手段。当需要在不修改源码的情况下对方法参数进行统一校验，或对三方库的方法调用进行监控时，可以通过字节码插桩技术实现。

以下示例通过字节码插桩，实现在saveUser方法入口处校验age属性的合法性（age>=0 and age<=150）。

```
1. saveUser(name: string, age: number): void {
2. // Insert here
3. // Check if age < 0 or age > 150, assign message to "save user failed, age abnormal" and return
4. this.message = 'name:' + name + ' ' + 'age:' + age + '\n';
5. }
```

[MethodParameter.ets](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/entry/src/main/ets/pages/scene/MethodParameter.ets#L35-L39)

**实现步骤：**

1. 初始化AbcManager实例。
2. 定位目标函数。
3. 执行block插桩操作。
4. 输出abc文件。

   代码如下：

   ```
   1. class Context {
   2. static readonly PROJECT_MODULE: string = 'entry';
   3. static readonly QUERY_PATH: string = 'src/main/ets/pages/scene/MethodParameter';
   4. static readonly QUERY_CLASS_NAME: string = 'MethodParameterPage';
   5. static readonly QUERY_FUNCTION_NAME: string = 'saveUser';
   6. static readonly REPLACE_MESSAGE: string = 'save user failed, age abnormal.';
   7. static readonly ATTRIBUTE_NAME: string = 'message';
   8. static readonly AGE_MAX: number = 150;
   9. }

   11. export class MethodParameterValidateTask {
   12. manager: AbcManager;
   13. targetFunc: AbcFunction | null = null;

   15. /**
   16. * step1. init AbcManager
   17. *
   18. * @param manager AbcManager
   19. */
   20. constructor(manager: AbcManager) {
   21. this.manager = manager;
   22. }

   24. run(): void {
   25. this.getTargetFunction();
   26. this.transform();
   27. this.manager.flush();
   28. }

   30. /**
   31. * step2. Position objective function
   32. */
   33. getTargetFunction(): void {
   34. const functions = this.manager.query()
   35. .projectModule(Context.PROJECT_MODULE)
   36. .path(Context.QUERY_PATH)
   37. .className(Context.QUERY_CLASS_NAME)
   38. .functionName(Context.QUERY_FUNCTION_NAME)
   39. .getFunction();
   40. if (functions.length === 0) {
   41. throw new Error('MethodParameterValidate Task function not found');
   42. }
   43. this.targetFunc = functions[0];
   44. }

   46. /**
   47. * step3. Perform block instrumentation.
   48. */
   49. transform(): void {
   50. if (!this.targetFunc) {
   51. return;
   52. }
   53. const isaKit = this.targetFunc.getIsaKit();

   55. const instructions: Instruction[] = [];
   56. const params = this.targetFunc.getParameters();
   57. if (params.length < 3) {
   58. return;
   59. }
   60. const loadStringInst = isaKit.createLdaString(Context.REPLACE_MESSAGE);
   61. const stobjbynameInst = isaKit.createStObjByName(loadStringInst, Context.ATTRIBUTE_NAME, params[2]);
   62. instructions.push(loadStringInst);
   63. instructions.push(stobjbynameInst);
   64. instructions.push(isaKit.createReturnUndefined());

   66. const startBlock = isaKit.bGetStartBlock();
   67. const succBlocks = isaKit.bGetSuccBlocks(startBlock);
   68. const const0 = isaKit.iCreateConstantU64(0);
   69. const const02 = isaKit.iCreateConstantU64(0);

   71. const trueBB = succBlocks[0];
   72. isaKit.bEraseSuccBlock(startBlock, 0);
   73. const falseBB = isaKit.bCreateEmptyBlock();
   74. isaKit.bAppendSuccBlock(falseBB, isaKit.bGetEndBlock());
   75. isaKit.bAddInstructionsBack(falseBB, instructions);

   77. const ifBB = isaKit.bCreateEmptyBlock();
   78. const lessInst = isaKit.createLess(const0, params[params.length - 1]);
   79. const callruntimeTrueInst = isaKit.createCallRuntimeIsTrue(lessInst);
   80. const ifInst =
   81. isaKit.createIf(callruntimeTrueInst, IsaApiDynamicConditionCode.ABCKIT_ISA_API_DYNAMIC_CONDITION_CODE_CC_EQ);
   82. isaKit.iSetInput(ifInst, 1, const02);

   84. const ifBB2 = isaKit.bCreateEmptyBlock();
   85. const const150 = isaKit.iCreateConstantU64(Context.AGE_MAX);
   86. const lessInst2 = isaKit.createGreater(const150, params[params.length - 1]);
   87. const callruntimeFalseInst2 = isaKit.createCallRuntimeIsFalse(lessInst2);
   88. const ifInst2 =
   89. isaKit.createIf(callruntimeFalseInst2, IsaApiDynamicConditionCode.ABCKIT_ISA_API_DYNAMIC_CONDITION_CODE_CC_NE);
   90. isaKit.iSetInput(ifInst2, 1, const02);

   92. isaKit.bAddInstructionsBack(ifBB, [lessInst, callruntimeTrueInst, ifInst]);
   93. isaKit.bAddInstructionsBack(ifBB2, [lessInst2, callruntimeFalseInst2, ifInst2]);
   94. isaKit.bAppendSuccBlock(startBlock, ifBB);
   95. isaKit.bAppendSuccBlock(ifBB, ifBB2);
   96. isaKit.bAppendSuccBlock(ifBB, falseBB);
   97. isaKit.bAppendSuccBlock(ifBB2, trueBB);
   98. isaKit.bAppendSuccBlock(ifBB2, falseBB);

   100. this.targetFunc.apply();
   101. }
   102. }
   ```

   [MethodParameterValidateTask.ts](https://gitcode.com/HarmonyOS_Samples/abckit-ts/blob/master/abckitTask/src/task/MethodParameterValidateTask.ts#L19-L120)

----结束↵

## 示例代码

* [基于AbcKitTS实现字节码插桩](https://gitcode.com/HarmonyOS_Samples/abckit-ts)
