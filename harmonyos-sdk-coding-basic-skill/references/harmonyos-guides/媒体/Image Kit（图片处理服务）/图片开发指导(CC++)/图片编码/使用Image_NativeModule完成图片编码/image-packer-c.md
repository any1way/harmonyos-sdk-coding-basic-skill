---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-c
title: 使用Image_NativeModule完成图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编码 > 使用Image_NativeModule完成图片编码
category: harmonyos-guides
scraped_at: 2026-06-11T14:57:07+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:f9e7c06a5398d3b70b86a9777c382eabb257164f21d81f66c8f09fc471191ec5
---
图像编码类，用于创建以及释放ImagePacker实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image_NativeModule/capi-image-nativemodule.md>)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

说明

* 根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。
* 部分接口（如：[OH\_ImagePackerNative\_GetSupportedFormats](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/头文件/image_packer_native.h/capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats>)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <string>
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/image_source_native.h>
   4. #include "napi/native_api.h"
   5. #include <multimedia/image_framework/image/image_common.h>
   6. #include <multimedia/image_framework/image/pixelmap_native.h>
   7. #include <set>
   8. #include <multimedia/image_framework/image/image_packer_native.h>
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L15-L28)
2. 日志宏定义可参考下述代码按实际需求自行修改。

   ```
   1. #undef LOG_DOMAIN
   2. #undef LOG_TAG
   3. #define LOG_DOMAIN 0x3200
   4. #define LOG_TAG "IMAGE_SAMPLE"
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L31-L36)
3. 定义ImageSourceNative类。

   ```
   1. class ImageSourceNative {
   2. public:
   3. OH_ImageSource_Info *imageInfo;
   4. OH_ImageSourceNative *source = nullptr;
   5. OH_PixelmapNative *resPixMap = nullptr;
   6. OH_Pixelmap_ImageInfo *pixelmapImageInfo = nullptr;
   7. uint32_t frameCnt = 0;
   8. ImageSourceNative() {}
   9. ~ImageSourceNative() {}
   10. };
   ```

   [imageKits.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/imageKits.h#L61-L72)
4. 创建ImageSourceNative的一个实例。

   ```
   1. static ImageSourceNative *g_thisImageSource = new ImageSourceNative();
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L41-L43)
5. 定义一个全局变量用来记录编码所支持的格式。

   ```
   1. static std::set<std::string> g_encodeSupportedFormats;
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L38-L40)
6. 创建GetJsResult函数处理napi返回值。

   ```
   1. // 处理napi返回值。
   2. napi_value GetJsResult(napi_env env, int result)
   3. {
   4. napi_value resultNapi = nullptr;
   5. napi_create_int32(env, result, &resultNapi);
   6. return resultNapi;
   7. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/napi_init.cpp#L21-L29)
7. 创建ImagePacker实例后，指定编码参数，将ImageSource或PixelMap编码至文件或者缓冲区。

   ```
   1. // 获取编码能力范围。
   2. Image_ErrorCode GetEncodeSupportedFormats()
   3. {
   4. Image_MimeType* mimeType = nullptr;
   5. size_t length = 0;
   6. Image_ErrorCode errCode = OH_ImagePackerNative_GetSupportedFormats(&mimeType, &length);
   7. if (errCode != IMAGE_SUCCESS) {
   8. OH_LOG_ERROR(LOG_APP, "OH_ImagePackerNative_GetSupportedFormats failed,"
   9. "errCode: %{public}d.", errCode);
   10. return errCode;
   11. }
   12. for (size_t count = 0; count < length; count++) {
   13. if (mimeType[count].data != nullptr) {
   14. g_encodeSupportedFormats.insert(std::string(mimeType[count].data));
   15. OH_LOG_INFO(LOG_APP, "Encode supportedFormats: %{public}s", mimeType[count].data);
   16. }
   17. }
   18. return IMAGE_SUCCESS;
   19. }

   21. Image_MimeType GetMimeTypeIfEncodable(const char *format)
   22. {
   23. auto it = g_encodeSupportedFormats.find(format);
   24. if (it == g_encodeSupportedFormats.end()) {
   25. return {const_cast<char *>(""), 0};
   26. }
   27. return {const_cast<char *>(format), strlen(format)};
   28. }

   30. static Image_ErrorCode ReleaseImageSourcePackingResources(OH_ImagePackerNative *testPacker,
   31. OH_PackingOptions *option)
   32. {
   33. Image_ErrorCode errCode = OH_ImagePackerNative_Release(testPacker);
   34. if (errCode != IMAGE_SUCCESS) {
   35. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Release failed,"
   36. "errCode: %{public}d.", errCode);
   37. OH_PackingOptions_Release(option);
   38. return errCode;
   39. }
   40. errCode = OH_PackingOptions_Release(option);
   41. if (errCode != IMAGE_SUCCESS) {
   42. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_PackingOptions_Release failed,"
   43. "errCode: %{public}d.", errCode);
   44. }
   45. return errCode;
   46. }

   48. Image_ErrorCode packToFileFromImageSourceTest(int fd, OH_ImageSourceNative* imageSource)
   49. {
   50. // 创建ImagePacker实例。
   51. OH_ImagePackerNative *testPacker = nullptr;
   52. Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
   53. if (errCode != IMAGE_SUCCESS) {
   54. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Create failed,"
   55. "errCode: %{public}d.", errCode);
   56. return errCode;
   57. }
   58. // 获取编码能力范围。
   59. errCode = GetEncodeSupportedFormats();
   60. if (errCode != IMAGE_SUCCESS) {
   61. OH_ImagePackerNative_Release(testPacker);
   62. return errCode;
   63. }
   64. // 指定编码参数，将ImageSource直接编码进文件。
   65. OH_PackingOptions *option = nullptr;
   66. errCode = OH_PackingOptions_Create(&option);
   67. if (errCode != IMAGE_SUCCESS || option == nullptr) {
   68. OH_ImagePackerNative_Release(testPacker);
   69. return errCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : errCode;
   70. }
   71. Image_MimeType image_MimeType = GetMimeTypeIfEncodable(MIME_TYPE_JPEG);
   72. if (image_MimeType.data == nullptr || image_MimeType.size == 0) {
   73. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest GetMimeTypeIfEncodable failed,"
   74. "format can't support encode.");
   75. OH_PackingOptions_Release(option);
   76. OH_ImagePackerNative_Release(testPacker);
   77. return IMAGE_BAD_PARAMETER;
   78. }
   79. OH_PackingOptions_SetMimeType(option, &image_MimeType);
   80. // 当设备支持HDR编码，资源本身为HDR图且图片资源的格式为jpeg时，编码产物才能为HDR内容。
   81. OH_PackingOptions_SetDesiredDynamicRange(option, IMAGE_PACKER_DYNAMIC_RANGE_AUTO);
   82. // 设置编码质量，quality默认为0，建议quality的值不低于80
   83. uint32_t quality = 90;
   84. OH_PackingOptions_SetQuality(option, quality);
   85. errCode = OH_ImagePackerNative_PackToFileFromImageSource(testPacker, option, imageSource, fd);
   86. if (errCode != IMAGE_SUCCESS) {
   87. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_PackToFileFromImageSource failed,"
   88. "errCode: %{public}d.", errCode);
   89. OH_PackingOptions_Release(option);
   90. OH_ImagePackerNative_Release(testPacker);
   91. return errCode;
   92. }
   93. return ReleaseImageSourcePackingResources(testPacker, option);
   94. }

   96. Image_ErrorCode packToFileFromPixelmapTest(int fd, OH_PixelmapNative *pixelmap)
   97. {
   98. // 创建ImagePacker实例。
   99. OH_ImagePackerNative *testPacker = nullptr;
   100. Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
   101. if (errCode != IMAGE_SUCCESS) {
   102. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest CreatePacker OH_ImagePackerNative_Create failed,"
   103. "errCode: %{public}d.", errCode);
   104. return errCode;
   105. }

   107. // 指定编码参数，将PixelMap直接编码进文件。
   108. OH_PackingOptions *option = nullptr;
   109. errCode = OH_PackingOptions_Create(&option);
   110. if (errCode != IMAGE_SUCCESS || option == nullptr) {
   111. OH_ImagePackerNative_Release(testPacker);
   112. return errCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : errCode;
   113. }
   114. char type[] = "image/jpeg";
   115. Image_MimeType image_MimeType = {type, strlen(type)};
   116. errCode = OH_PackingOptions_SetMimeType(option, &image_MimeType);
   117. if (errCode != IMAGE_SUCCESS) {
   118. OH_PackingOptions_Release(option);
   119. OH_ImagePackerNative_Release(testPacker);
   120. return errCode;
   121. }
   122. // 设置编码质量，quality默认为0，建议quality的值不低于80
   123. uint32_t quality = 90;
   124. OH_PackingOptions_SetQuality(option, quality);
   125. errCode = OH_ImagePackerNative_PackToFileFromPixelmap(testPacker, option, pixelmap, fd);
   126. if (errCode != IMAGE_SUCCESS) {
   127. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_ImagePackerNative_PackToFileFromPixelmap failed,"
   128. "errCode: %{public}d.", errCode);
   129. OH_PackingOptions_Release(option);
   130. OH_ImagePackerNative_Release(testPacker);
   131. return errCode;
   132. }

   134. // 释放ImagePacker实例。
   135. errCode = OH_ImagePackerNative_Release(testPacker);
   136. testPacker = nullptr;
   137. if (errCode != IMAGE_SUCCESS) {
   138. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest ReleasePacker OH_ImagePackerNative_Release failed,"
   139. "errCode: %{public}d.", errCode);
   140. OH_PackingOptions_Release(option);
   141. return errCode;
   142. }

   144. // 释放PackingOptions实例。
   145. errCode = OH_PackingOptions_Release(option);
   146. option = nullptr;
   147. if (errCode != IMAGE_SUCCESS) {
   148. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_PackingOptions_Release failed,"
   149. "errCode: %{public}d.", errCode);
   150. return errCode;
   151. }

   153. return IMAGE_SUCCESS;
   154. }

   156. napi_value PackToFileFromImageSourceTestJs(napi_env env, napi_callback_info info)
   157. {
   158. napi_value argv[1] = {0};
   159. size_t argc = 1;
   160. if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
   161. OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
   162. return nullptr;
   163. }

   165. int fd;
   166. napi_get_value_int32(env, argv[0], &fd);

   168. Image_ErrorCode errCode = packToFileFromImageSourceTest(fd, g_thisImageSource->source);
   169. if (errCode == IMAGE_SUCCESS) {
   170. OH_LOG_INFO(LOG_APP, "ImagePackerNativeCTest PackToFileFromImageSourceTestJs successfully.");
   171. }
   172. return GetJsResult(env, errCode);
   173. }

   175. napi_value PackToFileFromPixelmapTestJs(napi_env env, napi_callback_info info)
   176. {
   177. napi_value argv[1] = {0};
   178. size_t argc = 1;
   179. if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
   180. OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
   181. return nullptr;
   182. }

   184. int fd;
   185. napi_get_value_int32(env, argv[0], &fd);

   187. Image_ErrorCode errCode = packToFileFromPixelmapTest(fd, g_thisImageSource->resPixMap);
   188. if (errCode != IMAGE_SUCCESS) {
   189. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest failed,"
   190. "errCode: %{public}d.", errCode);
   191. return GetJsResult(env, errCode);
   192. } else {
   193. OH_LOG_INFO(LOG_APP, "PackToFileFromPixelmapTestJs successfully.");
   194. }
   195. return GetJsResult(env, errCode);
   196. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L413-L613)
