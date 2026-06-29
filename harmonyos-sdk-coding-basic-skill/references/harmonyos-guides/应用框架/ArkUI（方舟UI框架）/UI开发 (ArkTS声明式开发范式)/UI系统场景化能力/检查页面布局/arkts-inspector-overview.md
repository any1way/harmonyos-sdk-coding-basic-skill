---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-inspector-overview
title: 检查页面布局
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 检查页面布局
category: harmonyos-guides
scraped_at: 2026-06-11T14:32:55+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:d26c4cc209dd2b0f85bf31f4b9f5ea68f76619b3eb6d9cffee97054331d098c9
---
inspector用于检查页面布局，通过双向定位功能帮助开发者在DevEco Studio中快速定位组件、修改属性和调试组件，以提高开发效率。

ArkUI获取当前显示页面中所有组件的信息，包括组件树的父子结构、尺寸、位置、样式、属性和状态。获取组件树信息后，生成并展示为Inspector组件树。DevEco Studio的使用具体可以参考[Inspector调试能力](../../../UI开发调试调优/UI调优/ui-inspector-profiler.md#inspector调试能力)。

inspector针对UI组件的布局或绘制送显完成，还提供了注册与取消监听函数的C API接口，具体使用可以参考[添加事件监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-add-component-events)。

## 使用约束

1. 不支持动效类组件的控件树实时刷新功能。
2. 支持获取组件的属性和样式，但不支持获取controller和Builder对象。
3. 不支持获取组件的方法、事件。

## UIContext查询组件树和组件信息能力

ArkUI提供@ohos.arkui.UIContext([UIContext](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>))扩展能力，通过[getFilteredInspectorTree](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getfilteredinspectortree12>)获取组件树及组件属性，通过[getFilteredInspectorTreeById](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getfilteredinspectortreebyid12>)获取指定的组件及其子组件的属性。支持设置过滤条件进行查询。

下述示例，展示了getFilteredInspectorTree和getFilteredInspectorTreeById的基本用法。

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct ComponentPage {
7. loopConsole(inspectorStr: string, i: string) {
8. hilog.info(0x0000, `InsTree ${i}| type: ${JSON.parse(inspectorStr).$type}, ID: ${JSON.parse(inspectorStr).$ID}`,
9. 'InsTree');
10. if (JSON.parse(inspectorStr).$children) {
11. i += '-';
12. for (let index = 0; index < JSON.parse(inspectorStr).$children.length; index++) {
13. this.loopConsole(JSON.stringify(JSON.parse(inspectorStr).$children[index]), i);
14. }
15. }
16. }

18. build() {
19. Column() {
20. Text('Hello World')
21. .fontSize(20)
22. .id('TEXT')
23. Button('content').onClick(() => {
24. const uiContext: UIContext = this.getUIContext();
25. let inspectorStr = uiContext.getFilteredInspectorTree(['content']);
26. hilog.info(0x0000,`InsTree : ${inspectorStr}`, 'InsTree');
27. inspectorStr = JSON.stringify(JSON.parse(inspectorStr));
28. this.loopConsole(inspectorStr, '-');
29. })
30. Button('isLayoutInspector').onClick(() => {
31. const uiContext: UIContext = this.getUIContext();
32. let inspectorStr = uiContext.getFilteredInspectorTree(['isLayoutInspector']);
33. hilog.info(0x0000,`InsTree : ${inspectorStr}`, 'InsTree');
34. inspectorStr = JSON.stringify(JSON.parse(inspectorStr).content);
35. this.loopConsole(inspectorStr, '-');
36. })
37. Button('getFilteredInspectorTreeById').onClick(() => {
38. const uiContext: UIContext = this.getUIContext();
39. try {
40. let inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ['id', 'src']);
41. hilog.info(0x0000,`result1: ${inspectorStr}`, 'result1');
42. inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
43. hilog.info(0x0000,`result2: ${inspectorStr}`, 'result2');
44. inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ['src']);
45. inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
46. hilog.info(0x0000,`result3: ${inspectorStr}`, 'result13');
47. } catch (e) {
48. hilog.error(0x0000, `getFilteredInspectorTreeById error: ${e}`, 'error');
49. }
50. })

52. }
53. .width('100%')
54. .height('100%')
55. }
56. }
```

[ComponentPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/checkpage/entry/src/main/ets/pages/ComponentPage.ets#L15-L73)

## 布局回调

通过[@ohos.arkui.inspector (布局回调)](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.inspector (布局回调)/js-apis-arkui-inspector.md>)提供注册组件布局和组件绘制完成的回调通知能力。

下述示例，展示了布局回调的基本用法。

```
1. import { inspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ImageExample {
6. build() {
7. Column() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
9. Row({ space: 5 }) {
10. // 请将$r('app.media.startIcon')替换为实际资源文件
11. Image($r('app.media.startIcon'))
12. .width(110)
13. .height(110)
14. .border({ width: 1 })
15. .id('IMAGE_ID')
16. }
17. .id('ROW_ID')
18. }
19. }.height(320).width(360).padding({ right: 10, top: 10 })
20. }

22. listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID');
23. listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW_ID');

25. aboutToAppear() {
26. let onLayoutComplete: () => void = (): void => {
27. // 补充待实现的功能
28. };
29. let onDrawComplete: () => void = (): void => {
30. // 补充待实现的功能
31. };
32. let onDrawChildrenComplete: () => void = (): void => {
33. // 补充待实现的功能
34. };
35. let funcLayout = onLayoutComplete; // 绑定当前js对象
36. let funcDraw = onDrawComplete; // 绑定当前js对象
37. let funcDrawChildren = onDrawChildrenComplete; // 绑定当前js对象
38. let offFuncLayout = onLayoutComplete; // 绑定当前js对象
39. let offFuncDraw = onDrawComplete; // 绑定当前js对象
40. let offFuncDrawChildren = onDrawChildrenComplete; // 绑定当前js对象

42. this.listenerForImage.on('layout', funcLayout);
43. this.listenerForImage.on('draw', funcDraw);
44. this.listenerForRow.on('drawChildren', funcDrawChildren);

46. // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
47. // this.listenerForImage.off('layout', offFuncLayout)
48. // this.listenerForImage.off('draw', offFuncDraw)
49. // this.listenerForRow.off('drawChildren', offFuncDrawChildren)
50. }
51. }
```

[ImagePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/checkpage/entry/src/main/ets/pages/ImagePage.ets#L15-L67)

## 组件标识属性的扩展能力

通过getInspectorByKey、getInspectorTree、sendEventByKey提供组件标识属性扩展能力，具体如下：

* [getInspectorByKey](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/组件标识/ts-universal-attributes-component-id.md#getinspectorbykey9)，获取指定id的组件的所有属性。
* [getInspectorTree](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/组件标识/ts-universal-attributes-component-id.md#getinspectortree9)，获取组件树及组件属性。
* [sendEventByKey](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/组件标识/ts-universal-attributes-component-id.md#sendeventbykey9)，给指定id的组件发送事件。

下述示例，展示了getInspectorByKey、getInspectorTree和sendEventByKey的基本用法。

```
1. @Entry
2. @Component
3. struct ComponentPage {
4. build() {
5. Column() {
6. Text('Hello World')
7. .fontSize(20)
8. .id('TEXT')
9. .onClick(() => {
10. hilog.info(0x0000,`Text is clicked`, 'isClicked');
11. })
12. Button('getInspectorByKey').onClick(() => {
13. let result = getInspectorByKey('TEXT');
14. hilog.info(0x0000,`result is ${result}`, 'result');
15. })
16. Button('getInspectorTree').onClick(() => {
17. let result = getInspectorTree();
18. hilog.info(0x0000,`result is ${JSON.stringify(result)}`, 'result');
19. })
20. Button('sendEventByKey').onClick(() => {
21. sendEventByKey('TEXT', 10, '');
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

[ComponentPage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/checkpage/entry/src/main/ets/pages/ComponentPage1.ets#L17-L46)
