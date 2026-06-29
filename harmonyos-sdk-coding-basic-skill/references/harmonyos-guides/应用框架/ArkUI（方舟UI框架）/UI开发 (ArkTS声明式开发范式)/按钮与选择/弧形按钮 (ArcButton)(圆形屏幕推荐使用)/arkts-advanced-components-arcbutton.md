---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton
title: 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:01+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:29ea1b2e956c55c95abc60619551fcb03aedac21ea5dd146bc0f8ddd1605103e
---
从API version 18开始支持ArcButton。ArcButton是弧形按钮组件，推荐用于圆形屏幕。为用户提供强调、普通、警告等样式按钮。具体用法请参考[ArcButton](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md)。

## 创建按钮

ArcButton通过调用以下接口来创建。

```
1. ArcButton({
2. options: new ArcButtonOptions({
3. label: 'OK',
4. position: ArcButtonPosition.TOP_EDGE,
5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
6. // ···
7. })
8. })
```

[ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L27-L43)

其中，[label](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮文字，[position](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型，[styleMode](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/ipgZ9gIJT5qtSbEME-Jxwg/zh-cn_image_0000002592218278.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=BCEA94D110C2D1FF2EB030563C010A8F88DB3B749035374C3201EA5A072A37DC)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型。

* 下弧形按钮（默认类型）。

  通过将[position](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM\_EDGE，可以将按钮设置为下弧形按钮。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. position: ArcButtonPosition.BOTTOM_EDGE,
  5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  6. // ···
  7. })

  9. })
  ```

  [ButtonAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignBottom.ets#L27-L45)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/OMoKWHbNSv-vHJA40gUbZA/zh-cn_image_0000002592378212.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=E2B66F0F87AA86760C9E09774493FFBC7AE5795DC027EA38E04259FAB400B259)
* 上弧形按钮。

  通过将[position](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.TOP\_EDGE，可以将按钮设置为上弧形按钮。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. position: ArcButtonPosition.TOP_EDGE,
  5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  6. // ···
  7. })
  8. })
  ```

  [ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L27-L43)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/cRsznO7qTEmBmI2DHn4SHA/zh-cn_image_0000002622857719.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=90C79E3CFB71E9D4C4E027CC5529FF0F5D5486F6A810B36138EC62033E08AD79)

## 自定义样式

* 设置背景色。

  使用[backgroundColor](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的背景色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. styleMode: ArcButtonStyleMode.CUSTOM,
  5. backgroundColor: ColorMetrics.resourceColor('#707070')
  6. })
  7. })
  ```

  [ButtonBcgColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonBcgColor.ets#L23-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/3wEBM0nERU6F3pWX0Y4SFA/zh-cn_image_0000002622697841.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=5B6E1E5C9F585FBC83043FF6D850F6DEFCDC4156BF50E182C4838CB8D1283135)
* 设置文本颜色。

  使用[fontColor](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的文本颜色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. styleMode: ArcButtonStyleMode.CUSTOM,
  5. backgroundColor: ColorMetrics.resourceColor('#E84026'),
  6. fontColor: ColorMetrics.resourceColor('#707070')
  7. })
  8. })
  ```

  [ButtonFontColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonFontColor.ets#L23-L32)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/hmllmCQmTR29KSQMRJxk_Q/zh-cn_image_0000002592218280.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=0E8E41BDE379EE0A0444984997BAEB5FC77C06978B85F0DF87C5BBAAC151AA74)
* 设置阴影颜色。

  使用[shadowEnabled](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的阴影颜色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. shadowEnabled: true,
  5. shadowColor: ColorMetrics.resourceColor('#ffec1022')
  6. })
  7. })
  ```

  [ButtonShadow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonShadow.ets#L23-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/t5KPEUWBQFaZgIxSu6J_qw/zh-cn_image_0000002592378214.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=A1F4B44D4A6CB85C256D089412CD30606637EC1432A60714B25DB0314CCEFE79)

## 添加事件

* 绑定onClick事件来响应点击操作后的自定义行为。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. // ···
  5. onClick: () => {
  6. hilog.info(DOMAIN, TAG, 'ArcButton onClick');
  7. },
  8. })
  9. })
  ```

  [ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L28-L44)
* 绑定onTouch事件来响应触摸操作后的自定义行为。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. // ···
  5. onTouch: (event: TouchEvent) => {
  6. hilog.info(DOMAIN, TAG, 'ArcButton onTouch');
  7. }
  8. })

  10. })
  ```

  [ButtonAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignBottom.ets#L28-L44)

## 场景示例

在亮度设置界面，进度条显示当前亮度为30%。点击重置后，亮度值将被重置为默认的50%。

运行该示例推荐在Wearable设备上以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，在src/main目录下的工程配置文件[module.json5](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中[deviceTypes标签](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#devicetypes标签)内配置wearable。

```
1. "module": {
2. // ···
3. "deviceTypes": [
4. "wearable"
5. ],
6. // ···
7. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/module.json5#L17-L71)

```
1. import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

3. const BRIGHT_NESS_VALUE = 30;
4. const BRIGHT_NESS_VALUE_DEFAULT = 50;

6. @Entry
7. @ComponentV2
8. struct BrightnessPage {
9. @Local brightnessValue: number = BRIGHT_NESS_VALUE;
10. private defaultBrightnessValue: number = BRIGHT_NESS_VALUE_DEFAULT;

12. build() {
13. RelativeContainer() {
14. // 请将$r('app.string.Brightness')替换为实际资源文件，在本示例中该资源文件的value值为"设置亮度"
15. Text($r('app.string.Brightness'))
16. .fontColor(Color.White)
17. .id('id_brightness_set_text')
18. .fontSize(24)
19. .margin({ top: 16 })
20. .alignRules({
21. middle: { anchor: '__container__', align: HorizontalAlign.Center }
22. })

24. Text(`${this.brightnessValue} %`)
25. .fontColor(Color.White)
26. .id('id_brightness_min_text')
27. .margin({ left: 16 })
28. .alignRules({
29. start: { anchor: '__container__', align: HorizontalAlign.Start },
30. center: { anchor: '__container__', align: VerticalAlign.Center }
31. })

33. Slider({
34. value: this.brightnessValue,
35. min: 0,
36. max: 100,
37. style: SliderStyle.InSet
38. })
39. .blockColor('#191970')
40. .trackColor('#ADD8E6')
41. .selectedColor('#4169E1')
42. .width(150)
43. .id('id_brightness_slider')
44. .margin({ left: 16, right: 16 })
45. .onChange((value: number, mode: SliderChangeMode) => {
46. this.brightnessValue = value;
47. })
48. .alignRules({
49. center: { anchor: 'id_brightness_min_text', align: VerticalAlign.Center },
50. start: { anchor: 'id_brightness_min_text', align: HorizontalAlign.End }
51. })

53. ArcButton({
54. options: new ArcButtonOptions({
55. // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
56. label: $r('app.string.Reset'),
57. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
58. fontSize: new LengthMetrics(19, LengthUnit.FP),
59. onClick: () => {
60. this.brightnessValue = this.defaultBrightnessValue;
61. }
62. })
63. })
64. .alignRules({
65. middle: { anchor: '__container__', align: HorizontalAlign.Center },
66. bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
67. })
68. }
69. .height('100%')
70. .width('100%')
71. .backgroundColor(Color.Black)
72. }
73. }
```

[ButtonBrightness.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonBrightness.ets#L16-L90)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/vPDhqdBGRCuxTKmbWAsNcw/zh-cn_image_0000002622857721.png?HW-CC-KV=V1&HW-CC-Date=20260611T063059Z&HW-CC-Expire=86400&HW-CC-Sign=798114F64D0C38E285CC936022ED31EE39EED93E101F2839BD5DC8BE38B8C7DC)
