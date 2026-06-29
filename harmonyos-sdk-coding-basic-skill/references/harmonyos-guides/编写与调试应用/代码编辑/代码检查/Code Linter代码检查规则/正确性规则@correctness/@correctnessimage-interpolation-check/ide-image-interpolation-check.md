---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-interpolation-check
title: @correctness/image-interpolation-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/image-interpolation-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:40+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:2f36ef0379956bfbfcbe5c35476ebe97754a860a423f1ef915d741beffb228bb
---
在使用Image组件[interpolation](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md#interpolation)接口时，建议不要使用最邻近插值，避免出现明显锯齿问题。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/image-interpolation-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const ADAPTIVE_SCALE = 1.5;

3. @Component
4. export struct AppIcon {
5. @State icon: string | PixelMap = '';
6. @Prop iconSize: number = 1;
7. private mInterpolation: ImageInterpolation = ImageInterpolation.None;

9. aboutToAppear(): void {
10. this.mInterpolation = ImageInterpolation.Medium;
11. }

13. @Builder
14. overlayIcon() {
15. Image(this.icon)
16. .height(this.iconSize * ADAPTIVE_SCALE)
17. .width(this.iconSize * ADAPTIVE_SCALE)
18. .interpolation(ImageInterpolation.Medium)
19. }

21. @Builder
22. overlayIcon1() {
23. Image(this.icon)
24. .height(this.iconSize * ADAPTIVE_SCALE)
25. .width(this.iconSize * ADAPTIVE_SCALE)
26. .interpolation(this.mInterpolation)
27. }

29. build() {
30. Column() {
31. this.overlayIcon();
32. this.overlayIcon1();
33. Image($r('app.media.pause'))
34. .draggable(false)
35. .interpolation(ImageInterpolation.Medium)
36. }
37. }
38. }
```

## 反例

```
1. const ADAPTIVE_SCALE = 1.5;

3. @Component
4. export struct AppIcon {
5. @State icon: string | PixelMap = '';
6. @Prop iconSize: number = 1;
7. private mInterpolation: ImageInterpolation = ImageInterpolation.Medium;

9. aboutToAppear(): void {
10. this.mInterpolation = ImageInterpolation.None;
11. }

13. @Builder
14. overlayIcon() {
15. Image(this.icon)
16. .height(this.iconSize * ADAPTIVE_SCALE)
17. .width(this.iconSize * ADAPTIVE_SCALE)
18. // warning
19. .interpolation(ImageInterpolation.None)
20. }

22. @Builder
23. overlayIcon1() {
24. Image(this.icon)
25. .height(this.iconSize * ADAPTIVE_SCALE)
26. .width(this.iconSize * ADAPTIVE_SCALE)
27. // warning
28. .interpolation(this.mInterpolation)
29. }

31. build() {
32. Column() {
33. this.overlayIcon();
34. this.overlayIcon1();
35. Image($r('app.media.pause'))
36. .draggable(false)
37. // warning
38. .interpolation(ImageInterpolation.None)
39. }
40. }
41. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
