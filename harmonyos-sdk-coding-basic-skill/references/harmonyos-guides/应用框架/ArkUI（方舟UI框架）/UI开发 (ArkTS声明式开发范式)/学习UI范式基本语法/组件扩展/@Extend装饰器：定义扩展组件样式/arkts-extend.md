---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend
title: @Extend装饰器：定义扩展组件样式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @Extend装饰器：定义扩展组件样式
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:53+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:5bc41570199d19ae484d586e04f11a6a5e94e62de18fb1feee7c1bfa3e1aa5d8
---
在前文的示例中，可以使用[@Styles](../@Styles装饰器：定义组件重用样式/arkts-style.md)用于样式的重用，在@Styles的基础上，我们提供了@Extend，用于扩展组件样式。

说明

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 语法

```
1. @Extend(UIComponentName) function functionName { ... }
```

### 使用规则

* 和@Styles不同，@Extend支持封装指定组件的私有属性、私有事件和自身定义的全局方法。

  ```
  1. // @Extend(Text)可以支持Text的私有属性fontColor
  2. @Extend(Text)
  3. function fancy() {
  4. .fontColor(Color.Red)
  5. }

  7. // superFancyText可以调用预定义的fancy
  8. @Extend(Text)
  9. function superFancyText(size: number) {
  10. .fontSize(size)
  11. .fancy()
  12. }
  ```

  [GlobalFunctionExtension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/GlobalFunctionExtension.ets#L29-L42)
* 使用@Extend封装指定组件的私有属性、私有事件和自身定义的全局方法时，不支持和@Styles混用。

  ```
  1. @Styles
  2. function fancy() {
  3. .backgroundColor(Color.Red)
  4. }

  6. // superFancyText不可以调用预定义的fancy
  7. @Extend(Text)
  8. function superFancyText(size: number) {
  9. .fontSize(size)
  10. .fancy()
  11. }
  ```
* 和@Styles不同，@Extend装饰的方法支持传入参数，调用遵循TS方法传值调用。

  ```
  1. // xxx.ets
  2. @Extend(Text)
  3. function fancy(fontSize: number) {
  4. .fontColor(Color.Red)
  5. .fontSize(fontSize)
  6. }

  8. @Entry
  9. @Component
  10. struct FancyUse {
  11. build() {
  12. Row({ space: 10 }) {
  13. Text('Fancy')
  14. .fancy(16)
  15. Text('Fancy')
  16. .fancy(24)
  17. }
  18. }
  19. }
  ```

  [ExtendParameterUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendParameterUsage.ets#L28-L48)
* @Extend装饰的方法的参数可以为function，作为Event事件的句柄。

  ```
  1. @Extend(Text)
  2. function makeMeClick(onClick: () => void) {
  3. .backgroundColor(Color.Blue)
  4. .onClick(onClick)
  5. }

  7. @Entry
  8. @Component
  9. struct FancyUse {
  10. @State label: string = 'Hello World';

  12. onClickHandler() {
  13. this.label = 'Hello ArkUI';
  14. }

  16. build() {
  17. Row({ space: 10 }) {
  18. Text(`${this.label}`)
  19. .makeMeClick(() => {
  20. this.onClickHandler();
  21. })
  22. }
  23. }
  24. }
  ```

  [ExtendFunctionHandle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendFunctionHandle.ets#L29-L54)
* @Extend的参数可以为[状态变量](../../../学习UI范式状态管理/状态管理概述/arkts-state-management-overview.md)，当状态变量改变时，UI可以正常的被刷新渲染。

  ```
  1. @Extend(Text)
  2. function fancy(fontSize: number) {
  3. .fontColor(Color.Blue)
  4. .fontSize(fontSize)
  5. }

  7. @Entry
  8. @Component
  9. struct FancyUse {
  10. @State fontSizeValue: number = 20;

  12. build() {
  13. Column({ space: 10 }) {
  14. Text('Fancy')
  15. .fancy(this.fontSizeValue)
  16. .onClick(() => {
  17. this.fontSizeValue = 30;
  18. })
  19. }
  20. .width('100%')
  21. }
  22. }
  ```

  [ExtendUIStateVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUIStateVariable.ets#L29-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/w9fLDMNPQ5KPa-9ZOrmk-w/zh-cn_image_0000002592217974.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062852Z&HW-CC-Expire=86400&HW-CC-Sign=8A3A42FB5942BA5DC4F44599374928ED27F7DC7C20C38FEF5E5DE67FE638908D)

## 限制条件

* 和@Styles不同，@Extend仅支持在全局定义，不支持在组件内部定义。

说明

仅限在当前文件内使用，不支持导出。

如果要实现export功能，推荐使用[AttributeModifier](<../../../使用自定义能力/Modifier机制/属性修改器 (AttributeModifier)/arkts-user-defined-extension-attributemodifier.md>)。

【反例】

```
1. @Entry
2. @Component
3. struct FancyUse {
4. // 错误写法，@Extend仅支持在全局定义，不支持在组件内部定义
5. @Extend(Text) function fancy (fontSize: number) {
6. .fontSize(fontSize)
7. }

9. build() {
10. Row({ space: 10 }) {
11. Text('Fancy')
12. .fancy(16)
13. }
14. }
15. }
```

【正例】

```
1. // 正确写法
2. @Extend(Text)
3. function fancy(fontSize: number) {
4. .fontSize(fontSize)
5. }

7. @Entry
8. @Component
9. struct FancyUse {
10. build() {
11. Row({ space: 10 }) {
12. Text('Fancy')
13. .fancy(16)
14. }
15. }
16. }
```

[ExtendPositiveExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendPositiveExample.ets#L29-L46)

* @Extend装饰的函数仅限当前文件使用，不支持导出，不支持在其他文件调用。

【反例】

```
1. // 错误写法 不要在pageTwo当中使用在其他文件比如pageOne中定义的@Extend函数
2. // pageOne.ets
3. @Extend(Button)
4. function ButtonUse() {
5. .width(100)
6. .buttonStyle(ButtonStyleMode.NORMAL)
7. }

9. @Entry
10. @Component
11. struct extendUseOne {
12. build() {
13. Row() {
14. Button()
15. .ButtonUse()
16. .height(200)
17. }
18. }
19. }

21. // pageTwo.ets
22. @Entry
23. @Component
24. struct TextUse {
25. build() {
26. Row() {
27. Text('this is TextUse')

29. Button()
30. .ButtonUse()  // 会有编译告警提示: Property 'ButtonUse' does not exist on type 'ButtonAttribute'.
31. .height(50)
32. }
33. }
34. }
```

【正例】

```
1. // 正确写法 在pageTwo文件当中可以定义与pageOne文件中的@Extend函数不重名的@Extend函数
2. // pageOne.ets
3. @Extend(Button)
4. function ButtonUse() {
5. .width(100)
6. .buttonStyle(ButtonStyleMode.NORMAL)
7. }

9. @Entry
10. @Component
11. struct extendUseOne {
12. build() {
13. Row() {
14. Button()
15. .ButtonUse()
16. .height(200)
17. }
18. }
19. }

21. // pageTwo.ets
22. @Extend(Button)
23. function ButtonUse2() {
24. .width(200)
25. .buttonStyle(ButtonStyleMode.EMPHASIZED)
26. }

28. @Entry
29. @Component
30. struct TextUse {
31. build() {
32. Row() {
33. Text('this is TextUse')

35. Button()
36. .ButtonUse2()
37. .height(50)
38. }
39. }
40. }
```

## 使用场景

以下示例声明了3个Text组件，每个Text组件均设置了[fontStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#fontstyle)、[fontWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#fontweight) 和[backgroundColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundcolor)样式。

```
1. @Entry
2. @Component
3. struct FancyUse {
4. @State label: string = 'Hello World';

6. build() {
7. Row({ space: 10 }) {
8. Text(`${this.label}`)
9. .fontStyle(FontStyle.Italic)
10. .fontWeight(500)
11. .backgroundColor(Color.Yellow)
12. Text(`${this.label}`)
13. .fontStyle(FontStyle.Italic)
14. .fontWeight(600)
15. .backgroundColor(Color.Pink)
16. Text(`${this.label}`)
17. .fontStyle(FontStyle.Italic)
18. .fontWeight(700)
19. .backgroundColor(Color.Orange)
20. }.margin('20%')
21. }
22. }
```

[ExtendUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenario.ets#L29-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/_nmWA3bMRNidzIv-VXwZxA/zh-cn_image_0000002592377908.png?HW-CC-KV=V1&HW-CC-Date=20260611T062852Z&HW-CC-Expire=86400&HW-CC-Sign=1043FD4D87090DCA5B20E7F20EF7EF7088A41AE6C0BAE27D4B317C961D26ED3E)

使用@Extend将样式组合复用，示例如下。

```
1. @Extend(Text)
2. function fancyText(weightValue: number, color: Color) {
3. .fontStyle(FontStyle.Italic)
4. .fontWeight(weightValue)
5. .backgroundColor(color)
6. }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L29-L36)

通过@Extend组合样式后，使得代码更加简洁，增强可读性。

```
1. @Entry
2. @Component
3. struct FancyUse {
4. @State label: string = 'Hello World';

6. build() {
7. Row({ space: 10 }) {
8. Text(`${this.label}`)
9. .fancyText(100, Color.Blue)
10. Text(`${this.label}`)
11. .fancyText(200, Color.Pink)
12. Text(`${this.label}`)
13. .fancyText(300, Color.Orange)
14. }.margin('20%')
15. }
16. }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L37-L54)
