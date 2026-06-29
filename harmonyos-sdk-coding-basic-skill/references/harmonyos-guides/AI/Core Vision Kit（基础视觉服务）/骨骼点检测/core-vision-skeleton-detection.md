---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-skeleton-detection
title: 骨骼点检测
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 骨骼点检测
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:58+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:d46d3bba748acdfc7a9e3a26d8b93ff8d72955d997b4f433ebf6f6fb82c2dc0b
---
## 适用场景

人体骨骼关键点检测，主要检测人体的一些关键点，通过关键点描述人体骨骼信息。具体应用主要集中在智能视频监控，病人监护系统，人机交互，虚拟现实，人体动画，智能家居，智能安防，运动员辅助训练等等。

支持17个关键点的识别，具体为鼻子，左右眼，左右耳，左右肩，左右肘、左右手腕、左右髋、左右膝、左右脚踝。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/uDh98zQlRZy6ys42DRCPbQ/zh-cn_image_0000002592379678.png?HW-CC-KV=V1&HW-CC-Date=20260611T071756Z&HW-CC-Expire=86400&HW-CC-Sign=FCDC636EC157A5F422F4B70272450D818024AE3EA54E82FE3A7F3C5052565FE1)

## 开发步骤

1. 在使用骨骼点检测时，将实现骨骼点检测相关的类添加至工程。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，使用fileIo与image模块将URI转换为[PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，为后续检测接口准备输入数据。

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
   4. hilog.error(0x0000, 'skeletonDetectSample', 'Failed to define uri.');
   5. return;
   6. }
   7. this.loadImage(uri);
   8. }

   10. private async openPhoto(): Promise<string> {
   11. return new Promise<string>((resolve, reject) => {
   12. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   13. photoPicker.select({
   14. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   15. maxSelectNumber: 1
   16. }).then(res => {
   17. resolve(res.photoUris[0]);
   18. }).catch((err: BusinessError) => {
   19. hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
   20. reject(err);
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
3. 实例化visionBase.Request对象，将PixelMap封装为输入参数；调用[SkeletonDetector.create()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/skeletonDetection（骨骼点检测）/core-vision-skeleton-detection-api.md#create>)创建检测器实例，再调用其[process](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/skeletonDetection（骨骼点检测）/core-vision-skeleton-detection-api.md#process>)方法，获取图片中人体的17个关键点信息，并将结果展示在界面上。

   ```
   1. Button('开始骨骼点识别')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. // 调用封装的异步处理函数
   9. void this.handleSkeletonDetection();
   10. })
   ```

   骨骼点识别的方法实现如下：

   ```
   1. private async handleSkeletonDetection() {
   2. if (!this.chooseImage) {
   3. hilog.error(0x0000, 'skeletonDetectSample', 'Failed to choose image.');
   4. return;
   5. }
   6. // 调用骨骼点识别接口
   7. let request: visionBase.Request = {
   8. inputData: { pixelMap: this.chooseImage }
   9. };
   10. let detector = await skeletonDetection.SkeletonDetector.create();
   11. let data: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);
   12. let poseJson = JSON.stringify(data);
   13. hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
   14. this.dataValues = poseJson;
   15. }
   ```

## 开发实例

### Index.ets

```
1. import { image } from '@kit.ImageKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. private imageSource: image.ImageSource | undefined = undefined;
12. @State chooseImage: PixelMap | undefined = undefined;
13. @State dataValues: string = '';

15. build() {
16. Column() {
17. Image(this.chooseImage)
18. .objectFit(ImageFit.Fill)
19. .height('60%')

21. Text(this.dataValues)
22. .copyOption(CopyOptions.LocalDevice)
23. .height('15%')
24. .margin(10)
25. .width('60%')

27. Button('选择图片')
28. .type(ButtonType.Capsule)
29. .fontColor(Color.White)
30. .alignSelf(ItemAlign.Center)
31. .width('80%')
32. .margin(10)
33. .onClick(() => {
34. // 拉起图库
35. void this.selectImage();
36. })

38. Button('开始骨骼点识别')
39. .type(ButtonType.Capsule)
40. .fontColor(Color.White)
41. .alignSelf(ItemAlign.Center)
42. .width('80%')
43. .margin(10)
44. .onClick(() => {
45. // 调用封装的异步处理函数
46. void this.handleSkeletonDetection();
47. })
48. }
49. .width('100%')
50. .height('100%')
51. .justifyContent(FlexAlign.Center)
52. }

54. // 封装骨骼点识别的异步逻辑
55. private async handleSkeletonDetection() {
56. if (!this.chooseImage) {
57. hilog.error(0x0000, 'skeletonDetectSample', 'Failed to choose image.');
58. return;
59. }
60. // 调用骨骼点识别接口
61. let request: visionBase.Request = {
62. inputData: { pixelMap: this.chooseImage }
63. };
64. let detector = await skeletonDetection.SkeletonDetector.create();
65. let data: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);
66. let poseJson = JSON.stringify(data);
67. hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
68. this.dataValues = poseJson;
69. }

71. private async selectImage() {
72. let uri = await this.openPhoto();
73. if (!uri) {
74. hilog.error(0x0000, 'skeletonDetectSample', 'Failed to define uri.');
75. return;
76. }
77. this.loadImage(uri);
78. }

80. private async openPhoto(): Promise<string> {
81. return new Promise<string>((resolve, reject) => {
82. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
83. photoPicker.select({
84. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
85. maxSelectNumber: 1
86. }).then(res => {
87. resolve(res.photoUris[0]);
88. }).catch((err: BusinessError) => {
89. hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
90. reject(err);
91. });
92. });
93. }

95. private loadImage(name: string) {
96. setTimeout(async () => {
97. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
98. this.imageSource = image.createImageSource(fileSource.fd);
99. this.chooseImage = await this.imageSource.createPixelMap();
100. await fileIo.close(fileSource);
101. }, 100);
102. }
103. }
```
