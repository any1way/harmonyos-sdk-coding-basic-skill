---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-ticket-class
title: 多设备股票类界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备股票类界面
category: best-practices
scraped_at: 2026-06-12T10:10:30+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:6d84c18a8de3a088853eb08325885282e296b0fff85a9de2e55fb44f761da2cb
---
## 概述

本文以当前流行的垂类市场中的股票类应用为典型案例，详细介绍“一多”在实际开发中的应用，主要涵盖自选股和个股详情两个典型页面，展示其在直板机、双折叠、三折叠、阔折叠、平板和电脑六种产品形态上的“一次开发，多端部署”。下文将从UX设计、工程管理、移动端页面、电脑端页面四个角度，介绍“一多”股票类应用在开发过程中的最佳实践。

说明

阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/arkui.md)和[一次开发，多端部署概览](../../../一次开发，多端部署概览/bpta-multi-device-overview.md)相关知识。

## UX设计

股票类应用的目的是让用户更便捷地办理金融业务。常见类型包括银行理财、股票、基金等应用及业务场景，核心场景有数据查看和股票交易等。

股票类应用有以下特点：

* 丰富的信息聚合。
* 图表数据高效展示。
* 便捷高效的交互方式。

此类型的应用在多端设备的使用过程中，要保障用户办理金融业务时的基本体验与功能可用性，也需着力优化大屏幕设备上的交互效率。

以下是股票界面在多设备上的UX设计图。具体断点与对应设备的关系可参考[屏幕类型布局场景](../../界面布局响应式变化/屏幕类型布局场景/bpta-multi-device-screen-layout.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/zgqZJ_CMQq2uekJxUu1WIA/zh-cn_image_0000002579631774.png?HW-CC-KV=V1&HW-CC-Date=20260612T021011Z&HW-CC-Expire=86400&HW-CC-Sign=ADB95B0035EE9C70ED0228EDD5F3A48F5B03E9283AF36E63377E95850B7BCB37 "点击放大")

### 设计指南

金融理财类的多设备响应式设计指南，请参考[金融理财类](https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples6-0000001793536905)。

## 工程管理

### 创建工程

建议开发者参考[多设备工程部署与发布](../../../多设备工程部署与发布/bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建出模板项目工程。然后根据股票类应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

在创建“一多”工程时，开发者会面临工程结构目录的划分问题。考虑到复用性和可维护性，本文以股票类应用为例，提供推荐的参考方案。

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。详细请参见[分层架构设计](../../../../应用架构/分层架构设计/bpta-layered-architecture-design.md)。

股票类应用根据一多推荐的commons、features、products的"三层工程架构"划分目录。其中，features（基础特性层）按业务功能划分为三个独立模块：股票交易-stockdeal（包含买入弹窗、K线图表、交易详情等组件）、股票详情-stockdetail（包含股票详情页、多窗口入口、信息表格等）以及股票市场-stockmarket（包含市场列表组件）。公共常量、媒体播放工具以及窗口管理工具等需要被不同页面依赖引用的内容，划分为一个commons（公共能力层）：基础能力-base。products（产品定制层）包含default和pc两个模块定制了程序标准启动流程和多场景协同场景的入口能力。

工程结构如下（目录层级）：

```
1. ├──commons
2. │  └──base/src/main
3. │     └──ets
4. │        ├──baseviews                     // 公共视图组件
5. │        ├──models                        // 公共数据模型
6. │        └──utils                         // 公共工具类
7. ├──features
8. │  ├──stockdeal/src/main
9. │  │  └──ets
10. │  │     ├──chartmodels                   // 图表组件
11. │  │     ├──models                        // 股票交易数据模型
12. │  │     ├──viewmodels                    // 股票交易视图模型
13. │  │     └──views                         // 股票交易视图组件
14. │  ├──stockdetail/src/main
15. │  │  ├──ets
16. │  │  │  ├──models                        // 股票详情数据模型
17. │  │  │  ├──viewmodels                    // 股票详情视图模型
18. │  │  │  ├──pages                         // 股票详情页
19. │  │  │  └──views                         // 股票详情视图组件
20. │  └──stockmarket/src/main
21. │     └──ets
22. │        ├──models                        // 股票市场数据模型
23. │        ├──viewmodels                    // 股票市场视图模型
24. │        └──views                         // 股票市场视图组件
25. └──products
26. ├──default/src/main
27. │  ├──ets
28. │  │  ├──entryability                  // 移动端程序入口
29. │  │  ├──entrybackupability            // 程序备份入口
30. │  │  ├──pages                         // 移动端首页
31. │  │  ├──splitScreenAbility            // 分屏能力
32. │  │  └──splitScreenBackupAbility      // 分屏备份能力
33. │  └──resources                        // 应用静态资源目录
34. └──pc/src/main
35. ├──ets
36. │  ├──pages                         // PC端页面
37. │  ├──pcability                     // PC端程序入口
38. │  └──pcbackupability               // PC程序备份入口
39. └──resources                        // 应用静态资源目录
```

## 移动端页面

### 窗口适配

**窗口模式**

[多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)示例，根据适配的设备，涉及全屏模式、分屏模式、悬浮窗模式、自由窗口模式，可参考[窗口模式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode)。其中分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用监听窗口尺寸变化，[通过断点刷新UI](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)，将自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。

使用系统UI组件进入全景多窗，实现一个应用多个窗口并行运行的体验，可参考[股票详情页](multi-ticket-class.md#section46312514204)——功能开发：应用多实例-多股比价部分。

**窗口方向**

通过设置[setPreferredOrientation()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setpreferredorientation9>)使应用跟随传感器自动旋转。在类直板机上推荐仅竖屏显示，在双折叠展开态、三折叠G态、平板等大屏幕场景下推荐四方向旋转并受控制中心的旋转开关控制。在股票应用中，通过module.json5配置文件，建议设置为FOLLOW\_DESKTOP，具体说明可参考[窗口方向](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction)。

**窗口沉浸式**

根据UX设计，实现不同窗口模式（全屏、分屏、悬浮窗）下窗口的沉浸式，可参考[窗口沉浸式](../../多设备窗口形态/窗口沉浸式/bpta-multi-device-window-immersive.md)。全屏、分屏和悬浮窗的沉浸式均可通过[setWindowLayoutFullscreen()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowlayoutfullscreen9>)实现，并进行动态安全区避让。

### 自选股页面

自选股页主要用于响应用户输入、展示指数、自选股票信息以及跳转股票详情页。按照功能设计，将自选股页相关内容划分为4个区域，效果图如下所示：

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
| --- | --- | --- | --- | --- |
| 自选股页 |  |  |  |  |

**界面开发**

对各个区域使用的多种能力进行分析，实现方案如下表：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部/侧边页签 | 借助[响应式组件](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section1914110349546)HdsTabs实现。同时在api版本低的设备上降级使用Tabs组件。 |
| 2 | 指数 | 最后一个组件固定，其他组件使用[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)实现延伸能力，随着设备宽度变大，页签间距变大，页面能够展示更多页签内容。 |
| 3 | 股票列表-工具栏 | 文字和功能按钮中间增加[Blank](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/空白与分隔/Blank/ts-basic-components-blank.md)，实现拉伸能力。 |
| 4 | 股票列表 | 通过使用[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)设置固定宽度和[Scroll](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)，可实现股票列表数据的上下或左右滑动。同时，支持对不同列设置不同的[justifyContent](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md#justifycontent8)，以便实现各列的不同对齐方式。 |

* 整个页面使用的是[分栏布局](../../界面布局响应式变化/页面布局场景/bpta-multi-device-page-layout.md#section11897247142110)，在股票列表区域，点击某一股票时，平板上会分栏显示该股票的详细信息。

### 股票详情页

股票详情页主要用于响应用户输入、展示具体股票详细信息以及查看讨论信息等内容。按照功能设计，将自选股页相关内容划分为6个区域，效果图如下所示：

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 个股详情页 |  |  |  |  |

**界面开发**

对各区域使用的能力进行分析，实现方案如表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 交易操作行 | 通过为“去交易”按钮设置[layoutWeight](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#layoutweight)布局权重，并使用Blank组件结合断点，实现该按钮的自适应拉伸。 |
| 2 | 标题 | 居中显示，其他操作两端对齐，空白空间使用[Blank](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/空白与分隔/Blank/ts-basic-components-blank.md)实现自适应布局拉伸能力。 |
| 3 | 行情列表数据 | 通过[栅格](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section1061332817545)并结合断点，控制在不同断点下显示不同的列数，列表自适应两列变多列。 |
| 4 | 中间Tab | 通过[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |
| 5 | 曲线图和柱状图 | 使用layoutWeight属性实现拉伸能力。 |
| 6 | 讨论Tab | 通过[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |

**功能开发：应用多实例-多股比价**

应用通过系统提供的[MultiWindowEntryInAPP](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/MultiWindowEntryInAPP/ui-design-multiwindowentryinapp-api.md>)组件，配置需拉起的bundleName与UIAbility（仅限本应用，无法拉起其他应用），单击组件页面进入分屏（双股对比），在分屏状态下，再点击组件进入全景多窗（三股对比）。

下表以Mate X5设备为例，展示应用在分屏及全景多窗模式下的效果。

| - | 折叠屏分屏-双股**比价** | 折叠屏全景多窗-三股**比价** |
| --- | --- | --- |
| 个股详情页-多股比价 |  |  |

**约束条件**

[MultiWindowEntryInAPP](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/MultiWindowEntryInAPP/ui-design-multiwindowentryinapp-api.md>)组件依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备型态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备型态，该组件不可交互，不响应点击事件。

说明

建议开发者在分屏副窗口左上角设置**关闭按钮**以直接关闭副窗口，本案例使用返回按钮，是股票比价场景需返回上级页面的特定需求。

**开发步骤**

应用使用[MultiWindowEntryInAPP](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/MultiWindowEntryInAPP/ui-design-multiwindowentryinapp-api.md>)组件主动分屏或进入全景多窗。具体开发步骤如下：

1. 导入模块。

   ```
   1. import { MultiWindowEntryInAPP } from '@kit.UIDesignKit';
   2. import { TextModifier } from '@kit.ArkUI';
   3. import { Want } from '@kit.AbilityKit';
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/HarmonyOS_Samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L16-L18)
2. 使用MultiWindowEntryInAPP组件，并且设置组件参数。

   ```
   1. @Component
   2. export struct MultiWindowEntryComponent {
   3. @Link textModifier: TextModifier;
   4. @Link want: Want;
   5. @State isShowMultiWindowEntry: boolean = false;
   6. // ...

   8. build() {
   9. Row() {
   10. MultiWindowEntryInAPP({
   11. want: this.want,
   12. isShowSubtitle: false,
   13. multiWindowEntryInAPPStyle: {
   14. iconOptions: {
   15. iconSize: 24,
   16. iconColor: $r('sys.color.font_primary'),
   17. iconWeight: FontWeight.Normal,
   18. backgroundColor: $r('sys.color.comp_background_tertiary')
   19. },
   20. subtitleOptions: {
   21. modifier: this.textModifier.fontColor($r('app.color.text_primary_color'))
   22. }
   23. }
   24. })
   25. .id('MultiWindowEntryInAPP')
   26. }
   27. .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
   28. }
   29. }
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L26-L86)
3. 导入封装好的MultiWindowEntryComponent组件，并且设置组件参数。

   ```
   1. import { MultiWindowEntryComponent } from './MultiWindowEntryComponent';

   3. @Component
   4. export struct TopTitleBar {
   5. // ...
   6. @State textModifier: TextModifier = new TextModifier();
   7. @State splitScreenWant: Want = {
   8. // Modify the bundleName, moduleName and abilityName of the current application,
   9. // and launch the UIAbility within the application.
   10. bundleName: 'com.example.multiticketclass',
   11. moduleName: 'multiticketclassdefaultsample',
   12. abilityName: 'SplitScreenAbility',
   13. };
   14. // ...
   15. build() {
   16. Row() {
   17. // ...
   18. // The area displayed by the icon on the right side
   19. Row({ space: 16 }) {
   20. // split screen
   21. Row() {
   22. MultiWindowEntryComponent({
   23. textModifier: this.textModifier,
   24. want: this.splitScreenWant
   25. })
   26. }
   27. .visibility(this.getMultiWindowVisibility())
   28. }
   29. }
   30. // ...
   31. }
   32. }
   ```

   [TopTitleBar.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/features/stockdetail/src/main/ets/views/TopTitleBar.ets#L34-L195)

**应用内分屏高阶组件窗口路由方案**

建议开发者采用应用级多实例来实现分屏页面的路由管理。以下是页面级多实例与应用级多实例的主要区别，多股比价场景的分屏路由管理采用应用级多实例：

| 场景 | 路由栈特点 | 是否需要路由改造 | 核心方案 |
| --- | --- | --- | --- |
| 页面级多实例 | 每个UI Ability创建后，基于当前节点改造路由栈 | 需要 | 以当前路由节点生成路由表，开发者手动定义路由方案 |
| 应用级多实例（**推荐**） | 每个UI Ability创建独立的相同路由栈 | 不需要 | 每个窗口启动时创建独立路由栈（路由表相同） |

**应用内分屏高阶组件窗口路由退栈方案**

在多股比价场景中，当在应用内进行分屏操作时，新增窗口应保留当前浏览的股票信息，而主窗口则应回到股票列表。为实现这一功能，建议在新窗口的启动生命周期中触发事件，原窗口通过监听该事件并执行退栈操作。

1. 在分屏程序的入口SplitScreenAbility.ets中的onCreate()和onNewWant()生命周期中进行事件触发。

   ```
   1. let eventData: emitter.EventData = {
   2. data: {
   3. 'isStart': 1,
   4. 'id': 1
   5. }
   6. };
   7. let innerEvent: emitter.InnerEvent = {
   8. eventId: 1,
   9. priority: emitter.EventPriority.HIGH
   10. };

   12. export default class SplitScreenAbility extends UIAbility {
   13. // ...

   15. onCreate(): void {
   16. // ...
   17. emitter.emit(innerEvent, eventData);
   18. }

   20. onNewWant(): void {
   21. // ...
   22. emitter.emit(innerEvent, eventData);
   23. }

   25. // ...
   26. }
   ```

   [SplitScreenAbility.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/products/default/src/main/ets/splitScreenAbility/SplitScreenAbility.ets#L32-L170)
2. 在原窗口进行事件监听并做退栈处理。

   ```
   1. @Component
   2. export struct TopTitleBar {
   3. // ...
   4. private innerEvent: emitter.InnerEvent = { eventId: 1 };
   5. private callBack: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
   6. Logger.info(`eventData:${eventData}`);
   7. if (this.pageInfos?.pop) {
   8. this.pageInfos.pop();
   9. }
   10. };

   12. aboutToAppear(): void {
   13. this.viewModel.loadData();
   14. if (this.context.abilityInfo.name === 'MultiticketclassdefaultAbility') {
   15. emitter.on(this.innerEvent, this.callBack);
   16. }
   17. }

   19. aboutToDisappear(): void {
   20. emitter.off(this.innerEvent.eventId, this.callBack);
   21. }

   23. // ...
   24. }
   25. }
   ```

   [TopTitleBar.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/features/stockdetail/src/main/ets/views/TopTitleBar.ets#L37-L194)

**应用内分屏高阶组件按钮显隐策略**

在应用内分屏高阶组件时，对不支持全景多窗的设备隐藏分屏按钮。方案的主要逻辑为：

1. 监听窗口尺寸变化。

   ```
   1. public onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
   2. this.mainWindowInfo.windowSize = windowSize;
   3. if (this.uiContext) {
   4. this.mainWindowInfo.widthBp = this.uiContext.getWindowWidthBreakpoint();
   5. this.mainWindowInfo.heightBp = this.uiContext.getWindowHeightBreakpoint();
   6. }
   7. };
   8. // ...
   9. updateWindowInfo(): void {
   10. try {
   11. // ...
   12. // Register for window size change monitoring, update window size and width/height breakpoint.
   13. this.mainWindow.on('windowSizeChange', this.onWindowSizeChange);
   14. // ...
   15. AppStorage.setOrCreate(KEY_MAIN_WINDOW_INFO, this.mainWindowInfo);
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. Logger.error(`Failed to update window info. Code: ${err.code}, message: ${err.message}`);
   19. }
   20. }
   ```

   [WindowUtil.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/commons/base/src/main/ets/utils/WindowUtil.ets#L39-L246)
2. 尺寸变化时获取按钮节点，查询其enabled属性。

   ```
   1. private timerId: number = -1;

   3. aboutToAppear(): void {
   4. this.checkMultiWindowEnabled();
   5. }

   7. aboutToDisappear(): void {
   8. if (this.timerId !== -1) {
   9. clearTimeout(this.timerId);
   10. }
   11. }

   13. private checkMultiWindowEnabled(): void {
   14. this.timerId = setTimeout(() => {
   15. const frameNode = this.getUIContext()?.getFrameNodeById('MultiWindowEntryInAPP');
   16. const inspectorInfo = JSON.stringify(frameNode?.getInspectorInfo() as InspectorInfo);
   17. if (inspectorInfo?.search('"enabled":true') && inspectorInfo?.search('"enabled":true') !== -1) {
   18. this.isShowMultiWindowEntry = true;
   19. } else {
   20. this.isShowMultiWindowEntry = false;
   21. }
   22. }) as number;
   23. }
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L33-L55)
3. 根据enabled属性通过visibility控制组件的显隐。

   ```
   1. Row() {
   2. MultiWindowEntryInAPP({
   3. want: this.want,
   4. isShowSubtitle: false,
   5. multiWindowEntryInAPPStyle: {
   6. // ...
   7. }
   8. })
   9. .id('MultiWindowEntryInAPP')
   10. }
   11. .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/wangwenbo551/multi-ticket-class/blob/dev_homs_check/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L62-L83)

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成股票类应用在电脑设备上的界面开发。

### 窗口适配

* 窗口模式

  长视频应用在电脑端上支持全屏和自由窗口两种模式，具体实现可参考[窗口模式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-mode)。应用内监听窗口尺寸变化，[通过断点刷新UI](../../界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏和自由窗口模式下的布局。
* 窗口沉浸式

  根据UX设计规范，需要实现全屏和自由窗口下的沉浸式效果，具体实现可参考[窗口沉浸式](../../多设备窗口形态/窗口沉浸式/bpta-multi-device-window-immersive.md)。全屏模式下，通过[window.setWindowLayoutFullscreen()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowlayoutfullscreen9>)实现沉浸式。自由窗口模式下，通过[window.setWindowDecorVisible(false)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowdecorvisible11>)隐藏标题栏，仅保留右上角三键，使页面内容延伸至标题栏区域，实现沉浸式显示效果。

### 自选股页面

**页面布局**

* 将电脑端自选股页划分为四个部分，效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-L_PGsbWTqW5d5e_LJ0aFA/zh-cn_image_0000002610071557.png?HW-CC-KV=V1&HW-CC-Date=20260612T021011Z&HW-CC-Expire=86400&HW-CC-Sign=52894FC4204107D93592E5D62AB7E3FA13320A7642D7BD616EC32C62547D2AD4 "点击放大")

* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 侧边页签 | 同移动端[自选股页面](multi-ticket-class.md#section2034582411817)对应区域的布局实现方案一致。 |
  | 2 | 指数 |
  | 3 | 股票列表-工具栏 |
  | 4 | 股票列表 |

### 股票详情页

**页面布局**

* 将电脑端股票详情页划分为五个部分，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/ZesXTTvMS164mX1-0V4NBA/zh-cn_image_0000002579631780.png?HW-CC-KV=V1&HW-CC-Date=20260612T021011Z&HW-CC-Expire=86400&HW-CC-Sign=EB45B41E93241B62078425427C25FB8295ADAE21FD328F8504CFC4D78969B9E4 "点击放大")

* 对各区域使用的能力进行分析，实现方案如表所示：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 交易操作行 | 同移动端[股票详情页](multi-ticket-class.md#section46312514204)对应区域的布局实现方案一致。 |
  | 2 | 标题 |
  | 3 | 行情列表数据 |
  | 4 | 中间Tab |
  | 5 | 曲线图和柱状图 |

## 示例代码

* [多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)
