---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-dynamiclayout
title: 动态布局 (DynamicLayout)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 动态布局 (DynamicLayout)
category: harmonyos-guides
scraped_at: 2026-06-11T14:30:25+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:c6430c4e2cf7d526431cf08bbe6e2fe2a2f4cb149b9562edfddef9d724bcf08c
---
## 概述

从API version 24开始，支持动态布局容器组件[DynamicLayout](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/动态布局/DynamicLayout/ts-container-dynamiclayout.md)。DynamicLayout支持在运行时动态切换不同的布局算法，同时保持子组件的状态不变。通过DynamicLayout，开发者可以灵活实现同一种内容在不同场景下的多种布局展示。DynamicLayout组件支持的布局算法类包括[RowLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#rowlayoutalgorithm>)、[ColumnLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#columnlayoutalgorithm>)、[StackLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#stacklayoutalgorithm>)、[GridLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#gridlayoutalgorithm>)和自定义布局算法类[CustomLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#customlayoutalgorithm>)。

## 约束与限制

1. 布局算法类使用[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰，不支持[@State](../../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md)装饰器。
2. 切换布局算法时，子组件的状态（如输入框内容、滚动位置等）保持不变。
3. 在自定义布局算法的[onMeasure](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onmeasure>)和[onLayout](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onlayout>)方法中不允许修改状态变量，避免不可预期的行为。

## 创建DynamicLayout

通过传入[LayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#layoutalgorithm-1>)类型入参，创建[DynamicLayout](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/动态布局/DynamicLayout/ts-container-dynamiclayout.md#接口)组件并设置布局算法。[LayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#layoutalgorithm-1>)类型变量支持赋值具体的布局算法类对象，包括[内置布局算法](arkts-layout-development-dynamiclayout.md#内置布局算法)和[自定义布局算法](arkts-layout-development-dynamiclayout.md#自定义布局算法)。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute,RowLayoutAlgorithm, ColumnLayoutAlgorithm, LayoutAlgorithm
3. } from '@kit.ArkUI';

5. @Entry
6. @ComponentV2
7. struct CreateDynamicLayout {
8. @Local algorithm: LayoutAlgorithm = new RowLayoutAlgorithm();

10. build() {
11. Column({ space: 10 }) {
12. DynamicLayout(this.algorithm) {
13. Text('Item 1')
14. .fontSize(16)
15. .backgroundColor(0xF5DEB3)
16. .padding(10)
17. Text('Item 2')
18. .fontSize(16)
19. .backgroundColor(0xD2B48C)
20. .padding(10)
21. Text('Item 3')
22. .fontSize(16)
23. .backgroundColor(0xF5DEB3)
24. .padding(10)
25. }
26. .width('100%')
27. .height(150)
28. .backgroundColor(0xEFEFEF)

30. Button('切换为Column布局')
31. .fontSize(16)
32. .onClick(() => {
33. this.algorithm = new ColumnLayoutAlgorithm();
34. })
35. }
36. .width('100%')
37. .padding(20)
38. }
39. }
```

[CreateDynamicLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/basic/CreateDynamicLayout.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/NhsOSi1XT7eZjtAZWB5BQQ/zh-cn_image_0000002592218138.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=8BE4DD8F7E720CD8CEC3836BEA697E50C17F9713AF396CD662E633BFDAE8B65C)

## 内置布局算法

线性布局算法[RowLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#rowlayoutalgorithm>)和[ColumnLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#columnlayoutalgorithm>)具有自适应拉伸、缩放的能力，可以用于界面元素自适应布局的场景。堆叠布局算法[StackLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#stacklayoutalgorithm>)具有较强的页面层叠、位置定位能力，可以用于广告、卡片层叠等页面场景。网格布局算法[GridLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#gridlayoutalgorithm>)具有较好的规律结构，适合展示同类项目集合，例如显示图片、视频、音乐、新闻、商品等。

### RowLayoutAlgorithm

[RowLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#rowlayoutalgorithm>)是水平方向线性布局算法，子组件沿水平方向依次排列。该算法支持设置子组件间距、子组件在主轴（水平方向）上的对齐方式、在交叉轴（垂直方向）上的对齐方式，以及是否反转子组件的排列方向。该布局算法与[Row](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)组件布局效果一致，详细效果说明请参考[线性布局（Row/Column）](<../线性布局 (RowColumn)/arkts-layout-development-linear.md>)。下述示例通过修改RowLayoutAlgorithm对象的space、justifyContent、alignItems和isReverse成员变量，调整子组件间距、主轴（水平方向）对齐方式、交叉轴（竖直方向）对齐方式和排列方向。

从API version 24开始，新增[RowLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#rowlayoutalgorithm>)的[space](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性>)、[justifyContent](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性>)、[alignItems](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性>)、[isReverse](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性>)属性。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, RowLayoutAlgorithm, LengthMetrics
3. } from '@kit.ArkUI';

5. @Entry
6. @ComponentV2
7. struct RowLayoutExample {
8. @Local algorithm: RowLayoutAlgorithm = new RowLayoutAlgorithm({
9. space: LengthMetrics.vp(10),
10. alignItems: VerticalAlign.Top,
11. justifyContent: FlexAlign.Start,
12. isReverse: false
13. });

15. build() {
16. Column({ space: 10 }) {
17. DynamicLayout(this.algorithm) {
18. Text('Item 1')
19. .width(80)
20. .height(40)
21. .fontSize(14)
22. .backgroundColor(0xF5DEB3)
23. Text('Item 2')
24. .width(80)
25. .height(40)
26. .fontSize(14)
27. .backgroundColor(0xD2B48C)
28. Text('Item 3')
29. .width(80)
30. .height(40)
31. .fontSize(14)
32. .backgroundColor(0xF5DEB3)
33. }
34. .width('100%')
35. .height(80)
36. .backgroundColor(0xEFEFEF)

38. Row({ space: 10 }) {
39. Button('修改间距')
40. .fontSize(14)
41. .onClick(() => {
42. this.algorithm.space = LengthMetrics.vp(20);
43. })
44. Button('反转排列')
45. .fontSize(14)
46. .onClick(() => {
47. this.algorithm.isReverse = !this.algorithm.isReverse;
48. })
49. }

51. Row({ space: 10 }) {
52. Button('竖直居中')
53. .fontSize(14)
54. .onClick(() => {
55. this.algorithm.alignItems = VerticalAlign.Center;
56. })
57. Button('水平居中')
58. .fontSize(14)
59. .onClick(() => {
60. this.algorithm.justifyContent = FlexAlign.Center;
61. })
62. }
63. }
64. .padding(20)
65. }
66. }
```

[RowLayoutAlgorithm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/linearlayout/RowLayoutAlgorithm.ets#L16-L83)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/y4wfP_sSR4qT9t88eNv-ug/zh-cn_image_0000002592378072.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=D3631AD76373FFC9085295CEF8E13FFBA7B575136AA2F01191DA3D43C89A32D6)

### ColumnLayoutAlgorithm

[ColumnLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#columnlayoutalgorithm>)是垂直方向线性布局算法，子组件沿垂直方向依次排列。该算法支持设置子组件间距、子组件在主轴（垂直方向）上的对齐方式、在交叉轴（水平方向）上的对齐方式，以及是否反转子组件的排列方向。该布局算法与[Column](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md)组件布局效果一致，详细效果说明请参考[线性布局（Row/Column）](<../线性布局 (RowColumn)/arkts-layout-development-linear.md>)。下述示例通过修改ColumnLayoutAlgorithm的space、justifyContent、alignItems和isReverse属性，调整子组件间距、主轴（竖直方向）对齐方式、交叉轴（水平方向）对齐方式和排列方向。

从API version 24开始，新增[ColumnLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#columnlayoutalgorithm>)的[space](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-1>)、[justifyContent](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-1>)、[alignItems](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-1>)、[isReverse](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-1>)属性。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, ColumnLayoutAlgorithm, LengthMetrics
3. } from '@kit.ArkUI';

5. @Entry
6. @ComponentV2
7. struct ColumnLayoutExample {
8. @Local algorithm: ColumnLayoutAlgorithm = new ColumnLayoutAlgorithm({
9. space: LengthMetrics.vp(10),
10. alignItems: HorizontalAlign.Start,
11. justifyContent: FlexAlign.Start,
12. isReverse: false
13. });

15. build() {
16. Column({ space: 10 }) {
17. DynamicLayout(this.algorithm) {
18. Text('Item 1')
19. .width('80%')
20. .height(40)
21. .fontSize(14)
22. .backgroundColor(0xF5DEB3)
23. Text('Item 2')
24. .width('80%')
25. .height(40)
26. .fontSize(14)
27. .backgroundColor(0xD2B48C)
28. Text('Item 3')
29. .width('80%')
30. .height(40)
31. .fontSize(14)
32. .backgroundColor(0xF5DEB3)
33. }
34. .width('100%')
35. .height(200)
36. .backgroundColor(0xEFEFEF)

38. Row({ space: 10 }) {
39. Button('修改间距')
40. .fontSize(14)
41. .onClick(() => {
42. this.algorithm.space = LengthMetrics.vp(20);
43. })
44. Button('反转排列')
45. .fontSize(14)
46. .onClick(() => {
47. this.algorithm.isReverse = !this.algorithm.isReverse;
48. })
49. }

51. Row({ space: 10 }) {
52. Button('竖直居中')
53. .fontSize(14)
54. .onClick(() => {
55. this.algorithm.justifyContent = FlexAlign.Center;
56. })
57. Button('水平居中')
58. .fontSize(14)
59. .onClick(() => {
60. this.algorithm.alignItems = HorizontalAlign.Center;
61. })
62. }
63. }
64. .padding(20)
65. }
66. }
```

[ColumnLayoutAlgorithm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/linearlayout/ColumnLayoutAlgorithm.ets#L16-L83)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/EhHJ1qm2QAK1kLPNP0aGlg/zh-cn_image_0000002622857579.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=F0158117762C6AC633E43C4A99D0660F36E56ECDFA411032480901EDA015051A)

### StackLayoutAlgorithm

[StackLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#stacklayoutalgorithm>)是堆叠布局算法，子组件堆叠排列，后添加的子组件覆盖先添加的子组件。该算法支持通过alignContent设置子组件在容器中的九宫格对齐位置，子组件可以通过[layoutGravity](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#layoutgravity20)属性单独设置自己的对齐方式，优先级高于容器的alignContent。该布局算法与[Stack](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Stack/ts-container-stack.md)组件布局效果一致，详细效果说明请参考[堆叠布局](<../层叠布局 (Stack)/arkts-layout-development-stack-layout.md>)。下述示例通过修改[StackLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#stacklayoutalgorithm>)的[alignContent](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-2>)属性，调整子组件在容器中的九宫格对齐位置。

从API version 24开始，新增[StackLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#stacklayoutalgorithm>)的[alignContent](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-2>)属性。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, StackLayoutAlgorithm
3. } from '@kit.ArkUI';

5. @Entry
6. @ComponentV2
7. struct StackLayoutExample {
8. @Local algorithm: StackLayoutAlgorithm = new StackLayoutAlgorithm({
9. alignContent: LocalizedAlignment.CENTER
10. });

12. build() {
13. Column() {
14. DynamicLayout(this.algorithm) {
15. Text('第一层')
16. .fontSize(14)
17. .width(150)
18. .height(150)
19. .backgroundColor(0xD2B48C)
20. .layoutGravity(LocalizedAlignment.TOP_START)

22. Text('第二层')
23. .fontSize(14)
24. .width(150)
25. .height(150)
26. .backgroundColor(0xF5DEB3)
27. .layoutGravity(LocalizedAlignment.CENTER)

29. Text('第三层')
30. .fontSize(14)
31. .width(100)
32. .height(100)
33. .backgroundColor(0x8B4513)
34. }
35. .width(250)
36. .height(250)
37. .backgroundColor(0xEFEFEF)

39. Row({ space: 10 }) {
40. Button('顶部居中')
41. .fontSize(14)
42. .onClick(() => {
43. this.algorithm.alignContent = LocalizedAlignment.TOP;
44. })
45. Button('居中对齐')
46. .fontSize(14)
47. .onClick(() => {
48. this.algorithm.alignContent = LocalizedAlignment.CENTER;
49. })
50. Button('底部居中')
51. .fontSize(14)
52. .onClick(() => {
53. this.algorithm.alignContent = LocalizedAlignment.BOTTOM;
54. })
55. }
56. .margin({ top: 20 })
57. }
58. .width('100%')
59. }
60. }
```

[StackLayoutAlgorithm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/stacklayout/StackLayoutAlgorithm.ets#L16-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/bPVWiSNQS3uXRZU077xA_A/zh-cn_image_0000002622697701.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=33B749471F2204A7872DF593E96C8F6C6E017F0EF5F8F5B1A346C40EB42AF1A1)

### GridLayoutAlgorithm

[GridLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#gridlayoutalgorithm>)是垂直方向网格布局算法。该算法支持通过[columnsTemplate](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/LazyVGridLayout/ts-container-lazyvgridlayout.md#columnstemplate)或[ItemFillPolicy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#itemfillpolicy22)设置列数，设置[ItemFillPolicy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#itemfillpolicy22)为BREAKPOINT\_DEFAULT时行为与[Grid](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)一致，行数由子节点数量和列数决定。该算法支持通过[LengthMetrics](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>)设置行间距和列间距，通过[align](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#align20)设置组件在网格中的对齐方式。下述示例修改GridLayoutAlgorithm的columnsTemplate属性调整网格列数。

从API version 24开始，新增[GridLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#gridlayoutalgorithm>)的[columnsTemplate](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#属性-3>)属性。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, GridLayoutAlgorithm, LengthMetrics
3. } from '@kit.ArkUI';

5. export class GridDataSource implements IDataSource {
6. private list: string[] = [];
7. private listeners: DataChangeListener[] = [];

9. constructor(list: string[]) {
10. this.list = list;
11. }

13. totalCount(): number {
14. return this.list.length;
15. }

17. getData(index: number): string {
18. return this.list[index];
19. }

21. registerDataChangeListener(listener: DataChangeListener): void {
22. if (this.listeners.indexOf(listener) < 0) {
23. this.listeners.push(listener);
24. }
25. }

27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. this.listeners.splice(pos, 1);
31. }
32. }

34. // 通知控制器数据位置变化
35. notifyDataMove(from: number, to: number): void {
36. this.listeners.forEach(listener => {
37. listener.onDataMove(from, to);
38. })
39. }

41. // 交换元素位置
42. public swapItem(from: number, to: number): void {
43. let temp: string = this.list[from];
44. this.list[from] = this.list[to];
45. this.list[to] = temp;
46. this.notifyDataMove(from, to);
47. }
48. }

50. @Entry
51. @ComponentV2
52. struct GridLayoutExample {
53. numbers: GridDataSource = new GridDataSource([]);
54. @Local flag: boolean = false
55. @Local gridLayoutAlgorithm: GridLayoutAlgorithm = new GridLayoutAlgorithm({
56. columnsTemplate: '1fr 1fr 1fr',
57. columnsGap: LengthMetrics.vp(10),
58. rowsGap: LengthMetrics.vp(10)
59. })

61. aboutToAppear() {
62. let list: string[] = [];
63. for (let i = 0; i < 4; i++) {
64. for (let j = 0; j < 3; j++) {
65. list.push((i * 3 + j).toString());
66. }
67. }
68. this.numbers = new GridDataSource(list);
69. }

71. build() {
72. Column({ space: 10 }) {
73. DynamicLayout(this.gridLayoutAlgorithm) {
74. LazyForEach(this.numbers, (day: string) => {
75. GridItem() {
76. Text(day)
77. .fontSize(16)
78. .backgroundColor(0xF9CF93)
79. .width('100%')
80. .height(80)
81. .textAlign(TextAlign.Center)
82. }
83. }, (index: number) => index.toString())
84. }.width('100%')
85. Button('change gridLayoutAlgorithm columns').onClick(() => {
86. this.flag = !this.flag
87. if (this.flag) {
88. this.gridLayoutAlgorithm.columnsTemplate = '1fr 1fr'
89. } else {
90. this.gridLayoutAlgorithm.columnsTemplate = '1fr 1fr 1fr'
91. }
92. })
93. }
94. }
95. }
```

[GridLayoutAlgorithm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/gridlayout/GridLayoutAlgorithm.ets#L16-L112)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/9I-pxd60Td648Sr5sTgRMQ/zh-cn_image_0000002592218140.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=E86F3C29896A4EF68B58DA6F567471C11F8F278BA1B6B58F335207E69314437C)

## 自定义布局算法

自定义布局算法通过继承[CustomLayoutAlgorithm](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#customlayoutalgorithm>)类，重写[onMeasure](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onmeasure>)和[onLayout](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onlayout>)方法实现。开发者可以根据具体业务需求，自定义子组件的大小测量和位置排列，实现内置布局算法无法满足的个性化布局效果，如瀑布流、标签云等不规则布局。

### 自定义布局算法实现指导

通过调用[FrameNode](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#framenode-1>)的[getChildrenCount()](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#getchildrencount12>)和[getChild()](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#getchild12>)方法，开发者可以获取所有子组件FrameNode。在onMeasure方法中，调用[measure()](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#measure12>)方法可以自定义测量子组件大小。在onLayout方法中，调用[getMeasuredSize()](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#getmeasuredsize12>)可以获取子组件测量后的尺寸，调用[layout()](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#layout12>)方法可以自定义排列子组件位置。下述示例展示如何重写[onMeasure](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onmeasure>)和[onLayout](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/LayoutAlgorithm/js-apis-arkui-layoutalgorithm.md#onlayout>)方法，调用[FrameNode](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#framenode-1>)的相关方法实现水平方向线性布局的效果。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, CustomLayoutAlgorithm, FrameNode, LayoutConstraint, Position, LayoutAlgorithm
3. } from '@kit.ArkUI';

5. // 自定义布局算法类
6. class MyCustomLayout extends CustomLayoutAlgorithm {
7. onMeasure(self: FrameNode, constraint: LayoutConstraint): void {
8. // 1. 获取子组件数量
9. const childCount = self.getChildrenCount();
10. let totalWidth = 0;
11. let maxHeight = 0;
12. // 2. 遍历子组件，进行测量
13. for (let i = 0; i < childCount; i++) {
14. const child = self.getChild(i);
15. if (child) {
16. // 3. 创建子组件的布局约束
17. const childConstraint: LayoutConstraint = {
18. maxSize: { width: 150, height: 150},
19. minSize: { width: 150, height: 150},
20. percentReference: constraint.percentReference
21. };
22. // 4. 测量子组件
23. child.measure(childConstraint);
24. // 5. 获取子组件测量后的尺寸
25. const childSize = child.getMeasuredSize();
26. totalWidth += childSize.width;
27. maxHeight = Math.max(maxHeight, childSize.height);
28. }
29. }
30. const measuredSize: Size = {
31. width: Math.min(totalWidth, constraint.maxSize.width),
32. height: Math.min(maxHeight, constraint.maxSize.height)
33. };
34. // 6. 设置自身的测量尺寸
35. self.setMeasuredSize(measuredSize);
36. }

38. onLayout(self: FrameNode, position: Position): void {
39. // 1. 获取子组件数量
40. const childCount = self.getChildrenCount();
41. let offsetX = 0;
42. // 2. 遍历子组件，设置布局位置
43. for (let i = 0; i < childCount; i++) {
44. const child = self.getChild(i);
45. if (child) {
46. // 3. 获取子组件测量后的尺寸
47. const childSize = child.getMeasuredSize();
48. const childPosition: Position = {
49. x: offsetX,
50. y: 0
51. };
52. // 4. 设置子组件的布局位置
53. child.layout(childPosition);
54. // 5. 更新偏移量
55. offsetX += childSize.width;
56. }
57. }
58. // 6. 设置自身的布局位置
59. self.setLayoutPosition(position);
60. }
61. }

63. @Entry
64. @ComponentV2
65. struct CustomLayoutBasic {
66. @Local algorithm: LayoutAlgorithm = new MyCustomLayout()
67. build() {
68. Column({ space: 10 }) {
69. DynamicLayout(this.algorithm) {
70. Text('Item 1')
71. .fontSize(14)
72. .backgroundColor(0xF5DEB3)
73. Text('Item 2')
74. .fontSize(14)
75. .backgroundColor(0xD2B48C)
76. Text('Item 3')
77. .fontSize(14)
78. .backgroundColor(0xF5DEB3)
79. Text('Item 4')
80. .fontSize(14)
81. .backgroundColor(0xD2B48C)
82. }
83. .width('100%')
84. .height(200)
85. .backgroundColor(0xEFEFEF)
86. }
87. .padding(20)
88. }
89. }
```

[CustomLayoutBasic.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/customlayout/CustomLayoutBasic.ets#L16-L106)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/MjnrjAoURw-E0uahDRbn8g/zh-cn_image_0000002592378074.png?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=ABC249F1FDCCCF9F6D5AEE7FD936436246BCFECF769F30EFBBDFD8EA1619B0CA)

### 瀑布流布局

下述示例实现了自定义瀑布流布局算法，将子组件按列排列，每列中的子组件依次堆叠，适用于商品展示的场景。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, CustomLayoutAlgorithm, LayoutAlgorithm, FrameNode, LayoutConstraint, Position
3. } from '@kit.ArkUI';

5. // 瀑布流布局算法
6. class WaterfallLayout extends CustomLayoutAlgorithm {
7. private columnCount: number = 2;
8. private columnGap: number = 10;
9. private rowGap: number = 10;

11. onMeasure(self: FrameNode, constraint: LayoutConstraint): void {
12. const childCount = self.getChildrenCount();
13. const columnWidth = (constraint.maxSize.width - (this.columnCount - 1) * this.columnGap) / this.columnCount;
14. // 记录每列的当前高度
15. const columnHeights: number[] = new Array(this.columnCount).fill(0);
16. for (let i = 0; i < childCount; i++) {
17. const child = self.getChild(i);
18. if (child) {
19. // 通过将minSize和maxSize设置为相同值来约束子组件宽度
20. const childConstraint: LayoutConstraint = {
21. maxSize: {
22. width: columnWidth,
23. height: constraint.maxSize.height
24. },
25. minSize: {
26. width: columnWidth,
27. height: 0
28. },
29. percentReference: constraint.percentReference
30. };
31. child.measure(childConstraint);
32. // 找到当前高度最小的列
33. const minColumn = columnHeights.indexOf(Math.min(...columnHeights));
34. columnHeights[minColumn] += child.getMeasuredSize().height + this.rowGap;
35. }
36. }
37. const maxHeight = Math.max(...columnHeights);
38. self.setMeasuredSize({
39. width: constraint.maxSize.width,
40. height: maxHeight
41. });
42. }

44. onLayout(self: FrameNode, position: Position): void {
45. const childCount = self.getChildrenCount();
46. const measuredSize = self.getMeasuredSize();
47. const columnWidth = (measuredSize.width - (this.columnCount - 1) * this.columnGap) / this.columnCount;
48. // 记录每列的当前Y坐标
49. const columnYs: number[] = new Array(this.columnCount).fill(0);
50. for (let i = 0; i < childCount; i++) {
51. const child = self.getChild(i);
52. if (child) {
53. const childSize = child.getMeasuredSize();
54. // 找到当前Y坐标最小的列
55. const minColumn = columnYs.indexOf(Math.min(...columnYs));
56. const x = minColumn * (columnWidth + this.columnGap);
57. const y = columnYs[minColumn];
58. child.layout({ x, y });
59. columnYs[minColumn] += childSize.height + this.rowGap;
60. }
61. }
62. self.setLayoutPosition(position);
63. }
64. }

66. @Entry
67. @ComponentV2
68. struct WaterfallLayoutExample {
69. @Local algorithm: LayoutAlgorithm = new WaterfallLayout();

71. // 商品数据
72. private products: Product[] = [
73. { id: '1', name: '时尚运动鞋', price: '¥399', height: 180, image: '商品图' },
74. { id: '2', name: '休闲双肩包', price: '¥259', height: 220, image: '商品图' },
75. { id: '3', name: '无线蓝牙耳机', price: '¥599', height: 150, image: '商品图' },
76. { id: '4', name: '智能手表', price: '¥1299', height: 200, image: '商品图' },
77. { id: '5', name: '太阳眼镜', price: '¥199', height: 130, image: '商品图' },
78. { id: '6', name: '便携充电宝', price: '¥129', height: 170, image: '商品图' },
79. { id: '7', name: '机械键盘', price: '¥459', height: 160, image: '商品图' },
80. { id: '8', name: '游戏鼠标', price: '¥189', height: 140, image: '商品图' },
81. { id: '9', name: '高清显示器', price: '¥1599', height: 210, image: '商品图' },
82. { id: '10', name: '智能音箱', price: '¥299', height: 190, image: '商品图' }
83. ];

85. // 商品卡片组件
86. @Builder ProductCard(product: Product) {
87. Column() {
88. Text(product.image)
89. .fontSize(18)
90. .margin({ bottom: 8 })
91. Text(product.name)
92. .fontSize(14)
93. .fontWeight(FontWeight.Medium)
94. .fontColor(0x333333)
95. .margin({ bottom: 4 })
96. .maxLines(1)
97. .textOverflow({ overflow: TextOverflow.Ellipsis })
98. Text(product.price)
99. .fontSize(16)
100. .fontColor(0xFF6B35)
101. .fontWeight(FontWeight.Bold)
102. }
103. .width('100%')
104. .padding(12)
105. .backgroundColor(0xFAFAFA)
106. .borderRadius(8)
107. .border({ width: 1, color: 0xE0E0E0 })
108. .height(product.height)
109. .justifyContent(FlexAlign.Center)
110. }

112. build() {
113. Column() {
114. Text('商品列表 - 瀑布流布局')
115. .fontSize(18)
116. .fontWeight(FontWeight.Bold)
117. .margin({ bottom: 20 })

119. Scroll() {
120. DynamicLayout(this.algorithm) {
121. ForEach(this.products, (product: Product) => {
122. this.ProductCard(product)
123. })
124. }
125. .width('100%')
126. .backgroundColor(0xEFEFEF)
127. .borderRadius(12)
128. .padding(10)
129. }
130. .scrollable(ScrollDirection.Vertical)
131. .scrollBar(BarState.Auto)
132. .edgeEffect(EdgeEffect.Spring)
133. .width('100%')
134. .layoutWeight(1)

136. Text('商品卡片自动分配到高度最小的列')
137. .fontSize(14)
138. .fontColor(Color.Gray)
139. .margin({ top: 12 })
140. }
141. .padding(20)
142. .width('100%')
143. .height('100%')
144. }
145. }

147. // 商品数据模型
148. interface Product {
149. id: string;
150. name: string;
151. price: string;
152. height: number;
153. image: string;
154. }
```

[WaterFlowLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/customlayout/WaterFlowLayout.ets#L16-L171)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/3rBrmLhyTFGY8IkCMz_joA/zh-cn_image_0000002622857581.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=23F21CF5A99FDC5D689AF4618BBBF2BA7B4AECA1797F6C0631BC9AC96A636A34)

### 网格布局

下述示例实现一个自定义网格布局算法，将子组件按网格排列，同一行的子组件高度保持一致。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, CustomLayoutAlgorithm, LayoutAlgorithm, FrameNode, LayoutConstraint, Position
3. } from '@kit.ArkUI';

5. // 2x2网格布局算法
6. export class GridLayout extends CustomLayoutAlgorithm {
7. private gap: number = 12;
8. private itemHeights: number[] = [];

10. onMeasure(self: FrameNode, constraint: LayoutConstraint): void {
11. const childCount = self.getChildrenCount();
12. const columns = 2;
13. const itemWidth = (constraint.maxSize.width - (columns - 1) * this.gap) / columns;
14. this.itemHeights = [];

16. // 第一遍测量：获取每个子组件的理想高度
17. for (let i = 0; i < childCount; i++) {
18. const child = self.getChild(i);
19. if (child) {
20. const childConstraint: LayoutConstraint = {
21. maxSize: { width: itemWidth, height: Number.MAX_VALUE },
22. minSize: { width: itemWidth, height: 0 },
23. percentReference: constraint.percentReference
24. };
25. child.measure(childConstraint);
26. this.itemHeights.push(child.getMeasuredSize().height);
27. }
28. }

30. // 计算每行的最大高度
31. const rows = Math.ceil(childCount / columns);
32. const rowHeights: number[] = [];
33. for (let r = 0; r < rows; r++) {
34. let maxRowHeight = 0;
35. for (let c = 0; c < columns; c++) {
36. const index = r * columns + c;
37. if (index < this.itemHeights.length && this.itemHeights[index] > maxRowHeight) {
38. maxRowHeight = this.itemHeights[index];
39. }
40. }
41. rowHeights.push(maxRowHeight);
42. }

44. // 计算总高度
45. const totalHeight = rowHeights.reduce((sum, h) => sum + h, 0) + (rows - 1) * this.gap;

47. // 第二遍测量：使用每行的统一高度重新测量子组件
48. for (let i = 0; i < childCount; i++) {
49. const child = self.getChild(i);
50. if (child) {
51. const row = Math.floor(i / columns);
52. const rowHeight = rowHeights[row];
53. const childConstraint: LayoutConstraint = {
54. maxSize: { width: itemWidth, height: rowHeight },
55. minSize: { width: itemWidth, height: rowHeight },
56. percentReference: constraint.percentReference
57. };
58. child.measure(childConstraint);
59. }
60. }

62. self.setMeasuredSize({
63. width: constraint.maxSize.width,
64. height: totalHeight
65. });
66. }

68. onLayout(self: FrameNode, position: Position): void {
69. const childCount = self.getChildrenCount();
70. const measuredSize = self.getMeasuredSize();
71. const columns = 2;
72. const itemWidth = (measuredSize.width - (columns - 1) * this.gap) / columns;

74. // 重新计算每行的最大高度
75. const rows = Math.ceil(childCount / columns);
76. const rowHeights: number[] = [];
77. for (let r = 0; r < rows; r++) {
78. let maxRowHeight = 0;
79. for (let c = 0; c < columns; c++) {
80. const index = r * columns + c;
81. if (index < this.itemHeights.length && this.itemHeights[index] > maxRowHeight) {
82. maxRowHeight = this.itemHeights[index];
83. }
84. }
85. rowHeights.push(maxRowHeight);
86. }

88. for (let i = 0; i < childCount; i++) {
89. const child = self.getChild(i);
90. if (child) {
91. const row = Math.floor(i / columns);
92. const col = i % columns;
93. const x = col * (itemWidth + this.gap);
94. const y = row === 0 ? 0 : rowHeights.slice(0, row).reduce((sum, h) => sum + h, 0) + row * this.gap;
95. child.layout({ x, y });
96. }
97. }

99. self.setLayoutPosition(position);
100. }
101. }

103. @Entry
104. @ComponentV2
105. struct GridLayoutExample {
106. @Local algorithm: LayoutAlgorithm = new GridLayout();

108. build() {
109. Column() {
110. Text('网格布局示例')
111. .fontSize(18)
112. .margin({ bottom: 20 })

114. DynamicLayout(this.algorithm) {
115. ForEach(['卡片1', '卡片2', '卡片3', '卡片4'], (title: string, index: number) => {
116. Column() {
117. Text(title)
118. .fontSize(16)
119. .fontWeight(FontWeight.Bold)
120. .fontColor(0x333333)
121. .margin({ bottom: 8 })
122. Text('内容区域')
123. .fontSize(12)
124. .fontColor(0x666666)
125. }
126. .width('100%')
127. .padding(12)
128. .backgroundColor(0xFAFAFA)
129. .borderRadius(8)
130. .border({ width: 1, color: 0xE0E0E0 })
131. })
132. }
133. .width('100%')
134. .backgroundColor(0xEFEFEF)
135. .borderRadius(12)
136. .padding(12)

138. Text('同一行的子组件高度保持一致')
139. .fontSize(14)
140. .fontColor(Color.Gray)
141. .margin({ top: 20 })
142. }
143. .padding(20)
144. .width('100%')
145. }
146. }
```

[GridLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/customlayout/GridLayout.ets#L16-L163)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/bIfCsIkmRdCNdhdDz4wMzQ/zh-cn_image_0000002622697703.png?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=1DF871391DCDD299E2C25909C1A4A2073E6BF083950EA5FF85E7AF73087AA7A3)

### 标签云布局

下述示例实现一个自定义标签云布局，标签自动换行排列，适合展示搜索历史、热门标签、技能标签等不规则布局的场景。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, CustomLayoutAlgorithm, LayoutAlgorithm, FrameNode, LayoutConstraint, Position
3. } from '@kit.ArkUI';

5. // 标签云布局算法
6. class TagCloudLayout extends CustomLayoutAlgorithm {
7. private horizontalGap: number = 12;
8. private verticalGap: number = 12;

10. onMeasure(self: FrameNode, constraint: LayoutConstraint): void {
11. const childCount = self.getChildrenCount();
12. const maxWidth = constraint.maxSize.width;

14. let currentLineWidth = 0;
15. let totalHeight = 0;
16. let maxLineWidth = 0;
17. let currentLineHeight = 0;

19. for (let i = 0; i < childCount; i++) {
20. const child = self.getChild(i);
21. if (child) {
22. // 测量子组件，不限制宽高
23. const childConstraint: LayoutConstraint = {
24. maxSize: { width: maxWidth, height: Number.MAX_VALUE },
25. minSize: { width: 0, height: 0 },
26. percentReference: constraint.percentReference
27. };
28. child.measure(childConstraint);
29. const childSize = child.getMeasuredSize();

31. // 检查是否需要换行
32. if (currentLineWidth + childSize.width > maxWidth && currentLineWidth > 0) {
33. // 换行前，累加上一行的高度
34. totalHeight += currentLineHeight + this.verticalGap;
35. currentLineWidth = childSize.width + this.horizontalGap;
36. currentLineHeight = childSize.height;
37. maxLineWidth = Math.max(maxLineWidth, currentLineWidth - this.horizontalGap);
38. } else {
39. // 继续当前行
40. currentLineWidth += childSize.width + this.horizontalGap;
41. currentLineHeight = Math.max(currentLineHeight, childSize.height);
42. maxLineWidth = Math.max(maxLineWidth, currentLineWidth - this.horizontalGap);
43. }
44. }
45. }
46. // 累加最后一行的高度
47. totalHeight += currentLineHeight;

49. self.setMeasuredSize({
50. width: Math.min(maxLineWidth, maxWidth),
51. height: totalHeight
52. });
53. }

55. onLayout(self: FrameNode, position: Position): void {
56. const childCount = self.getChildrenCount();
57. const measuredSize = self.getMeasuredSize();
58. const maxWidth = measuredSize.width;

60. let currentX = 0;
61. let currentY = 0;
62. let currentLineHeight = 0;

64. for (let i = 0; i < childCount; i++) {
65. const child = self.getChild(i);
66. if (child) {
67. const childSize = child.getMeasuredSize();
68. // 检查是否需要换行
69. if (currentX + childSize.width > maxWidth && currentX > 0) {
70. // 换行
71. currentY += currentLineHeight + this.verticalGap;
72. currentX = 0;
73. currentLineHeight = 0;
74. }
75. // 布局子组件
76. child.layout({ x: currentX, y: currentY })
77. // 更新位置
78. currentX += childSize.width + this.horizontalGap;
79. currentLineHeight = Math.max(currentLineHeight, childSize.height);
80. }
81. }
82. self.setLayoutPosition(position);
83. }
84. }

86. @Entry
87. @ComponentV2
88. struct TagCloudExample {
89. @Local algorithm: LayoutAlgorithm = new TagCloudLayout();

91. // 热门标签数据
92. private tags: string[] = [
93. '标签1', '标签标签标签', '标签2', '标签标签', '标签标签标',
94. '标签标签标', '标签标签标签标签', '标签标签', '标签标签',
95. '标签标', '标签标签', '标签标签', '标签标签标签',
96. '标签标', '标签标签', '标签标签', '标签标签标'
97. ];

99. // 标签组件
100. @Builder TagItem(tag: string, index: number) {
101. Text(tag)
102. .fontSize(14)
103. .fontColor([0xFF6B6B, 0x4ECDC4, 0x45B7D1, 0xFFA07A, 0x98D8C8, 0xF7DC6F][index % 6])
104. .padding({ left: 12, right: 12, top: 8, bottom: 8 })
105. .backgroundColor(0xF5F5F5)
106. .borderRadius(16)
107. .border({ width: 1, color: 0xE0E0E0 })
108. }

110. build() {
111. Column() {
112. Text('热门话题 - 标签云布局')
113. .fontSize(18)
114. .fontWeight(FontWeight.Bold)
115. .margin({ bottom: 20 })

117. Scroll() {
118. DynamicLayout(this.algorithm) {
119. ForEach(this.tags, (tag: string, index: number) => {
120. this.TagItem(tag, index)
121. }, (tag: string, index: number) => `${index}_${tag}`)
122. }
123. .width('100%')
124. .padding(16)
125. }
126. .scrollable(ScrollDirection.Vertical)
127. .scrollBar(BarState.Auto)
128. .edgeEffect(EdgeEffect.Spring)
129. .width('100%')

131. Text('标签自动换行，紧凑排列')
132. .fontSize(14)
133. .fontColor(Color.Gray)
134. .margin({ top: 12 })
135. }
136. .padding(20)
137. .width('100%')
138. .height('100%')
139. }
140. }
```

[TagCloudLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/customlayout/TagCloudLayout.ets#L16-L157)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/YA6F_TAZSAyuF5l6EOb7qQ/zh-cn_image_0000002592218142.png?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=F133D5C8B69B6A463A282FBDF0A65783260BA547AF6C4D0134077398DF76FDEF)

## 切换布局算法

DynamicLayout在切换布局算法时会保持子组件的状态不变，比如输入框内容、开关状态、进度条值等。下述示例展示[TextInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#接口)、[Toggle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md#接口)、[Slider](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md#接口)和[CheckBox](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md)组件在布局切换过程中保持状态，同时使用[animateTo](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#animateto>)为布局切换添加平滑的动画效果。

```
1. import {
2. DynamicLayout, DynamicLayoutAttribute, ColumnLayoutAlgorithm, LayoutAlgorithm, curves, LengthMetrics,
3. GridLayoutAlgorithm
4. } from '@kit.ArkUI';

6. @Entry
7. @ComponentV2
8. struct StatePreservationExample {
9. @Local algorithm: LayoutAlgorithm = new ColumnLayoutAlgorithm({
10. space: LengthMetrics.vp(12)
11. });

13. build() {
14. Column() {
15. Text('布局切换状态保持示例')
16. .fontSize(18)
17. .margin({ bottom: 20 })

19. // 使用animateTo为布局切换添加动画效果
20. DynamicLayout(this.algorithm) {
21. // 子组件1：带输入框的卡片
22. Column() {
23. Text('输入框')
24. .fontSize(14)
25. .fontWeight(FontWeight.Bold)
26. .fontColor(0x333333)
27. .margin({ bottom: 8 })
28. TextInput({ placeholder: '请输入' })
29. .width('100%')
30. .height(36)
31. .fontSize(12)
32. }
33. .width('100%')
34. .padding(12)
35. .backgroundColor(0x80F0F0F0)
36. .borderRadius(8)

38. // 子组件2：带开关的卡片
39. Column() {
40. Text('开关')
41. .fontSize(14)
42. .fontWeight(FontWeight.Bold)
43. .fontColor(0x333333)
44. .margin({ bottom: 8 })
45. Toggle({ type: ToggleType.Switch, isOn: true })
46. .selectedColor(0xD4D4D4)
47. .height(26)
48. .width(52)
49. }
50. .width('100%')
51. .padding(12)
52. .backgroundColor(0x80F0F0F0)
53. .borderRadius(8)

55. // 子组件3：带进度条的卡片
56. Column() {
57. Text('进度条')
58. .fontSize(14)
59. .fontWeight(FontWeight.Bold)
60. .fontColor(0x333333)
61. .margin({ bottom: 8 })
62. Slider({ value: 60, min: 0, max: 100 })
63. .width('100%')
64. .trackColor(0xD4D4D4)
65. .selectedColor(0xD4D4D4)
66. .height(36)
67. }
68. .width('100%')
69. .padding(12)
70. .backgroundColor(0x80F0F0F0)
71. .borderRadius(8)

73. // 子组件4：带复选框的卡片
74. Column() {
75. Text('复选框')
76. .fontSize(14)
77. .fontWeight(FontWeight.Bold)
78. .fontColor(0x333333)
79. .margin({ bottom: 8 })
80. Row() {
81. Checkbox({ name: 'check1' })
82. .select(false)
83. .selectedColor(0xD4D4D4)
84. Text('记住密码')
85. .fontSize(12)
86. .fontColor(0x333333)
87. .margin({ left: 8 })
88. }
89. .height(36)
90. }
91. .width('100%')
92. .padding(12)
93. .backgroundColor(0x80F0F0F0)
94. .borderRadius(8)
95. }
96. .width('100%')
97. .borderRadius(12)
98. .padding(12)

100. Row({ space: 10 }) {
101. Button('列表布局')
102. .onClick(() => {
103. this.getUIContext()?.animateTo({ duration: 300, curve: curves.springMotion() }, () => {
104. this.algorithm = new ColumnLayoutAlgorithm({
105. space: LengthMetrics.vp(12)
106. });
107. });
108. })
109. Button('网格布局')
110. .onClick(() => {
111. this.getUIContext()?.animateTo({ duration: 300, curve: curves.springMotion() }, () => {
112. this.algorithm = new GridLayoutAlgorithm({
113. columnsTemplate: '1fr 1fr',
114. columnsGap: LengthMetrics.vp(10),
115. rowsGap: LengthMetrics.vp(10)
116. });
117. });
118. })
119. }
120. .margin({ top: 20 })

122. Text('切换布局后，子组件状态保持不变')
123. .fontSize(14)
124. .fontColor(Color.Gray)
125. .margin({ top: 12 })
126. }
127. .padding(20)
128. .width('100%')
129. }
130. }
```

[ReserveChildState.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/responsivelayout/ReserveChildState.ets#L16-L147)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Xu4D8Y7rQp25uWUBYSQLFQ/zh-cn_image_0000002592378076.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=77837FBB3DBD9572C096F88CB13EEA72CFC236CC933219D531DD30568BFD600A)

DynamicLayout支持以下几种方式触发重新布局：

* 通过状态变量切换布局算法。

  开发者使用@Local装饰器修饰布局算法变量，可以实现运行时动态切换布局。

  ```
  1. import {
  2. DynamicLayout, DynamicLayoutAttribute, RowLayoutAlgorithm, ColumnLayoutAlgorithm,
  3. StackLayoutAlgorithm, GridLayoutAlgorithm, LayoutAlgorithm, LengthMetrics
  4. } from '@kit.ArkUI';

  6. @Entry
  7. @ComponentV2
  8. struct LayoutSwitchExample {
  9. @Local algorithm: LayoutAlgorithm = new RowLayoutAlgorithm({
  10. space: LengthMetrics.vp(10),
  11. alignItems: VerticalAlign.Center
  12. });
  13. @Local childWidth: string = '20%'
  14. @Local childHeight: string = '20%'

  16. build() {
  17. Column() {
  18. // 使用状态变量控制布局算法
  19. DynamicLayout(this.algorithm) {
  20. Text('Item 1')
  21. .width(this.childWidth)
  22. .height(this.childHeight)
  23. .fontSize(14)
  24. .textAlign(TextAlign.Center)
  25. .backgroundColor(0xF5DEB3)
  26. .borderRadius(8)
  27. .layoutGravity(LocalizedAlignment.TOP_START)
  28. Text('Item 2')
  29. .width(this.childWidth)
  30. .height(this.childHeight)
  31. .fontSize(14)
  32. .textAlign(TextAlign.Center)
  33. .backgroundColor(0xF5DEB3)
  34. .borderRadius(8)
  35. .layoutGravity(LocalizedAlignment.TOP_END)
  36. Text('Item 3')
  37. .width(this.childWidth)
  38. .height(this.childHeight)
  39. .fontSize(14)
  40. .textAlign(TextAlign.Center)
  41. .backgroundColor(0xF5DEB3)
  42. .borderRadius(8)
  43. .layoutGravity(LocalizedAlignment.BOTTOM_START)
  44. Text('Item 4')
  45. .width(this.childWidth)
  46. .height(this.childHeight)
  47. .fontSize(14)
  48. .textAlign(TextAlign.Center)
  49. .backgroundColor(0xF5DEB3)
  50. .borderRadius(8)
  51. .layoutGravity(LocalizedAlignment.BOTTOM_END)
  52. }
  53. .width(300)
  54. .height(280)
  55. .backgroundColor(0xEFEFEF)
  56. .borderRadius(12)
  57. .padding(10)

  59. Column({ space: 10 }) {
  60. Row({ space: 10 }) {
  61. Button('Row布局')
  62. .onClick(() => {
  63. this.algorithm = new RowLayoutAlgorithm({
  64. space: LengthMetrics.vp(10),
  65. alignItems: VerticalAlign.Center
  66. });
  67. this.childWidth = '20%'
  68. this.childHeight = '20%'
  69. })
  70. Button('Column布局')
  71. .onClick(() => {
  72. this.algorithm = new ColumnLayoutAlgorithm({
  73. space: LengthMetrics.vp(10),
  74. alignItems: HorizontalAlign.Center
  75. });
  76. this.childWidth = '20%'
  77. this.childHeight = '20%'
  78. })
  79. }
  80. Row({ space: 10 }) {
  81. Button('Stack布局')
  82. .onClick(() => {
  83. this.algorithm = new StackLayoutAlgorithm({
  84. alignContent: LocalizedAlignment.CENTER
  85. });
  86. this.childWidth = '20%'
  87. this.childHeight = '20%'
  88. })
  89. Button('Grid布局')
  90. .onClick(() => {
  91. this.algorithm = new GridLayoutAlgorithm({
  92. columnsTemplate: '1fr 1fr',
  93. rowsGap: LengthMetrics.vp(5),
  94. columnsGap: LengthMetrics.vp(5)
  95. });
  96. this.childWidth = '100%'
  97. this.childHeight = '50%'
  98. })
  99. }
  100. }
  101. .margin({ top: 20 })
  102. }
  103. .padding(20)
  104. }
  105. }
  ```

  [ChangeLayoutAlgorithm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/responsivelayout/ChangeLayoutAlgorithm.ets#L16-L122)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Dt9OYskLS-qMrI69RcZ3Zw/zh-cn_image_0000002622857583.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=AF17DB204E863AF8C64DD9D47555364E4C52E05D61E43AF54F9A90F76FA9CDE2)
* 通过条件运算符切换布局算法。

  开发者可以使用条件运算符，根据状态变量的值选择合适的布局算法。

  ```
  1. import {
  2. DynamicLayout, DynamicLayoutAttribute, RowLayoutAlgorithm, ColumnLayoutAlgorithm, LengthMetrics
  3. } from '@kit.ArkUI';

  5. @Entry
  6. @ComponentV2
  7. struct ConditionalLayoutExample {
  8. @Local isHorizontal: boolean = true;

  10. build() {
  11. Column() {
  12. // 使用三元运算符根据条件选择布局算法
  13. DynamicLayout(
  14. this.isHorizontal
  15. ? new RowLayoutAlgorithm({ space: LengthMetrics.vp(10) })
  16. : new ColumnLayoutAlgorithm({ space: LengthMetrics.vp(10) })
  17. ) {
  18. Text('Item 1')
  19. .width(80)
  20. .height(40)
  21. .fontSize(14)
  22. .backgroundColor(0xF5DEB3)
  23. Text('Item 2')
  24. .width(80)
  25. .height(40)
  26. .fontSize(14)
  27. .backgroundColor(0xD2B48C)
  28. Text('Item 3')
  29. .width(80)
  30. .height(40)
  31. .fontSize(14)
  32. .backgroundColor(0xF5DEB3)
  33. }
  34. .width('100%')
  35. .height(150)
  36. .backgroundColor(0xEFEFEF)

  38. Button('切换方向')
  39. .onClick(() => {
  40. this.isHorizontal = !this.isHorizontal;
  41. })
  42. }
  43. .padding(20)
  44. }
  45. }
  ```

  [ChangeLayoutWithConditionVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/responsivelayout/ChangeLayoutWithConditionVariable.ets#L16-L62)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FPwR0X7bSQiJGOfGCY66Mg/zh-cn_image_0000002622697705.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=AB1A8548D733FA20304B7FE0A8DBD6A99DA58CF6FE5DEC2262B949DCF7CACB8C)
* 通过修改算法属性触发重新布局。

  布局算法类使用[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰，布局算法成员属性使用[@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰，修改属性值可以触发DynamicLayout组件重新布局。

  ```
  1. import {
  2. DynamicLayout, DynamicLayoutAttribute, RowLayoutAlgorithm, LengthMetrics
  3. } from '@kit.ArkUI';

  5. @Entry
  6. @ComponentV2
  7. struct PropertyChangeExample {
  8. @Local algorithm: RowLayoutAlgorithm = new RowLayoutAlgorithm({
  9. space: LengthMetrics.vp(10),
  10. justifyContent: FlexAlign.Start
  11. });

  13. build() {
  14. Column() {
  15. DynamicLayout(this.algorithm) {
  16. Text('Item 1')
  17. .width(60)
  18. .height(40)
  19. .fontSize(14)
  20. .backgroundColor(0xF5DEB3)
  21. Text('Item 2')
  22. .width(60)
  23. .height(40)
  24. .fontSize(14)
  25. .backgroundColor(0xD2B48C)
  26. Text('Item 3')
  27. .width(60)
  28. .height(40)
  29. .fontSize(14)
  30. .backgroundColor(0xF5DEB3)
  31. }
  32. .width('100%')
  33. .height(80)
  34. .backgroundColor(0xEFEFEF)

  36. Row({ space: 10 }) {
  37. Button('增加间距')
  38. .fontSize(14)
  39. .onClick(() => {
  40. // 修改space属性触发重新布局
  41. const currentSpace = this.algorithm.space?.value;
  42. this.algorithm.space = LengthMetrics.vp(currentSpace as number + 5);
  43. })
  44. Button('居中对齐')
  45. .fontSize(14)
  46. .onClick(() => {
  47. // 修改justifyContent属性触发重新布局
  48. this.algorithm.justifyContent = FlexAlign.Center;
  49. })
  50. Button('两端对齐')
  51. .fontSize(14)
  52. .onClick(() => {
  53. this.algorithm.justifyContent = FlexAlign.SpaceBetween;
  54. })
  55. }
  56. .margin({ top: 20 })
  57. }
  58. .padding(20)
  59. }
  60. }
  ```

  [ChangeAlgorithmProperties.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/responsivelayout/ChangeAlgorithmProperties.ets#L16-L77)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/maofitqvTGi7qh_FBEdq5A/zh-cn_image_0000002592218144.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=3CC79671CD4473E894F5C0F5EBDE2B650E7F07FF77B6A715826DDC9722206612)
* 响应式布局算法切换。

  开发者可以结合[mediaquery](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (MediaQuery)/arkts-apis-uicontext-mediaquery.md>)接口监听屏幕方向变化，自动切换商品列表的布局方式。竖屏时使用列表视图（每行一个商品），横屏时使用网格视图（2x2网格布局）。

  ```
  1. import {
  2. DynamicLayout, DynamicLayoutAttribute, ColumnLayoutAlgorithm, LayoutAlgorithm, LengthMetrics, mediaquery,
  3. GridLayoutAlgorithm
  4. } from '@kit.ArkUI';

  6. // 商品数据模型
  7. interface Product {
  8. id: string;
  9. name: string;
  10. price: string;
  11. image: string;
  12. }

  14. @Entry
  15. @ComponentV2
  16. struct ProductListExample {
  17. @Local algorithm: LayoutAlgorithm = new ColumnLayoutAlgorithm({
  18. space: LengthMetrics.vp(12)
  19. });
  20. @Local currentOrientation: string = '竖屏';
  21. // 商品数据
  22. private products: Product[] = [
  23. { id: '1', name: '智能手机 Pro', price: '¥5999', image: '商品' },
  24. { id: '2', name: '无线耳机', price: '¥899', image: '商品' },
  25. { id: '3', name: '智能手表', price: '¥1999', image: '商品' },
  26. { id: '4', name: '平板电脑', price: '¥3999', image: '商品' }
  27. ];

  29. // 监听横屏事件
  30. listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');

  32. // 当满足媒体查询条件时，触发回调
  33. onOrientationChange(mediaQueryResult: mediaquery.MediaQueryResult) {
  34. if (mediaQueryResult.matches) {
  35. // 横屏：使用2x2网格布局
  36. this.algorithm = new GridLayoutAlgorithm({
  37. columnsTemplate: '1fr 1fr',
  38. columnsGap: LengthMetrics.vp(10),
  39. rowsGap: LengthMetrics.vp(10)
  40. });
  41. this.currentOrientation = '横屏';
  42. } else {
  43. // 竖屏：使用列表布局（每行一个商品）
  44. this.algorithm = new ColumnLayoutAlgorithm({
  45. space: LengthMetrics.vp(12)
  46. });
  47. this.currentOrientation = '竖屏';
  48. }
  49. }

  51. aboutToAppear() {
  52. // 绑定回调函数
  53. this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
  54. this.onOrientationChange(mediaQueryResult);
  55. });
  56. }

  58. aboutToDisappear() {
  59. // 解绑listener中注册的回调函数
  60. this.listener.off('change');
  61. }

  63. // 商品卡片组件
  64. @Builder ProductCard(product: Product) {
  65. Row() {
  66. Text(product.image)
  67. .fontSize(20)
  68. .margin({ right: 12 })
  69. Column() {
  70. Text(product.name)
  71. .fontSize(16)
  72. .fontWeight(FontWeight.Medium)
  73. .fontColor(0x333333)
  74. .margin({ bottom: 4 })
  75. Text(product.price)
  76. .fontSize(18)
  77. .fontColor(0xFF6B35)
  78. .fontWeight(FontWeight.Bold)
  79. }
  80. .alignItems(HorizontalAlign.Start)
  81. .layoutWeight(1)
  82. .margin({ right: 12 })
  83. Button('购买')
  84. .fontSize(14)
  85. .height(32)
  86. }
  87. .width('100%')
  88. .padding(16)
  89. .backgroundColor(0xFAFAFA)
  90. .borderRadius(8)
  91. .border({ width: 1, color: 0xE0E0E0 })
  92. }

  94. build() {
  95. Column() {
  96. // 标题栏
  97. Row() {
  98. Text('商品列表')
  99. .fontSize(20)
  100. .fontWeight(FontWeight.Bold)
  101. .fontColor(0x333333)
  102. Blank()
  103. Text(`${this.currentOrientation}`)
  104. .fontSize(12)
  105. .fontColor(0x999999)
  106. .padding({ left: 8, right: 8, top: 4, bottom: 4 })
  107. .backgroundColor(0xF0F0F0)
  108. .borderRadius(4)
  109. }
  110. .width('100%')
  111. .padding({ left: 16, right: 16, top: 12, bottom: 12 })
  112. .backgroundColor(Color.White)

  114. // 商品列表
  115. Scroll() {
  116. DynamicLayout(this.algorithm) {
  117. ForEach(this.products, (product: Product) => {
  118. this.ProductCard(product)
  119. })
  120. }
  121. .width('100%')
  122. .layoutWeight(1)
  123. .padding(12)
  124. }
  125. .layoutWeight(1)
  126. .width('100%')
  127. .backgroundColor(0xF5F5F5)

  129. // 提示信息
  130. Text('旋转设备可查看不同布局效果')
  131. .fontSize(12)
  132. .fontColor(0x999999)
  133. .textAlign(TextAlign.Center)
  134. .padding(12)
  135. .width('100%')
  136. .backgroundColor(Color.White)
  137. }
  138. .width('100%')
  139. .height('100%')
  140. }
  141. }
  ```

  [ChangeLayoutWithMediaQuery.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/DynamicLayout/entry/src/main/ets/pages/responsivelayout/ChangeLayoutWithMediaQuery.ets#L16-L158)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/p7fLV92NSRK1z0j2pBKZeQ/zh-cn_image_0000002592378078.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063023Z&HW-CC-Expire=86400&HW-CC-Sign=C13BBD42B3AF7B97830D9809E528DC6BA0927776EEA13D36453071437E1BBAD6)
