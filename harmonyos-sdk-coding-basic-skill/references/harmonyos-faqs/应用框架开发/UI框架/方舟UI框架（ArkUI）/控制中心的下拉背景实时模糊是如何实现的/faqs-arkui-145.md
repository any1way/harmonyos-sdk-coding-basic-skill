---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-145
title: 控制中心的下拉背景实时模糊是如何实现的
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 控制中心的下拉背景实时模糊是如何实现的
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5f38c22656dbcd901dc59af1f625bd985afe74ac22b19b55969b7e71c806e91b
---
实时模糊，就是通过状态变量实时改变模糊值。实现模糊可以通过组件的通用属性[backdropBlur](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backdropblur)来设置组件的模糊效果。参考代码如下：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackGroundBlur {
5. private imageSize: number = 150;

7. build() {
8. Column() {
9. // backdropBlur Only blur radius and grayscale parameters can be set
10. Stack() {
11. Image($r('app.media.startIcon'))
12. .width(this.imageSize)
13. .height(this.imageSize)
14. Column()
15. .width(this.imageSize)
16. .height(this.imageSize)
17. .backdropBlur(20, { grayscale: [30, 50] })
18. }
19. }
20. .width('100%')
21. .padding({ top: 5 })
22. }
23. }
```

[ImplementDropdownBackgroundBlurring.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementDropdownBackgroundBlurring.ets#L21-L43)

**参考链接**

[图像效果](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md)
