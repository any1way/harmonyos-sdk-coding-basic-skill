---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speech-aicaption-guide
title: AI字幕控件
breadcrumb: 指南 > AI > Speech Kit（场景化语音服务） > AI字幕控件
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:34+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:4d3c9e79de0afb723b26cd036b26d6c758670673e02b84b32f9d7b0c997bd2b9
---
## 适用场景

AI字幕控件应用广泛，例如在用户不熟悉音频源语言或者静音的时候，为用户提供字幕服务。

本章节将向您介绍如何使用AI字幕组件[AICaptionComponent](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md>)和[AICaptionController](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md#aicaptioncontroller>)展示AI字幕，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/prFtRRh6SxmUfD9aM1bgWQ/zh-cn_image_0000002622699357.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071933Z&HW-CC-Expire=86400&HW-CC-Sign=404E00E330BA42061EF1E60874FF87FC1A6BCAB4ADD6F9EBC3A196E74C6EE6EF)

## 接口说明

AI字幕功能主要由[AICaptionComponent](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md>)提供，更多接口及使用方法请参见[API参考](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md>)。

| 接口 | 描述 |
| --- | --- |
| [AICaptionComponent](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md>) | AI字幕组件。 |
| [AICaptionOptions](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md#aicaptionoptions>) | AI字幕初始化参数。 |
| [AICaptionController](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md#aicaptioncontroller>) | AI字幕组件的控制器，是AI字幕组件的主要功能入口类，用来操作AI字幕。它所承载的工作包括：写音频数据、获取音频流信息等。 |

## 开发步骤

1. 从项目根目录进入/src/main/ets/pages/Index.ets文件，在使用AI字幕控件前，将实现AI字幕控件和其他相关的类添加至工程。

   ```
   1. import { AICaptionComponent, AICaptionController, AICaptionOptions,AICaptionFontSize } from '@kit.SpeechKit';
   ```
2. 简单配置页面的布局，加入AI字幕组件，并在aboutToAppear中设置AI字幕组件的传入参数。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'AI_CAPTION_DEMO';

   5. class Logger {
   6. static info(...msg: string[]) {
   7. hilog.info(0x0000, TAG, msg.join());
   8. }

   10. static error(...msg: string[]) {
   11. hilog.error(0x0000, TAG, msg.join());
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct Index {
   18. private captionOption ?: AICaptionOptions;
   19. private controller = new AICaptionController();
   20. @State isShown: boolean = false;

   22. aboutToAppear(): void {
   23. // AI字幕初始化参数，设置字幕的不透明度和回调函数
   24. this.captionOption = {
   25. initialOpacity: 1,
   26. onPrepared: () => {
   27. Logger.info('onPrepared')
   28. },
   29. onError: (error) => {
   30. Logger.error(`onError, code: ${error.code}, msg: ${error.message}`)
   31. },
   32. // 源语言
   33. sourceLanguage: 'zh',
   34. // 目标语言
   35. targetLanguage: 'zh',
   36. // 字体大小
   37. fontSize: AICaptionFontSize.NORMAL,
   38. // 字体颜色
   39. fontColor: Color.Black
   40. };
   41. }

   43. build() {
   44. Column({ space: 20 }) {
   45. // 调用AICaptionComponent组件初始化字幕
   46. AICaptionComponent({
   47. isShown: this.isShown,
   48. controller: this.controller,
   49. options: this.captionOption
   50. })
   51. .width('100%')
   52. .height(100)
   53. Divider()
   54. if (this.isShown) {
   55. Text('上面是字幕区域')
   56. .fontColor(Color.White)
   57. }
   58. }
   59. .width('100%')
   60. .height('100%')
   61. .padding(10)
   62. .backgroundColor('#7A7D6A')
   63. }
   64. }
   ```
3. 在布局中加入两个按钮以及点击事件的回调函数。

   * 第一个按钮的回调函数负责控制AI字幕组件的显示状态。
   * 第二个按钮的回调函数负责读取资源目录中的音频文件，将音频数据传给AI字幕组件。

   ```
   1. import { AudioData } from '@kit.SpeechKit';

   3. @Entry
   4. @Component
   5. struct Index {

   7. isReading: boolean = false;

   9. async readPcmAudio() {
   10. this.isReading = true;
   11. let fileData: Uint8Array | undefined = undefined;
   12. try {
   13. fileData =
   14. await this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent($r('app.media.chineseAudio').id);
   15. } catch (e) {
   16. Logger.info(`get fileData fail , msg ${e} `)
   17. }
   18. if (fileData === undefined) {
   19. return;
   20. }
   21. const bufferSize = 640;
   22. const byteLength = fileData.byteLength;
   23. let offset = 0;
   24. Logger.info('byteLength', byteLength.toString());
   25. let startTime = new Date().getTime();
   26. while (offset < byteLength) {
   27. // 模拟实际情况，读文件比录音机返回流快，所以要等待一段时间
   28. let nextOffset = offset + bufferSize;
   29. if (offset > byteLength) {
   30. this.isReading = false;
   31. return;
   32. }
   33. const arrayBuffer = fileData.buffer.slice(offset, nextOffset);
   34. let data = new Uint8Array(arrayBuffer);
   35. Logger.info('data byteLength', data.byteLength.toString());
   36. const audioData: AudioData = {
   37. data: data
   38. };
   39. Logger.info(`offset: ${offset} | byteLength: ${byteLength} | bufferSize: ${bufferSize}`);

   41. if (this.controller) {
   42. Logger.info(`writeAudio: ${audioData.data.byteLength}`);
   43. try {
   44. this.controller.writeAudio(audioData);
   45. } catch (e) {
   46. Logger.error(`writeAudio exception`);
   47. }
   48. }
   49. offset = offset + bufferSize;
   50. const waitTime = bufferSize / 32;
   51. await this.sleep(waitTime);
   52. }
   53. let endTime = new Date().getTime();
   54. this.isReading = false;
   55. Logger.info('playtime', JSON.stringify(endTime - startTime));
   56. }

   58. async sleep(time: number): Promise<void> {
   59. return new Promise(resolve => setTimeout(resolve, time));
   60. }

   62. build() {
   63. Column({ space: 20 }) {
   64. // ...
   65. Button('切换字幕显示状态：' + (this.isShown ? '显示' : '隐藏'))
   66. .backgroundColor('#B8BDA0')
   67. .width(200)
   68. .onClick(() => {
   69. this.isShown = !this.isShown;
   70. })
   71. Button('读取PCM音频')
   72. .backgroundColor('#B8BDA0')
   73. .width(200)
   74. .onClick(() => {
   75. if (!this.isReading) {
   76. void this.readPcmAudio();
   77. }
   78. })
   79. // ...
   80. }
   81. }
   82. }
   ```

## 开发实例

Index.ets

```
1. import { AICaptionComponent, AICaptionOptions, AICaptionController, AudioData,AICaptionFontSize } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = 'AI_CAPTION_DEMO';

7. class Logger {
8. static info(...msg: string[]) {
9. hilog.info(0x0000, TAG, msg.join());
10. }

12. static error(...msg: string[]) {
13. hilog.error(0x0000, TAG, msg.join());
14. }
15. }

17. @Entry
18. @Component
19. struct Index {
20. private captionOption?: AICaptionOptions;
21. private controller: AICaptionController = new AICaptionController();
22. @State isShown: boolean = false;
23. isReading: boolean = false;

25. aboutToAppear(): void {
26. // AI字幕初始化参数，设置字幕的不透明度和回调函数
27. this.captionOption = {
28. initialOpacity: 1,
29. onPrepared: () => {
30. Logger.info('onPrepared')
31. },
32. onError: (error: BusinessError) => {
33. Logger.error(`AICaption component error. Error code: ${error.code}, message: ${error.message}`);
34. },
35. // 源语言
36. sourceLanguage: 'zh',
37. // 目标语言
38. targetLanguage: 'zh',
39. // 字体大小
40. fontSize: AICaptionFontSize.NORMAL,
41. // 字体颜色
42. fontColor: Color.Black
43. };
44. }

46. async readPcmAudio() {
47. this.isReading = true;
48. // ChineseAudio.pcm文件放在entry\src\main\resources\base\media路径下
49. let fileData: Uint8Array | undefined = undefined;
50. try {
51. fileData =
52. await this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent($r('app.media.ChineseAudio').id);
53. } catch (e) {
54. Logger.info(`get fileData fail , msg ${e} `);
55. }
56. if (fileData === undefined) {
57. return;
58. }
59. const bufferSize = 640;
60. const byteLength = fileData.byteLength;
61. let offset = 0;
62. Logger.info(`Pcm data total bytes: ${byteLength.toString()}`);
63. let startTime = new Date().getTime();
64. while (offset < byteLength) {
65. // 模拟实际情况，读文件比录音机返回流快，所以要等待一段时间
66. let nextOffset = offset + bufferSize;
67. if (offset > byteLength) {
68. this.isReading = false;
69. return;
70. }
71. const arrayBuffer = fileData.buffer.slice(offset, nextOffset);
72. let data = new Uint8Array(arrayBuffer);
73. const audioData: AudioData = {
74. data: data
75. };

77. if (this.controller) {
78. try {
79. this.controller.writeAudio(audioData);
80. } catch (e) {
81. Logger.error(`writeAudio exception`);
82. }
83. }
84. offset = offset + bufferSize;
85. const waitTime = bufferSize / 32;
86. await this.sleep(waitTime);
87. }
88. let endTime = new Date().getTime();
89. this.isReading = false;
90. Logger.info(`Audio play time: ${JSON.stringify(endTime - startTime)}`);
91. }

93. async sleep(time: number): Promise<void> {
94. return new Promise(resolve => setTimeout(resolve, time))
95. }

97. build() {
98. Column({ space: 20 }) {
99. Button('切换字幕显示状态：' + (this.isShown ? '显示' : '隐藏'))
100. .backgroundColor('#B8BDA0')
101. .width(200)
102. .onClick(() => {
103. this.isShown = !this.isShown;
104. })
105. Button('读取PCM音频')
106. .backgroundColor('#B8BDA0')
107. .width(200)
108. .onClick(() => {
109. if (!this.isReading) {
110. void this.readPcmAudio();
111. }
112. })
113. Divider()
114. // 调用AICaptionComponent组件初始化字幕
115. AICaptionComponent({
116. isShown: this.isShown,
117. controller: this.controller,
118. options: this.captionOption
119. })
120. .width('100%')
121. .height(100)
122. Divider()
123. if (this.isShown) {
124. Text('上面是字幕区域')
125. .fontColor(Color.White)
126. }
127. }
128. .width('100%')
129. .height('100%')
130. .padding(10)
131. .backgroundColor('#7A7D6A')
132. }
133. }
```
