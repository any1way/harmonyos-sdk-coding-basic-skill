---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-picture-decoding
title: 使用ImageSource完成多图对象解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource完成多图对象解码
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:46+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:ea205edf563321aa194fc7ce09da68e99fe9da6fb3ed7e0c829eb719178d2be5
---
将所支持格式的图片文件解码成[Picture](<../../../Image Kit简介/image-overview.md#基础概念>)多图对象，以便在应用或系统中进行HDR图片显示、辅助图处理等操作。当前支持的图片文件格式包括JPEG、HEIF。

Picture是包含主图、辅助图和元数据的多图对象。主图包含主要图像信息，辅助图用于存储与主图相关的附加信息（如HDR增益图GAINMAP），元数据用于存储与图片相关的其他信息。Picture适用于HDR图片处理、HEIF专业格式解码等场景。

## Picture与PixelMap的区别

Picture和PixelMap是两种不同的图片解码对象，适用于不同的场景：

| 对象类型 | 适用场景 | 特性 |
| --- | --- | --- |
| [PixelMap](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>) | 单图显示、基础图片处理 | 单一像素数据，支持图像变换（裁剪、缩放、旋转等）、位图操作，可直接传给Image组件显示。 |
| [Picture](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md>) | HDR图片、HEIF专业格式、辅助图处理 | 包含主图+辅助图+元数据，可提取主图/增益图/合成HDR图为PixelMap后显示或处理，支持辅助图和元数据操作。 |

**选择建议：**

* 需要直接显示单张图片或进行裁剪、缩放、旋转等图像处理时，使用PixelMap。
* 需要处理HDR图片、获取辅助图（如GAINMAP）、操作图片元数据时，使用Picture。如需对Picture的内容进行裁剪缩放，可通过[getMainPixelmap](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md#getmainpixelmap13>)等方法提取PixelMap后再处理。

## 开发步骤

图片解码相关API的详细介绍请参见[ImageSource](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageSource)/arkts-apis-image-imagesource.md>)。

1. 全局导入Image模块。

   ```
   1. // 导入相关模块。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   ```

   [DecodingPicture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPicture.ets#L16-L23)
2. 获取图片。

   * 方法一：通过沙箱路径直接获取。该方法仅适用于应用沙箱中的图片。更多细节请参考[获取应用文件路径](<../../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#获取应用文件路径>)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](<../../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)。

     ```
     1. function getFilePath(context: Context, fileName: string): string {
     2. const filePath: string = context.cacheDir + '/' + fileName;
     3. return filePath;
     4. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L47-L52)
   * 方法二：通过沙箱路径获取图片的文件描述符。具体请参考文档[@ohos.file.fs (文件管理)](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md>)。该方法需要导入@kit.CoreFileKit模块。

     ```
     1. function getFileFd(context: Context, fileName: string): number | undefined {
     2. try {
     3. const filePath: string = context.cacheDir + '/' + fileName;
     4. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
     5. const fd: number = file?.fd;
     6. return fd;
     7. } catch (err) {
     8. console.error(`Failed to get the fileFd with error: ${err}.`);
     9. return undefined;
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L54-L66)
   * 方法三：通过资源管理器获取资源文件的ArrayBuffer。具体请参考[getRawFileContent](<../../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md#getrawfilecontent9-1>)。该方法需要导入@kit.LocalizationKit模块。

     ```
     1. async function getFileBuffer(context: Context, fileName: string): Promise<ArrayBuffer | undefined> {
     2. try {
     3. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     4. // 获取资源文件内容，返回Uint8Array。
     5. const fileData: Uint8Array = await resourceMgr.getRawFileContent(fileName);
     6. console.info('Successfully get the RawFileContent.');
     7. // 转为ArrayBuffer并返回。
     8. const buffer: ArrayBuffer = fileData.buffer.slice(0);
     9. return buffer;
     10. } catch (error) {
     11. console.error(`Failed to get the RawFileContent with error: ${error}.`);
     12. return undefined;
     13. }
     14. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L68-L83)
   * 方法四：通过资源管理器获取资源文件的RawFileDescriptor。具体请参考[getRawFd](<../../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md#getrawfd9-1>)。该方法需要导入@kit.LocalizationKit模块。

     ```
     1. async function getRawFd(context: Context, fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
     2. try {
     3. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     4. const rawFileDescriptor: resourceManager.RawFileDescriptor = await resourceMgr.getRawFd(fileName);
     5. console.info('Successfully get the RawFileDescriptor.');
     6. return rawFileDescriptor;
     7. } catch (error) {
     8. console.error(`Failed to get the RawFileDescriptor with error: ${error}.`);
     9. return undefined;
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L85-L97)
3. 创建ImageSource实例。

   * 方法一：通过沙箱路径创建ImageSource。沙箱路径可以通过步骤2的方法一获取。

     ```
     1. // path为已获得的沙箱路径。
     2. const imageSource : image.ImageSource = image.createImageSource(filePath);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L224-L227)
   * 方法二：通过文件描述符fd创建ImageSource。文件描述符可以通过步骤2的方法二获取。

     ```
     1. // fd为已获得的文件描述符。
     2. const imageSource: image.ImageSource = image.createImageSource(fd);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L237-L240)
   * 方法三：通过缓冲区数组创建ImageSource。缓冲区数组可以通过步骤2的方法三获取。

     ```
     1. const imageSource: image.ImageSource = image.createImageSource(buffer);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L251-L253)
   * 方法四：通过资源文件的RawFileDescriptor创建ImageSource。RawFileDescriptor可以通过步骤2的方法四获取。

     ```
     1. const imageSource: image.ImageSource = image.createImageSource(rawFileDescriptor);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L264-L266)
4. 设置解码参数DecodingOptionsForPicture，解码获取picture多图对象。

   解码时可指定需要解码的辅助图类型。辅助图本身不作为独立图像直接显示，而是作为辅助数据参与图像处理（如HDR合成、深度信息提取等）。常见的辅助图类型包括：

   | 辅助图类型 | 说明 |
   | --- | --- |
   | GAINMAP | 增益图，用于HDR图像的高动态范围渲染。 |
   | DEPTH\_MAP | 深度图，存储像素距离信息，用于3D重建、背景分离等场景。 |
   | UNREFOCUS\_MAP | 未重对焦原图，用于人像虚化后期处理。 |
   | LINEAR\_MAP | 线性图，用于视觉效果增强与色彩后期处理。 |
   | FRAGMENT\_MAP | 水印裁剪图，用于水印移除、原图恢复等场景。 |

   说明

   并非所有图片都包含辅助图。在获取辅助图前，应先调用Picture的[getAuxiliaryPicture](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md#getauxiliarypicture13>)方法尝试获取。其他辅助图类型请参考[AuxiliaryPictureType](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Enums/arkts-apis-image-e.md#auxiliarypicturetype13>)。

   ```
   1. async createPicture(imageSource : image.ImageSource | undefined, isReturnAux: Boolean)
   2. : Promise<image.PixelMap | undefined | image.Picture> {
   3. // 配置解码选项参数。
   4. let options: image.DecodingOptionsForPicture = {
   5. desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP] // GAINMAP为需要解码的辅助图类型。
   6. };
   7. let returnPixelMap: image.PixelMap | undefined = undefined;
   8. // 创建picture。
   9. try {
   10. let picture = await imageSource?.createPicture(options);
   11. if (picture) {
   12. // 返回解码后获取到的辅助图
   13. if (isReturnAux) {
   14. // type为解码参数中包含的辅助图类型
   15. let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
   16. let auxPicture: image.AuxiliaryPicture | null = picture.getAuxiliaryPicture(type);
   17. // 获取辅助图信息。
   18. if (auxPicture != null) {
   19. let auxInfo: image.AuxiliaryPictureInfo = auxPicture.getAuxiliaryPictureInfo();
   20. console.info('GetAuxiliaryPictureInfo type: ' + auxInfo.auxiliaryPictureType +
   21. ' height: ' + auxInfo.size.height + ' width: ' + auxInfo.size.width +
   22. ' rowStride: ' + auxInfo.rowStride + ' pixelFormat: ' + auxInfo.pixelFormat +
   23. ' colorSpace: ' + auxInfo.colorSpace);
   24. // 将辅助图数据读到ArrayBuffer。
   25. try {
   26. let pixelsBuffer = await auxPicture.readPixelsToBuffer();
   27. let opts: image.InitializationOptions = { size: auxInfo.size };
   28. try {
   29. returnPixelMap = image.createPixelMapSync(pixelsBuffer, opts) as image.PixelMap;
   30. console.info(`Create PixelMap with buffer successfully.`);
   31. } catch (error) {
   32. console.error(`Create PixelMap failed with ${error}.`);
   33. }
   34. } catch (error) {
   35. console.error(`Read pixels to buffer failed, error.code: ${error.code},
   36. error.message: ${error.message}`);
   37. }
   38. auxPicture.release();
   39. }
   40. return returnPixelMap;
   41. } else {
   42. return picture; // 返回解码后获取到的picture
   43. }
   44. }
   45. return returnPixelMap;
   46. } catch (error) {
   47. console.error(`Create picture failed: ${error}.`);
   48. }
   49. return returnPixelMap;
   50. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L307-L358)
5. 释放picture。

   确认picture的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```
   1. async release(picture: image.Picture) {
   2. picture?.release();
   3. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L468-L472)
