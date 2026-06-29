---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-layout
title: 自定义组件的自定义布局
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件的自定义布局
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:30+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e9187e6ca1152f8a483b074d80d1656ddb938b173f7a99c08add27eee3139eff
---
如果系统提供的布局组件（如[Flex](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)，[Column](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md)，[Row](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)等）无法满足复杂布局需求，或开发者希望自定义计算组件内子组件的大小和位置，建议在自定义组件中使用以下接口：

* [onMeasureSize](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的自定义布局/ts-custom-component-layout.md#onmeasuresize10)：组件每次布局时触发，开发者可以在这个回调中增加自定义组件内子组件的大小的计算逻辑，返回自定义组件的尺寸信息，其执行时间先于onPlaceChildren。
* [onPlaceChildren](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的自定义布局/ts-custom-component-layout.md#onplacechildren10)：组件每次布局时触发，开发者可以在这个回调中增加放置自定义组件内子组件位置的逻辑。

以下示例中，Index页面包含一个实现了自定义布局的自定义组件，且对应自定义组件的子组件通过index页面内的builder方式传入。

而在自定义组件中，调用了onMeasureSize和onPlaceChildren设置子组件大小和放置位置。例如，在本示例中，在onMeasureSize中初始化组件大小size=100，后续的每一个子组件size会加上上一个子组件大小的一半，实现组件大小递增的效果。而在onPlaceChildren中，定义startPos=300，设置每一个子组件的位置为startPos减去子组件自身的高度，所有子组件右下角一致在顶点位置(300, 300)，实现一个从右下角开始展示组件的类Stack组件。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. CustomLayout({ builder: columnChildren })
8. }
9. }
10. }

12. // 通过builder的方式传递多个组件，作为自定义组件的一级子组件（即不包含容器组件，如Column）
13. @Builder
14. function columnChildren() {
15. ForEach([1, 2, 3], (index: number) => { // 暂不支持lazyForEach的写法
16. Text('S' + index)
17. .fontSize(30)
18. .width(100)
19. .height(100)
20. .borderWidth(2)
21. .offset({ x: 10, y: 20 })
22. })
23. }

25. @Component
26. struct CustomLayout {
27. @Builder
28. doNothingBuilder() {
29. };

31. @BuilderParam builder: () => void = this.doNothingBuilder;
32. @State startSize: number = 100;
33. result: SizeResult = {
34. width: 0,
35. height: 0
36. };

38. // 第一步：计算各子组件的大小
39. onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
40. let size = 100;
41. children.forEach((child) => {
42. let result: MeasureResult = child.measure({ minHeight: size, minWidth: size, maxWidth: size, maxHeight: size })
43. size += result.width / 2;
44. })
45. // this.result在该用例中代表自定义组件本身的大小，onMeasureSize方法返回的是组件自身的尺寸。
46. this.result.width = 100;
47. this.result.height = 400;
48. return this.result;
49. }
50. // 第二步：放置各子组件的位置
51. onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
52. let startPos = 300;
53. children.forEach((child) => {
54. let pos = startPos - child.measureResult.height;
55. child.layout({ x: pos, y: pos })
56. })
57. }

59. build() {
60. this.builder()
61. }
62. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ComponentsLayout/entry/src/main/ets/pages/Index.ets#L16-L79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/FxvAXdXhSOOJMsiAKo-LLg/zh-cn_image_0000002622857385.png?HW-CC-KV=V1&HW-CC-Date=20260611T062828Z&HW-CC-Expire=86400&HW-CC-Sign=1AE990AD208F2C6C7940275BC0F346E976CEB1E64E3BFCBC3AD6421F16468FCD)
