---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect
title: 阴影
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画效果 > 阴影
category: harmonyos-guides
scraped_at: 2026-06-11T14:32:30+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:2a6932c85b591cfb384a1e08102e6503693d15dfdc59a810ec5d704a3cb4c3f2
---
阴影接口[shadow](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadow)可以为当前组件添加阴影效果，该接口支持两种类型参数，开发者可配置[ShadowOptions](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明)自定义阴影效果。ShadowOptions模式下，当radius = 0或者color的透明度为0时，无阴影效果。

```
1. @Entry
2. @Component
3. struct ShadowOptionDemo {
4. build() {
5. Row() {
6. Column() {
7. Column() {
8. Text('shadowOption').fontSize(12)
9. }
10. .width(100)
11. .aspectRatio(1)
12. .margin(10)
13. .justifyContent(FlexAlign.Center)
14. .backgroundColor(Color.White)
15. .borderRadius(20)
16. .shadow({ radius: 10, color: Color.Gray })

18. Column() {
19. Text('shadowOption').fontSize(12)
20. }
21. .width(100)
22. .aspectRatio(1)
23. .margin(10)
24. .justifyContent(FlexAlign.Center)
25. .backgroundColor('#a8a888')
26. .borderRadius(20)
27. .shadow({
28. radius: 10,
29. color: Color.Gray,
30. offsetX: 20,
31. offsetY: 20
32. })
33. }
34. .width('100%')
35. .height('100%')
36. .justifyContent(FlexAlign.Center)
37. }
38. .height('100%')
39. }
40. }
```

[Shadow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/Shadow/entry/src/main/ets/pages/Shadow.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/e5UlGaH9Qzu0_TBk-O9zBQ/zh-cn_image_0000002622857839.png?HW-CC-KV=V1&HW-CC-Date=20260611T063229Z&HW-CC-Expire=86400&HW-CC-Sign=CDB6742AC45209219E6C3CFFE510BFA8FDEC7F2CD786DC8800C26E017B4188D1)
