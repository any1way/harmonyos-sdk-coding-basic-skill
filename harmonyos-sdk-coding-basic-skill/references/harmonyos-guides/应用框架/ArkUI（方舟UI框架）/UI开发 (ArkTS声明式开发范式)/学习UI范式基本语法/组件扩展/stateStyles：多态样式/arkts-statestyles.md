---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles
title: stateStyles：多态样式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > stateStyles：多态样式
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:53+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e349936577ef81508e7dc6fbf8ec67e39aca10c59788ef29c0649d9c59c019d5
---
@Styles仅应用于静态页面的样式复用，stateStyles可以依据组件的内部状态的不同，快速设置不同样式。这就是我们本章要介绍的内容stateStyles（又称为：多态样式）。

说明

多态样式仅支持通用属性。如果多态样式不生效，则该属性可能为组件的私有属性，例如：[fontColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Button/ts-basic-components-button.md#fontcolor)、[TextInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)组件的[backgroundColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundcolor)等。此时，可以通过[attributeModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置组件属性来解决此问题。

## 概述

stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下六种状态：

* focused：获焦态。
* normal：正常态。
* pressed：按压态。
* disabled：不可用态。
* clicked：点击态。
* selected10+：选中态。

说明

获焦态目前仅支持通过外接键盘的Tab键或方向键触发，不支持在嵌套滚动组件场景下通过按键触发。

## 使用场景

### 基础场景

下面的示例展示了stateStyles最基本的使用场景。Button1处于第一个组件，Button2处于第二个组件。按压时显示为pressed态指定的黑色。使用Tab键走焦，Button1获焦并显示为focused态指定的粉色。当Button2获焦的时候，Button2显示为focused态指定的粉色，Button1失焦显示normal态指定的蓝色。

```
1. @Entry
2. @Component
3. struct StateStylesSample {
4. build() {
5. Column() {
6. Button('Button1')
7. .stateStyles({
8. focused: {
9. .backgroundColor('#ffffeef0')
10. },
11. pressed: {
12. .backgroundColor('#ff707070')
13. },
14. normal: {
15. .backgroundColor('#ff2787d9')
16. }
17. })
18. .margin(20)
19. Button('Button2')
20. .stateStyles({
21. focused: {
22. .backgroundColor('#ffffeef0')
23. },
24. pressed: {
25. .backgroundColor('#ff707070')
26. },
27. normal: {
28. .backgroundColor('#ff2787d9')
29. }
30. })
31. }.margin('30%')
32. }
33. }
```

[StateStylesSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/StateStyle/entry/src/main/ets/pages/StateStyle/StateStylesSample.ets#L16-L50)

**图1** 获焦态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/52AdDWkHS4msRuCCISNdpA/zh-cn_image_0000002622857415.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062744Z&HW-CC-Expire=86400&HW-CC-Sign=308C80F76DE2902A1887ABF758BFCE4003FA43DDA3082DF8550890490F53ED64)

### @Styles和stateStyles联合使用

以下示例通过@Styles指定stateStyles的不同状态。

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @Styles normalStyle() {
5. .backgroundColor(Color.Gray)
6. }

8. @Styles pressedStyle() {
9. .backgroundColor(Color.Red)
10. }
11. build() {
12. Column() {
13. Text('Text1')
14. .fontSize(50)
15. .fontColor(Color.White)
16. .stateStyles({
17. normal: this.normalStyle,
18. pressed: this.pressedStyle,
19. })
20. }
21. }
22. }
```

[MyComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/StateStyle/entry/src/main/ets/pages/NormalStyle/MyComponent.ets#L16-L39)

**图2** 正常态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/K-WY51smTZSPJcIxrBc5Fg/zh-cn_image_0000002622697537.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062744Z&HW-CC-Expire=86400&HW-CC-Sign=1979A356693A270D2BB9454642284A14C52355294685ED1D7EC6C2C72FC095F9)

### 在stateStyles里使用常规变量和状态变量

stateStyles可以通过this绑定组件内的常规变量和状态变量。

```
1. @Entry
2. @Component
3. struct CompWithInlineStateStyles {
4. @State focusedColor: Color = 0xD5D5D5;
5. normalColor: Color = 0x004AAF;

7. build() {
8. Column() {
9. Button('clickMe')
10. .height(100)
11. .width(100)
12. .stateStyles({
13. normal: {
14. .backgroundColor(this.normalColor)
15. },
16. focused: {
17. .backgroundColor(this.focusedColor)
18. }
19. })
20. .onClick(() => {
21. this.focusedColor = 0x707070;
22. })
23. .margin('30%')
24. }
25. }
26. }
```

[CompWithInlineStateStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/StateStyle/entry/src/main/ets/pages/FocusStyle/CompWithInlineStateStyles.ets#L15-L42)

Button默认normal态显示蓝色，第一次按下Tab键让Button获焦显示为focus态的浅灰色，点击事件触发后，再次按下Tab键让Button获焦，focus态变为深灰色。

**图3** 点击改变获焦态样式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/KKsLctl0QB-OQEhAuFbBjA/zh-cn_image_0000002592217976.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062744Z&HW-CC-Expire=86400&HW-CC-Sign=FF7E101382A521EC805A4D40125F265A664EB0433DD6BE16EA5358252830051F)
