---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-face-detector
title: 人脸检测
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 人脸检测
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:53+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:880c3658765a371e240b20659a779a65fd5af3766ccbbd3fe8b832d7f7d4f84d
---
## 适用场景

检测图片中的人脸，返回高精度人脸矩形框坐标、人脸五官位置、人脸朝向、人脸置信度。可通过对人脸的定位，实现对人脸特定位置的美化修饰。广泛应用于各类人脸识别场景，如人脸聚类、美颜等场景中。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/oLsnshOoQdSNgr2V0LXR2g/zh-cn_image_0000002592219742.png?HW-CC-KV=V1&HW-CC-Date=20260611T071752Z&HW-CC-Expire=86400&HW-CC-Sign=197472AD0A62B7C875F1261592E0A94E6498B1407F3F2CFC6CD099DBB1F5924F)

## 世界坐标系

以下方图片指示坐标系辅助表示人脸朝向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/U9jXx6c4QrONuGGO-MrI7w/zh-cn_image_0000002592379676.png?HW-CC-KV=V1&HW-CC-Date=20260611T071752Z&HW-CC-Expire=86400&HW-CC-Sign=EE9F2C4886DBDEA7F6C209AC147EEE764F207918B224763A028C438924565E99)

## 开发步骤

1. 在使用人脸检测时，将实现人脸检测相关的类添加至工程。

   ```
   1. import { faceDetector } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 初始化和释放：在aboutToAppear中调用[faceDetector.init()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceDetector（人脸检测）/core-vision-face-detector-api.md#facedetectorinit>)初始化人脸检测分析器（加载模型），在aboutToDisappear中调用[faceDetector.release()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceDetector（人脸检测）/core-vision-face-detector-api.md#facedetectorrelease>)释放资源。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await faceDetector.init();
   3. hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await faceDetector.release();
   8. hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
   9. }
   ```
3. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，使用fileIo与image模块将URI转换为[PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，为后续检测接口准备输入数据。

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
   3. if (!uri) {
   4. hilog.error(0x0000, 'faceDetectorSample', 'Failed to get uri.');
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
   16. }).then(res => {
   17. resolve(res.photoUris[0]);
   18. }).catch((err: BusinessError) => {
   19. hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
   20. resolve('');
   21. });
   22. });
   23. }

   25. private loadImage(name: string) {
   26. setTimeout(async () => {
   27. let imageSource: image.ImageSource | undefined = undefined;
   28. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
   29. imageSource = image.createImageSource(fileSource.fd);
   30. this.chooseImage = await imageSource.createPixelMap();
   31. this.dataValues = '';
   32. await fileIo.close(fileSource);
   33. }, 100);
   34. }
   ```
4. 构造[VisionInfo](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceDetector（人脸检测）/core-vision-face-detector-api.md#visioninfo>)对象并传入待检测图片的PixelMap，调用[faceDetector.detect](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceDetector（人脸检测）/core-vision-face-detector-api.md#facedetectordetect>)方法，获取人脸位置、五官、朝向等检测结果并展示在界面上。

   ```
   1. Button('人脸检测')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. if (!this.chooseImage) {
   9. hilog.error(0x0000, 'faceDetectorSample', 'Failed to detect face.');
   10. return;
   11. }
   12. // 调用人脸检测接口
   13. let visionInfo: faceDetector.VisionInfo = {
   14. pixelMap: this.chooseImage
   15. };
   16. faceDetector.detect(visionInfo)
   17. .then((data: faceDetector.Face[]) => {
   18. if (data.length === 0) {
   19. this.dataValues = 'No face is detected in the image. Select an image that contains a face.';
   20. } else {
   21. let faceString = JSON.stringify(data);
   22. hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
   23. this.dataValues = faceString;
   24. }
   25. })
   26. .catch((error: BusinessError) => {
   27. hilog.error(0x0000, 'faceDetectorSample', `Face detection failed. Code: ${error.code}, message: ${error.message}`);
   28. this.dataValues = `Error: ${error.message}`;
   29. });
   30. })
   ```

## 开发实例

### Index.ets

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. @State chooseImage: PixelMap | undefined = undefined;
12. @State dataValues: string = '';

14. async aboutToAppear(): Promise<void> {
15. const initResult = await faceDetector.init();
16. hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);
17. }

19. async aboutToDisappear(): Promise<void> {
20. await faceDetector.release();
21. hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
22. }

24. build() {
25. Column() {
26. Image(this.chooseImage)
27. .objectFit(ImageFit.Fill)
28. .height('60%')
29. Text(this.dataValues)
30. .copyOption(CopyOptions.LocalDevice)
31. .height('15%')
32. .margin(10)
33. .width('60%')
34. Button('选择图片')
35. .type(ButtonType.Capsule)
36. .fontColor(Color.White)
37. .alignSelf(ItemAlign.Center)
38. .width('80%')
39. .margin(10)
40. .onClick(() => {
41. // 拉起图库
42. void this.selectImage();
43. })
44. Button('人脸检测')
45. .type(ButtonType.Capsule)
46. .fontColor(Color.White)
47. .alignSelf(ItemAlign.Center)
48. .width('80%')
49. .margin(10)
50. .onClick(() => {
51. if (!this.chooseImage) {
52. hilog.error(0x0000, 'faceDetectorSample', 'Failed to detect face.');
53. return;
54. }
55. // 调用人脸检测接口
56. let visionInfo: faceDetector.VisionInfo = {
57. pixelMap: this.chooseImage
58. };
59. faceDetector.detect(visionInfo)
60. .then((data: faceDetector.Face[]) => {
61. if (data.length === 0) {
62. this.dataValues = 'No face is detected in the image. Select an image that contains a face.';
63. } else {
64. let faceString = JSON.stringify(data);
65. hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
66. this.dataValues = faceString;
67. }
68. })
69. .catch((error: BusinessError) => {
70. hilog.error(0x0000, 'faceDetectorSample', `Face detection failed. Code: ${error.code}, message: ${error.message}`);
71. this.dataValues = `Error: ${error.message}`;
72. });
73. })
74. }
75. .width('100%')
76. .height('100%')
77. .justifyContent(FlexAlign.Center)
78. }

80. private async selectImage() {
81. let uri = await this.openPhoto();
82. if (!uri) {
83. hilog.error(0x0000, 'faceDetectorSample', 'Failed to get uri.');
84. return;
85. }
86. this.loadImage(uri);
87. }

89. private async openPhoto(): Promise<string> {
90. return new Promise<string>((resolve) => {
91. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
92. photoPicker.select({
93. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
94. maxSelectNumber: 1
95. }).then(res => {
96. resolve(res.photoUris[0]);
97. }).catch((err: BusinessError) => {
98. hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
99. resolve('');
100. });
101. });
102. }

104. private loadImage(name: string) {
105. setTimeout(async () => {
106. let imageSource: image.ImageSource | undefined = undefined;
107. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
108. imageSource = image.createImageSource(fileSource.fd);
109. this.chooseImage = await imageSource.createPixelMap();
110. this.dataValues = '';
111. await fileIo.close(fileSource);
112. }, 100);
113. }
114. }
```
