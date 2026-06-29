---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-desktop-lyrics
title: 应用接入歌词组件
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 应用接入歌词组件
category: harmonyos-guides
scraped_at: 2026-06-01T11:28:08+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:856fdfba72e7efcb7f86c079195fe21c07c3892d5dc8f4a09c66976cc3ce1cb9
---
从API version 23开始，系统提供歌词组件功能。歌词组件以悬浮窗形式显示于系统桌面，支持歌词内容展示、组件隐藏、组件锁定等操作。暂不支持应用对组件进行自定义样式设置。本文将说明应用接入歌词组件的开发步骤。

## 具体步骤

1. 调用[isDesktopLyricSupported](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Functions/arkts-apis-avsession-f.md#avsessionisdesktoplyricsupported23>)接口判断系统/设备是否支持歌词组件能力，返回true时表示支持歌词组件能力。
2. 创建[AVSession实例](../应用接入AVSession场景介绍/avsession-access-scene.md#创建不同类型的会话)，通过[设置元数据](../应用接入AVSession场景介绍/avsession-access-scene.md#设置元数据)填入LRC格式的歌词数据，包含时间标签及对应的歌词文本。不符合LRC格式的歌词数据，系统可能存在解析异常导致无法展示歌词内容。
3. 调用[enableDesktopLyric](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#enabledesktoplyric23>)接口进行使能，需传入参数true打开歌词组件。
4. 歌词组件使能打开后默认是隐藏（不显示），应用可以通过接口主动显示/隐藏歌词组件，具体接口如下：

   **设置可见性：** 调用[setDesktopLyricVisible](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#setdesktoplyricvisible23>)接口，设置歌词组件是否显示。

   **查询可见性：** 调用[isDesktopLyricVisible](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#isdesktoplyricvisible23>)接口，查询当前歌词组件是否显示。
5. 歌词组件使能打开后默认是非锁定状态，应用可以通过接口主动锁定/解锁歌词组件，具体接口如下：

   **设置锁定状态：** 调用[setDesktopLyricState](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#setdesktoplyricstate23>)接口，设置歌词窗口是否锁定（限制歌词窗口的拖动、设置等操作）。

   **查询锁定状态：** 调用[getDesktopLyricState](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#getdesktoplyricstate23>)接口，查询当前歌词组件锁定状态。
6. 应用可以通过系统提供的回调监听歌词组件可见性、锁定状态的变化，具体接口如下：

   **监听歌词组件是否可见：** 监听[onDesktopLyricVisibilityChanged](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#ondesktoplyricvisibilitychanged23>)，回调返回false，表示当前歌词组件不可见；回调返回true，表示当前歌词组件可见。如需取消该监听，使用[offDesktopLyricVisibilityChanged](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#offdesktoplyricvisibilitychanged23>)接口。

   **监听歌词组件是否锁定：** 监听[onDesktopLyricStateChanged](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#ondesktoplyricstatechanged23>)，回调返回false，表示当前歌词组件未锁定；回调返回true，表示当前歌词组件锁定。如需取消该监听，使用[offDesktopLyricStateChanged](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#offdesktoplyricstatechanged23>)接口。

   说明

   确保AVSession对象在后台播放期间不被系统回收/应用不主动释放，否则会导致歌词组件异常。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'hello world';
   9. // ...

   11. build() {
   12. Column() {
   13. // ...
   14. Text(this.message)
   15. .onClick(async () => {
   16. console.info(`DesktopLyric set start`);
   17. let context = this.getUIContext().getHostContext() as Context;
   18. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');

   21. // 系统是否支持歌词组件
   22. let isDesktopLyricSupported: boolean = false;
   23. try {
   24. isDesktopLyricSupported = await AVSessionManager.isDesktopLyricSupported();
   25. } catch (err) {
   26. console.error(`Failed to get isDesktopLyricSupported. Code: ${err.code}, message: ${err.message}`);
   27. }
   28. if (!isDesktopLyricSupported) {
   29. return;
   30. }

   32. try {
   33. // 使能歌词组件
   34. await session.enableDesktopLyric(true);
   35. } catch (err) {
   36. console.error(`enableDesktopLyric err. Code: ${err.code}, message: ${err.message}`);
   37. }

   39. try {
   40. // 监听歌词组件是否显示
   41. session.onDesktopLyricVisibilityChanged((isVisible: boolean) => {
   42. console.info(`onDesktopLyricVisibilityChanged changed: ${isVisible}`)
   43. });
   44. } catch (err) {
   45. console.error(`onDesktopLyricVisibilityChanged err. Code: ${err.code}, message: ${err.message}`);
   46. }

   48. try {
   49. // 监听歌词组件锁定状态
   50. session.onDesktopLyricStateChanged((state) => {
   51. console.info(`onDesktopLyricStateChanged changed: ${state.isLocked}`)
   52. });
   53. } catch (err) {
   54. console.error(`onDesktopLyricStateChanged err. Code: ${err.code}, message: ${err.message}`);
   55. }

   57. try {
   58. // 显示或隐藏歌词组件，歌词组件使能后默认隐藏
   59. await session.setDesktopLyricVisible(true);
   60. } catch (err) {
   61. console.error(`setDesktopLyricVisible err. Code: ${err.code}, message: ${err.message}`);
   62. }

   64. try {
   65. // 锁定或解锁歌词组件，歌词组件使能后默认是解锁状态
   66. await session.setDesktopLyricState({isLocked: true});
   67. } catch (err) {
   68. console.error(`setDesktopLyricState err. Code: ${err.code}, message: ${err.message}`);
   69. }

   71. console.info(`DesktopLyric set done`);
   72. })
   73. }
   74. .width('100%')
   75. .height('100%')
   76. }
   77. }
   ```

   [DesktopLyric.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/AVSession/LocalAVSession/AVSessionProvider/entry/src/main/ets/pages/DesktopLyric.ets#L16-L121)
