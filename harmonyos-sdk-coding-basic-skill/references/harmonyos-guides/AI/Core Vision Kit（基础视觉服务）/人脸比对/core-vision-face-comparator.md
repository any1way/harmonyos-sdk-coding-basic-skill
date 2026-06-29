---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-face-comparator
title: 人脸比对
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 人脸比对
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:54+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:80c46af284f5670f6dcca1a718a619ca68933c47f5b2a9970c68420e9b769efe
---
## 适用场景

输入的两张比对图片是同一个人的照片时，系统返回的比对结果为"同一个人"，置信分数比较高；当两张比对图片不是同一个人的照片时，系统返回的比对结果为"非同一个人"，置信分数很低。可以用于APP中需要用到人脸比对功能的场景，比如娱乐类APP中比较两个人的相似度、与明星的相似度等。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RpENqRlCSZSkqvrfBMVwxw/zh-cn_image_0000002622859185.png?HW-CC-KV=V1&HW-CC-Date=20260611T071753Z&HW-CC-Expire=86400&HW-CC-Sign=1B7EF08588B0A84BA29D3B2AA309148E7FC263FECB38A0EAF2DA049EA6A71796)

## 开发步骤

1. 在使用人脸比对时，将实现人脸比对相关的类添加至工程。

   ```
   1. import { faceComparator } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 初始化和释放：在aboutToAppear中调用[faceComparator.init()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceComparator（人脸比对）/core-vision-facecomparator-api.md#facecomparatorinit>)初始化人脸比对分析器（加载模型），在aboutToDisappear中调用[faceComparator.release()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceComparator（人脸比对）/core-vision-facecomparator-api.md#facecomparatorrelease>)释放资源。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await faceComparator.init();
   3. hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await faceComparator.release();
   8. hilog.info(0x0000, TAG, 'Face comparator released successfully');
   9. }
   ```
3. 通过photoAccessHelper.PhotoViewPicker拉起图库选择两张待比对的图片，使用fileIo与image模块将URI转换为[PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，为后续比对接口准备输入数据。

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
   4. hilog.error(0x0000, TAG, 'Failed to get two image uris.');
   5. return;
   6. }
   7. this.loadImage(uri);
   8. }

   10. private async openPhoto(): Promise<string[]> {
   11. return new Promise<string[]>((resolve, reject) => {
   12. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   13. photoPicker.select({
   14. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   15. maxSelectNumber: 2
   16. }).then(res => {
   17. resolve(res.photoUris);
   18. }).catch((err: BusinessError) => {
   19. hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
   20. reject();
   21. });
   22. });
   23. }

   25. private loadImage(names: string[]) {
   26. setTimeout(async () => {
   27. let imageSource: image.ImageSource | undefined = undefined;
   28. let fileSource: fileIo.File;
   29. fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
   30. imageSource = image.createImageSource(fileSource.fd);
   31. this.chooseImage = await imageSource.createPixelMap();
   32. fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
   33. imageSource = image.createImageSource(fileSource.fd);
   34. this.chooseImage1 = await imageSource.createPixelMap();
   35. await fileIo.close(fileSource);
   36. }, 100);
   37. }
   ```
4. 构造[VisionInfo](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceComparator（人脸比对）/core-vision-facecomparator-api.md#visioninfo>)对象并传入两张图片的PixelMap，调用[faceComparator.compareFaces](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/faceComparator（人脸比对）/core-vision-facecomparator-api.md#facecomparatorcomparefaces>)方法，获取相似度分数，并将结果展示在界面上。

   ```
   1. Button('人脸比对')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. if (!this.chooseImage || !this.chooseImage1) {
   9. hilog.error(0x0000, TAG, 'Failed to choose image');
   10. return;
   11. }
   12. // 调用人脸比对接口
   13. let visionInfo: faceComparator.VisionInfo = {
   14. pixelMap: this.chooseImage
   15. };
   16. let visionInfo1: faceComparator.VisionInfo = {
   17. pixelMap: this.chooseImage1
   18. };
   19. faceComparator.compareFaces(visionInfo, visionInfo1)
   20. .then((data: faceComparator.FaceCompareResult) => {
   21. let faceString = `degree of similarity: ${this.toPercentage(data.similarity)}${(data.isSamePerson) ? '. is' : '. no'} same person`;
   22. hilog.info(0x0000, TAG, 'faceString data is ' + faceString);
   23. this.dataValues = faceString;
   24. })
   25. .catch((error: BusinessError) => {
   26. hilog.error(0x0000, TAG, `Face comparison failed. Code: ${error.code}, message: ${error.message}`);
   27. this.dataValues = `Error: ${error.message}`;
   28. });
   29. })
   ```

   相似度数值转百分比展示的辅助方法：

   ```
   1. private toPercentage(num: number): string {
   2. return `${(num * 100).toFixed(2)}%`;
   3. }
   ```

## 开发实例

### Index.ets

```
1. import { faceComparator } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. const TAG: string = 'FaceCompareSample';

10. @Entry
11. @Component
12. struct Index {
13. @State chooseImage: PixelMap | undefined = undefined;
14. @State chooseImage1: PixelMap | undefined = undefined;
15. @State dataValues: string = '';

17. async aboutToAppear(): Promise<void> {
18. const initResult = await faceComparator.init();
19. hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
20. }

22. async aboutToDisappear(): Promise<void> {
23. await faceComparator.release();
24. hilog.info(0x0000, TAG, 'Face comparator released successfully');
25. }

27. build() {
28. Column() {
29. Image(this.chooseImage)
30. .objectFit(ImageFit.Fill)
31. .height('30%')
32. .accessibilityDescription('默认图片1')
33. Image(this.chooseImage1)
34. .objectFit(ImageFit.Fill)
35. .height('30%')
36. .accessibilityDescription('默认图片2')
37. Text(this.dataValues)
38. .copyOption(CopyOptions.LocalDevice)
39. .height('15%')
40. .margin(10)
41. .width('60%')
42. Button('选择图片')
43. .type(ButtonType.Capsule)
44. .fontColor(Color.White)
45. .alignSelf(ItemAlign.Center)
46. .width('80%')
47. .margin(10)
48. .onClick(() => {
49. // 拉起图库
50. void this.selectImage();
51. })
52. Button('人脸比对')
53. .type(ButtonType.Capsule)
54. .fontColor(Color.White)
55. .alignSelf(ItemAlign.Center)
56. .width('80%')
57. .margin(10)
58. .onClick(() => {
59. if (!this.chooseImage || !this.chooseImage1) {
60. hilog.error(0x0000, TAG, 'Failed to choose image');
61. return;
62. }
63. // 调用人脸比对接口
64. let visionInfo: faceComparator.VisionInfo = {
65. pixelMap: this.chooseImage
66. };
67. let visionInfo1: faceComparator.VisionInfo = {
68. pixelMap: this.chooseImage1
69. };
70. faceComparator.compareFaces(visionInfo, visionInfo1)
71. .then((data: faceComparator.FaceCompareResult) => {
72. let faceString = `degree of similarity: ${this.toPercentage(data.similarity)}${(data.isSamePerson) ? '. is' : '. no'} same person`;
73. hilog.info(0x0000, TAG, 'faceString data is ' + faceString);
74. this.dataValues = faceString;
75. })
76. .catch((error: BusinessError) => {
77. hilog.error(0x0000, TAG, `Face comparison failed. Code: ${error.code}, message: ${error.message}`);
78. this.dataValues = `Error: ${error.message}`;
79. });
80. })
81. }
82. .width('100%')
83. .height('100%')
84. .justifyContent(FlexAlign.Center)
85. }

87. private toPercentage(num: number): string {
88. return `${(num * 100).toFixed(2)}%`;
89. }

91. private async selectImage() {
92. let uri = await this.openPhoto();
93. if (uri === undefined) {
94. hilog.error(0x0000, TAG, 'Failed to get two image uris.');
95. return;
96. }
97. this.loadImage(uri);
98. }

100. private async openPhoto(): Promise<string[]> {
101. return new Promise<string[]>((resolve, reject) => {
102. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
103. photoPicker.select({
104. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
105. maxSelectNumber: 2
106. }).then(res => {
107. resolve(res.photoUris);
108. }).catch((err: BusinessError) => {
109. hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
110. reject();
111. });
112. });
113. }

115. private loadImage(names: string[]) {
116. setTimeout(async () => {
117. let imageSource: image.ImageSource | undefined = undefined;
118. let fileSource: fileIo.File;
119. fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
120. imageSource = image.createImageSource(fileSource.fd);
121. this.chooseImage = await imageSource.createPixelMap();
122. fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
123. imageSource = image.createImageSource(fileSource.fd);
124. this.chooseImage1 = await imageSource.createPixelMap();
125. await fileIo.close(fileSource);
126. }, 100);
127. }
128. }
```
