---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-text-recognition
title: 通用文字识别
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 通用文字识别
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:52+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:3230a8c6ebe37a16d4adf524c2e159e66827b95f8be6d95709b5b106b5f1c932
---
## 适用场景

通用文字识别，是通过拍照、扫描等光学输入方式，将各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息的技术。

* 可以对文档翻拍、街景翻拍等图片进行文字检测和识别，也可以集成于其他应用中，提供文字检测、识别的功能，并根据识别结果提供翻译、搜索等相关服务。
* 可以处理来自相机、图库等多种来源的图像数据，提供一个自动检测文本、识别图像中文本位置以及文本内容功能的开放能力。
* 支持特定角度范围内的文本倾斜、拍摄角度倾斜、复杂光照条件以及复杂文本背景等场景的文字识别。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/FmlceYdWQHeLBH-YvwM1Og/zh-cn_image_0000002622699303.png?HW-CC-KV=V1&HW-CC-Date=20260611T071751Z&HW-CC-Expire=86400&HW-CC-Sign=496E5C70B28192D59D72EB72D019032101A130C4D602AA99BE6FCB6CEC908910)

## 开发步骤

1. 在使用通用文字识别时，将实现文字识别的相关的类添加至工程。

   ```
   1. import { textRecognition } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 初始化和释放：在aboutToAppear中调用[textRecognition.init()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/textRecognition（文字识别）/core-vision-text-recognition-api.md#textrecognitioninit>)初始化文字识别服务（加载模型），在aboutToDisappear中调用[textRecognition.release()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/textRecognition（文字识别）/core-vision-text-recognition-api.md#textrecognitionrelease>)释放资源。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await textRecognition.init();
   3. hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await textRecognition.release();
   8. hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
   9. }
   ```
3. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，使用fileIo与image模块将URI转换为[PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，为后续识别接口准备输入数据。

   ```
   1. Button('选择图片')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. // 拉起图库，获取图片资源
   9. void this.selectImage();
   10. })
   ```

   选择图片与解码图片的方法实现如下：

   ```
   1. private async selectImage() {
   2. let uri = await this.openPhoto();
   3. if (uri === undefined) {
   4. hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
   5. return;
   6. }
   7. this.loadImage(uri);
   8. }

   10. private async openPhoto(): Promise<string> {
   11. return new Promise<string>((resolve) => {
   12. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   13. photoPicker.select({
   14. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   15. maxSelectNumber: 1
   16. }).then((res: photoAccessHelper.PhotoSelectResult) => {
   17. resolve(res.photoUris[0]);
   18. }).catch((err: BusinessError) => {
   19. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
   20. resolve('');
   21. });
   22. });
   23. }

   25. private loadImage(name: string) {
   26. setTimeout(async () => {
   27. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
   28. this.imageSource = image.createImageSource(fileSource.fd);
   29. this.chooseImage = await this.imageSource.createPixelMap();
   30. await fileIo.close(fileSource);
   31. }, 100);
   32. }
   ```
4. 构造[VisionInfo](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/textRecognition（文字识别）/core-vision-text-recognition-api.md#visioninfo>)并传入待检测图片的PixelMap，同时配置[TextRecognitionConfiguration](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/textRecognition（文字识别）/core-vision-text-recognition-api.md#textrecognitionconfiguration>)（用于配置是否支持朝向检测），调用[textRecognition.recognizeText](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/textRecognition（文字识别）/core-vision-text-recognition-api.md#textrecognitionrecognizetext-1>)接口，获取图片中文字识别的结果并展示在界面上。

   ```
   1. Button('开始识别')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. this.textRecognitionTest();
   9. })
   ```

   文字识别的方法实现如下：

   ```
   1. private textRecognitionTest() {
   2. if (!this.chooseImage) {
   3. return;
   4. }
   5. // 调用文本识别接口
   6. let visionInfo: textRecognition.VisionInfo = {
   7. pixelMap: this.chooseImage
   8. };
   9. let textConfiguration: textRecognition.TextRecognitionConfiguration = {
   10. isDirectionDetectionSupported: false
   11. };
   12. textRecognition.recognizeText(visionInfo, textConfiguration)
   13. .then((data: textRecognition.TextRecognitionResult) => {
   14. // 识别成功，获取对应的结果
   15. let recognitionString = JSON.stringify(data);
   16. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);
   17. // 将结果更新到Text中显示
   18. this.dataValues = data.value;
   19. })
   20. .catch((error: BusinessError) => {
   21. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
   22. this.dataValues = `Error: ${error.message}`;
   23. });
   24. }
   ```

## 开发实例

点击按钮，识别一张图片的文字内容，并通过日志打印。

### Index.ets

```
1. import { textRecognition } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. private imageSource: image.ImageSource | undefined = undefined;
12. @State chooseImage: PixelMap | undefined = undefined;
13. @State dataValues: string = '';

15. async aboutToAppear(): Promise<void> {
16. const initResult = await textRecognition.init();
17. hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
18. }

20. async aboutToDisappear(): Promise<void> {
21. await textRecognition.release();
22. hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
23. }

25. build() {
26. Column() {
27. Image(this.chooseImage)
28. .objectFit(ImageFit.Fill)
29. .height('60%')

31. Text(this.dataValues)
32. .copyOption(CopyOptions.LocalDevice)
33. .height('15%')
34. .margin(10)
35. .width('60%')

37. Button('选择图片')
38. .type(ButtonType.Capsule)
39. .fontColor(Color.White)
40. .alignSelf(ItemAlign.Center)
41. .width('80%')
42. .margin(10)
43. .onClick(() => {
44. // 拉起图库，获取图片资源
45. void this.selectImage();
46. })

48. Button('开始识别')
49. .type(ButtonType.Capsule)
50. .fontColor(Color.White)
51. .alignSelf(ItemAlign.Center)
52. .width('80%')
53. .margin(10)
54. .onClick(() => {
55. this.textRecognitionTest();
56. })
57. }
58. .width('100%')
59. .height('100%')
60. .justifyContent(FlexAlign.Center)
61. }

63. private textRecognitionTest() {
64. if (!this.chooseImage) {
65. return;
66. }
67. // 调用文本识别接口
68. let visionInfo: textRecognition.VisionInfo = {
69. pixelMap: this.chooseImage
70. };
71. let textConfiguration: textRecognition.TextRecognitionConfiguration = {
72. isDirectionDetectionSupported: false
73. };
74. textRecognition.recognizeText(visionInfo, textConfiguration)
75. .then((data: textRecognition.TextRecognitionResult) => {
76. // 识别成功，获取对应的结果
77. let recognitionString = JSON.stringify(data);
78. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);
79. // 将结果更新到Text中显示
80. this.dataValues = data.value;
81. })
82. .catch((error: BusinessError) => {
83. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
84. this.dataValues = `Error: ${error.message}`;
85. });
86. }

88. private async selectImage() {
89. let uri = await this.openPhoto();
90. if (uri === undefined) {
91. hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
92. return;
93. }
94. this.loadImage(uri);
95. }

97. private async openPhoto(): Promise<string> {
98. return new Promise<string>((resolve) => {
99. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
100. photoPicker.select({
101. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
102. maxSelectNumber: 1
103. }).then((res: photoAccessHelper.PhotoSelectResult) => {
104. resolve(res.photoUris[0]);
105. }).catch((err: BusinessError) => {
106. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
107. resolve('');
108. });
109. });
110. }

112. private loadImage(name: string) {
113. setTimeout(async () => {
114. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
115. this.imageSource = image.createImageSource(fileSource.fd);
116. this.chooseImage = await this.imageSource.createPixelMap();
117. await fileIo.close(fileSource);
118. }, 100);
119. }
120. }
```
