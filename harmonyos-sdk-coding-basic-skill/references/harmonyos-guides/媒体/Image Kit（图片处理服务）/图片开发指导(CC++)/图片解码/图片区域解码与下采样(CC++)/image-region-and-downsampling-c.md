---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-region-and-downsampling-c
title: 图片区域解码与下采样(C/C++)
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 图片区域解码与下采样(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:57:04+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:4ea8ca9c3f9659deb23c609659895248f4223697d7100fbbbc0054595b4021b9
---
应用在处理大尺寸图片时，直接解码整张图片可能导致内存占用过高和解码耗时较长。通过区域解码和下采样解码功能，可以有效优化这一场景：

* **区域解码**：仅解码图片的指定矩形区域，适用于需要查看图片局部的场景。
* **下采样解码**：按期望尺寸解码图片，解码器自动选择最优采样率，适用于大图预览场景。

**适用场景**：

| 场景 | 推荐方式 | 说明 |
| --- | --- | --- |
| 图片局部放大查看 | 区域解码 | 只解码需要查看的区域。 |
| 大图预览（如4K图片在手机屏幕显示） | 下采样解码 | 降低分辨率，减少内存占用。 |
| 地图/全景图瓦片加载 | 组合使用 | 指定区域并指定输出尺寸。 |

## 区域解码

区域解码通过设置解码参数cropRegion，指定需要解码的矩形区域。解码器仅解码该区域的数据。参数详情请参考[Image\_Region](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/结构体/Image_Region/capi-image-nativemodule-image-region.md>)。

说明

Native C版本区域解码需使用OH\_DecodingOptions\_SetCropRegion接口，而非SetDesiredRegion。SetDesiredRegion接口不生效。

### 开发步骤

1. 参考[使用Image\_NativeModule完成图片解码](../使用Image_NativeModule完成图片解码/image-source-c.md)创建OH\_ImageSourceNative实例。
2. 设置cropRegion参数执行区域解码。

   ```
   1. // 区域解码示例。
   2. napi_value DecodeRegion(napi_env env, napi_callback_info info)
   3. {
   4. OH_DecodingOptions *ops = nullptr;
   5. OH_DecodingOptions_Create(&ops);

   7. // 设置裁剪区域参数，使用SetCropRegion实现区域解码。
   8. Image_Region region = {
   9. .x = 0,
   10. .y = 0,
   11. .width = 1000,
   12. .height = 1000
   13. };
   14. OH_DecodingOptions_SetCropRegion(ops, &region);

   16. OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
   17. g_thisImageSource->resPixMap = nullptr;

   19. Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
   20. ops, &g_thisImageSource->resPixMap);
   21. OH_DecodingOptions_Release(ops);
   22. ops = nullptr;

   24. if (errCode != IMAGE_SUCCESS) {
   25. OH_LOG_ERROR(LOG_APP, "DecodeRegion failed, errCode: %{public}d.", errCode);
   26. return GetJsResult(env, errCode);
   27. }
   28. OH_LOG_INFO(LOG_APP, "DecodeRegion succeeded.");
   29. return GetJsResult(env, errCode);
   30. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L241-L272)

### 使用限制

* 区域坐标和大小必须在原图范围内。
* 区域大小必须为正整数。

## 下采样解码

下采样解码通过设置解码参数desiredSize，指定期望输出的图片尺寸。解码器会根据期望尺寸输出PixelMap，减少最终的内存占用。

**解码处理差异**：

* **JPEG、PNG、HEIF格式**：解码过程中采用下采样策略，按最优采样率解码，解码效率更高。
* **其他格式**：先完整解码原图，再缩放至期望尺寸。

参数详情请参考[OH\_DecodingOptions](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/结构体/OH_DecodingOptions/capi-image-nativemodule-oh-decodingoptions.md>)。

### 开发步骤

1. 参考[图片开发指导(C/C++)](../使用Image_NativeModule完成图片解码/image-source-c.md)创建OH\_ImageSourceNative实例。
2. 设置desiredSize参数执行下采样解码。

   ```
   1. // 下采样解码示例。
   2. napi_value DownsampleDecode(napi_env env, napi_callback_info info)
   3. {
   4. OH_DecodingOptions *ops = nullptr;
   5. OH_DecodingOptions_Create(&ops);

   7. // 设置期望输出大小参数。
   8. Image_Size desiredSize = {
   9. .width = 512,
   10. .height = 512
   11. };
   12. OH_DecodingOptions_SetDesiredSize(ops, &desiredSize);

   14. OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
   15. g_thisImageSource->resPixMap = nullptr;

   17. Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
   18. ops, &g_thisImageSource->resPixMap);
   19. OH_DecodingOptions_Release(ops);
   20. ops = nullptr;

   22. if (errCode != IMAGE_SUCCESS) {
   23. OH_LOG_ERROR(LOG_APP, "DownsampleDecode failed, errCode: %{public}d.", errCode);
   24. return GetJsResult(env, errCode);
   25. }
   26. OH_LOG_INFO(LOG_APP, "DownsampleDecode succeeded.");
   27. return GetJsResult(env, errCode);
   28. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L274-L303)

## 区域解码与下采样组合使用

当同时设置cropRegion和desiredSize时，需要通过cropAndScaleStrategy参数指定裁剪与缩放的先后顺序。

### cropAndScaleStrategy策略

| 策略 | 常量值 | 操作顺序 | 说明 |
| --- | --- | --- | --- |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_SCALE\_FIRST | 1 | 先缩放，再裁剪。 | - |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST | 2 | 先裁剪，再缩放。 | 推荐使用，可减少解码峰值内存。 |

**推荐使用CROP\_FIRST**：先裁剪再缩放可精确控制裁剪区域，保证不同格式解码效果一致。

参数详情请参考[Image\_CropAndScaleStrategy](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/头文件/image_source_native.h/capi-image-source-native-h.md#image_cropandscalestrategy>)。

### 开发步骤

1. 参考[图片开发指导(C/C++)](../使用Image_NativeModule完成图片解码/image-source-c.md)创建OH\_ImageSourceNative实例。
2. 同时设置cropRegion、desiredSize和cropAndScaleStrategy参数。

   ```
   1. // 区域解码与下采样组合使用示例。
   2. napi_value CombinedDecode(napi_env env, napi_callback_info info)
   3. {
   4. OH_DecodingOptions *ops = nullptr;
   5. OH_DecodingOptions_Create(&ops);

   7. Image_Region region = {
   8. .x = 1000,
   9. .y = 500,
   10. .width = 2000,
   11. .height = 2000
   12. };
   13. OH_DecodingOptions_SetCropRegion(ops, &region);

   15. Image_Size desiredSize = {
   16. .width = 512,
   17. .height = 512
   18. };
   19. OH_DecodingOptions_SetDesiredSize(ops, &desiredSize);

   21. OH_DecodingOptions_SetCropAndScaleStrategy(ops, IMAGE_CROP_AND_SCALE_STRATEGY_CROP_FIRST);

   23. OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
   24. g_thisImageSource->resPixMap = nullptr;

   26. Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
   27. ops, &g_thisImageSource->resPixMap);
   28. OH_DecodingOptions_Release(ops);
   29. ops = nullptr;

   31. if (errCode != IMAGE_SUCCESS) {
   32. OH_LOG_ERROR(LOG_APP, "CombinedDecode failed, errCode: %{public}d.", errCode);
   33. return GetJsResult(env, errCode);
   34. }
   35. OH_LOG_INFO(LOG_APP, "CombinedDecode succeeded.");
   36. return GetJsResult(env, errCode);
   37. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L305-L343)

## 注意事项

* 同时设置cropRegion和desiredSize时，建议设置cropAndScaleStrategy为IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST，以保证解码效果一致。
* 对于原始像素内存超过2GB的图片，建议使用下采样解码避免内存溢出。
