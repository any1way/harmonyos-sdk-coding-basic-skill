---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multimedia-use-stride-in-image-receiver
title: @correctness/multimedia-use-stride-in-image-receiver
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/multimedia-use-stride-in-image-receiver
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a4a4abcb4b8ac4f8a20c7b1945000431711717f224f6997fe50b044d0f735fc
---
在使用ImageReceiver组件中[readNextImage](<../../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageReceiver)/arkts-apis-image-imagereceiver.md#readnextimage9>)接口时，建议设置且调用rowStride属性，避免出现相机获取预览流数据异常的问题。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/multimedia-use-stride-in-image-receiver": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. function onImageArrival(receiver: image.ImageReceiver): void {
5. receiver.on('imageArrival', () => {
6. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
7. if (err || nextImage === undefined) {
8. console.error('readNextImage failed');
9. return;
10. }
11. nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
12. if (err || imgComponent === undefined) {
13. console.error('getComponent failed');
14. }
15. if (imgComponent.byteBuffer) {
16. let width = nextImage.size.width;
17. let height = nextImage.size.height;
18. let stride = imgComponent.rowStride;  // 调用rowStride
19. console.debug(`getComponent with width:${width} height:${height} stride:${stride}`);
20. if (stride == width) {
21. let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
22. size: { height: height, width: width },
23. srcPixelFormat: 8,
24. })
25. } else {
26. const dstBufferSize = width * height * 1.5
27. const dstArr = new Uint8Array(dstBufferSize)
28. for (let j = 0; j < height * 1.5; j++) {
29. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
30. dstArr.set(srcBuf, j * width)
31. }
32. let pixelMap = await image.createPixelMap(dstArr.buffer, {
33. size: { height: height, width: width },
34. srcPixelFormat: 8,
35. })
36. }
37. } else {
38. console.error('byteBuffer is null');
39. }
40. nextImage.release();
41. })
42. })
43. })
44. }
```

## 反例

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. function onImageArrival(receiver: image.ImageReceiver): void {
5. receiver.on('imageArrival', () => {
6. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
7. if (err || nextImage === undefined) {
8. console.error('readNextImage failed');
9. return;
10. }
11. nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
12. if (err || imgComponent === undefined) {
13. console.error('getComponent failed');
14. }
15. if (imgComponent.byteBuffer) {
16. let width = nextImage.size.width;
17. let height = nextImage.size.height; // 未调用rowStride
18. } else {
19. console.error('byteBuffer is null');
20. }
21. nextImage.release();
22. })
23. })
24. })
25. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
