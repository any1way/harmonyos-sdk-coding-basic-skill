---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-55
title: 图片如何添加渐变模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 图片如何添加渐变模糊
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9a764c6e7aa0c46e80ada5680d08413771fa96098ebea96aaf5ed3ace31e877e
---
组件通用样式属性linearGradientBlur可以为当前组件添加线性渐变模糊效果。以下为参考代码：

```
1. @Entry
2. @Component
3. struct ImageExample1 {
4. privateResource1: Resource = $r('app.media.icon');
5. @State imageSrc: Resource = this.privateResource1;

7. build() {
8. Column() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
10. Row({ space: 5 }) {
11. Image(this.imageSrc)
12. .linearGradientBlur(60, {
13. fractionStops: [[0, 0], [0, 0.33], [1, 0.66], [1, 1]],
14. direction: GradientDirection.Bottom
15. })
16. }
17. }
18. }
19. }
20. }
```

[ImageAddGradientBlur.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageAddGradientBlur.ets#L21-L40)

**参考链接**

[linearGradientBlur](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#lineargradientblur12)
