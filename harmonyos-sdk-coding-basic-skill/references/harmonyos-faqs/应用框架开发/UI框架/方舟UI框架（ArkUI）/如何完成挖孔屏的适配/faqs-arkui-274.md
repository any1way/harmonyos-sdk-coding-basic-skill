---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-274
title: 如何完成挖孔屏的适配
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何完成挖孔屏的适配
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:17+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:06dd75900c0f99d346af67a3db83fe80f833da288319465c1dae6a777252171d
---

1. 使用setWindowLayoutFullScreen和setWindowSystemBarEnable将窗口设置为全屏并隐藏顶部状态栏。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. AppStorage.setOrCreate('context', this.context);
   3. windowStage.getMainWindow((err: BusinessError, window: window.Window) => {
   4. // The settings window is displayed in full screen
   5. window.setWindowLayoutFullScreen(true)
   6. .then(() => {
   7. console.info('Succeeded in setting the window layout to full-screen mode.');
   8. }).catch((err: BusinessError) => {
   9. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
   10. });
   11. // Set the top status bar to be hidden
   12. let names: Array<'status' | 'navigation'> = [];
   13. window.setWindowSystemBarEnable(names)
   14. .then(() => {
   15. console.info('Succeeded in setting the system bar to be invisible.');
   16. }).catch((err: BusinessError) => {
   17. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
   18. });
   19. })
   20. // ...
   21. }
   ```

   [EntryAbilityExtactScreenAdaption.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityExtactScreenAdaption.ets#L42-L62)
2. 使用getDefaultDisplaySync获取同步display对象，再通过其异步方法getCutoutInfo回调获取挖孔区域信息，然后根据这些信息计算偏移量，实现对不可用区域的适配。

   ```
   1. import { display, window } from '@kit.ArkUI';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError, batteryInfo } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. class TextMargin {
   7. left: number = 0; // Status bar left offset
   8. right: number = 0; // Status bar right offset
   9. }

   11. @Entry
   12. @Component
   13. struct Index {
   14. @State date: Date = new Date();
   15. @State currentTime: string = ''; // Top status bar time
   16. @State boundingRect: display.Rect[] = []; // Unavailable area data
   17. @State screenWidth: number = 0; // Screen width
   18. @State displayClass: display.Display | null = null;
   19. @State topTextMargin: TextMargin = { left: 0, right: 0 }; // Top status bar offset
   20. @StorageLink('context') context: common.UIAbilityContext | undefined = AppStorage.get('context'); // Get UIAbilityContext

   22. aboutToAppear(): void {
   23. try {
   24. this.displayClass = display.getDefaultDisplaySync();
   25. display.getDefaultDisplaySync().getCutoutInfo((err, data) => {
   26. if (err.code) {
   27. console.log('getCutoutInfo failed. error is:', JSON.stringify(err));
   28. return;
   29. }
   30. this.boundingRect = data.boundingRects;
   31. this.topTextMargin = this.getBoundingRectPosition();
   32. })
   33. } catch (error) {
   34. let err = error as BusinessError;
   35. hilog.error(0x000, 'testTag', `err.code=${err.code}, err.message=${err.message}`);
   36. }
   37. // Get hour
   38. let hours = this.date.getHours();
   39. // Get minute
   40. let minutes = this.date.getMinutes();
   41. // Add 0 before minute if less than 10
   42. this.currentTime = hours.toString() + ':' + (minutes < 10 ? '0' + minutes : minutes.toString());
   43. }

   45. // Reset window to initial state when leaving the page
   46. aboutToDisappear() {
   47. if (this.context !== undefined) {
   48. window.getLastWindow(this.context, async (err, data) => {
   49. if (err.code) {
   50. console.log('getLastWindow failed. error is:', JSON.stringify(err));
   51. return;
   52. }
   53. data.setWindowSystemBarEnable(['status', 'navigation'])
   54. .then(() => {
   55. hilog.info(0x000, 'testTag', `setWindowSystemBarEnable succeed.`);
   56. })
   57. .catch((err: BusinessError) => {
   58. hilog.error(0x000, 'testTag',
   59. `setWindowSystemBarEnable failed. err.code=${err.code}, err.message=${err.message}`);
   60. })
   61. data.setWindowLayoutFullScreen(false)
   62. .then(() => {
   63. hilog.info(0x000, 'testTag', `setWindowLayoutFullScreen succeed.`);
   64. })
   65. .catch((err: BusinessError) => {
   66. hilog.error(0x000, 'testTag',
   67. `setWindowLayoutFullScreen failed. err.code=${err.code}, err.message=${err.message}`);
   68. })
   69. })
   70. }
   71. }

   73. /**
   74. * Calculate the left and right margins of the unusable areas of the punch hole screen
   75. * @returns {TextMargin} Objects that include left/right offsets
   76. */
   77. getBoundingRectPosition(): TextMargin {
   78. if (this.boundingRect !== null && this.displayClass !== null && this.boundingRect[0] !== undefined) {
   79. // Distance from the right of the unavailable area to the right edge of the screen: screen width minus left width and unavailable area width
   80. let boundingRectRight: number =
   81. this.displayClass.width - (this.boundingRect[0].left + this.boundingRect[0].width);
   82. // Distance from the left of the unavailable area to the left edge of the screen: can be obtained directly by getCutoutInfo
   83. let boundingRectLeft: number = this.boundingRect[0].left;
   84. // For some devices, if the unavailable area is in the middle, the difference between the left and right distances is less than 10 pixels, treat it as being in the middle
   85. if (Math.abs(boundingRectLeft - boundingRectRight) <= 10) {
   86. return { left: 0, right: 0 };
   87. }
   88. if (boundingRectLeft > boundingRectRight) {
   89. // Unavailable area on the right
   90. return { left: 0, right: this.displayClass.width - boundingRectLeft };
   91. } else if (boundingRectLeft < boundingRectRight) {
   92. // Unavailable area on the left
   93. return { left: this.boundingRect[0].left + this.boundingRect[0].width, right: 0 };
   94. }
   95. }
   96. return { left: 0, right: 0 };
   97. }

   99. build() {
   100. Stack() {
   101. Image($r('app.media.digging_hole_screen_2048game'))
   102. .objectFit(ImageFit.Fill)
   103. .width('100%')
   104. .height('100%')
   105. .onClick(() => {
   106. try {
   107. this.getUIContext().getPromptAction().showToast({
   108. message: 'This function is not yet developed',
   109. duration: 2000
   110. })
   111. } catch (error) {
   112. let err = error as BusinessError;
   113. hilog.error(0x000, 'testTag', `showToast failed. err.code=${err.code}, err.message=${err.message}`);
   114. }
   115. })
   116. Column() {
   117. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) {
   118. Text(this.currentTime) // Time
   119. .fontSize(16)
   120. .fontColor(Color.Black)
   121. .fontWeight(FontWeight.Regular)
   122. .padding({ left: 12 })
   123. .margin({
   124. left: this.getUIContext().px2vp(this.topTextMargin.left),
   125. top: 14
   126. }) // The obtained offset is in px and needs to be converted
   127. Text(batteryInfo.batterySOC.toString() + '%')// Battery level
   128. .fontSize(16)
   129. .fontColor(Color.Black)
   130. .fontWeight(FontWeight.Regular)
   131. .padding({ right: 16 })
   132. .margin({
   133. right: this.getUIContext().px2vp(this.topTextMargin.right),
   134. top: 14
   135. }) // The obtained offset is in px and needs to be converted
   136. }
   137. .width('100%')
   138. }
   139. .width('100%')
   140. }
   141. .width('100%')
   142. .height('100%')
   143. .alignContent(Alignment.TopStart)
   144. }
   145. }
   ```

   [ExcavationScreenAdaptation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ExcavationScreenAdaptation.ets#L21-L165)
