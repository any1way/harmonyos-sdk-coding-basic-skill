---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization
title: UI国际化
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI国际化
category: harmonyos-guides
scraped_at: 2026-06-11T14:32:43+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:4144068d2734a55db5092ee59c4608b0f9c75dc404726586ef5e905d148da7d2
---
本文介绍如何实现应用程序UI界面的国际化，包含资源配置和镜像布局，关于应用适配国际化的详细参考，请参考[Localization Kit（本地化开发服务）](<../../../Localization Kit（本地化开发服务）/国际化和本地化概述/i18n-l10n.md>)。

## 利用资源限定词配置国际化资源

在开发阶段，通过DevEco Studio，可以为应用在对应语言和地区的资源限定词目录下配置不同的资源，来实现UI国际化。详细介绍请参考[资源分类与访问](../../../../基础入门/资源分类与访问/resource-categories-and-access.md)。

## 使用镜像能力

不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语和希腊语则采用从右到左（RTL）的顺序。为满足不同用户的阅读习惯，ArkUI提供了镜像能力。在特定情况下将显示内容在X轴上进行镜像反转，由从左到右显示变成从右到左显示。

| 镜像前 | 镜像后 |
| --- | --- |
|  |  |

当组件满足以下任意条件时，镜像能力生效：

1. 组件的direction属性设置为Direction.Rtl。
2. 组件的direction属性设置为Direction.Auto，且当前的系统语言（如维吾尔语）的阅读习惯是从右向左。

### 基本概念

* LTR：顺序为从左到右。
* RTL：顺序为从右到左。

### 使用约束

ArkUI 如下能力已默认适配镜像：

| 类别 | 名称 |
| --- | --- |
| 基础组件 | [Swiper](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)、[Tabs](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md)、[TabContent](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/TabContent/ts-container-tabcontent.md)、[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)、[Progress](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Progress/ts-basic-components-progress.md)、[CalendarPicker](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md)、[CalendarPickerDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/日历选择器弹窗 (CalendarPickerDialog)/ts-methods-calendarpicker-dialog.md>)、[TextPicker](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md)、[TextPickerDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/文本滑动选择器弹窗 (TextPickerDialog)/ts-methods-textpicker-dialog.md>)、[DatePicker](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/DatePicker/ts-basic-components-datepicker.md)、[DatePickerDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/日期滑动选择器弹窗 (DatePickerDialog)/ts-methods-datepicker-dialog.md>)、[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)、[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)、[Scroll](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)、[ScrollBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ScrollBar/ts-basic-components-scrollbar.md)、[AlphabetIndexer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、[Stepper](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/已停止维护的组件与接口/Stepper/ts-basic-components-stepper.md)、[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)、[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)、[NavDestination](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md)、[Rating](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Rating/ts-basic-components-rating.md)、[Slider](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md)、[Toggle](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md)、[Badge](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Badge/ts-container-badge.md)、[Counter](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Counter/ts-container-counter.md)、[Chip](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[SegmentButton](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SegmentButton/ohos-arkui-advanced-segmentbutton.md)、[bindMenu](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#bindmenu)、[bindContextMenu](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#bindcontextmenu8)、[TextInput](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、[TextArea](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md)、[Search](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md)、[Stack](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Stack/ts-container-stack.md)、[GridRow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridRow/ts-container-gridrow.md)、[Text](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md)、[Select](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Marquee](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Marquee/ts-basic-components-marquee.md)、[Row](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Row/ts-container-row.md)、[Column](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Column/ts-container-column.md)、[Flex](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/Flex/ts-container-flex.md)、[RelativeContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)、[ListItemGroup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ListItemGroup/ts-container-listitemgroup.md) |
| 高级组件 | [SelectionMenu](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SelectionMenu/ohos-arkui-advanced-selectionmenu.md) 、[TreeView](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) 、[Filter](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/Filter/ohos-arkui-advanced-filter.md)、[SplitLayout](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SplitLayout/ohos-arkui-advanced-splitlayout.md)、[ToolBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ToolBar/ohos-arkui-advanced-toolbar.md)、[ComposeListItem](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ComposeListItem/ohos-arkui-advanced-composelistitem.md)、[EditableTitleBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[ProgressButton](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ProgressButton/ohos-arkui-advanced-progressbutton.md)、[SubHeader](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md) 、[Popup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/Popup/ohos-arkui-advanced-popup.md)、[Dialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md>)、[SwipeRefresher](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SwipeRefresher/ohos-arkui-advanced-swiperefresher.md) |
| 通用属性 | [position](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#position)、[markAnchor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#markanchor)、[offset](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#offset)、[alignRules](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#alignrules12)、[borderWidth](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#borderwidth)、[borderColor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#bordercolor)、[borderRadius](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#borderradius)、[padding](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#padding)、[margin](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#margin) |
| 接口 | [AlertDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md>)、[ActionSheet](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/列表选择弹窗 (ActionSheet)/ts-methods-action-sheet.md>)、[promptAction.showDialog](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md#promptactionshowdialogdeprecated>)、[promptAction.showToast](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md#promptactionshowtoastdeprecated>) |

但如下三种场景还需要进行适配：

1. 界面布局、边框设置：关于方向类的通用属性，如果需要支持镜像能力，使用泛化的方向指示词 start/end入参类型替换 left/right、x/y等绝对方向指示词的入参类型，来表示自适应镜像能力。
2. [Canvas](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/Canvas/ts-components-canvas-canvas.md)组件只有限支持文本绘制的镜像能力。
3. [XComponent](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/XComponent/ts-basic-components-xcomponent.md)组件不支持组件镜像能力。

### 界面布局和边框设置

目前，以下三类通用属性需要使用新入参类型适配：

位置设置：[position](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#position)、[markAnchor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#markanchor)、[offset](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#offset)、[alignRules](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#alignrules12)

边框设置：[borderWidth](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#borderwidth)、[borderColor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#bordercolor)、[borderRadius](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/边框设置/ts-universal-attributes-border.md#borderradius)

尺寸设置：[padding](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#padding)、[margin](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#margin)

以position为例，需要把绝对方向x、y描述改为新入参类型start、end的描述，其他属性类似。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct InterfaceLayoutBorderSettings {
6. build() {
7. Stack({ alignContent: Alignment.TopStart }) {
8. Stack({ alignContent: Alignment.TopStart }) {
9. Column()
10. .width(100)
11. .height(100)
12. .backgroundColor(Color.Red)
13. .position({
14. start: LengthMetrics.px(200),
15. top: LengthMetrics.px(200)
16. }) // 需要同时支持LTR和RTL时使用API12新增的LocalizedEdges入参类型,
17. // 仅支持LTR时等同于.position({ x: '200px', y: '200px' })

19. }.backgroundColor(Color.Blue)
20. }.width('100%').height('100%').border({ color: '#880606' })
21. }
22. }
```

[InterfaceLayoutBorderSettings.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/internationalization/entry/src/main/ets/homePage/InterfaceLayoutBorderSettings.ets#L15-L38)

### 自定义绘制Canvas组件

Canvas组件的绘制内容和坐标均不支持镜像能力。已绘制到Canvas组件上的内容并不会跟随系统语言的切换自动做镜像效果。

[CanvasRenderingContext2D](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md)的文本绘制支持镜像能力，在使用时需要与Canvas组件的通用属性direction（组件显示方向）和CanvasRenderingContext2D的属性direction（文本绘制方向）协同使用。具体规格如下：

1. 优先级：CanvasRenderingContext2D的direction属性 > Canvas组件通用属性direction > 系统语言决定的水平显示方向。
2. Canvas组件本身不会自动跟随系统语言切换镜像效果，需要应用监听到系统语言切换后自行重新绘制。
3. CanvasRenderingContext2D绘制文本时，只有符号等文本会对绘制方向生效，英文字母和数字不响应绘制方向的变化。

```
1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct CustomizeCanvasComponentDrawing {
6. @State message: string = 'Hello world';
7. private settings: RenderingContextSettings = new RenderingContextSettings(true)
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

10. aboutToAppear(): void {
11. // 监听系统语言切换
12. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
13. let subscribeInfo2: commonEventManager.CommonEventSubscribeInfo = {
14. events: ['usual.event.LOCALE_CHANGED'],
15. }
16. commonEventManager.createSubscriber(subscribeInfo2,
17. (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
18. if (err) {
19. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
20. return;
21. }

23. subscriber = data;
24. if (subscriber !== null) {
25. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
26. if (err) {
27. return;
28. }
29. // 监听到语言切换后，需要重新绘制Canvas内容
30. this.drawText();
31. })
32. } else {
33. console.error(`MayTest Need create subscriber`);
34. }
35. })
36. }

38. drawText(): void {
39. console.error('MayTest drawText')
40. this.context.reset()
41. this.context.direction = 'inherit'
42. this.context.font = '30px sans-serif'
43. this.context.fillText('ab%123&*@', 50, 50)
44. }

46. build() {
47. Row() {
48. Canvas(this.context)
49. .direction(Direction.Auto)
50. .width('100%')
51. .height('100%')
52. .onReady(() =>{
53. this.drawText()
54. })
55. }
56. .height('100%')
57. }

59. }
```

[CustomizeCanvasComponentDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/internationalization/entry/src/main/ets/homePage/CustomizeCanvasComponentDrawing.ets#L15-L76)

| 镜像前 | 镜像后 |
| --- | --- |
|  |  |

### 镜像状态字符对齐

[Direction](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#direction)是指文字的方向，即文本在屏幕上呈现时字符的顺序。在从左到右（LTR）文本中，显示顺序是从左向右；在从右到左（RTL）文本中，显示顺序是从右到左。

[TextAlign](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#textalign)是将文本作为一个整体，在布局上的影响，具体位置会受Direction影响，以TextAlign为start为例，当Direction为LTR时，布局位置靠左；当Direction为RTL时，布局位置靠右。

在LTR与RTL文本混排时，如一个英文句子中包含阿拉伯语的单词或短语，显示顺序将变得复杂。下图为数字和维吾尔语混合时对应的字符逻辑顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/5-1xDpETRlKX7fBiGKqDjw/zh-cn_image_0000002622857873.png?HW-CC-KV=V1&HW-CC-Date=20260611T063241Z&HW-CC-Expire=86400&HW-CC-Sign=52F928DFC03B6BF05E32B44D2F77EF1515AA0FB66C4302D0AB381F8809CC3F6D)

此时，文本渲染引擎会采用名为“双向算法”或“Unicode双向算法”（Unicode Bidirectional Algorithm）的方法来确定字符的显示顺序。下图展示了LTR与RTL文本混合时对应的字符显示顺序，确定字符方向的基本原则如下：

1. 强字符的方向性：强字符具有明确的方向性，例如，中文为LTR，阿拉伯语为RTL，这类字符的方向性会影响其周围的中性字符。
2. 弱字符的方向性：弱字符不具备明确的方向性，这些字符不会影响其周围中性字符的方向。
3. 中性字符的方向性：中性字符无固定方向性，它们会继承其最近的强字符的方向；若附近无强字符，则采用全局方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ybFQpiMXRo-TsOelZbXVEw/zh-cn_image_0000002622697995.png?HW-CC-KV=V1&HW-CC-Date=20260611T063241Z&HW-CC-Expire=86400&HW-CC-Sign=159FD21F70E153D5980203021D7CE5994968D240751783E346D3622D4D166498)
