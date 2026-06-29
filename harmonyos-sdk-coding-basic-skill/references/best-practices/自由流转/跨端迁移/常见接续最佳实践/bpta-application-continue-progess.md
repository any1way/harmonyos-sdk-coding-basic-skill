---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-continue-progess
title: 常见接续最佳实践
breadcrumb: 最佳实践 > 自由流转 > 跨端迁移 > 常见接续最佳实践
category: best-practices
scraped_at: 2026-06-12T10:12:23+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:aaabf9414b06da0911e36095561065ba6f8873f8019e73809efa4e3d8442215c
---
## 概述

接续是一种用户体验优化技术。在个人设备数量激增的当代，若用户在使用应用时附近有合适的设备，可通过该功能将应用无缝切换至新设备继续操作。本文主要针对长列表进度、媒体播放进度和Web浏览进度三个场景，实现了浏览进度的高效接续。用户切换设备时可轻松恢复之前的浏览进度，极大提升使用便捷性与连贯性，提供设备无缝切换的流畅体验。

* [长列表进度接续](bpta-application-continue-progess.md#section16702516134216)：允许用户从上次离开位置继续浏览，精准定位到目标条目附近，避免重复滚动，节省时间并减少操作成本，提升浏览体验。
* [媒体播放进度接续](bpta-application-continue-progess.md#section12439210434)：从源设备当前播放位置继续视频播放，保持播放进度、画面质量及音频设置的一致性，确保用户观影体验不被打断。支持在线视频平台的剧集、电影以及本地存储的视频文件，实现流畅接续播放。
* [Web浏览进度接续](bpta-application-continue-progess.md#section3512987460)：可快速定位至源设备浏览的网页位置，确保用户浏览连续性，避免重复查找信息的不便，提升信息获取效率。

## 实现原理

接续过程底层依赖分布式框架和软总线，开发者只需要启用接续、保存数据和恢复数据，具体运作机制可参考：[运作机制](../应用接续概述/bpta-continue-cast.md#section1218874218264)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2iRfgeVQT7qe0AnvNieo2Q/zh-cn_image_0000002622048193.png?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=22A33B6DD4D169B0C06B2B478198B86EBCB737CE5E7C5B9B756C46821AB4D8D5 "点击放大")

## 开发流程

进度接续的核心在于确保进度数据在不同设备间的精确传输与同步。在实际开发过程中，开发者会遇到各类复杂的接续需求，首要任务是深入分析对接续控制至关重要的数据。源设备启动接续时应保存数据，目标设备接续时需准确恢复数据，以确保进度的连续性与设备间数据的一致性。本章节将介绍如何配置应用以使用接续能力，以及如何保存和恢复数据以实现应用的无缝接续。具体开发流程如下：

1. 启用接续

   在module.json5文件的abilities中，需将continuable标签配置为"true"，以表示该UIAbility可被迁移。该配置默认值为"false"，未配置或显式配置为"false"的UIAbility将被系统识别为不可迁移。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "continuable": true
   8. }
   9. ],
   10. // ...
   11. }
   12. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/module.json5#L2-L83)
2. 源端保存迁移数据

   当对端点击接续图标时，源端将触发UIAbility中的[onContinue()](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIAbility (带界面的应用组件)/js-apis-app-ability-uiability.md#oncontinue>)接口。在此接口中，开发者可将需要迁移的数据以键值对形式保存至wantParam中，并返回AbilityConstant.OnContinueResult.AGREE，标识应用同意迁移，从而将数据迁移至对端。

   ```
   1. async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
   2. // 1.1 Retrieve the data to be connected and transmit it via wantParam.
   3. let continueIndex = AppStorage.get('continueIndex') as number;
   4. wantParam.continueIndex = continueIndex;
   5. let currentOffset = AppStorage.get('currentOffset') as number;
   6. wantParam.currentOffset = currentOffset;
   7. let continueHeight = AppStorage.get('listItemHeight') as number;
   8. wantParam.continueHeight = continueHeight;
   9. let currentTime = AppStorage.get('currentTime') as number;
   10. wantParam.continueTime = currentTime;
   11. let videoIndex = AppStorage.get('videoIndex') as number;
   12. wantParam.continueItem = videoIndex;
   13. let flag = AppStorage.get('flag') as boolean;
   14. wantParam.flag = flag;
   15. let url = AppStorage.get('pageUrl') as string;
   16. wantParam.pageUrl = url;
   17. let distance = AppStorage.get('scrollDistance') as number;
   18. wantParam.scrollDistance = distance;
   19. let breakpoint = AppStorage.get(BreakpointConstants.BREAKPOINT_NAME) as string;
   20. wantParam.breakpoint = breakpoint;
   21. let pageInfos = AppStorage.get('pageInfos') as NavPathStack;
   22. let pageArr = pageInfos.getAllPathName();
   23. let currentPage = '';
   24. if (pageArr.length > 0) {
   25. currentPage = pageArr[pageArr.length - 1];
   26. }
   27. AppStorage.setOrCreate('continue', false);
   28. wantParam.currentPage = currentPage;

   30. return AbilityConstant.OnContinueResult.AGREE;
   31. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L107-L138)
3. 对端恢复数据

   在源端保存数据并同意迁移后，对端可启动应用，开发者可在UIAbility中的[onCreate()](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件生命周期/uiability-lifecycle.md#oncreate>)或[onNewWant()](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件生命周期/uiability-lifecycle.md#onnewwant>)生命周期回调中恢复数据。如果Ability的启动原因为LaunchReason.CONTINUATION，可从want.parameters中获取保存的键值对数据。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. GlobalContext.getContext().setObject('abilityWant', want);
   3. GlobalContext.getContext().setObject('context', this.context);
   4. if (want.parameters) {
   5. if (want.parameters.currentTime) {
   6. GlobalContext.getContext().setObject('currentTime', want.parameters.currentTime);
   7. }
   8. }
   9. try {
   10. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   11. } catch (e) {
   12. hilog.error(0x000, 'progress', `setColorMode error ${JSON.stringify(e)}`);
   13. }
   14. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   15. if (want.parameters) {
   16. this.continueRestore(want);
   17. }
   18. }
   19. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   20. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L30-L50)

   可将恢复数据的方法提取为公共方法，以便在UIAbility的onCreate()或onNewWant()中调用。

   ```
   1. continueRestore(want: Want) {
   2. if (!want.parameters) {
   3. hilog.error(0x0000, 'EntryAbility', 'missing sessionId');
   4. return;
   5. }
   6. let currentPage = want.parameters.currentPage as string;
   7. AppStorage.setOrCreate('currentPage', currentPage);
   8. want.parameters.continueIndex && AppStorage.setOrCreate('continueWaterOffset', want.parameters.continueIndex);
   9. want.parameters.currentOffset && AppStorage.setOrCreate('continueOffset', want.parameters.currentOffset);
   10. want.parameters.continueHeight && AppStorage.setOrCreate('continueHeight', want.parameters.continueHeight);
   11. AppStorage.setOrCreate('continueEntry', true);
   12. AppStorage.setOrCreate('setCurrentOffset', true);
   13. want.parameters.continueTime && AppStorage.setOrCreate('currentTime', want.parameters.continueTime);
   14. want.parameters.continueItem && AppStorage.setOrCreate('videoIndex', want.parameters.continueItem);
   15. want.parameters.continueItem && AppStorage.setOrCreate('videoSelect', want.parameters.continueItem);
   16. want.parameters.flag && AppStorage.setOrCreate('flag', want.parameters.flag);
   17. AppStorage.setOrCreate('continue', true);
   18. AppStorage.setOrCreate('continueRestore', true);
   19. want.parameters.pageUrl && AppStorage.setOrCreate('pageUrl', want.parameters.pageUrl);
   20. want.parameters.scrollDistance && AppStorage.setOrCreate('scrollDistance', want.parameters.scrollDistance);
   21. want.parameters.breakpoint && AppStorage.setOrCreate('continueBreakpoint', want.parameters.breakpoint);

   23. try {
   24. this.context.restoreWindowStage(new LocalStorage());
   25. } catch (e) {
   26. hilog.error(0x000, 'progress', `restoreWindowStage error ${JSON.stringify(e)}`);
   27. }
   28. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L75-L103)

## 长列表进度接续

### 场景描述

在社交媒体、新闻资讯等应用中，用户经常需要浏览长列表内容。当用户滚动到列表的某个位置后，可能会切换设备，且切换后希望自动恢复到之前的滚动位置，避免重复操作。开发者可以利用接续能力提升此类场景的用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/qsBmTNkrTDqoo_guJXLyrQ/zh-cn_image_0000002591568722.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=808423030BFB1423B4E189597D066400BDBABFDC103FBF4AA7553AF951709803 "点击放大")

### 实现原理

长列表通常用于存储大量信息，可以通过List、Grid、Scroll、WaterFlow等组件进行封装。系统提供了分布式迁移标识，以便在使用这些组件时恢复进度状态。这种方式调用便捷，使用示例如下：

```
1. WaterFlow({ footer: this.footStyle, scroller: this.waterFlowScroller }) {
2. // ...
3. }
4. .restoreId(1)
```

[WaterFlowView.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/WaterFlowView.ets#L131-L217)

然而，该方法存在局限性，具体支持的场景和版本详见[分布式迁移标识](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/分布式迁移标识/ts-universal-attributes-restoreid.md)的说明。若需在开发中进行更多自定义设置以提升用户体验，可参考以下步骤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/wu2b3fP-STKSX4ialswOgA/zh-cn_image_0000002622128325.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=A2F0091AD1C68CFD8E92C5DE9B44A040A85B9A09FFCF8A83971BC1F762FF2C57 "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 在Scroll组件的[onDidScroll()](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md#ondidscroll12)接口中监听长列表的浏览进度变化。

   ```
   1. Scroll(this.scroller) {
   2. // ...
   3. .onDidScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
   4. if (!this.setCurrentOffset) {
   5. this.currentOffset = this.scroller.currentOffset().yOffset;
   6. }
   7. })
   ```

   [HomeContent.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/HomeContent.ets#L192-L223)
3. 在UIAbility的onContinue()回调中，将进度相关数据保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在[onDidBuild()](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期（推荐）/ts-custom-component-new-lifecycle.md#ondidbuild)事件中恢复浏览状态。

   ```
   1. onDidBuild(): void {
   2. hilog.info(0x000, 'progress', `onDidBuild ${this.setCurrentOffset} ${this.continueOffset}`);
   3. if (this.setCurrentOffset) {
   4. this.scroller.scrollTo({ xOffset: 0, yOffset: this.continueOffset });
   5. this.setCurrentOffset = false;
   6. }
   7. }
   ```

   [HomeContent.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/HomeContent.ets#L107-L114)

## 媒体播放进度接续

### 场景描述

在视频播放场景中，用户可能会在观看视频的过程中切换至其他设备，例如从手机切换到平板/PC等大屏设备。用户切换设备后期望能从之前的播放位置继续观看而非重新开始播放。针对此类场景，开发者可以通过接续功能提升用户观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/_uqLCU2nQImIySkoEyzlaA/zh-cn_image_0000002591728656.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=82A01FAC0246B9AE3E65B23AA30F0B54511F4A730E45B0CB157AE54DACF4FD2C "点击放大")

### 实现原理

媒体播放接续的内容主要包括播放列表中的集数、播放状态和进度。此外，还可以接续其他播放设置，以进一步提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/y2TUke83S5CXsw7aMR-M_A/zh-cn_image_0000002622048215.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=84E31878104B25E4EAE79949F9A0AAB926104DEB71E79483670D1FD2D9200D3B "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用avPlayer.on('timeUpdate')接口来监听媒体播放进度的变化。

   ```
   1. this.avPlayer.on('timeUpdate', (time: number) => {
   2. if (this.isSliderAction) {
   3. return;
   4. }
   5. this.currentTime = time;
   6. AppStorage.set('currentTime', this.currentTime)
   7. });
   ```

   [AvPlayManager.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/viewmodel/video/AvPlayManager.ets#L182-L188)
3. 在UIAbility的onContinue()回调中，将当前播放时间this.time保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility中的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在avPlayer初始化完成后，判断当前为接续状态，调用封装的调整视频进度方法videoSeek()，恢复至接续前的播放状态。

   ```
   1. if (this.continue) {
   2. this.videoSeek(continueTime);
   3. this.continue = false;
   4. AppStorage.set('continue', false);
   5. }
   ```

   [AvPlayManager.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/viewmodel/video/AvPlayManager.ets#L135-L139)

## Web浏览进度接续

### 场景描述

在Web网页浏览场景中，用户可能会在浏览网页的过程中切换至其他设备。用户切换后期望能恢复到之前的网页URL和滚动位置，以保持浏览上下文的连续性。针对此类场景，开发者可以利用接续功能，进一步提升用户的浏览体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/exr1vKuIQEytJ8p-38FuWA/zh-cn_image_0000002591568746.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=1CA0058D39B0C631D2BA84327FD420DC9109601CAA81CEA3D4393E61A245F2D8 "点击放大")

### 实现原理

系统提供的Web组件用于在应用程序中展示Web页面内容。当Web组件加载大量信息时，保持浏览进度的连续性尤为重要。为了实现内容的连续展示，需要像处理长列表一样，通过传递当前的滚动位置来维持这一连续性。这可以通过使用[runJavaScript()](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#runjavascript>)接口来获取和恢复滚动位置来实现。具体步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Eouzv9pKSuq-6p4pfJtTcw/zh-cn_image_0000002622128349.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T021219Z&HW-CC-Expire=86400&HW-CC-Sign=9A676F77E84B3903F83612C85CD973769A2DFC2144E3BF5D2EB0148CE4E4C3B1 "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用onTouch()事件监听屏幕滑动，并通过runJavaScript()接口获取页面滚动条距离顶部的距离。
3. 在onContinue()回调中，将this.scrollDistance保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在onPageEnd()回调中调用runJavaScript()接口以恢复进度。

   ```
   1. Web({ src: this.pageUrl, controller: this.controller })
   2. // ...
   3. .onPageEnd(async () => {
   4. // ...
   5. if (this.pageUrl.includes('product_list') && this.continueRestore) {
   6. this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop = ' +
   7. this.scrollDistance);
   8. }
   9. this.pageUrl = this.controller.getUrl();
   10. let result =
   11. await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
   12. this.scrollDistance = Number(result);
   13. })
   14. // ...
   15. .onTouch(async (event: TouchEvent) => {
   16. if (event.type === TouchType.Up) {
   17. if (this.pageUrl.includes('product_list')) {
   18. let result =
   19. await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
   20. this.scrollDistance = Number(result);
   21. }
   22. }
   23. })
   ```

   [WebPageComponent.ets](https://gitcode.com/HarmonyOS_Samples/continue-progress/blob/master/entry/src/main/ets/view/web/WebPageComponent.ets#L130-L175)

## 示例代码

* [实现浏览进度接续功能](https://gitcode.com/harmonyos_samples/continue-progress)
