---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import
title: 动态加载
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 动态加载
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:36+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:34f5c1348f8d06e2a854f4fac7eeb0580e3aac426bead294111d9c1d59a991b6
---
动态import支持条件延迟加载，支持部分反射功能，可以提升页面的加载速度；动态import支持加载HSP模块/HAR模块/ohpm包/Native库等，并且HAR模块之间可通过变量动态import来访问彼此导出的内容，可避免编译期强依赖，实现模块解耦。

## 技术适用场景介绍

应用开发的有些场景中，如果希望根据条件导入模块或者按需导入模块，可以使用动态import代替[静态import](../../../../../基础入门/学习ArkTS语言/ArkTS语言介绍/introduction-to-arkts.md#导入)。下面是可能会需要动态import的场景：

* 当静态import的模块明显降低了代码的加载速度且很少被使用，或者并不需要马上使用它。
* 当静态import的模块明显占用了大量的系统内存且很少被使用。
* 当被导入的模块，在加载时并不存在，需要异步获取。
* 当需要动态构建模块说明符时，应使用动态import。静态import仅支持静态说明符。
* 当导入的模块存在副作用（即模块中包含直接运行的代码），这些副作用仅在满足特定条件时才需要。

## 业务扩展场景介绍

动态import在业务上除了能实现条件延迟加载，还可以实现部分反射功能。实例如下，HAP动态import HAR包harlibrary，并调用类Calc的静态成员函数staticAdd()、成员函数instanceAdd()，以及全局方法addHarLibrary()。

```
1. // harlibrary's src/main/ets/utils/Calc.ets
2. export class Calc {
3. public static staticAdd(a: number, b: number): number {
4. let c = a + b;
5. console.info('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
6. return c;
7. }

9. public instanceAdd(a: number, b: number): number {
10. let c = a + b;
11. console.info('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
12. return c;
13. }
14. }

16. export function addHarlibrary(a: number, b: number): number {
17. let c = a + b;
18. console.info('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
19. return c;
20. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/harlibrary/src/main/ets/utils/Calc.ets#L16-L37)

```
1. // harlibrary's Index.ets
2. export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/harlibrary/Index.ets#L18-L21)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "harlibrary": "file:../harlibrary",
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L23-L70)

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('harlibrary').then((ns: ESObject) => {
3. ns.Calc.staticAdd(8, 9); // 调用静态成员函数staticAdd()
4. let calc: ESObject = new ns.Calc(); // 实例化类Calc
5. calc.instanceAdd(10, 11); // 调用成员函数instanceAdd()
6. ns.addHarlibrary(6, 7); // 调用全局方法addHarlibrary()

8. // 使用类、成员函数和方法的字符串名字进行反射调用
9. let className = 'Calc';
10. let methodName = 'instanceAdd';
11. let staticMethod = 'staticAdd';
12. let functionName = 'addHarlibrary';
13. ns[className][staticMethod](12, 13); // 调用静态成员函数staticAdd()
14. let calc1: ESObject = new ns[className](); // 实例化类Calc
15. calc1[methodName](14, 15); // 调用成员函数instanceAdd()
16. ns[functionName](16, 17); // 调用全局方法addHarlibrary()
17. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L85-L103)

## 动态import实现方案介绍

动态import根据入参是常量或变量，分为动态import常量表达式和动态import变量表达式两大特性规格。

以下是动态import支持的规格列表：

| 动态import场景 | 动态import详细分类 | 说明 |
| --- | --- | --- |
| 本地工程模块 | 动态import模块内文件路径 | 要求路径以./或../开头。 |
| 本地工程模块 | 动态import HSP模块名 | - |
| 本地工程模块 | 动态import HSP模块文件路径 | - |
| 本地工程模块 | 动态import HAR模块名 | - |
| 本地工程模块 | 动态import HAR模块文件路径 | - |
| 远程包 | 动态import远程HAR模块名 | - |
| 远程包 | 动态import ohpm包名 | - |
| API | 动态import @system.\* | - |
| API | 动态import @ohos.\* | - |
| API | 动态import @arkui-x.\* | - |
| 模块Native库 | 动态import libNativeLibrary.so | - |

说明

1.当前所有import中使用的模块名都是依赖方oh-package.json5文件中dependencies项的别名。

2.本地模块在依赖方的dependencies中配置的别名建议与moduleName以及packageName三者一致。moduleName指的是被依赖的HSP/HAR的module.json5中配置的名字，packageName指的是被依赖的HSP/HAR的oh-package.json5中配置的名字。

3.import一个模块名，实际的行为是import该模块的入口文件，一般为Index.ets/ts。

## 动态import实现中的关键点

### 动态import常量表达式

动态import常量表达式是指动态import的入参为常量的场景。下面以HAP引用其他模块的API的示例来说明典型用法。

本文示例代码中的路径，如Index.ets，是根据当前DevEco Studio的模块配置设置的。如果后续有变化，请调整文件的位置和相对路径。

* **HAP常量动态import HAR模块名**

```
1. // HAR's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('myhar').then((ns: ESObject) => {
3. console.info(ns.add(3, 5));
4. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L106-L111)

```
1. // 可使用 await 处理动态import (必须在 async 函数内使用)
2. async function asyncDynamicImport() {
3. let ns = await import('myhar');
4. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
5. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L18-L24)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhar": "file:../myHar"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L24-L71)

* **HAP常量动态import HAR模块文件路径**

```
1. // HAR's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('myhar/Index').then((ns: ESObject) => {
3. console.info(ns.add(3, 5));
4. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L114-L119)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhar": "file:../myHar"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L24-L71)

* **HAP常量动态import HSP模块名**

```
1. // HSP's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('myhsp').then((ns: ESObject) => {
3. console.info(ns.add(3, 5));
4. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L122-L127)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhsp": "file:../myHsp"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L25-L72)

* **HAP常量动态import HSP模块名文件路径**

```
1. // HSP's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('myhsp/Index').then((ns: ESObject) => {
3. console.info(ns.add(3, 5));
4. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L130-L135)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhsp": "file:../myHsp"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L25-L72)

* **HAP常量动态import远程HAR模块名**

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('@ohos/crypto-js').then((ns: ESObject) => {
3. console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.src);
4. });
```

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "@ohos/crypto-js": "2.0.3-rc.0"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L26-L73)

* **HAP常量动态import ohpm包**

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('@ohos/hypium').then((ns: ESObject) => {
3. console.info('DynamicImport @ohos/hypium: ', ns.TestType.FUNCTION.toString());
4. });
```

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "@ohos/hypium": "1.0.19"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L27-L74)

* **HAP常量动态import自己的单文件**

```
1. // HAP's src/main/ets/Calc.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('../Calc').then((ns: ESObject) => {
3. console.info(ns.add(3, 5));
4. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L154-L159)

* **HAP常量动态import自己的Native库**

```
1. // libnativeapi.so's index.d.ts
2. export const add: (a: number, b: number) => number;
```

[index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/cpp/types/libentry/index.d.ts#L16-L19)

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('libentry.so').then((ns: ESObject) => {
3. console.info('DynamicImport libnativeapi.so: ' + ns.default.add(2, 3));
4. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L162-L167)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "libentry.so": "file:./src/main/cpp/types/libentry"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L28-L75)

* **HAP常量动态import加载API**

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('@system.app').then((ns: ESObject) => {
3. ns.default.getInfo();
4. });
5. import('@ohos.curves').then((ns: ESObject) => {
6. ns.default.springMotion(0.555, 0.75, 0.001).interpolate(1);
7. });
8. import('@ohos.matrix4').then((ns: ESObject) => {
9. ns.default.identity().transformPoint([1, 2])[0];
10. });
11. import('@ohos.hilog').then((ns: ESObject) => {
12. ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.');
13. hilog.info(0x000, 'testTag', '%{public}s', ns.default.LogLevel.DEBUG);
14. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L170-L197)

### 动态import变量表达式

DevEco Studio中模块间的依赖关系通过oh-package.json5中的dependencies字段进行配置。dependencies列表中所有的模块默认都会进行安装（本地模块）或下载（远程模块），但是不会默认参与编译。HAP/HSP编译时会以入口文件（一般为Index.ets/Index.ts）开始搜索依赖关系，搜索到的模块或文件才会加入编译。

在编译期，静态import和常量动态import可以被打包工具rollup及其插件识别解析，加入依赖树中，参与编译流程，最终生成方舟字节码。但是，如果是变量动态import，该变量值可能需要进行运算或外部传入才能得到，在编译态无法解析其内容，也就无法加入编译。为了将这部分模块/文件加入编译，还需要额外增加一个runtimeOnly的buildOption配置，用于指定动态import的变量实际的模块名或文件路径。

**1. runtimeOnly字段schema配置格式**

在HAP/HSP/HAR的build-profile.json5中的buildOption中增加runtimeOnly配置项，仅在通过变量动态import时配置，静态import和常量动态import无需配置；并且，通过变量动态import加载API时也无需配置runtimeOnly。如下实例说明如何配置通过变量动态import其他模块，以及变量动态import本模块自己的单文件：

```
1. // HAP's src/main/ets/pages/Index.ets
2. // 变量动态import其他模块myHar
3. let harName = 'myhar';
4. import(harName).then((ns: ESObject) => {
5. console.info(ns.add(3, 5));
6. });

8. // 变量动态import本模块自己的单文件
9. let filePath = '../utils/Calc';
10. import(filePath).then((ns: ESObject) => {
11. console.info(ns.add(3, 5));
12. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L199-L215)

对应的runtimeOnly配置：

```
1. "buildOption": {
2. "arkOptions": {
3. "runtimeOnly": {
4. "packages": [ "myhar" ],
5. "sources": [ "./src/main/ets/utils/Calc.ets" ]
6. }
7. }
8. }
```

"runtimeOnly"的"packages"：用于配置本模块变量动态import其他模块名，要求与dependencies中配置的名字一致。

"runtimeOnly"的"sources"：用于配置本模块变量动态import自己的文件路径，路径相对于当前build-profile.json5文件。

**2. 使用实例**

* **HAP变量动态import HAR模块名**

```
1. // HAR's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
5. return c;
6. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/myHar/Index.ets#L18-L25)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let harPackageName = 'myhar';
3. import(harPackageName).then((ns: ESObject) => {
4. console.info(ns.add(3, 5));
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L218-L224)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhar": "file:../myHar"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L24-L71)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "myhar",  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L19-L115)

* **HAP变量动态import HSP模块名**

```
1. // HSP's Index.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
5. return c;
6. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/myHsp/Index.ets#L16-L23)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let hspPackageName = 'myhsp';
3. import(hspPackageName).then((ns: ESObject) => {
4. console.info(ns.add(3, 5));
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L227-L233)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "myhsp": "file:../myHsp"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L25-L72)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "myhsp",  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L20-L116)

* **HAP变量动态import远程HAR模块名**

```
1. // HAP's src/main/ets/pages/Index.ets
2. let remoteHarPackageName = '@ohos/crypto-js';
3. import(remoteHarPackageName).then((ns: ESObject) => {
4. console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.src);
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L236-L242)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "@ohos/crypto-js": "2.0.3-rc.0"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L26-L73)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "@ohos/crypto-js",
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L22-L117)

* **HAP变量动态import ohpm包**

```
1. // HAP's src/main/ets/pages/Index.ets
2. let ohpmPackageName = '@ohos/hypium';
3. import(ohpmPackageName).then((ns: ESObject) => {
4. console.info('DynamicImport @ohos/hypium: ', ns.TestType.FUNCTION.toString());
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L245-L251)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "@ohos/hypium": "1.0.19"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L27-L74)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "@ohos/hypium",
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L21-L118)

* **HAP变量动态import自己的单文件**

```
1. // HAP's src/main/ets/Calc.ets
2. export function add(a: number, b: number): number {
3. let c = a + b;
4. console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
5. return c;
6. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/Calc.ets#L16-L23)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let calcFilePath = '../Calc';
3. import(calcFilePath).then((ns: ESObject) => {
4. console.info(ns.add(3, 5));
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L254-L260)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "sources": [
6. "./src/main/ets/Calc.ets"  // 仅用于使用变量动态import模块自己单文件场景，静态import或常量动态import无需配置。
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L25-L119)

* **HAP变量动态import自己的Native库**

```
1. // libnativeapi.so's index.d.ts
2. export const add: (a: number, b: number) => number;
```

[index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/cpp/types/libentry/index.d.ts#L16-L19)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let soName = 'libentry.so';
3. import(soName).then((ns: ESObject) => {
4. console.info('DynamicImport libnativeapi.so: ' + ns.default.add(2, 3));
5. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L263-L269)

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "libentry.so": "file:./src/main/cpp/types/libentry"
4. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L28-L75)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "libentry.so",
7. ]
8. }
9. }
10. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L23-L120)

* **HAP变量动态import加载API**

```
1. // HAP's src/main/ets/pages/Index.ets
2. let packageName = '@system.app';
3. import(packageName).then((ns: ESObject) => {
4. ns.default.getInfo();
5. });
6. let packageName = '@ohos.curves';
7. import(packageName).then((ns: ESObject) => {
8. ns.default.springMotion(0.555, 0.75, 0.001).interpolate(1);
9. });
10. let packageName = '@ohos.matrix4';
11. import(packageName).then((ns: ESObject) => {
12. ns.default.identity().transformPoint([1, 2])[0];
13. });
14. let packageName = '@ohos.hilog';
15. import(packageName).then((ns: ESObject) => {
16. ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.');
17. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L272-L302)

通过变量动态import加载API时无需配置runtimeOnly。

### HAR模块间动态import依赖解耦

当应用包含多个HAR包，HAR包之间的依赖关系比较复杂。在DevEco Studio中配置依赖关系时，可能会形成循环依赖。这时，如果HAR之间的依赖关系中仅有变量动态import，可以将HAR包之间直接依赖关系转移到HAP/HSP中配置，HAR包之间无需配置依赖关系，从而达到HAR包间依赖解耦的目的。如下示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/TYXbWGQPQa2skoahdiXVjQ/zh-cn_image_0000002583118046.png?HW-CC-KV=V1&HW-CC-Date=20260601T030135Z&HW-CC-Expire=86400&HW-CC-Sign=F3651BF9E174DE9A6A31A4C80C76A0ABF8EFF37EBE4EB78C7AB72BC041BC1A69)

HAR之间的依赖关系转移至HAP/HSP后：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/SVurq094TeqpfZsSiwCYMw/zh-cn_image_0000002613637811.png?HW-CC-KV=V1&HW-CC-Date=20260601T030135Z&HW-CC-Expire=86400&HW-CC-Sign=250CC63DC32F2D7E13604115A9CBA5CCE287F314FF3E0DF83E80185C9C63791D)

**使用限制**

* 仅限在本地源码HAR包之间存在循环依赖时，使用该规避方案。
* 被转移依赖的HAR之间只能通过变量动态import，不能有静态import或常量动态import。
* 转移依赖时，需同时转移**dependencies**和**runtimeOnly**依赖配置。
* HSP不支持转移依赖。即：HAP->HSP1->HSP2->HSP3，这里的HSP2和HSP3不能转移到HAP上面。
* 转移依赖的整个链路上只能有HAR包，不能跨越HSP转移。即：HAP->HAR1->HAR2->HSP->HAR3->HAR4，HAR1对HAR2的依赖可以转移到HAP上，HAR3对HAR4的依赖可以转移到HSP上。但是，不能将HAR3或HAR4转移到HAP上。
* 如果引用了其他工程模块、远程包或集成HSP，需确保在[工程级build-profile.json5文件](../../../../../构建应用/配置文件/工程级build-profile.json5文件/ide-hvigor-build-profile-app.md)中的**useNormalizedOHMUrl**配置一致，同时设置为true或false，否则可能导致运行错误：**Cannot find dynamic-import module library**。

**使用实例**

下面的实例通过在单向依赖HAP->HAR1->HAR2->HAR3之上增加依赖HAR2->HAR1、HAR3->HAR1，形成了循环依赖。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/myQoJuVxQxiScvlYUEGrpw/zh-cn_image_0000002583118046.png?HW-CC-KV=V1&HW-CC-Date=20260601T030135Z&HW-CC-Expire=86400&HW-CC-Sign=60897C2A94B8B97AB630D2010C445D676781B58142ECC214DAF48E10F876E333)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let harName = 'har1'
3. import(harName).then((ns: ESObject) => {
4. console.info('[DynamicImport] hap -> har1, 0 + 1 = ' + ns.ClassHar1.add(0, 1));
5. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/src/main/ets/pages/Index.ets#L304-L310)

```
1. // HAR1's src/main/ets/utils/Calc.ets
2. export class ClassHar1 {
3. public static isImportedHar2: boolean = false;

5. static add(a: number, b: number): number {
6. const c = a + b;
7. console.info('[DynamicImport] ClassHar1.add(), %d + %d = %d', a, b, c);

9. if (!ClassHar1.isImportedHar2) {
10. const harName = 'har2';
11. import(harName).then((ns: ESObject) => {
12. ClassHar1.isImportedHar2 = true;
13. console.info('[DynamicImport] har1 -> har2, 1 + 2 = ' + ns.ClassHar2.add(1, 2));
14. })
15. }

17. return c;
18. }
19. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har1/src/main/ets/utils/Calc.ets#L16-L36)

```
1. // HAR1's Index.ets
2. export { ClassHar1 } from './src/main/ets/utils/Calc';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har1/Index.ets#L18-L21)

```
1. // HAR2's src/main/ets/utils/Calc.ets
2. export class ClassHar2 {
3. public static isImportedHar1: boolean = false;
4. public static isImportedHar3: boolean = false;

6. static add(a: number, b: number): number {
7. const c = a + b;
8. console.info('[DynamicImport] ClassHar2.add(), %d + %d = %d', a, b, c);

10. if (!ClassHar2.isImportedHar1) {
11. const harName = 'har1';
12. import(harName).then((ns: ESObject) => {
13. ClassHar2.isImportedHar1 = true;
14. console.info('[DynamicImport] har2 -> har1, 2 + 1 = ' + ns.ClassHar1.add(2, 1));
15. })
16. }

18. if (!ClassHar2.isImportedHar3) {
19. const harName = 'har3';
20. import(harName).then((ns: ESObject) => {
21. ClassHar2.isImportedHar3 = true;
22. console.info('[DynamicImport] har2 -> har3, 2 + 3 = ' + ns.ClassHar3.add(2, 3));
23. })
24. }

26. return c;
27. }
28. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har2/src/main/ets/utils/Calc.ets#L16-L45)

```
1. // HAR2's Index.ets
2. export { ClassHar2 } from './src/main/ets/utils/Calc';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har2/Index.ets#L18-L21)

```
1. // HAR3's src/main/ets/utils/Calc.ets
2. export class ClassHar3 {
3. public static isImportedHar1: boolean = false;

5. static add(a: number, b: number): number {
6. const c = a + b;
7. console.info('[DynamicImport] ClassHar3.add(), %d + %d = %d', a, b, c);

9. if (!ClassHar3.isImportedHar1) {
10. const harName = 'har1';
11. import(harName).then((ns: ESObject) => {
12. ClassHar3.isImportedHar1 = true;
13. console.info('[DynamicImport] har3 -> har1, 3 + 1 = ' + ns.ClassHar1.add(3, 1));
14. })
15. }

17. return c;
18. }
19. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har3/src/main/ets/utils/Calc.ets#L16-L36)

```
1. // HAR3's Index.ets
2. export { ClassHar3 } from './src/main/ets/utils/Calc';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har3/Index.ets#L18-L21)

若未对HAR之间的**dependencies**和**runtimeOnly**配置进行依赖解耦，ohpm无法解决循环依赖，依赖安装失败。

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "har1": "file:../har1"
4. }
5. // HAP's build-profile.json5
6. "buildOption": {
7. "arkOptions": {
8. "runtimeOnly": {
9. "packages": [
10. "har1"
11. ]
12. }
13. }
14. }

16. // HAR1's oh-package.json5
17. "dependencies": {
18. "har2": "file:../har2"
19. }
20. // HAR1's build-profile.json5
21. "buildOption": {
22. "arkOptions": {
23. "runtimeOnly": {
24. "packages": [
25. "har2"
26. ]
27. }
28. }
29. }

31. // HAR2's oh-package.json5
32. "dependencies": {
33. "har1": "file:../har1",
34. "har3": "file:../har3"
35. }
36. // HAR2's build-profile.json5
37. "buildOption": {
38. "arkOptions": {
39. "runtimeOnly": {
40. "packages": [
41. "har1",
42. "har3"
43. ]
44. }
45. }
46. }

48. // HAR3's oh-package.json5
49. "dependencies": {
50. "har1": "file:../har1"
51. }
52. // HAR3's build-profile.json5
53. "buildOption": {
54. "arkOptions": {
55. "runtimeOnly": {
56. "packages": [
57. "har1"
58. ]
59. }
60. }
61. }
```

**对应的报错信息如下：**

```
1. ohpm ERROR: Run install command failed
2. Error: 00618005 Invalid Dependency
3. Error Message: Invalid dependency har2@~\Coupled\har2 -> har2@1.0.0.

5. Try the following:
6. The name of an indirect dependency cannot be the same as the module name.
```

将HAR之间的**dependencies**和**runtimeOnly**配置转移到HAP中，解耦了包间循环依赖，程序能够正确运行。

```
1. // HAP's oh-package.json5
2. "har1": "file:../har1",
3. "har2": "file:../har2",
4. "har3": "file:../har3"
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/oh-package.json5#L57-L62)

```
1. // HAP's build-profile.json5
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "har1",
7. "har2",
8. "har3"
9. ]
10. }
11. }
12. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/entry/build-profile.json5#L24-L121)

```
1. // HAR1's oh-package.json5
2. "dependencies": {}
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har1/oh-package.json5#L23-L26)

```
1. // HAR1's build-profile.json5
2. "buildOption": {
3. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har1/build-profile.json5#L18-L22)

```
1. // HAR2's oh-package.json5
2. "dependencies": {}
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har2/oh-package.json5#L23-L26)

```
1. // HAR2's build-profile.json5
2. "buildOption": {
3. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har2/build-profile.json5#L18-L22)

```
1. // HAR3's oh-package.json5
2. "dependencies": {}
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har3/oh-package.json5#L23-L26)

```
1. // HAR3's build-profile.json5
2. "buildOption": {
3. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTSRuntime/ArkTSModule/DynamicImport/har3/build-profile.json5#L18-L22)

**对应的运行日志如下：**

```
1. [DynamicImport] ClassHar1.add(), 0 + 1 = 1
2. [DynamicImport] hap -> har1, 0 + 1 = 1
3. [DynamicImport] ClassHar2.add(), 1 + 2 = 3
4. [DynamicImport] har1 -> har2, 1 + 2 = 3
5. [DynamicImport] ClassHar1.add(), 2 + 1 = 3
6. [DynamicImport] har2 -> har1, 2 + 1 = 3
7. [DynamicImport] ClassHar3.add(), 2 + 3 = 5
8. [DynamicImport] har2 -> har3, 2 + 3 = 5
9. [DynamicImport] ClassHar1.add(), 3 + 1 = 4
10. [DynamicImport] har3 -> har1, 3 + 1 = 4
```
