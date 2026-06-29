---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-object-detection
title: 多目标识别
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 多目标识别
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:56+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:5a13507175e636d955e77bcbbc35f7b4d2b0c5d8cc46ea1fad0010559eb1f5ce
---
## 适用场景

可同时检测出给定图片中的各种物体，包括风景、动物、植物、建筑、人脸、表格、文本等位置，并框选出物体。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/FY-FtPSQRMSIhLCx0G8qHw/zh-cn_image_0000002592219744.png?HW-CC-KV=V1&HW-CC-Date=20260611T071755Z&HW-CC-Expire=86400&HW-CC-Sign=2FAC13568C7FD85DDF600EE3F678411AA4EC8AB01122F59DF1416C55DE1F0D3D)

## 开发步骤

1. 在使用多目标识别时，将实现多目标识别相关的类添加至工程。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { objectDetection, visionBase } from '@kit.CoreVisionKit';
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
   4. hilog.error(0x0000, 'objectDetectSample', 'Failed to define uri.');
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
   19. hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
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
3. 实例化visionBase.Request对象，将PixelMap封装为输入参数；调用[ObjectDetector.create()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/objectDetection（多目标识别）/core-vision-object-detection-api.md#create>)创建检测器实例，再调用其[process](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/objectDetection（多目标识别）/core-vision-object-detection-api.md#process>)方法，获取图片中各物体的位置与类别信息，并将结果展示在界面上。

   ```
   1. Button('开始多目标识别')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. // 调用封装的异步识别函数
   9. void this.handleMultiObjectDetection();
   10. })
   ```

   多目标识别的方法实现如下：

   ```
   1. private async handleMultiObjectDetection() {
   2. if (!this.chooseImage) {
   3. hilog.error(0x0000, 'objectDetectSample', 'Failed to choose image.');
   4. return;
   5. }
   6. // 调用多目标检测接口
   7. let request: visionBase.Request = {
   8. inputData: { pixelMap: this.chooseImage }
   9. };
   10. let detector = await objectDetection.ObjectDetector.create();
   11. let data: objectDetection.ObjectDetectionResponse = await detector.process(request);
   12. let objectJson = JSON.stringify(data);
   13. hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection: ${objectJson}`);
   14. this.dataValues = objectJson;
   15. }
   ```

## 开发实例

### Index.ets

```
1. import { image } from '@kit.ImageKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { objectDetection, visionBase } from '@kit.CoreVisionKit';
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

38. Button('开始多目标识别')
39. .type(ButtonType.Capsule)
40. .fontColor(Color.White)
41. .alignSelf(ItemAlign.Center)
42. .width('80%')
43. .margin(10)
44. .onClick(() => {
45. // 调用封装的异步识别函数
46. void this.handleMultiObjectDetection();
47. })
48. }
49. .width('100%')
50. .height('100%')
51. .justifyContent(FlexAlign.Center)
52. }

54. // 封装多目标识别的异步逻辑
55. private async handleMultiObjectDetection() {
56. if (!this.chooseImage) {
57. hilog.error(0x0000, 'objectDetectSample', 'Failed to choose image.');
58. return;
59. }
60. // 调用多目标检测接口
61. let request: visionBase.Request = {
62. inputData: { pixelMap: this.chooseImage }
63. };
64. let detector = await objectDetection.ObjectDetector.create();
65. let data: objectDetection.ObjectDetectionResponse = await detector.process(request);
66. let objectJson = JSON.stringify(data);
67. hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection: ${objectJson}`);
68. this.dataValues = objectJson;
69. }

71. private async selectImage() {
72. let uri = await this.openPhoto();
73. if (!uri) {
74. hilog.error(0x0000, 'objectDetectSample', 'Failed to define uri.');
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
89. hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
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
