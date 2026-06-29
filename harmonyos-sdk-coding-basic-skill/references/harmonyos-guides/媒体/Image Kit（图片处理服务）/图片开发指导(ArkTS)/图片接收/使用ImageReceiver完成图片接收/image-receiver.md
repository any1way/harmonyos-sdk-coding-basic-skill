---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver
title: 使用ImageReceiver完成图片接收
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片接收 > 使用ImageReceiver完成图片接收
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:59+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:0e97d35cfbc0419e4a9890ae64110091119218039417b3fdd7a2de988e438240
---
图片接收类ImageReceiver用于获取组件SurfaceId，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

说明

Receiver作为消费者，需要有对应的生产者提供数据才能实现完整功能。常见的生产者是相机的拍照流或预览流。ImageReceiver只作为图片的接收方、消费者，在ImageReceiver设置的size、format等属性实际上并不会生效，图片createImageReceiver时传入的参数不产生实际影响。图片属性需要在发送方、生产者进行设置，如在使用[createpreviewoutput](<../../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (CameraManager)/arkts-apis-camera-cameramanager.md#createpreviewoutput>)创建相机预览流时配置[profile](<../../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interfaces (其他)/arkts-apis-camera-i.md#profile>)。

ImageReceiver可以接收相机预览流中的图片，实现[双路预览](<../../../../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/双路预览(ArkTS)/camera-dual-channel-preview.md>)。

相关API的详细介绍请参见[ImageReceiver](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageReceiver)/arkts-apis-image-imagereceiver.md>)。

## 开发步骤

创建ImageReceiver对象，获取SurfaceId创建预览流，注册图像监听，按需处理预览流每帧图像。

1. 导入相关模块包。

   ```
   1. import { image } from '@kit.ImageKit'
   2. import { camera } from '@kit.CameraKit';
   3. import { BusinessError } from '@kit.BasicServicesKit'
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [ReceiverUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ReceiverUtility.ets#L16-L21)
2. 创建ImageReceiver对象，通过ImageReceiver对象可获取预览流SurfaceId。

   ```
   1. async function initImageReceiver(): Promise<void> {
   2. // 创建ImageReceiver对象。createImageReceiver的参数不会对接收到的数据产生实际影响。
   3. let size: image.Size = { width: imageWidth, height: imageHeight };
   4. // capacity为期望缓存数量，实际值由设备能力决定，此处8仅为示例值。
   5. let imageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
   6. // 获取预览流SurfaceId。
   7. let imageReceiverSurfaceId = await imageReceiver.getReceivingSurfaceId();
   8. console.info(`initImageReceiver imageReceiverSurfaceId:${imageReceiverSurfaceId}`);
   9. }
   ```

   [ReceiverUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ReceiverUtility.ets#L33-L43)
3. 注册监听处理预览流每帧图像数据：通过ImageReceiver中imageArrival事件监听获取底层返回的图像数据。详细的API说明请参考[ImageReceiver](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageReceiver)/arkts-apis-image-imagereceiver.md>)。

   ```
   1. function onImageArrival(receiver: image.ImageReceiver) {
   2. // 注册imageArrival监听。
   3. receiver.on('imageArrival', () => {
   4. // 获取图像。
   5. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
   6. if (err || nextImage === undefined) {
   7. console.error('readNextImage failed');
   8. return;
   9. }
   10. // 解析图像内容。
   11. (async () => {
   12. try {
   13. let imgComponent = await nextImage.getComponent(image.ComponentType.JPEG);
   14. if (!imgComponent.byteBuffer) {
   15. console.error('byteBuffer is null');
   16. return;
   17. }
   18. // 详情见下方解析图片buffer数据参考，本示例以方式一为例。
   19. let width = nextImage.size.width; // 获取图片的宽。
   20. let height = nextImage.size.height; // 获取图片的高。
   21. let stride = imgComponent.rowStride; // 获取图片的stride。
   22. console.debug(`getComponent with width:${width} height:${height} stride:${stride}`);
   23. // stride与width一致。
   24. if (stride == width) {
   25. let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
   26. size: { height: height, width: width },
   27. srcPixelFormat: image.PixelMapFormat.NV21,
   28. })
   29. } else {
   30. // stride与width不一致。
   31. const dstBufferSize = width * height * 1.5;
   32. const dstArr = new Uint8Array(dstBufferSize);
   33. for (let j = 0; j < height * 1.5; j++) {
   34. // 不同设备内存不同，若内存太小，则无法全部写完。
   35. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
   36. dstArr.set(srcBuf, j * width);
   37. }
   38. let pixelMap = await image.createPixelMap(dstArr.buffer, {
   39. size: { height: height, width: width },
   40. srcPixelFormat: image.PixelMapFormat.NV21,
   41. })
   42. }
   43. } catch (error) {
   44. console.error('getComponent failed');
   45. } finally {
   46. // 确保当前buffer没有在使用的情况下，可进行资源释放。
   47. // 如果对buffer进行异步操作，需要在异步操作结束后再释放该资源（nextImage.release()）。
   48. await nextImage.release();
   49. }
   50. })();
   51. })
   52. })
   53. }
   ```

   [ReceiverUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ReceiverUtility.ets#L45-L99)

通过[image.Component](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interfaces (其他)/arkts-apis-image-i.md#component9>)解析图片的buffer数据。

注意

需要确认图像的宽（width）是否与行距（rowStride）一致，如果不一致可参考以下方式一和方式二进行预处理。

方式一：去除imgComponent.byteBuffer中stride数据，拷贝得到新的buffer，调用不支持stride的接口处理buffer。

```
1. // stride与width不一致。
2. const dstBufferSize = width * height * 1.5
3. const dstArr = new Uint8Array(dstBufferSize)
4. for (let j = 0; j < height * 1.5; j++) {
5. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
6. dstArr.set(srcBuf, j * width)
7. }
8. let pixelMap = await image.createPixelMap(dstArr.buffer, {
9. size: { height: height, width: width },
10. srcPixelFormat: image.PixelMapFormat.NV21,
11. })
```

[ReceiverUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ReceiverUtility.ets#L103-L115)

方式二：根据stride \* height创建pixelMap，然后调用pixelMap的cropSync方法裁剪掉多余的像素。

```
1. // 创建pixelMap，width传入行距（stride）的值。
2. let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
3. size:{height: height, width: stride}, srcPixelFormat: image.PixelMapFormat.NV21});
4. // 裁剪多余的像素。
5. try {
6. pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
7. } catch (err) {
8. hilog.error(0x00000, TAG, `adjust bufferSize failed: ${err}!`);
9. }
```

[ReceiverUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ReceiverUtility.ets#L121-L131)
