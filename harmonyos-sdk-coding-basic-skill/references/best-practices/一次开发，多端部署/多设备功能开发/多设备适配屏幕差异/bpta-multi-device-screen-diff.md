---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-screen-diff
title: 多设备适配屏幕差异
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备功能开发 > 多设备适配屏幕差异
category: best-practices
scraped_at: 2026-06-12T10:12:15+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:7624951266867a0dcc7ec49e9fa741cb3e25fcbb9ae7b9ac025e69a1b42ebd9a
---
## 概述

多设备适配技术旨在解决跨设备界面一致性问题，如在折叠屏开合、窗口自由调整等场景中保障布局完整性。其核心策略在于通过动态布局调整和响应式设计，消除屏幕尺寸差异导致的截断与留白问题，并确保交互状态切换时的视觉连续性。

本文主要面向中高级开发者。开始之前，建议先了解[一次开发，多端部署](../../一次开发，多端部署概览/bpta-multi-device-overview.md)、[断点](../../多设备界面开发/界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section1532120147301)等知识点。

本文主要内容如下：

* [适配多设备屏幕差异](bpta-multi-device-screen-diff.md#section82114465127)：根据多设备屏幕的差异，建议页面适配不同尺寸的屏幕，具体可参考[页面适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section103508214132)；在短视频等场景下，建议考虑视频在多设备下的沉浸式体验和尺寸适配，具体可参考[视频适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section1452572513130)。
* [适配折叠设备屏幕](bpta-multi-device-screen-diff.md#section2079763671319)：开发者在适配折叠设备屏幕时，除了页面需要适配不同尺寸屏幕外，建议适配：[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)和[悬停态](bpta-multi-device-screen-diff.md#section32851531135)。

## 适配多设备屏幕差异

### 页面适配不同尺寸屏幕

页面适配不同尺寸屏幕的本质，是适配不同尺寸的窗口——无论是手机、折叠屏、平板还是电脑，其屏幕差异最终都体现为应用显示窗口宽高、比例的差异。因此，适配的核心应基于窗口属性抽象出响应式能力，通过“[断点](../../多设备界面开发/界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section1532120147301)适配”实现界面随窗口尺寸动态调整，确保在任意窗口规格下均能稳定显示，详情可参考[通过断点刷新UI](../../多设备界面开发/界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)。通过一次性基于断点的布局适配，即可支持分屏、悬浮窗、自由窗口等多种窗口模式，确保界面在不同形态间平滑、连续地响应变化。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/HY9Rp6PNRHiiPCKxUSrPSA/zh-cn_image_0000002506596732.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=C6B52CDA4EC72FED93562846DAD92B6A3AF47858998EDD5FEA316FFBD7EA6BD7 "点击放大")

开发多设备界面时，不同屏幕类型常用的响应式布局可参考[屏幕类型布局场景](../../多设备界面开发/界面布局响应式变化/屏幕类型布局场景/bpta-multi-device-screen-layout.md)，包含[直板机竖屏](../../多设备界面开发/界面布局响应式变化/屏幕类型布局场景/bpta-multi-device-screen-layout.md#section1919517165814)、[大屏横屏](../../多设备界面开发/界面布局响应式变化/屏幕类型布局场景/bpta-multi-device-screen-layout.md#section6493354468)等常见窗口形态和[小方形屏](../../多设备界面开发/界面布局响应式变化/屏幕类型布局场景/bpta-multi-device-screen-layout.md#section1395830175918)等特殊窗口形态的适配。

### 视频适配不同尺寸屏幕

视频适配不同尺寸屏幕，旨在确保各类宽高比的视频在多种设备屏幕上均能呈现良好效果，避免拉伸变形或关键内容被过度裁切。为提升视频观看体验，可通过全屏展示、弱化界面干扰，使用户更加专注于视频内容。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/3aZy7kQTT_K00L5611qX_g/zh-cn_image_0000002506436906.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=0F3578F9A892DA5F1583D39BA72B0880AFDD73C1D4BB546529A68E21E9CFACFF "点击放大")

为了实现这一效果，需考虑不同尺寸视频在不同尺寸窗口上的适配规则。从视频的宽高比出发，可分为9:16和非9:16两种类型。

说明

本章节的适配规则适用于宽度大于320vp的窗口。

**适配宽高比非9:16的视频**

宽高比非9:16的视频包括竖向视频（高>宽）或横向视频（宽>高），红色区域为推荐的视频显示区域，适配建议如下图所示，其中横向坐标为窗口宽高比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/CFYQcTwxSWG3qiD7aG_MtA/zh-cn_image_0000002538396643.png?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=D2DD99F6B48A230D1885584B1D1434C18C997B169BB5E330D89F0999D59BB7DA "点击放大")

**适配宽高比为9:16的视频**

当视频宽高比为9:16时，其在断点区间的适配效果图如下图所示，红色区域为推荐的视频显示区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/spvvIXZXTeO6_IshNHiV1w/zh-cn_image_0000002538316627.png?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=0DB15764CB46A5AAF67D8AAE6D62C6A64DC4B1E8333FFF79055A35C254FF9586 "点击放大")

当横向断点为sm、纵向断点为lg时，由于设备尺寸的差异，存在不同的适配建议。具体如下图所示，其中横坐标为窗口宽高比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tWsDVx2_SQOCW6HpuST7ww/zh-cn_image_0000002506596740.png?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=471F438FE554CC2B78CAA98C1E269D93CD420A2123A1251614BBED9789B86E49 "点击放大")对于不满足横向断点为sm、纵向断点为lg的其他窗口尺寸，建议顶部状态栏和底部Tab栏均采用沉浸式设计，内容区高度=窗口高度，内容区宽度=内容区高度×视频宽高比。

**获取窗口信息**

如前述章节所述，在视频适配不同窗口尺寸时，需获取窗口尺寸信息、避让区信息等参数用于计算。以下列举的方法将在适配过程中使用：

* 使用[getWindowProperties()](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getwindowproperties9>)方法，返回的对象中windowRect.width和windowRect.height分别表示窗口的宽度和高度；
* 使用[getWindowAvoidArea()](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getwindowavoidarea9>)方法，返回的[AvoidArea](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#avoidarea7>)对象可获得当前设备的避让区域信息；
* 屏幕窗口尺寸可能会发生变化，比如在自由窗口模式下可任意调整窗口大小，需使用[on('windowSizeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onwindowsizechange7>)监听窗口尺寸的变化。当窗口尺寸变化时，应依据适配规则重新计算内容区域的尺寸，确保视频展示效果良好；
* 系统避让区可能会发生变化，例如窗口从全屏模式切换至悬浮窗模式，需要使用[on('avoidAreaChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onavoidareachange9>)监听系统避让区的尺寸变化，避让区尺寸变化时，应依据适配规则重新计算内容区域的尺寸；

以上适配建议的实现示例代码可参考[基于adaptive\_video的短视频适配](../../../行业场景解决方案/影音娱乐/基于adaptive_video的短视频适配/bpta-short-video-base-adaptivevideo.md)。

## 适配折叠设备屏幕

折叠设备通常具有支持独立显示的两块或多块屏幕，例如Mate X5、Mate XT和MateBook Fold等。开发者在适配折叠设备屏幕时，除了页面适配不同尺寸屏幕外，还需关注两个特殊点：[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)和[悬停态](bpta-multi-device-screen-diff.md#section32851531135)。

### 开合连续

开合连续指应用在各种屏幕和窗口状态间切换时页面内容连续，切换之前的任务和相关状态能保存、延续，或能够快速恢复，给用户提供连续的体验。主要标准有页面不发生改变和焦点不发生偏移，具体可参考[开合接续](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141#section5560057912)。应用页面和功能相关的开合连续能力建议使用断点实现，并通过[window.on('windowSizeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onwindowsizechange7>)接口监听。

display提供了折叠状态监听的接口，这些接口建议使用在某些应用功能的适配上，比如[适配设备悬停态](bpta-multi-device-screen-diff.md#section1223242181220)、[设置多设备上相机预览画面比例](../相机硬件差异/bpta-multi-device-camera.md#section882216138497)，但不能用于页面布局的开合连续适配。

说明

* **不推荐使用折叠状态监听接口实现页面布局的响应式布局和接续，避免在窗口变化但折叠状态未改变的场景下布局未能及时调整，出现页面异常。**
* 在双折叠开合过程中，各种监听回调的触发时序如下。
  + 展开态->折叠态：foldStatusChange(悬停态) -> foldStatusChange(折叠态) -> foldDisplayModeChange -> windowSizeChange
  + 折叠态->展开态：foldStatusChange(悬停态) -> foldDisplayModeChange -> windowSizeChange -> foldStatusChange(展开态)

常见的接口汇总如下。

| API | 说明 |
| --- | --- |
| [getWindowWidthBreakpoint](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13>) | 获取当前实例所在窗口的宽度断点 |
| [getWindowHeightBreakpoint](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13>) | 获取当前实例所在窗口的高度断点 |
| [window.on('windowSizeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onwindowsizechange7>) | 开启窗口尺寸变化的监听 |
| [window.off('windowSizeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#offwindowsizechange7>) | 关闭窗口尺寸变化的监听 |
| [display.isFoldable](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayisfoldable10>) | 检查设备是否可折叠 |
| [display.getCurrentFoldCreaseRegion](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displaygetcurrentfoldcreaseregion10>) | 在当前模式下获取折叠折痕区域 |
| [display.getFoldStatus](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displaygetfoldstatus10>) | 获取可折叠设备的当前折叠状态 |
| [display.getFoldDisplayMode](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displaygetfolddisplaymode10>) | 获取可折叠设备的显示模式 |
| [display.on('foldStatusChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayonfoldstatuschange10>) | 开启折叠设备折叠状态变化的监听 |
| [display.off('foldStatusChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayofffoldstatuschange10>) | 关闭折叠设备折叠状态变化的监听 |
| [display.on('foldDisplayModeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayonfolddisplaymodechange10>) | 开启折叠设备屏幕显示模式变化的监听 |
| [display.off('foldDisplayModeChange')](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayofffolddisplaymodechange10>) | 关闭折叠设备屏幕显示模式变化的监听 |

**开合页面后刷新UI布局效果**

双折叠开合状态变化时会伴随着窗口尺寸的变化，可通过注册on('windowSizeChange')事件监听器来捕获窗口尺寸变化，在回调函数中重新计算当前断点，通过断点变化更新UI布局，确保界面始终与当前窗口尺寸保持同步。这一机制能够有效处理设备展开/折叠、分屏模式切换以及屏幕旋转等多种场景下的界面适配需求，为用户提供流畅的双折叠使用体验。

```
1. private onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
2. AppStorage.setOrCreate('currentWidthBreakpoint', this.uiContext!.getWindowWidthBreakpoint());
3. AppStorage.setOrCreate('currentHeightBreakpoint', this.uiContext!.getWindowHeightBreakpoint());
4. };
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L37-L40)

触发断点变化回调后，需要通过断点更新UI布局实现双折叠开合前后布局连续，具体可参考[通过断点刷新UI](../../多设备界面开发/界面布局响应式变化/响应式布局/bpta-multi-device-responsive-layout.md#section175001836203617)。

**可滑动组件的阅读焦点不偏移**

对于双折叠开合连续使用场景，应用在完成折叠状态切换操作后，需确保[List](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件、[WaterFlow](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)组件以及 [Scroll](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)组件等可滑动组件的阅读焦点不发生偏移。目前，这些组件依据折叠状态改变前的滑动偏移量来维持阅读焦点位置，然而，由于折叠状态切换前后，组件内部高度可能发生变化，即便滑动相同的偏移量，也难以达成阅读焦点不偏移的目标。因此，有必要针对上述可滑动组件采取特殊处理措施。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/XucH3j8eSIGmXv0iBjMOog/zh-cn_image_0000002585654510.png?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=FFCE758C406B9ED934832A846AA2D6DEA857F59F4BEE3921D6D54EED6F19E383 "点击放大")

* List组件

  List组件可以通过[onScrollIndex()](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#onscrollindex)来监听子组件划入或划出List显示区域，可以获取到当前处于List显示区域头部的索引值。获取到头部索引值后，在监听双折叠状态变化的回调中，利用Scroller控制器提供的[scrollToIndex()](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md#scrolltoindex)方法，使列表滑动到指定索引值的位置，从而保证阅读焦点不偏移，示例如下。

  在aboutToAppear中注册监听索引值变化的回调，触发刷新。

  ```
  1. aboutToAppear(): void {
  2. let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  3. if (data === display.FoldStatus.FOLD_STATUS_EXPANDED) {
  4. this.barOpacity = 1;
  5. this.listScroller.scrollToIndex(this.currentIndex);
  6. } else if (data === display.FoldStatus.FOLD_STATUS_FOLDED) {
  7. this.listScroller.scrollToIndex(this.currentIndex);
  8. }
  9. hilog.info(0x0000, TAG, 'Listening enabled. Data: ' + JSON.stringify(data));
  10. };
  11. try {
  12. display.on('foldStatusChange', callback);
  13. } catch (error) {
  14. let err = error as BusinessError;
  15. hilog.error(0x0000, 'TestLog', `Failed to update fold status. Code: ${err.code}, message: ${err.message}`);
  16. }
  17. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L52-L69)

  在List组件scrollToIndex()方法中更新索引值。

  ```
  1. List({
  2. space: CommonConstants.LIST_SPACE[0],
  3. scroller: this.listScroller,
  4. }) {
  5. // ...
  6. }
  7. .onScrollIndex((start: number) => {
  8. this.currentIndex = start;
  9. })
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L152-L200)
* WaterFlow组件

  WaterFlow组件需要根据场景进行特殊的判断，若双折叠状态改变前后，WaterFlow未改变展示列数，则系统默认使用改变前的滑动偏移量，以确保阅读焦点不发生偏移；若双折叠状态改变前后，WaterFlow改变了列数，则需要将[WaterFlowLayoutMode](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)改为SLIDING\_WINDOW。修改后，系统将根据WaterFlow可展示区域的最小索引值，自动调整以确保阅读焦点不偏移。

  ```
  1. WaterFlow({ layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
  2. LazyForEach(this.dataSource, (item: number) => {
  3. FlowItem() {
  4. Column() {
  5. Text('Num' + item).fontSize(12).height('16')
  6. }
  7. }
  8. .onAppear(() => {
  9. if (item + 20 == this.dataSource.totalCount()) {
  10. for (let i = 0; i < 100; i++) {
  11. this.dataSource.addLastItem();
  12. }
  13. }
  14. })
  15. .width('100%')
  16. .height(this.itemHeightArray[item % 100])
  17. .backgroundColor(this.colors[item % 5])
  18. }, (item: string) => item)
  19. }
  20. .columnsTemplate(this.waterFlowColumnsTemplate)
  ```

  [WaterFlowView.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/views/WaterFlowView.ets#L82-L101)
* Scroll组件

  Scroll组件会根据折叠前的滑动偏移量来保证阅读焦点不偏移，但Scroll组件无法做到List组件一样，根据列表项索引来保证阅读焦点不偏移。Scroll组件提供了[scrollBy()](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md#scrollby9)方法，以实现滑动指定距离。开发者需要根据具体的业务场景，计算出需要滑动的距离，再通过scrollBy()方法，自行适配Scroll组件的阅读焦点不偏移。

### 悬停态

折叠屏在悬停态下可平稳放置于桌面，实现免手持体验，适用于视频通话、播放视频、拍照及听歌等无需频繁交互的场景。设计规范可参照[悬停态](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141#section183378919119)。设备在悬停态时，应用需避开中间折痕区域，并对上下两个界面进行悬停适配，重新布局。悬停状态的实现方案可参考[折叠屏悬停态](../../多设备界面开发/特殊界面布局场景/折叠屏悬停态/bpta-folded-hover.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/5oadlpMLRzu0MWclhdygrw/zh-cn_image_0000002506436912.png?HW-CC-KV=V1&HW-CC-Date=20260612T021209Z&HW-CC-Expire=86400&HW-CC-Sign=EC6685DB8C0AB12E9CB8A4A11BA5EFFEF9F4090A836E0C860312960CF12226DE "点击放大")
