---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-c
title: 使用Image_NativeModule完成位图操作
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用Image_NativeModule完成位图操作
category: harmonyos-guides
scraped_at: 2026-06-01T11:30:05+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:060a6a03a5795f4a730864cca15b01abe13dcc856a7fb64e8acbb0e6dc8d7b73
---
创建位图，获取位图的宽、高、pixelFormat、alphaType、rowStride信息、对位图进行操作以及释放位图实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libpixelmap.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image_NativeModule/capi-image-nativemodule.md>)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**位图接口使用示例**

在初始化参数后创建Pixelmap实例，进行图片像素数据的读写，对图片进行缩放、位置变换、反转、旋转、裁剪等操作。

```
1. #include <hilog/log.h>
2. #include <multimedia/image_framework/image/pixelmap_native.h>

4. #undef LOG_DOMAIN
5. #undef LOG_TAG
6. #define LOG_DOMAIN 0x3200
7. #define LOG_TAG "MY_TAG"

9. Image_ErrorCode PixelmapTest()
10. {
11. uint8_t data[96];
12. size_t dataSize = 96;
13. for (int i = 0; i < dataSize; i++) {
14. data[i] = i + 1;
15. }

17. // 创建参数结构体实例，并设置参数。
18. OH_Pixelmap_InitializationOptions *createOpts;
19. OH_PixelmapInitializationOptions_Create(&createOpts);
20. OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
21. OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
22. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
23. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);

25. // 创建Pixelmap实例。
26. OH_PixelmapNative *pixelmap = nullptr;
27. Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &pixelmap);

29. // 读取图像像素数据，结果写入数组里。
30. uint8_t destination[96];
31. size_t destinationSize = 96;
32. errCode = OH_PixelmapNative_ReadPixels(pixelmap, destination, &destinationSize);
33. if (errCode != IMAGE_SUCCESS) {
34. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_ReadPixels failed, errCode: %{public}d.", errCode);
35. return errCode;
36. }

38. // 读取缓冲区中的图片数据，结果写入Pixelmap中。
39. uint8_t source[96];
40. size_t sourceSize = 96;
41. for (int i = 0; i < sourceSize; i++) {
42. source[i] = i + 1;
43. }
44. errCode = OH_PixelmapNative_WritePixels(pixelmap, source, sourceSize);
45. if (errCode != IMAGE_SUCCESS) {
46. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_WritePixels failed, errCode: %{public}d.", errCode);
47. return errCode;
48. }

50. // 创建图片信息实例，并获取图像像素信息。
51. OH_Pixelmap_ImageInfo *imageInfo;
52. OH_PixelmapImageInfo_Create(&imageInfo);
53. errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
54. if (errCode != IMAGE_SUCCESS) {
55. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_GetImageInfo failed, errCode: %{public}d.", errCode);
56. return errCode;
57. }

59. // 获取图片的宽，高，pixel格式，透明度等信息。
60. uint32_t width, height, rowStride;
61. int32_t pixelFormat, alphaType;
62. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
63. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
64. OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
65. OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
66. OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
67. OH_PixelmapImageInfo_Release(imageInfo);
68. OH_LOG_INFO(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest GetImageInfo success, width: %{public}d, height: %{public}d, rowStride: %{public}d, pixelFormat: %{public}d, alphaType: %{public}d.", width, height, rowStride, pixelFormat, alphaType);

70. // 设置透明比率来让Pixelmap达到对应的透明效果。
71. errCode = OH_PixelmapNative_Opacity(pixelmap, 0.5);
72. if (errCode != IMAGE_SUCCESS) {
73. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Opacity failed, errCode: %{public}d.", errCode);
74. return errCode;
75. }

77. // 对图片进行缩放。
78. errCode = OH_PixelmapNative_Scale(pixelmap, 2.0, 1.0);
79. if (errCode != IMAGE_SUCCESS) {
80. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Scale failed, errCode: %{public}d.", errCode);
81. return errCode;
82. }

84. // 对图片进行位置变换。
85. errCode = OH_PixelmapNative_Translate(pixelmap, 50.0, 10.0);
86. if (errCode != IMAGE_SUCCESS) {
87. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Translate failed, errCode: %{public}d.", errCode);
88. return errCode;
89. }

91. // 对图片进行旋转。
92. errCode = OH_PixelmapNative_Rotate(pixelmap, 90.0);
93. if (errCode != IMAGE_SUCCESS) {
94. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Rotate failed, errCode: %{public}d.", errCode);
95. return errCode;
96. }

98. // 对图片进行翻转。
99. errCode = OH_PixelmapNative_Flip(pixelmap, true, true);
100. if (errCode != IMAGE_SUCCESS) {
101. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Flip failed, errCode: %{public}d.", errCode);
102. return errCode;
103. }

105. // 对图片进行裁剪。
106. Image_Region region;
107. region.x = 100;
108. region.y = 100;
109. region.width = 6;
110. region.height = 4;
111. errCode = OH_PixelmapNative_Crop(pixelmap, &region);
112. if (errCode != IMAGE_SUCCESS) {
113. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Crop failed, errCode: %{public}d.", errCode);
114. return errCode;
115. }

117. // 释放Pixelmap, InitializationOptions实例。
118. OH_PixelmapNative_Release(pixelmap);
119. OH_PixelmapInitializationOptions_Release(createOpts);
120. return IMAGE_SUCCESS;
121. }

123. // PixelMap预乘/非预乘格式转换示例。
124. Image_ErrorCode PixelmapConvertAlphaTypeTest()
125. {
126. uint8_t data[96];
127. size_t dataSize = 96;
128. for (int i = 0; i < dataSize; i++) {
129. data[i] = i + 1;
130. }

132. // 创建参数结构体实例，并设置参数。
133. OH_Pixelmap_InitializationOptions *createOpts;
134. OH_PixelmapInitializationOptions_Create(&createOpts);
135. OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
136. OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
137. OH_PixelmapInitializationOptions_SetSrcPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
138. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
139. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNPREMULTIPLIED);

141. // 创建非预乘格式的位图实例。
142. OH_PixelmapNative *SrcPixelmap = nullptr;
143. Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &SrcPixelmap);
144. if (errCode != IMAGE_SUCCESS) {
145. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest CreateSrcPixelMap failed, errCode: %{public}d.", errCode);
146. }

148. // 创建预乘格式的位图实例，该DstPixelmap实例将用于保存SrcPixelmap转换AlphaType后的数据。
149. OH_PixelmapNative *DstPixelmap = nullptr;
150. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_PREMULTIPLIED);
151. errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &DstPixelmap);
152. if (errCode != IMAGE_SUCCESS) {
153. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest CreateDstPixelMap failed, errCode: %{public}d.", errCode);
154. }

156. // 转换AlphaType，SrcPixelmap的数据将被转换为预乘格式，并保存到DstPixelmap中。
157. errCode = OH_PixelmapNative_ConvertAlphaFormat(SrcPixelmap, DstPixelmap, true);
158. if (errCode != IMAGE_SUCCESS) {
159. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest ConvertAlphaFormat failed, errCode: %{public}d.", errCode);
160. }

162. // 释放Pixelmap，InitializationOptions实例。
163. OH_PixelmapNative_Release(SrcPixelmap);
164. OH_PixelmapNative_Release(DstPixelmap);
165. OH_PixelmapInitializationOptions_Release(createOpts);
166. return errCode;
167. }
```

**提取图片平均颜色示例**

通过将图片缩放到较小尺寸，遍历所有像素计算RGB平均值来获取图片的主色调。

```
1. #include <cmath>
2. #include <hilog/log.h>
3. #include <multimedia/image_framework/image/pixelmap_native.h>
4. // 颜色结构体。
5. struct AverageColor {
6. uint8_t r;
7. uint8_t g;
8. uint8_t b;
9. };

11. // 提取图片平均颜色。
12. // 基本思路：
13. // 1. 将原始PixelMap缩放到较小尺寸（如32像素×32像素），减少像素数量以提高计算效率。
14. // 2. 读取缩放后的像素数据。
15. // 3. 遍历所有像素，累加R、G、B通道的值。
16. // 4. 计算各通道的平均值作为最终颜色。
17. Image_ErrorCode ExtractAverageColor(OH_PixelmapNative* pixelmap, AverageColor& avgColor)
18. {
19. if (pixelmap == nullptr) {
20. OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: pixelmap is nullptr");
21. return IMAGE_BAD_PARAMETER;
22. }

24. // 获取原始图片信息，判断是否需要缩放。
25. OH_Pixelmap_ImageInfo* imageInfo;
26. OH_PixelmapImageInfo_Create(&imageInfo);
27. Image_ErrorCode errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
28. if (errCode != IMAGE_SUCCESS) {
29. OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: GetImageInfo failed, errCode: %{public}d", errCode);
30. OH_PixelmapImageInfo_Release(imageInfo);
31. return errCode;
32. }

34. uint32_t width, height;
35. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
36. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
37. OH_PixelmapImageInfo_Release(imageInfo);

39. // 定义缩小后的目标尺寸（32像素×32像素是经验值，平衡性能和准确度）。
40. const uint32_t SAMPLE_SIZE = 32;

42. // 如果图片较大，先进行缩放处理。
43. if (width > SAMPLE_SIZE || height > SAMPLE_SIZE) {
44. // 计算缩放比例。
45. double scaleX = (double)SAMPLE_SIZE / width;
46. double scaleY = (double)SAMPLE_SIZE / height;

48. // 对图片进行缩放。
49. errCode = OH_PixelmapNative_Scale(pixelmap, scaleX, scaleY);
50. if (errCode != IMAGE_SUCCESS) {
51. OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: Scale failed, errCode: %{public}d", errCode);
52. OH_PixelmapNative_Release(pixelmap);
53. return errCode;
54. }
55. } else {
56. // 图片较小，直接使用原图。
57. pixelmap = pixelmap;
58. }

60. // 重新获取缩放后的图片信息。
61. OH_PixelmapImageInfo_Create(&imageInfo);
62. errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
63. if (errCode != IMAGE_SUCCESS) {
64. OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: GetImageInfo after scale failed, errCode: %{public}d", errCode);
65. OH_PixelmapImageInfo_Release(imageInfo);
66. return errCode;
67. }

69. uint32_t scaledWidth, scaledHeight, rowStride;
70. int32_t pixelFormat, alphaType;
71. OH_PixelmapImageInfo_GetWidth(imageInfo, &scaledWidth);
72. OH_PixelmapImageInfo_GetHeight(imageInfo, &scaledHeight);
73. OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
74. OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
75. OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
76. OH_PixelmapImageInfo_Release(imageInfo);
77. if (pixelFormat != PIXEL_FORMAT_RGBA_8888) {
78. // 此案例中只处理RGBA格式。
79. return IMAGE_BAD_SOURCE;
80. }

82. // 读取像素数据。
83. size_t bufferSize = rowStride * scaledHeight;
84. uint8_t* pixelData = new uint8_t[bufferSize];
85. errCode = OH_PixelmapNative_ReadPixels(pixelmap, pixelData, &bufferSize);
86. if (errCode != IMAGE_SUCCESS) {
87. OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: ReadPixels failed, errCode: %{public}d", errCode);
88. delete[] pixelData;
89. return errCode;
90. }

92. // 根据像素格式确定每像素字节数。
93. constexpr int bytesPerPixel = 4; // 默认RGBA_8888

95. // 累加RGB值。
96. uint64_t totalR = 0, totalG = 0, totalB = 0;
97. uint32_t pixelCount = 0;

99. for (uint32_t y = 0; y < scaledHeight; y++) {
100. for (uint32_t x = 0; x < scaledWidth; x++) {
101. size_t offset = y * rowStride + x * bytesPerPixel;
102. // RGBA_8888格式：R-G-B-A
103. totalR += pixelData[offset];
104. totalG += pixelData[offset + 1];
105. totalB += pixelData[offset + 2];
106. pixelCount++;
107. }
108. }

110. // 释放资源。
111. delete[] pixelData;
112. // 计算平均值。
113. if (pixelCount > 0) {
114. avgColor.r = (uint8_t)(totalR / pixelCount);
115. avgColor.g = (uint8_t)(totalG / pixelCount);
116. avgColor.b = (uint8_t)(totalB / pixelCount);
117. } else {
118. avgColor.r = 0;
119. avgColor.g = 0;
120. avgColor.b = 0;
121. }

123. OH_LOG_INFO(LOG_APP,
124. "ExtractAverageColor success, avgColor: R=%{public}d, G=%{public}d, B=%{public}d, pixelCount=%{public}d",
125. avgColor.r, avgColor.g, avgColor.b, pixelCount);

127. return IMAGE_SUCCESS;
128. }
```
