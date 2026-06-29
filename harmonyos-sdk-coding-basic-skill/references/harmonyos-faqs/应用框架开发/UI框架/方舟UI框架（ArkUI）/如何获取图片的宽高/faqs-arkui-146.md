---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-146
title: 如何获取图片的宽高
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取图片的宽高
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee13caeee669201bca039f3f03e25c8918efdc8744b1d5d12c48b3180a7a0256
---
通过Image组件的[onComplete](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md#oncomplete)事件，图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。参考代码如下：

```
1. Image($r('app.media.startIcon'))
2. .width(200)
3. .height(200)
4. .objectFit(ImageFit.Contain)
5. .onComplete((event) => {
6. let imageWidth = event?.width;
7. let imageHeight = event?.height;
8. console.info('imageWidth:'+imageWidth,'imageHeight:'+imageHeight);
9. })
```

[ObtainTheWidthAndHeightOfTheImage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ObtainTheWidthAndHeightOfTheImage.ets#L24-L32)

**参考链接**

[Image](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md)
