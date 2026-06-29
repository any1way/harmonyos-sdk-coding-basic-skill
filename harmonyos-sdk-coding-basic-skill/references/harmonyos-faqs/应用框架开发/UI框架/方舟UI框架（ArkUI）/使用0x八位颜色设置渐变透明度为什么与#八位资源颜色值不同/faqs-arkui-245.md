---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-245
title: 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:28d709f63e3cf12078d1436cf4427d4eaadfbab9d695b4c8ea0699985496ad4b
---

HarmonyOS支持0x开头加八位或六位的写法。当透明度设为00时，前两位透明度不再借位，即0x00333333等于0x333333，相当于没有设置透明度，因此没有透明效果。建议使用rgba方式明确颜色。参考代码如下：

```
1. @Entry
2. @Component
3. struct ColorGradientExample {
4. @State transparent: number | string = '#00333333';
5. private bool: boolean = true;

7. build() {
8. Column({ space: 5 }) {
9. Text('linearGradient')
10. .fontSize(12)
11. .width('90%')
12. .fontColor(0xCCCCCC)
13. Row()
14. .width('90%')
15. .height(150)
16. .linearGradient({
17. direction: GradientDirection.Bottom,
18. colors: [[this.transparent, 0.0], [0x80000000, 1.0]]
19. })
20. Button('Switch color resources')
21. .onClick(() => {
22. if (this.bool) {
23. this.transparent = 0x00333333;
24. this.bool = false;
25. } else {
26. this.transparent = '#00333333';
27. this.bool = true;
28. }
29. })
30. }
31. .justifyContent(FlexAlign.Center)
32. .width('100%')
33. .height('100%')
34. .padding({ top: 5 })
35. }
36. }
```

[GradientTransparencyVaries.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GradientTransparencyVaries.ets#L21-L56)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/o__qvC5rQ_6lkFeZ592cvw/zh-cn_image_0000002458749397.png?HW-CC-KV=V1&HW-CC-Date=20260612T022947Z&HW-CC-Expire=86400&HW-CC-Sign=E672CDE56AE2F2E0BF8D8A50DEA0D54C7470B0B39FB56565965D3251198D2153)
