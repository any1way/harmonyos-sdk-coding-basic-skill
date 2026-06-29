---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-raw-data
title: 使用ImageSource获取RAW数据
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource获取RAW数据
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:48+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:e3a9bfc7d9461c9a85cd023143b852e3c6fdc088ddb588823f0ddb5b052eda4d
---
图像的 RAW 数据是直接从图像传感器获取的原始数据，完整保留了所有传感器信息且无任何压缩损失。通过使用RAW数据，开发者可以获得最高质量的图像信息，并根据具体需求自定义图像处理算法，实现更灵活的图像处理和优化效果。

从API version 24开始，支持将符合格式的图片文件解码为[ImageRawData](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interfaces (其他)/arkts-apis-image-i.md#imagerawdata24>)，以便在应用或系统中获取RAW数据。RAW数据包含图像缓冲区和像素位数。

当前支持的图片文件格式为DNG。

## 开发步骤

获取图片RAW数据相关API的详细介绍请参见：[createImageRawData](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageSource)/arkts-apis-image-imagesource.md#createimagerawdata24>)。

1. 全局导入Image模块，根据实际需求导入对应的Kit模块。

   ```
   1. // 导入相关模块。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   ```

   [DecodingPixelMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPixelMap.ets#L16-L23)
2. 获取图片。

   * 方法一：通过沙箱路径直接获取，此方法**仅适用**于应用沙箱中的图片。获取方式请参考[获取应用文件路径](<../../../../../应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#获取应用文件路径>)。

     ```
     1. function getFilePath(context: Context, fileName: string): string {
     2. const filePath: string = context.cacheDir + '/' + fileName;
     3. return filePath;
     4. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L47-L52)
   * 方法二：通过沙箱路径获取图片的文件描述符。具体请参考[@ohos.file.fs (文件管理)](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md>)文档。该方法需要导入@kit.CoreFileKit模块。

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
   * 方法三：通过资源管理器获取资源文件的ArrayBuffer。具体请参考[getRawFileContent](<../../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md#getrawfilecontent9-1>)接口。该方法需要导入@kit.LocalizationKit模块。

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
   * 方法四：通过资源管理器获取资源文件的RawFileDescriptor。具体请参考[getRawFd](<../../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md#getrawfd9-1>)接口。该方法需要导入@kit.LocalizationKit模块。

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
4. 获取ImageRawData图片对象并打印像素值。

   ```
   1. async  createImageRawData(imageSource: image.ImageSource | undefined) : Promise<image.ImageRawData | undefined> {
   2. if (!imageSource) {
   3. console.error('imageSource is undefined.');
   4. return undefined;
   5. }
   6. await imageSource.createImageRawData().then((data: image.ImageRawData) => {
   7. let array: Uint16Array = new Uint16Array();
   8. if (data.bitsPerPixel == 16 && data.buffer) {
   9. array = new Uint16Array(data.buffer);
   10. }
   11. let length = array.byteLength.valueOf();
   12. console.info(`uint16Array length: ${length}`);
   13. let value: string = '';
   14. for (let i = 0; i < array.length && i < 10; i++) {
   15. value += array[i] + ', ';
   16. }
   17. console.info(`get dng rawdata is:${value}.`);
   18. return data
   19. }).catch((err: BusinessError) => {
   20. console.error(`get dng rawdata failed.err: ${JSON.stringify(err)}`);
   21. return undefined;
   22. })
   23. return undefined;
   24. }
   ```
5. 释放imageSource。

   确认imageSource的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```
   1. async release(pixelMap: image.PixelMap | undefined, imageSource: image.ImageSource | undefined) {
   2. await pixelMap?.release();
   3. pixelMap = undefined;
   4. await imageSource?.release();
   5. imageSource = undefined;
   6. }
   ```

   [DecodingPixelMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPixelMap.ets#L44-L51)
