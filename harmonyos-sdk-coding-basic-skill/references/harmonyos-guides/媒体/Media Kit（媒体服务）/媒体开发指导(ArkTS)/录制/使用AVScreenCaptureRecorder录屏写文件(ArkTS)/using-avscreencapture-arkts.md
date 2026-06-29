---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avscreencapture-arkts
title: 使用AVScreenCaptureRecorder录屏写文件(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 录制 > 使用AVScreenCaptureRecorder录屏写文件(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-11T14:57:42+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:4d9c9cd2c4fbeb85c45bd5fa0fe647ede819c43e745067ff2cb0b045eb2c86b6
---
屏幕录制主要为主屏幕录屏功能。

开发者可以调用录屏（[AVScreenCaptureRecorder](<../../../Media Kit简介/media-kit-intro.md#avscreencapture>)）模块的ArkTs接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。可以调用录屏模块获取音视频文件，然后通过文件的形式流转到其他模块进行播放或处理，达成文件形式分享屏幕内容的场景。

录屏模块和窗口（Window）、图形（Graphic）等模块协同完成整个视频采集的流程。

使用AVScreenCaptureRecorder录制屏幕涉及到AVScreenCaptureRecorder实例的创建、音视频采集参数的配置、采集的开始与停止、资源的释放等。

开始屏幕录制时正在通话中或者屏幕录制过程中来电，录屏将自动停止。因通话中断的录屏会上报SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL状态。

本开发指导将以完成一次屏幕数据录制的过程为例，向开发者讲解如何使用AVScreenCaptureRecorder进行屏幕录制，详细的API声明请参考[AVScreenCaptureRecorder](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md>)。

如果配置了采集麦克风音频数据，需对应配置麦克风权限ohos.permission.MICROPHONE和申请长时任务，配置方式请参见[向用户申请权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)、[申请长时任务](<../../../../../应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。
* 当需要读取图片或视频文件时，请优先使用媒体库[Picker选择媒体资源](<../../../../Media Library Kit（媒体文件管理服务）/使用Picker选择媒体库资源/photoaccesshelper-photoviewpicker.md>)。
* 当需要保存图片或视频文件时，请优先使用[安全控件保存媒体资源](<../../../../Media Library Kit（媒体文件管理服务）/保存媒体库资源/photoaccesshelper-savebutton.md>)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK**，实现在屏幕熄灭但不锁屏的场景下，继续保持录制的效果，配置方式请参见[声明权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.CUSTOM\_SCREEN\_RECORDING**，实现在录制屏幕时不再弹出隐私告警弹窗。配置方式请参见[受限开放权限](../../../../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。

  说明

  仅应用需要克隆、备份或同步用户公共目录的图片、视频类文件时，可申请ohos.permission.READ\_IMAGEVIDEO、ohos.permission.WRITE\_IMAGEVIDEO权限来读写音频文件，申请方式请参考[申请受控权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/申请受限权限/declare-permissions-in-acl.md)，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合[特殊场景](../../../../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md#ohospermissionread_imagevideo)的应用被允许申请受限权限。

## 开发步骤及注意事项

使用AVScreenCaptureRecorder时要明确其状态的变化，在创建实例后，调用对应的方法可以进入指定的状态实现对应的行为。在确定的状态下执行不合适的方法会导致AVScreenCaptureRecorder发生错误，开发者需要在调用状态转换的方法前进行状态检查，避免程序运行异常。

1. 添加头文件。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { media } from '@kit.MediaKit';
   3. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 创建AVScreenCaptureRecorder类型的成员变量screenCapture。

   ```
   1. // 声明一个AVScreenCaptureRecorder类型的变量。
   2. private screenCapture?: media.AVScreenCaptureRecorder;
   3. // 创建一个AVScreenCaptureRecorder，并赋值给screenCapture成员变量。
   4. this.screenCapture = await media.createAVScreenCaptureRecorder();
   ```
3. 对成员变量screenCapture设置监听函数，分别监听不同状态和异常情况。

   ```
   1. this.screenCapture.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
   2. switch (infoType) {
   3. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
   4. console.info("录屏成功开始后会收到的回调");
   5. break;
   6. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_CANCELED:
   7. this.screenCapture?.release();
   8. this.screenCapture = undefined;
   9. console.info("不允许使用录屏功能");
   10. break;
   11. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER:
   12. this.screenCapture?.release();
   13. this.screenCapture = undefined;
   14. console.info("通过录屏胶囊结束录屏，底层录制会停止");
   15. break;
   16. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER:
   17. console.info("录屏因其他中断而停止，底层录制会停止");
   18. break;
   19. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_CALL:
   20. console.info("录屏过程因通话中断，底层录制会停止");
   21. break;
   22. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNAVAILABLE:
   23. console.info("录屏麦克风不可用");
   24. break;
   25. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_MUTED_BY_USER:
   26. console.info("录屏麦克风被用户静音");
   27. break;
   28. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER:
   29. console.info("录屏麦克风被用户取消静音");
   30. break;
   31. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE:
   32. // 目前可以从系统直接注册监听到进入隐私场景。
   33. console.info("录屏进入隐私场景");
   34. break;
   35. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE:
   36. console.info("录屏退出隐私场景");
   37. break;
   38. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES:
   39. console.info("用户账号切换，底层录制会停止");
   40. break;
   41. default:
   42. break;
   43. }
   44. })
   45. this.screenCapture.on('error', (err) => {
   46. console.error(`处理异常情况, code is ${err.code}, message is ${err.message}.`);
   47. })
   ```
4. 配置屏幕录制参数。

   ​创建AVScreenCaptureRecorder实例screenCapture后，可以设置屏幕录制所需要的参数。

   ​参数videoBitrate、audioSampleRate、audioChannelCount、audioBitrate、preset、displayId为可选参数，若不设置则可按默认值进行设置，如下示例中提供了可选参数的默认值。麦克风和系统音的音频流共用一套音频参数，分别是音频采样率、音频通道数和音频比特率，对应audioSampleRate、audioChannelCount和audioBitrate参数。

   参数fd可以参考应用文件访问与管理的开发实例[新建并读写一个文件fd](<../../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用文件访问与管理/应用文件访问(ArkTS)/app-file-access.md>)。本示例中提供的getFileFd()仅作为参考。

   2in1设备配置displayId为扩展屏Id，可拉起录屏窗口选择界面，用户在界面上选择录屏内容，最终录屏内容以用户在弹窗界面上的选择为准。

   ```
   1. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. let filePath: string = context.filesDir + '/screenCapture.mp4';
   3. let captureFile: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   4. if (!captureFile) {
   5. console.error("处理异常情况");
   6. return;
   7. }

   9. captureConfig: media.AVScreenCaptureRecordConfig = {
   10. // 开发者可以根据自身的需要设置宽高。
   11. frameWidth: 768,
   12. frameHeight: 1280,
   13. // 参考应用文件访问与管理开发示例新建并读写一个文件fd。
   14. fd: captureFile.fd,
   15. // 可选参数及其默认值。
   16. videoBitrate: 10000000,
   17. audioSampleRate: 48000,
   18. audioChannelCount: 2,
   19. audioBitrate: 96000,
   20. displayId: 0,
   21. preset: media.AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4
   22. };
   ```
5. 基于预先配置的屏幕录制参数，调用[init](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md#init12>)方法初始化screenCapture。

   ```
   1. await this.screenCapture.init(this.captureConfig);
   ```
6. 创建豁免隐私窗口，这里填写的是子窗口id和主窗口id，具体开发步骤可参见窗口API[WindowProperties](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#windowproperties>)。

   ```
   1. let windowIDs = [57, 86];
   2. await this.screenCapture.skipPrivacyMode(windowIDs);
   ```
7. 调用[startRecording](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md#startrecording12>)方法开始进行屏幕录制，并通过监听函数监听状态。

   ```
   1. await this.screenCapture.startRecording();
   ```
8. 停止录屏。

   * 点击录屏胶囊中的结束按钮停止录制：基于回调函数实现，录屏对象实例screenCapture会触发SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER的回调，通知应用此次录屏已停止，不需要开发者主动调用[stopRecording](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md#stoprecording12>)方法。
   * 应用主动调用[stopRecording](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md#stoprecording12>)方法，停止录屏。

     ```
     1. await this.screenCapture.stopRecording();
     ```
9. 调用[release](<../../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md#release12>)方法销毁实例，释放资源。

   ```
   1. await this.screenCapture.release();
   ```

## 完整示例

以下是通过AVScreenCaptureRecorder实现录屏存文件的完整代码示例。

```
1. import { media } from '@kit.MediaKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. export class AVScreenCaptureDemo {
5. private screenCapture?: media.AVScreenCaptureRecorder;
6. private captureFile: fileIo.File | undefined = undefined;
7. private captureConfig: media.AVScreenCaptureRecordConfig | undefined = undefined;

9. private openFile(context: Context): void {
10. const path: string = context.filesDir + '/screenCapture.mp4'; // 文件沙箱路径，文件后缀名应与封装格式对应。
11. this.captureFile = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
12. }

14. private closeFile(): void {
15. if (!this.captureFile) {
16. return;
17. }
18. try {
19. fileIo.closeSync(this.captureFile.fd);
20. } catch (error) {
21. let err = error as BusinessError;
22. console.error(`Failed to close fd, error code: ${err.code}, message: ${err.message}`);
23. }
24. }

26. private setConfig(): void {
27. if (!this.captureFile) {
28. return;
29. }
30. this.captureConfig = {
31. // 开发者可以根据自身的需要设置宽高。
32. frameWidth: 768,
33. frameHeight: 1280,
34. // 参考应用文件访问与管理开发示例新建并读写一个文件fd。
35. fd: this.captureFile.fd,
36. // 可选参数及其默认值。
37. videoBitrate: 10000000,
38. audioSampleRate: 48000,
39. audioChannelCount: 2,
40. audioBitrate: 96000,
41. displayId: 0,
42. preset: media.AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4
43. };
44. }

46. // 注册screenCapture回调函数。
47. private registerScreenCaptureCallback(): void {
48. this.screenCapture?.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
49. switch (infoType) {
50. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
51. console.info("录屏成功开始后会收到的回调");
52. break;
53. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_CANCELED:
54. this.screenCapture?.release();
55. this.screenCapture = undefined;
56. console.info("不允许使用录屏功能");
57. break;
58. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER:
59. this.screenCapture?.release();
60. this.screenCapture = undefined;
61. console.info("通过录屏胶囊结束录屏，底层录制会停止");
62. break;
63. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER:
64. console.info("录屏因其他中断而停止，底层录制会停止");
65. break;
66. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_CALL:
67. console.info("录屏过程因通话中断，底层录制会停止");
68. break;
69. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNAVAILABLE:
70. console.info("录屏麦克风不可用");
71. break;
72. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_MUTED_BY_USER:
73. console.info("录屏麦克风被用户静音");
74. break;
75. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER:
76. console.info("录屏麦克风被用户取消静音");
77. break;
78. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE:
79. // 目前可以从系统直接注册监听到进入隐私场景。
80. console.info("录屏进入隐私场景");
81. break;
82. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE:
83. console.info("录屏退出隐私场景");
84. break;
85. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES:
86. console.info("用户账号切换，底层录制会停止");
87. break;
88. default:
89. break;
90. }
91. })
92. this.screenCapture?.on('error', (err) => {
93. console.error(`处理异常情况, code is ${err.code}, message is ${err.message}.`);
94. })
95. }

97. // 取消注册screenCapture回调函数。
98. private unRegisterScreenCaptureCallback(): void {
99. this.screenCapture?.off('stateChange');
100. this.screenCapture?.off('error');
101. }

103. // 调用startRecording方法可以开始一次录屏存文件的流程，结束录屏可以通过点击录屏胶囊停止按钮进行操作。
104. async startRecording(context: Context): Promise<void> {
105. this.screenCapture = await media.createAVScreenCaptureRecorder();
106. if (!this.screenCapture) {
107. // failed.
108. return;
109. }
110. this.openFile(context);
111. if (!this.captureFile) {
112. console.error("处理异常情况");
113. return;
114. }
115. this.setConfig();
116. await this.screenCapture?.init(this.captureConfig);

118. this.registerScreenCaptureCallback();
119. // 豁免隐私窗口。
120. let windowIDs = [57, 86];
121. await this.screenCapture?.skipPrivacyMode(windowIDs);

123. await this.screenCapture?.startRecording();
124. }

126. // 可以主动调用stopRecording方法来停止录屏。
127. async stopRecording(): Promise<void> {
128. if (!this.screenCapture) {
129. // Error.
130. this.closeFile();
131. return;
132. }

134. await this.screenCapture?.stopRecording();
135. this.unRegisterScreenCaptureCallback();
136. // 调用release()方法销毁实例，释放资源。
137. await this.screenCapture?.release();

139. // 最后需要关闭创建的录屏文件;
140. this.closeFile();
141. }
142. }
```
