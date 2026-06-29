---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch
title: 切换按钮 (Toggle)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 切换按钮 (Toggle)
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:03+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:bb98eb9e5191ff5451d01e5f0d90351ae577b9d1de9468decb1b3c945cff1407
---
Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md)。

## 创建切换按钮

Toggle通过调用[ToggleOptions](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md#toggleoptions18对象说明)来创建，具体调用形式如下：

```
1. Toggle(options: { type: ToggleType, isOn?: boolean })
```

其中，ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态。

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

接口调用有以下两种形式：

* 创建不包含子组件的Toggle。

  当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

  ```
  1. Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id
  2. Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L30-L33)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/boAQqzbxRJ2bPjPSOtM1eA/zh-cn_image_0000002592378216.png?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=6ED5B83D8036601ECFA6F0E684AAF4A30DF9B5CF4769C3B41C3B379D9E55CDE7)

  ```
  1. Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id
  2. Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L39-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/uONZf9d3SEu4vEJQgaA8Yg/zh-cn_image_0000002622857723.png?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=7C83DEED82646F979530C8269A8FC2AD7EB645EB751CEBC8F34988AC733FCAD7)
* 创建包含子组件的Toggle。

  当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。

  ```
  1. Toggle({ type: ToggleType.Button, isOn: false }) {
  2. Text('status button')
  3. .fontColor('#182431')
  4. .fontSize(12)
  5. }.width(100).id('toggle5') // 请开发者替换为实际的id

  7. Toggle({ type: ToggleType.Button, isOn: true }) {
  8. Text('status button')
  9. .fontColor('#182431')
  10. .fontSize(12)
  11. }.width(100).id('toggle6') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L61-L73)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/PHPmUHGaTp6xPsSQqlbBYw/zh-cn_image_0000002622697845.png?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=9F3DDDCD7C8DDC832106A2523B77069C3D548A67FBC58A46BF9ED67719A9631A)

## 自定义样式

* 通过selectedColor属性设置Toggle打开选中后的背景颜色。

  ```
  1. Toggle({ type: ToggleType.Button, isOn: true }) {
  2. Text('status button')
  3. .fontColor('#182431')
  4. .fontSize(12)
  5. }.width(100)
  6. .selectedColor(Color.Pink)
  7. // ···

  9. Toggle({ type: ToggleType.Checkbox, isOn: true })
  10. .selectedColor(Color.Pink)
  11. // ···
  12. Toggle({ type: ToggleType.Switch, isOn: true })
  13. .selectedColor(Color.Pink)
  14. // ···
  ```

  [ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L31-L52)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/f3Klof-XRrG0DgFMdhEtMg/zh-cn_image_0000002592218284.png?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=E050164962C601CCA5527E04244D6687903F12DF5DE71B633BB0A7ECA4641A8C)
* 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

  ```
  1. Toggle({ type: ToggleType.Switch, isOn: false })
  2. .switchPointColor(Color.Pink)
  3. // ···
  4. Toggle({ type: ToggleType.Switch, isOn: true })
  5. .switchPointColor(Color.Pink)
  6. // ···
  ```

  [ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L60-L71)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/RzVfOhcPS_W9oKMfEaW9iQ/zh-cn_image_0000002592378218.png?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=4ACF6F2CC123FDB5A0FC98C43DBA07AB5B71C1542CA110F1A0247393A4D0A112)

## 添加事件

除支持[通用事件](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/ts-component-general-events.md)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```
1. Toggle({ type: ToggleType.Switch, isOn: false })
2. .onChange((isOn: boolean) => {
3. if(isOn) {
4. // 需要执行的操作
5. // ···
6. }
7. })
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L44-L54)

## 场景示例

Toggle用于切换蓝牙开关状态。

```
1. // xxx.ets
2. import { promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. export struct ToggleSample {
7. @State message: string = 'off';
8. pathStack: NavPathStack = new NavPathStack();

10. build() {
11. NavDestination() {
12. Column({ space: 8 }) {
13. Column({ space: 8 }) {
14. Text('Bluetooth Mode: ' + this.message)
15. .id('message')
16. Row() {
17. Text('Bluetooth')
18. Blank()
19. Toggle({ type: ToggleType.Switch })
20. .id('toggle') // 请开发者替换为实际的id
21. .onChange((isOn: boolean) => {
22. if (isOn) {
23. this.message = 'on';
24. promptAction.openToast({ 'message': 'Bluetooth is on.' });
25. } else {
26. this.message = 'off';
27. promptAction.openToast({ 'message': 'Bluetooth is off.' });
28. }
29. })
30. }.width('100%')
31. }
32. .alignItems(HorizontalAlign.Start)
33. .backgroundColor('#fff')
34. .borderRadius(12)
35. .padding(12)
36. .width('100%')
37. }
38. .width('100%')
39. .height('100%')
40. .padding({ left: 12, right: 12 })
41. }
42. .backgroundColor('#f1f2f3')
43. // 请将$r('app.string.ToggleCaseExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"toggle蓝牙示例"
44. .title($r('app.string.ToggleCaseExample_title'))
45. }
46. }
```

[ToggleCaseExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCaseExample.ets#L16-L69)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/bzfeSlZfRySfsFBV7grCKQ/zh-cn_image_0000002622857725.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063102Z&HW-CC-Expire=86400&HW-CC-Sign=BB49C3342CD8C8DB9DF504211A2CB25102566C8C9192A369883CD911BA68557E)
