---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-picture-encoding
title: 使用ImagePacker完成多图对象编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编码 > 使用ImagePacker完成多图对象编码
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:51+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:5539137e33fd0fc58f81277dd1a30763f132b265ffcbb447b44091e940e4edd6
---
图片编码指将[Picture](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md>)对象编码成不同格式的图片文件（当前仅支持编码为JPEG 和 HEIF 格式），用于后续处理，如保存、传输等。

## 开发步骤

图片编码相关API的详细介绍请参见[ImagePacker](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImagePacker)/arkts-apis-image-imagepacker.md>)。

1. 导入相关模块包。

   ```
   1. // 导入相关模块。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   ```

   [EncodingPicture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/EncodingPicture.ets#L16-L23)
2. 设置编码选项[PackingOption](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interfaces (其他)/arkts-apis-image-i.md#packingoption>)。

   说明

   这里以编码成jpeg图片为例。编码的目标格式format遵循MIME标准定义，因此PackingOption.format应设置为image/jpeg，编码后的文件扩展名可设为.jpg或.jpeg。

   ```
   1. let packOpts: image.PackingOption = {
   2. format: 'image/jpeg',
   3. quality: 95,
   4. needsPackProperties: true
   5. };
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L39-L45)
3. 封装函数，传入picture，使用[packing](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImagePacker)/arkts-apis-image-imagepacker.md#packing13>)接口编码到ArrayBuffer，或使用[packToFile](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImagePacker)/arkts-apis-image-imagepacker.md#packtofile11-2>)接口编码到文件。

   说明

   在进行编码前，需要先通过解码获取picture，可参考[使用ImageSource完成多图对象解码](../../图片解码/使用ImageSource完成多图对象解码/image-picture-decoding.md)。

   * picture编码到ArrayBuffer。

     ```
     1. async function packing(picture: image.Picture, packOpts: image.PackingOption) {
     2. const imagePackerApi = image.createImagePacker();
     3. try {
     4. let data = await imagePackerApi.packing(picture, packOpts);
     5. copyData = data;
     6. console.info('Succeeded in packing the image.');
     7. } catch (error) {
     8. console.error('Failed to pack the picture to data. And the error is: ' + error);
     9. } finally {
     10. await imagePackerApi.release();
     11. }
     12. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L179-L196)
   * picture编码到文件。

     ```
     1. async function packToFile(picture: image.Picture, packOpts: image.PackingOption, context: Context) {
     2. let imagePackerApi: image.ImagePacker | undefined = undefined;
     3. let file: fileIo.File | undefined = undefined;
     4. try {
     5. const path : string = context.cacheDir + '/picture.jpg';
     6. file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
     7. imagePackerApi = image.createImagePacker();
     8. await imagePackerApi.packToFile(picture, file.fd, packOpts);
     9. } catch (error) {
     10. console.error('Failed to pack the picture to file. And the error is: ' + error);
     11. } finally {
     12. if (file) {
     13. fileIo.closeSync(file.fd);
     14. }
     15. if (imagePackerApi) {
     16. await imagePackerApi.release();
     17. }
     18. }
     19. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L198-L218)
