---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-subject-segmentation
title: 主体分割
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 主体分割
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:55+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:80eb25cf8d24411a4ff448f41856d57a677c2df791988ff6da36726afde6397e
---
## 适用场景

主体分割，可以检测出图片中区别于背景的前景物体或区域（即"显著主体"），并将其从背景中分离出来，适用于需要识别和提取图像主要信息的场景，广泛使用于前景目标检测和前景主体分离的场景。例如：

* 主体贴纸，从图片中提取显著性的主体，去掉背景。
* 背景替换，替换并提取出主体对象的背景。
* 显著性检测，快速定位图片中显著性区域。
* 辅助图片编辑，例如单独对主体进行美化处理。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/mdl3oH95SQmQLYHd0GtWIg/zh-cn_image_0000002622699305.png?HW-CC-KV=V1&HW-CC-Date=20260611T071754Z&HW-CC-Expire=86400&HW-CC-Sign=93DF1C7717EF2A5F0ECC14ECDBC65B8AE7E554E5E743CFCBEBC355431B37B91D)

## 开发步骤

1. 引用相关类添加至工程。

   ```
   1. import { subjectSegmentation } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 初始化和释放：在aboutToAppear中调用[subjectSegmentation.init()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/subjectSegmentation（主体分割）/core-vision-subjectsegmentation-api.md#subjectsegmentationinit>)初始化主体分割服务（加载模型），在aboutToDisappear中调用[subjectSegmentation.release()](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/subjectSegmentation（主体分割）/core-vision-subjectsegmentation-api.md#subjectsegmentationrelease>)释放资源。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await subjectSegmentation.init();
   3. hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await subjectSegmentation.release();
   8. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
   9. }
   ```
3. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，使用fileIo与image模块将URI转换为[PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，为后续分割接口准备输入数据。

   ```
   1. private async selectImage() {
   2. let uri = await this.openPhoto();
   3. if (uri === undefined) {
   4. hilog.error(0x0000, TAG, 'uri is undefined');
   5. return;
   6. }
   7. this.loadImage(uri);
   8. }

   10. private async openPhoto(): Promise<Array<string>> {
   11. return new Promise<Array<string>>((resolve, reject) => {
   12. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   13. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
   14. photoSelectOptions.maxSelectNumber = 1;
   15. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   16. photoPicker.select(photoSelectOptions).then((photoSelectResult) => {
   17. hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, photoSelectResult uri: ${photoSelectResult.photoUris}`);
   18. resolve(photoSelectResult.photoUris);
   19. }).catch((err: BusinessError) => {
   20. hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
   21. reject(err);
   22. });
   23. });
   24. }

   26. private loadImage(names: string[]) {
   27. setTimeout(async () => {
   28. let imageSource: image.ImageSource | undefined = undefined;
   29. let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
   30. imageSource = image.createImageSource(fileSource.fd);
   31. this.chooseImage = await imageSource.createPixelMap();
   32. await fileIo.close(fileSource);
   33. }, 100);
   34. }
   ```
4. 实例化[VisionInfo](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/subjectSegmentation（主体分割）/core-vision-subjectsegmentation-api.md#visioninfo>)并传入待检测图片的PixelMap，同时配置[SegmentationConfig](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/subjectSegmentation（主体分割）/core-vision-subjectsegmentation-api.md#segmentationconfig>)，设置最大主体个数、是否输出详细信息与前景图。

   ```
   1. let visionInfo: subjectSegmentation.VisionInfo = {
   2. pixelMap: this.chooseImage
   3. };
   4. let config: subjectSegmentation.SegmentationConfig = {
   5. maxCount: parseInt(this.maxNum),
   6. enableSubjectDetails: true,
   7. enableSubjectForegroundImage: true
   8. };
   ```
5. 调用subjectSegmentation的[subjectSegmentation.doSegmentation](<../../../../harmonyos-references/Core Vision Kit（基础视觉服务）/ArkTS API/subjectSegmentation（主体分割）/core-vision-subjectsegmentation-api.md#subjectsegmentationdosegmentation>)接口实现主体分割，并将结果展示在界面上。

   ```
   1. Button('Image Segmentation')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. if (!this.chooseImage) {
   9. hilog.error(0x0000, TAG, 'imageSegmentation not have chooseImage');
   10. return;
   11. }
   12. let visionInfo: subjectSegmentation.VisionInfo = {
   13. pixelMap: this.chooseImage
   14. };
   15. let config: subjectSegmentation.SegmentationConfig = {
   16. maxCount: parseInt(this.maxNum),
   17. enableSubjectDetails: true,
   18. enableSubjectForegroundImage: true
   19. };
   20. subjectSegmentation.doSegmentation(visionInfo, config)
   21. .then((data: subjectSegmentation.SegmentationResult) => {
   22. // 拼装分割结果信息
   23. let outputString = `Subject count: ${data.subjectCount}\n`;
   24. outputString += `Max subject count: ${config.maxCount}\n`;
   25. outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
   26. let segBox: subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
   27. outputString += `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;

   29. // 拼装每个主体的详细分割信息
   30. if (config.enableSubjectDetails && data.subjectDetails) {
   31. outputString += 'Individual subject boxes:\n';
   32. for (let i = 0; i < data.subjectDetails.length; i++) {
   33. let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
   34. outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
   35. }
   36. }

   38. hilog.info(0x0000, TAG, 'Segmentation result: ' + outputString);
   39. this.dataValues = outputString;

   41. if (data.fullSubject && data.fullSubject.foregroundImage) {
   42. this.segmentedImage = data.fullSubject.foregroundImage;
   43. } else {
   44. hilog.warn(0x0000, TAG, 'No foreground image in segmentation result');
   45. }
   46. })
   47. .catch((error: BusinessError) => {
   48. hilog.error(0x0000, TAG, `Image segmentation failed errCode: ${error.code}, errMessage: ${error.message}`);
   49. this.dataValues = `Error: ${error.message}`;
   50. this.segmentedImage = undefined;
   51. });
   52. })
   ```

## 开发实例

### Index.ets

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. const TAG: string = 'ImageSegmentationSample';

10. @Entry
11. @Component
12. struct Index {
13. @State chooseImage: PixelMap | undefined = undefined;
14. @State dataValues: string = '';
15. @State segmentedImage: PixelMap | undefined = undefined;
16. // 设置识别主体数量的上限
17. @State maxNum: string = '20';

19. async aboutToAppear(): Promise<void> {
20. const initResult = await subjectSegmentation.init();
21. hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
22. }

24. async aboutToDisappear(): Promise<void> {
25. await subjectSegmentation.release();
26. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
27. }

29. build() {
30. Column() {
31. Image(this.chooseImage)
32. .objectFit(ImageFit.Fill)
33. .height('30%')
34. .accessibilityDescription('Image to be segmented')

36. Scroll() {
37. Text(this.dataValues)
38. .copyOption(CopyOptions.LocalDevice)
39. .margin(10)
40. .width('100%')
41. }
42. .height('20%')

44. Image(this.segmentedImage)
45. .objectFit(ImageFit.Fill)
46. .height('30%')
47. .accessibilityDescription('Segmented subject image')

49. Row() {
50. Text('Max subject count:')
51. .fontSize(16)
52. TextInput({ placeholder: 'Enter max subject count', text: this.maxNum })
53. .type(InputType.Number)
54. .placeholderColor(Color.Gray)
55. .fontSize(16)
56. .backgroundColor(Color.White)
57. .onChange((value: string) => {
58. this.maxNum = value;
59. })
60. }
61. .width('80%')
62. .margin(10)

64. Button('Select Image')
65. .type(ButtonType.Capsule)
66. .fontColor(Color.White)
67. .alignSelf(ItemAlign.Center)
68. .width('80%')
69. .margin(10)
70. .onClick(() => {
71. void this.selectImage();
72. })

74. Button('Image Segmentation')
75. .type(ButtonType.Capsule)
76. .fontColor(Color.White)
77. .alignSelf(ItemAlign.Center)
78. .width('80%')
79. .margin(10)
80. .onClick(() => {
81. if (!this.chooseImage) {
82. hilog.error(0x0000, TAG, 'imageSegmentation not have chooseImage');
83. return;
84. }
85. let visionInfo: subjectSegmentation.VisionInfo = {
86. pixelMap: this.chooseImage
87. };
88. let config: subjectSegmentation.SegmentationConfig = {
89. maxCount: parseInt(this.maxNum),
90. enableSubjectDetails: true,
91. enableSubjectForegroundImage: true
92. };
93. subjectSegmentation.doSegmentation(visionInfo, config)
94. .then((data: subjectSegmentation.SegmentationResult) => {
95. // 拼装分割结果信息
96. let outputString = `Subject count: ${data.subjectCount}\n`;
97. outputString += `Max subject count: ${config.maxCount}\n`;
98. outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
99. let segBox: subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
100. outputString += `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;

102. // 拼装每个主体的详细分割信息
103. if (config.enableSubjectDetails && data.subjectDetails) {
104. outputString += 'Individual subject boxes:\n';
105. for (let i = 0; i < data.subjectDetails.length; i++) {
106. let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
107. outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
108. }
109. }

111. hilog.info(0x0000, TAG, 'Segmentation result: ' + outputString);
112. this.dataValues = outputString;

114. if (data.fullSubject && data.fullSubject.foregroundImage) {
115. this.segmentedImage = data.fullSubject.foregroundImage;
116. } else {
117. hilog.warn(0x0000, TAG, 'No foreground image in segmentation result');
118. }
119. })
120. .catch((error: BusinessError) => {
121. hilog.error(0x0000, TAG, `Image segmentation failed errCode: ${error.code}, errMessage: ${error.message}`);
122. this.dataValues = `Error: ${error.message}`;
123. this.segmentedImage = undefined;
124. });
125. })
126. }
127. .width('100%')
128. .height('80%')
129. .justifyContent(FlexAlign.Center)
130. }

132. private async selectImage() {
133. let uri = await this.openPhoto();
134. if (uri === undefined) {
135. hilog.error(0x0000, TAG, 'uri is undefined');
136. return;
137. }
138. this.loadImage(uri);
139. }

141. private async openPhoto(): Promise<Array<string>> {
142. return new Promise<Array<string>>((resolve, reject) => {
143. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
144. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
145. photoSelectOptions.maxSelectNumber = 1;
146. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
147. photoPicker.select(photoSelectOptions).then((photoSelectResult) => {
148. hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, photoSelectResult uri: ${photoSelectResult.photoUris}`);
149. resolve(photoSelectResult.photoUris);
150. }).catch((err: BusinessError) => {
151. hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
152. reject(err);
153. });
154. });
155. }

157. private loadImage(names: string[]) {
158. setTimeout(async () => {
159. let imageSource: image.ImageSource | undefined = undefined;
160. let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
161. imageSource = image.createImageSource(fileSource.fd);
162. this.chooseImage = await imageSource.createPixelMap();
163. await fileIo.close(fileSource);
164. }, 100);
165. }
166. }
```
