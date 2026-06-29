---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-pixel-format-check
title: @correctness/image-pixel-format-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/image-pixel-format-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:549299b578e9b8d76e286dadab1c8c5ac8608d32c38b7aaadb780592358778f7
---
在使用Image组件[createPixelMap](<../../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Functions/arkts-apis-image-f.md#imagecreatepixelmap8>)接口时，建议不要选择RGB\_565档位，避免出现色阶问题。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/image-pixel-format-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import image from '@ohos.multimedia.image';
2. const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
3. const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
4. export class AodFailTask {
5. private async setImage(): Promise<void> {
6. const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
7. let opts: image.InitializationOptions = {
8. editable: true,
9. pixelFormat: image.PixelMapFormat.RGBA_8888,
10. size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
11. }
12. const imageSrc = await image.createPixelMap(color, opts);
13. }
14. private async setImage1(): Promise<void> {
15. const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
16. let opts: image.InitializationOptions = {
17. editable: true,
18. pixelFormat: image.PixelMapFormat.RGBA_8888,
19. size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
20. }
21. const imageSrc = await image.createPixelMap(color, opts);
22. }

24. private setImage2() {
25. // Original image size
26. let width: number = 100;
27. let height: number = 100;
28. let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
29. image.createPixelMap(buffer, {
30. editable: false,
31. pixelFormat: image.PixelMapFormat.RGBA_8888,
32. size: { height: height, width: width }
33. })
34. }

36. }
```

## 反例

```
1. import image from '@ohos.multimedia.image';
2. const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
3. const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
4. export class AodFailTask {
5. private async setImage(): Promise<void> {
6. const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
7. let opts: image.InitializationOptions = {
8. editable: true,
9. pixelFormat: image.PixelMapFormat.RGB_565,
10. size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
11. }
12. // warning
13. const imageSrc = await image.createPixelMap(color, opts);
14. }
15. private async setImage1(): Promise<void> {
16. const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
17. let opts: image.InitializationOptions = {
18. editable: true,
19. pixelFormat: image.PixelMapFormat.RGB_565,
20. size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
21. }
22. // warning
23. const imageSrc = await image.createPixelMap(color, opts);
24. }
25. private setImage2() {
26. // Original image size
27. let width: number = 100;
28. let height: number = 100;
29. let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
30. // warning
31. image.createPixelMap(buffer, {
32. editable: false,
33. pixelFormat: image.PixelMapFormat.RGB_565,
34. size: { height: height, width: width }
35. })
36. }
37. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
