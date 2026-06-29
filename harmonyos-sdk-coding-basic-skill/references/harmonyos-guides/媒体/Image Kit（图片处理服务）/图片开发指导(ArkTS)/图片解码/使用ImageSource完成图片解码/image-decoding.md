---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding
title: 使用ImageSource完成图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource完成图片解码
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:45+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:7397af7a209f4dc9efbfeac96e8637c8c37b0eb7b7f2cb815de8ce2df94875cf
---
将所支持格式的图片文件解码成[PixelMap](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)，以便在应用或系统中显示或处理图片。当前支持的图片文件格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIC、TIFF23+、HEIFS23+、WBMP23+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats20+](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Functions/arkts-apis-image-f.md#imagegetimagesourcesupportedformats20>)接口，动态查询当前设备上的解码能力。

从API version 22开始，支持对专业相机拍摄的CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW格式图片内嵌的预览图（通常为JPEG格式）进行解码。该解码能力不受运行设备类型限制。

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

   [DecodingPixelMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPixelMap.ets#L16-L23)
2. （可选）查询设备解码能力。

   部分图片格式的解码能力依赖于设备硬件，解码前可先查询设备支持的解码格式列表：

   ```
   1. // 获取当前设备支持的解码格式列表。
   2. export function getSupportedFormats(): string[] {
   3. let formats = image.getImageSourceSupportedFormats();
   4. console.info('Supported formats: ' + formats);
   5. return formats;
   6. }

   8. // 检查指定格式是否支持解码。
   9. export function isFormatSupported(format: string): boolean {
   10. let formats = image.getImageSourceSupportedFormats();
   11. return formats.includes(format);
   12. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L24-L37)
3. 获取图片。

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
4. 创建ImageSource实例。

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
5. 设置解码参数DecodingOptions，解码获取pixelMap图片对象。

   配置解码选项参数进行解码：

   ```
   1. async createPixelMap(imageSource: image.ImageSource | undefined): Promise<image.PixelMap | undefined> {
   2. if (!imageSource) {
   3. console.error('imageSource is undefined.');
   4. return undefined;
   5. }
   6. // 配置解码选项参数。
   7. let decodingOptions: image.DecodingOptions = {
   8. editable: true,
   9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
   10. // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelMap。
   11. desiredDynamicRange: image.DecodingDynamicRange.HDR,
   12. };

   14. try {
   15. // 生成 pixelMap 并返回
   16. const pixelMap = await imageSource.createPixelMap(decodingOptions);
   17. if (pixelMap) {
   18. console.info('Create PixelMap successfully.');
   19. // 判断pixelMap是否为hdr内容。
   20. let imageInfo = await pixelMap.getImageInfo();
   21. console.info(`Create PixelMap successfully with imageInfo.isHdr: ${imageInfo.isHdr}.`);
   22. return pixelMap;
   23. } else {
   24. console.info('Create PixelMap failed.');
   25. return undefined;
   26. }
   27. } catch (error) {
   28. console.error(`Failed to create PixelMap: ${error}.`);
   29. return undefined;
   30. }
   31. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L273-L305)

   解码完成，获取到pixelMap对象后，可以进行后续[图片处理](../../图片编辑和处理/使用PixelMap完成图像变换/image-transformation.md)。
6. 释放pixelMap和imageSource。

   确认pixelMap和imageSource的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```
   1. async release(pixelMap: image.PixelMap | undefined, imageSource: image.ImageSource | undefined) {
   2. await pixelMap?.release();
   3. pixelMap = undefined;
   4. await imageSource?.release();
   5. imageSource = undefined;
   6. }
   ```

   [DecodingPixelMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPixelMap.ets#L44-L51)

   说明

   1. 释放imageSource的合适时机：createPixelMap执行完成，成功获取pixelMap后，如果确定不再使用imageSource的其他方法，可以手动释放imageSource。由于解码得到的pixelMap是一个独立的实例，imageSource的释放不会导致pixelMap不可用。
   2. 释放pixelMap的合适时机：如果使用系统的[Image组件](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md)进行图片显示，无需手动释放，Image组件会自动管理传递给它的pixelMap；如果应用自行处理pixelMap，则推荐在页面切换、应用退后台等场景下手动释放老页面pixelMap；在内存资源紧张的场景，推荐释放除当前页面外其他不可见页面的PixelMap。

## 进阶主题

* **内存优化解码**：使用DMA内存和YUV像素格式降低内存占用、提升解码性能，参见[图片解码内存优化](../图片解码内存优化(ArkTS)/image-allocator-type.md)。
* **区域解码**：解码图片指定区域，适用于大图局部查看和裁剪预览场景，参见[图片区域解码与下采样](../图片区域解码与下采样(ArkTS)/image-region-and-downsampling.md)。
* **下采样解码**：解码时直接缩放目标尺寸，避免解码后缩放的性能开销，适用于缩略图生成场景，参见[图片区域解码与下采样](../图片区域解码与下采样(ArkTS)/image-region-and-downsampling.md)。
* **多图对象解码**：解码包含主图和辅助图的Picture对象，适用于HDR图片和HEIF专业格式处理，参见[使用ImageSource完成多图对象解码](../使用ImageSource完成多图对象解码/image-picture-decoding.md)。

## 示例代码

* [实现图片获取与保存功能](https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave)
* [水印添加能力](https://gitcode.com/HarmonyOS_Samples/watermark)
