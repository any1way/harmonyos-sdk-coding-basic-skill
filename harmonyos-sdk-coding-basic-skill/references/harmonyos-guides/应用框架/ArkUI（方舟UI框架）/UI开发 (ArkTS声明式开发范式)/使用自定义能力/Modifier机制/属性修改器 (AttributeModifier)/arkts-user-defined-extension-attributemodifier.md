---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier
title: 属性修改器 (AttributeModifier)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > Modifier机制 > 属性修改器 (AttributeModifier)
category: harmonyos-guides
scraped_at: 2026-06-11T14:32:41+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:b03a27f686891106f233cb2f03e1c4e75dd3f816ec4f1243660f7624b90b3ff1
---
## 概述

声明式语法引入了[@Styles](../../../学习UI范式基本语法/组件扩展/@Styles装饰器：定义组件重用样式/arkts-style.md)和[@Extend](../../../学习UI范式基本语法/组件扩展/@Extend装饰器：定义扩展组件样式/arkts-extend.md)两个装饰器，可以解决复用相同自定义样式的问题，但是存在以下受限场景：

* @Styles和@Extend均是编译期处理，不支持跨文件的导出复用。
* @Styles仅能支持通用属性、事件，不支持组件特有的属性。
* @Styles虽然支持在多态样式下使用，但不支持传参，无法对外开放一些属性。
* @Extend虽然能支持特定组件的私有属性、事件，但同样不支持跨文件导出复用。
* @Styles、@Extend对于属性设置，无法支持业务逻辑编写，动态决定是否设置某些属性，只能通过三元表达式对所有可能设置的属性进行全量设置，设置大量属性时效率较低。

为了解决上述问题，ArkUI引入了AttributeModifier机制，可以通过Modifier对象动态修改属性。能力对比如下：

| 能力 | @Styles | @Extend | AttributeModifier |
| --- | --- | --- | --- |
| 跨文件导出 | 不支持 | 不支持 | 支持 |
| 通用属性设置 | 支持 | 支持 | 支持 |
| 通用事件设置 | 支持 | 支持 | 部分支持 |
| 组件特有属性设置 | 不支持 | 支持 | 部分支持 |
| 组件特有事件设置 | 不支持 | 支持 | 部分支持 |
| 参数传递 | 不支持 | 支持 | 支持 |
| 多态样式 | 支持 | 不支持 | 支持 |
| 业务逻辑 | 不支持 | 不支持 | 支持 |

可以看出，与@Styles和@Extend相比，AttributeModifier提供了更强的能力和灵活性，且在持续完善全量的属性和事件设置能力，因此推荐优先使用AttributeModifier。

## 接口定义

```
1. declare interface AttributeModifier<T> {

3. applyNormalAttribute?(instance: T): void;

5. applyPressedAttribute?(instance: T): void;

7. applyFocusedAttribute?(instance: T): void;

9. applyDisabledAttribute?(instance: T): void;

11. applySelectedAttribute?(instance: T): void;

13. }
```

[ButtonModifier01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier01.ets#L15-L29)

AttributeModifier是一个接口，开发者需要实现其中的applyXxxAttribute方法来实现对应场景的属性设置。Xxx表示多态的场景，支持默认态（Normal）、按压态（Pressed）、焦点态（Focused）、禁用态（Disabled）、选择态（Selected）。T是组件的属性类型，开发者可以在回调中获取到属性对象，通过该对象设置属性。

```
1. declare class CommonMethod<T> {
2. attributeModifier(modifier: AttributeModifier<T>): T;
3. }
```

[ButtonModifier01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier01.ets#L31-L35)

组件的通用方法增加了attributeModifier方法，支持传入自定义的Modifier。由于组件在实例化时会明确T的类型，所以调用该方法时，T必须指定为组件对应的Attribute类型，或者是CommonAttribute。

## 使用说明

* 组件通用方法attributeModifier支持传入一个实现AttributeModifier<T>接口的实例，T必须指定为组件对应的Attribute类型，或者是[通用属性](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/ts-component-general-attributes.md)（CommonAttribute）。
* 在组件首次初始化或者关联的状态变量发生变化时，如果传入的实例实现了对应接口，会触发applyNormalAttribute。
* 回调[applyNormalAttribute](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#applynormalattribute)时，会传入组件属性对象，通过该对象可以设置当前组件的属性/事件。
* 暂未支持的属性/事件，执行时会抛异常。
* 属性变化触发applyXxxAttribute函数时，该组件之前已设置的属性，在本次变化后未设置的属性会恢复为属性的默认值。
* 可以通过该接口使用多态样式的功能，例如如果需要在组件进入按压态时设置某些属性，就可以通过自定义实现[applyPressedAttribute](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#applypressedattribute)方法完成。
* 在attributeModifier中设置的属性尽量不要与其他方法设置的属性相同，避免在页面刷新时attributeModifier不生效。
* 一个Modifier实例对象可以在多个组件上使用。
* 一个组件上多次使用applyNormalAttribute设置不同的Modifier实例，每次状态变量刷新均会按顺序执行这些实例的方法属性设置，同样遵循属性覆盖原则。

## 设置和修改组件属性

AttributeModifier可以分离UI与样式，支持参数传递及业务逻辑编写，并且通过状态变量触发刷新。

```
1. export class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
2. // 可以实现一个Modifier，定义私有的成员变量，外部可动态修改
3. public isDark: boolean = false

5. // 通过构造函数，创建时传参
6. constructor(dark?: boolean) {
7. this.isDark = dark ?? false
8. }

10. applyNormalAttribute(instance: ButtonAttribute): void {
11. // instance为Button的属性对象，可以通过instance对象对属性进行修改
12. if (this.isDark) { // 支持业务逻辑的编写
13. // 属性变化触发apply函数时，变化前已设置并且变化后未设置的属性会恢复为默认值
14. instance.backgroundColor('#707070')
15. } else {
16. // 支持属性的链式调用
17. instance.backgroundColor('#17A98D')
18. .borderColor('#707070')
19. .borderWidth(2)
20. }
21. }
22. }
```

[ButtonModifier01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier01.ets#L37-L60)

```
1. // pages/Button1.ets
2. import { MyButtonModifier } from '../Common/ButtonModifier01'

4. @Entry
5. @Component
6. struct Button1 {
7. // 支持用状态装饰器修饰，行为和普通的对象一致
8. @State modifier: MyButtonModifier = new MyButtonModifier(true);

10. build() {
11. Row() {
12. Column() {
13. Button('Button')
14. .attributeModifier(this.modifier)
15. .onClick(() => {
16. // 对象的一层属性被修改时，会触发UI刷新，重新执行applyNormalAttribute
17. this.modifier.isDark = !this.modifier.isDark
18. })
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

[Button1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/pages/Button1.ets#L15-L41)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/GZWNj__eTwq4v6ycmfZcFA/zh-cn_image_0000002592218428.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063239Z&HW-CC-Expire=86400&HW-CC-Sign=4CE332868AF13759541101B2A957575466119327FD3C2E699E352130116388AF)

```
1. export class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
2. // 可以实现一个Modifier，定义私有的成员变量，外部可动态修改
3. public isDark: boolean = false

5. // 通过构造函数，创建时传参
6. constructor(dark?: boolean) {
7. this.isDark = dark ?? false
8. }

10. applyNormalAttribute(instance: ButtonAttribute): void {
11. // instance为Button的属性对象，可以通过instance对象对属性进行修改
12. if (this.isDark) { // 支持业务逻辑的编写
13. // 属性变化触发apply函数时，变化前已设置并且变化后未设置的属性会恢复为默认值
14. instance.backgroundColor('#707070')
15. } else {
16. // 支持属性的链式调用
17. instance.backgroundColor('#17A98D')
18. .borderColor('#707070')
19. .borderWidth(2)
20. }
21. }
22. }
```

[ButtonModifier01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier01.ets#L37-L60)

```
1. // pages/Button2.ets
2. import { MyButtonModifier } from '../Common/ButtonModifier01'

4. @Entry
5. @Component
6. struct Button2 {
7. @State modifier: MyButtonModifier = new MyButtonModifier(true);

9. build() {
10. Row() {
11. Column() {
12. // 先设置属性，后设置modifier，按钮颜色会跟随modifier的值改变
13. Button('Button')
14. .backgroundColor('#2787D9')
15. .attributeModifier(this.modifier)
16. .onClick(() => {
17. this.modifier.isDark = !this.modifier.isDark
18. })
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

[Button2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/pages/Button2.ets#L15-L41)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zPRStyotSdKffmJ0GDvvCA/zh-cn_image_0000002592378362.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063239Z&HW-CC-Expire=86400&HW-CC-Sign=7AFB55D8CE8A70ACC91430471D5E5EE1713F55F1B06D8BEA178BD1F25F54BAED)

当一个组件上多次使用applyNormalAttribute设置不同的Modifier实例时，每次状态变量刷新均会按顺序执行这些实例的方法属性设置，遵循属性覆盖原则，即后设置的属性生效。

```
1. export class MyButtonModifier2 implements AttributeModifier<ButtonAttribute> {
2. public isDark: boolean = false

4. constructor(dark?: boolean) {
5. this.isDark = dark ?? false
6. }

8. applyNormalAttribute(instance: ButtonAttribute): void {
9. if (this.isDark) {
10. instance.backgroundColor(Color.Black)
11. .width(200)
12. } else {
13. instance.backgroundColor(Color.Red)
14. .width(100)
15. }
16. }
17. }
```

[ButtonModifier02.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier02.ets#L16-L34)

```
1. export class MyButtonModifier3 implements AttributeModifier<ButtonAttribute> {
2. public isDark2: boolean = false

4. constructor(dark?: boolean) {
5. this.isDark2 = dark ? dark : false
6. }

8. applyNormalAttribute(instance: ButtonAttribute): void {
9. if (this.isDark2) {
10. instance.backgroundColor('#2787D9')
11. } else {
12. instance.backgroundColor('#707070')
13. }
14. }
15. }
```

[ButtonModifier03.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier03.ets#L16-L32)

```
1. // pages/Button3.ets
2. import { MyButtonModifier2 } from '../Common/ButtonModifier02';
3. import { MyButtonModifier3 } from '../Common/ButtonModifier03';

5. @Entry
6. @Component
7. struct Button3 {
8. @State modifier: MyButtonModifier2 = new MyButtonModifier2(true);
9. @State modifier2: MyButtonModifier3 = new MyButtonModifier3(true);

11. build() {
12. Row() {
13. Column() {
14. Button('Button')
15. .attributeModifier(this.modifier)
16. .attributeModifier(this.modifier2)
17. .onClick(() => {
18. this.modifier.isDark = !this.modifier.isDark
19. this.modifier2.isDark2 = !this.modifier2.isDark2
20. })
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

[Button3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/pages/Button3.ets#L15-L43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/AtT8zu1eQgqqZpOGSSvbiw/zh-cn_image_0000002622857869.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063239Z&HW-CC-Expire=86400&HW-CC-Sign=B69BDB384A422A1BDAB34F5D6DBF56ECA05D65BB249ACC398B16CE85B58E56BF)

## 设置多态样式、事件

使用AttributeModifier设置多态样式、事件，实现事件逻辑的复用，支持默认态（Normal）、按压态（Pressed）、焦点态（Focused）、禁用态（Disabled）、选择态（Selected）。例如如果需要在组件进入按压态时设置某些属性，就可以通过自定义实现applyPressedAttribute方法完成。

```
1. export class MyButtonModifier4 implements AttributeModifier<ButtonAttribute> {
2. applyNormalAttribute(instance: ButtonAttribute): void {
3. // instance为Button的属性对象，设置正常状态下属性值
4. instance.backgroundColor('#17A98D')
5. .borderColor('#707070')
6. .borderWidth(2)
7. }

9. applyPressedAttribute(instance: ButtonAttribute): void {
10. // instance为Button的属性对象，设置按压状态下属性值
11. instance.backgroundColor('#2787D9')
12. .borderColor('#FFC000')
13. .borderWidth(5)
14. }
15. }
```

[ButtonModifier04.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/Common/ButtonModifier04.ets#L16-L32)

```
1. // pages/Button4.ets
2. import { MyButtonModifier4 } from '../Common/ButtonModifier04'

4. @Entry
5. @Component
6. struct Button4 {
7. @State modifier: MyButtonModifier4 = new MyButtonModifier4();

9. build() {
10. Row() {
11. Column() {
12. Button('Button')
13. .attributeModifier(this.modifier)
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

[Button4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/ButtonAttribute/entry/src/main/ets/pages/Button4.ets#L15-L36)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/DbTFiV6RQrKZ0UYadmI7SQ/zh-cn_image_0000002622697991.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063239Z&HW-CC-Expire=86400&HW-CC-Sign=3109F11D317FE5B1D9DBD2378C4A1622E482B1C4FA8B7BF266965DD3774C8FFB)

## 属性或事件对attributeModifier的支持情况

通过attributeModifier动态设置属性或事件的能力从API version 11开始支持。

### 属性或事件不支持attributeModifier的范围

下表说明了当前不支持attributeModifier的属性或事件。若无特殊说明，属性或事件默认在首次开放时支持attributeModifier。

| 组件通用信息/系统组件的名称 | 属性/事件的名称 | 告警信息 | 说明 |
| --- | --- | --- | --- |
| CommonAttribute | [accessibilityText](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitytext12) | - | - |
| CommonAttribute | [accessibilityDescription](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitydescription12) | - | - |
| CommonAttribute | [animation](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/动画/属性动画 (animation)/ts-animatorproperty.md#animation>) | Method not implemented. | 不支持animation相关属性。 |
| CommonAttribute | [attributeModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier) | - | attributeModifier不支持嵌套使用，不生效。 |
| CommonAttribute | [backgroundFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#backgroundfilter) | is not callable | - |
| CommonAttribute | [chainWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainweight14) | is not callable | - |
| CommonAttribute | [compositingFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#compositingfilter) | is not callable | - |
| CommonAttribute | [drawModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/自定义绘制设置/ts-universal-attributes-draw-modifier.md#drawmodifier) | is not callable | 不支持modifier相关的属性。 |
| CommonAttribute | [foregroundFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#foregroundfilter) | is not callable | - |
| CommonAttribute | [freeze](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#freeze18) | is not callable | - |
| CommonAttribute | [gesture](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/绑定手势/绑定手势事件/ts-gesture-settings.md#gesture) | Method not implemented. | 不支持gesture相关的属性。 |
| CommonAttribute | [gestureModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态手势设置/ts-universal-attributes-gesture-modifier.md#gesturemodifier) | is not callable | 不支持modifier相关的属性。 |
| CommonAttribute | [onAccessibilityHover](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/无障碍相关/无障碍悬浮事件/ts-universal-accessibility-hover-event.md#onaccessibilityhover) | is not callable | - |
| CommonAttribute | [onDigitalCrown](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/表冠事件/ts-universal-events-crown.md#ondigitalcrown) | is not callable. | - |
| CommonAttribute | [parallelGesture](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/绑定手势/绑定手势事件/ts-gesture-settings.md#parallelgesture) | Method not implemented. | 不支持gesture相关的属性。 |
| CommonAttribute | [priorityGesture](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/绑定手势/绑定手势事件/ts-gesture-settings.md#prioritygesture) | Method not implemented. | 不支持gesture相关的属性。 |
| CommonAttribute | [reuseId](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/其他/复用标识/ts-universal-attributes-reuse-id.md#reuseid) | Method not implemented. | - |
| CommonAttribute | [stateStyles](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/多态样式/ts-universal-attributes-polymorphic-style.md#statestyles) | Method not implemented. | 不支持stateStyles相关的属性。 |
| CommonAttribute | [useSizeType](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/已停止维护的组件与接口/栅格设置/ts-universal-attributes-grid.md#属性) | Method not implemented. | 不支持已废弃属性。 |
| CommonAttribute | [visualEffect](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#visualeffect) | is not callable | - |
| CommonAttribute | [bindContextMenu](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#bindcontextmenu12) | Method not implemented. | 不支持入参为CustomBuilder。 |
| CommonAttribute | [bindContentCover](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/全屏模态转场/ts-universal-attributes-modal-transition.md#bindcontentcover) | Method not implemented. | 不支持入参为CustomBuilder。 |
| CommonAttribute | [bindSheet](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#bindsheet) | Method not implemented. | 不支持入参为CustomBuilder。 |
| CommonAttribute | [dragPreview](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/拖拽控制/ts-universal-attributes-drag-drop.md#dragpreview15) | Builder is not supported. | 不支持入参为CustomBuilder。 |
| CommonAttribute | [bindPopup](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/Popup控制/ts-universal-attributes-popup.md#bindpopup) | Method not implemented. | 不支持入参为CustomBuilder。 |
| CommonAttribute | [accessibilityVirtualNode](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilityvirtualnode11) | is not callable | 不支持入参为CustomBuilder。 |
| CommonAttribute | [chainWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainweight14) | - | - |
| CheckboxGroup | [contentModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md#contentmodifier21) | - | - |
| CommonAttribute | [backgroundImage](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundimage18) | - | - |
| CommonAttribute | [onClick](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/点击事件/ts-universal-events-click.md#onclick12) | - | - |
| CommonAttribute | [toolbar](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/其他/工具栏设置/ts-universal-attributes-toolbar.md#toolbar) | - | - |
| CommonAttribute | [accessibilityGroup](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitygroup14) | - | - |
| CommonAttribute | [reuse](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/其他/复用选项/ts-universal-attributes-reuse.md#reuse) | - | - |
| CommonAttribute | [onGestureRecognizerJudgeBegin](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势控制/手势拦截增强/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13) | - | - |
| EmbeddedComponent | [onError](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/EmbeddedComponent/ts-container-embedded-component.md#onerror) | - | - |
| EmbeddedComponent | [onTerminated](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/EmbeddedComponent/ts-container-embedded-component.md#onterminated) | - | - |
| NavDestination | [backButtonIcon19+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#backbuttonicon19) | - | - |
| NavDestination | [menus19+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#menus19) | - | - |
| NavDestination | [customTransition](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#customtransition15) | - | - |
| Navigation | [backButtonIcon](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#backbuttonicon19) | - | - |
| Navigation | [menus](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#menus19) | - | - |
| Repeat | [each](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/Repeat/ts-rendering-control-repeat.md#each) | - | - |
| Repeat | [key](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/Repeat/ts-rendering-control-repeat.md#key) | - | - |
| Repeat | [virtualScroll](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/Repeat/ts-rendering-control-repeat.md#virtualscroll) | - | - |
| Repeat | [template](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/Repeat/ts-rendering-control-repeat.md#template) | - | - |
| Repeat | [templateId](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/Repeat/ts-rendering-control-repeat.md#templateid) | - | - |
| Search | [customKeyboard](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md#customkeyboard10) | - | - |
| Search | [onWillAttachIME](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md#onwillattachime20) | - | - |
| Select | [menuItemContentModifier12+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#menuitemcontentmodifier12) | - | - |
| Select | [menuItemContentModifier18+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#menuitemcontentmodifier18) | - | - |
| Select | [textModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#textmodifier20) | - | - |
| Select | [arrowModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#arrowmodifier20) | - | - |
| Select | [optionTextModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#optiontextmodifier20) | - | - |
| Select | [selectedOptionTextModifier](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#selectedoptiontextmodifier20) | - | - |
| Slider | [digitalCrownSensitivity](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md#digitalcrownsensitivity18) | - | - |
| Swiper | [prevMargin](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md#prevmargin10) | - | - |
| Swiper | [nextMargin](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md#nextmargin10) | - | - |
| TextArea | [customKeyboard](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md#customkeyboard10) | - | - |
| Text | [bindSelectionMenu](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md#bindselectionmenu11) | - | - |
| TextInput | [customKeyboard](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#customkeyboard10) | - | - |
| TextInput | [onWillAttachIME](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onwillattachime20) | - | - |
| TextPicker | [onEnterSelectedArea](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md#onenterselectedarea18) | - | - |
| TimePicker | [onEnterSelectedArea](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md#onenterselectedarea18) | - | - |

### 属性或事件的起始版本与支持attributeModifier版本不一致的范围

下表说明了属性或事件的起始版本与默认支持attributeModifier版本不一致的情况。若无特殊说明，属性或事件默认在首次开放时支持attributeModifier。

| 组件通用信息/系统组件的名称 | 属性/事件的名称 | 属性/事件的起始版本 | 支持attributeModifier的版本 |
| --- | --- | --- | --- |
| AlphabetIndexer | [autoCollapse](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md#autocollapse11) | 11 | 12 |
| Button | [buttonStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Button/ts-basic-components-button.md#buttonstyle11) | 11 | 12 |
| Button | [controlSize](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Button/ts-basic-components-button.md#controlsize11) | 11 | 12 |
| CalendarPicker | [onChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/CalendarPicker/ts-basic-components-calendarpicker.md#onchange18) | 18 | 20 |
| Canvas | [enableAnalyzer](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/Canvas/ts-components-canvas-canvas.md#enableanalyzer12) | 12 | 20 |
| CommonAttribute | [accessibilityTextHint](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitytexthint12) | 12 | 20 |
| CommonAttribute | [accessibilityChecked](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitychecked13) | 13 | 20 |
| CommonAttribute | [accessibilitySelected](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilityselected13) | 13 | 20 |
| CommonAttribute | [background](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#background10) | 10 | 20 |
| CommonAttribute | [visualEffect](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#visualeffect) | 12 | 20 |
| CommonAttribute | [onDragStart](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/拖拽事件/ts-universal-events-drag-drop.md#ondragstart) | 8 | 13 |
| CommonAttribute | [onVisibleAreaApproximateChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/组件变化事件/组件可见区域变化事件/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17) | 17 | 23 |
| CommonAttribute | [onVisibleAreaChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/组件变化事件/组件可见区域变化事件/ts-universal-component-visible-area-change-event.md#onvisibleareachange) | 9 | 20 |
| CommonAttribute | [onTouchIntercept](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互事件分发控制/自定义事件拦截/ts-universal-attributes-on-touch-intercept.md#ontouchintercept) | 12 | 20 |
| CommonAttribute | [onPreDrag](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/拖拽事件/ts-universal-events-drag-drop.md#onpredrag12) | 12 | 20 |
| CommonAttribute | [onChildTouchTest](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互事件分发控制/自定义事件分发/ts-universal-attributes-on-child-touch-test.md#onchildtouchtest11) | 11 | 20 |
| CommonAttribute | [backgroundFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#backgroundfilter) | 12 | 20 |
| CommonAttribute | [foregroundFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#foregroundfilter) | 12 | 20 |
| CommonAttribute | [compositingFilter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/视效设置/ts-universal-attributes-filter-effect.md#compositingfilter) | 12 | 20 |
| CommonAttribute | [foregroundBlurStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/组件内容模糊/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle) | 10 | 18 |
| CommonAttribute | [freeze12+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#freeze12) | 12 | 20 |
| CommonAttribute | [freeze18+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#freeze18) | 18 | 20 |
| CommonAttribute | [dragPreviewOptions](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/拖拽控制/ts-universal-attributes-drag-drop.md#dragpreviewoptions11) | 11 | 12 |
| CommonAttribute | [bindMenu](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/弹窗控制/菜单控制/ts-universal-attributes-menu.md#bindmenu) | 11 | 20 |
| CommonAttribute | [transition](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/动画/组件内转场 (transition)/ts-transition-animation-component.md#transition12>) | 12 | 20 |
| CommonAttribute | [safeAreaPadding](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#safeareapadding14) | 14 | 18 |
| CommonAttribute | [pixelRound](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/组件级像素取整/ts-universal-attributes-pixelroundforcomponent.md#pixelround) | 11 | 12 |
| ContainerSpan | [textBackgroundStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/ContainerSpan/ts-basic-components-containerspan.md#textbackgroundstyle) | 11 | 12 |
| DatePicker | [onDateChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/DatePicker/ts-basic-components-datepicker.md#ondatechange18) | 18 | 20 |
| FolderStack | [alignContent](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/FolderStack/ts-container-folderstack.md#aligncontent) | 11 | 12 |
| FolderStack | [onFolderStateChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/FolderStack/ts-container-folderstack.md#onfolderstatechange) | 11 | 20 |
| FolderStack | [onHoverStatusChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/FolderStack/ts-container-folderstack.md#onhoverstatuschange12) | 11 | 20 |
| FolderStack | [enableAnimation](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/FolderStack/ts-container-folderstack.md#enableanimation) | 11 | 12 |
| FolderStack | [autoHalfFold](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/FolderStack/ts-container-folderstack.md#autohalffold) | 11 | 12 |
| Gauge | [privacySensitive](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Gauge/ts-basic-components-gauge.md#privacysensitive12) | 12 | 20 |
| Image | [enableAnalyzer](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md#enableanalyzer11) | 11 | 12 |
| Image | [resizable](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md#resizable11) | 11 | 20 |
| List | [OnScrollVisibleContentChangeCallback](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#onscrollvisiblecontentchangecallback12) | 12 | 14 |
| List | [onItemDragStart](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#onitemdragstart8) | 8 | 14 |
| NavDestination | [title](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#title) | 9 | 12 |
| NavDestination | [mode](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#mode11) | 11 | 12 |
| NavDestination | [backButtonIcon11+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#backbuttonicon11) | 11 | 12 |
| NavDestination | [menus12+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#menus12) | 12 | 14 |
| NavDestination | [toolbarConfiguration](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#toolbarconfiguration13) | 13 | 20 |
| NavDestination | [onReady](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onready11) | 11 | 20 |
| NavDestination | [onWillAppear](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onwillappear12) | 12 | 20 |
| NavDestination | [onWillDisappear](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onwilldisappear12) | 12 | 20 |
| NavDestination | [onWillShow](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onwillshow12) | 12 | 20 |
| NavDestination | [onWillHide](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onwillhide12) | 12 | 20 |
| NavDestination | [systemBarStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#systembarstyle12) | 12 | 20 |
| NavDestination | [onResult](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onresult15) | 15 | 22 |
| NavDestination | [bindToScrollable](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#bindtoscrollable14) | 14 | 22 |
| NavDestination | [bindToNestedScrollable](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#bindtonestedscrollable14) | 14 | 22 |
| NavDestination | [onActive](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onactive17) | 17 | 22 |
| NavDestination | [onInactive](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#oninactive17) | 17 | 22 |
| NavDestination | [onNewParam](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onnewparam19) | 19 | 22 |
| Navigation | [title](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#title) | 8 | 12 |
| Navigation | [toolbarConfiguration](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#toolbarconfiguration10) | 10 | 20 |
| Navigation | [customNavContentTransition](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#customnavcontenttransition11) | 11 | 20 |
| Navigation | [systemBarStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#systembarstyle12) | 12 | 20 |
| Navigation | [enableVisibilityLifecycleWithContentCover](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#enablevisibilitylifecyclewithcontentcover21) | 21 | 23 |
| PatternLock | [backgroundColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/PatternLock/ts-basic-components-patternlock.md#backgroundcolor) | 9 | 20 |
| PatternLock | [onDotConnect](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/PatternLock/ts-basic-components-patternlock.md#ondotconnect11) | 11 | 20 |
| Progress | [privacySensitive](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Progress/ts-basic-components-progress.md#privacysensitive12) | 12 | 20 |
| Refresh | [onOffsetChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Refresh/ts-container-refresh.md#onoffsetchange12) | 12 | 20 |
| RichEditor | [customKeyboard](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#customkeyboard) | 10 | 23 |
| RichEditor | [onDidIMEInput](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#ondidimeinput12) | 12 | 20 |
| RichEditor | [enablePreviewText](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#enablepreviewtext12) | 12 | 18 |
| RichEditor | [placeholder](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#placeholder12) | 12 | 18 |
| RichEditor | [onWillChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#onwillchange12) | 12 | 18 |
| RichEditor | [onDidChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#ondidchange12) | 12 | 18 |
| RichEditor | [editMenuOptions](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#editmenuoptions12) | 12 | 18 |
| RichEditor | [enableKeyboardOnFocus](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#enablekeyboardonfocus12) | 12 | 18 |
| RichEditor | [enableHapticFeedback](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#enablehapticfeedback13) | 13 | 20 |
| RichEditor | [barState](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#barstate13) | 13 | 18 |
| Select | [menuBackgroundColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#menubackgroundcolor11) | 11 | 12 |
| Select | [menuBackgroundBlurStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/Select/ts-basic-components-select.md#menubackgroundblurstyle11) | 11 | 12 |
| Swiper | [displayCount](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md#displaycount8) | 8 | 12 |
| SymbolGlyph | [fontSize](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md#fontsize) | 11 | 12 |
| SymbolGlyph | [fontColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md#fontcolor) | 11 | 12 |
| SymbolGlyph | [fontWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md#fontweight) | 11 | 12 |
| SymbolGlyph | [effectStrategy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md#effectstrategy) | 11 | 12 |
| SymbolGlyph | [renderingStrategy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md#renderingstrategy) | 11 | 12 |
| SymbolSpan | [fontSize](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolSpan/ts-basic-components-symbolspan.md#fontsize) | 11 | 12 |
| SymbolSpan | [fontColor](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolSpan/ts-basic-components-symbolspan.md#fontcolor) | 11 | 12 |
| SymbolSpan | [fontWeight](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolSpan/ts-basic-components-symbolspan.md#fontweight) | 11 | 12 |
| SymbolSpan | [effectStrategy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolSpan/ts-basic-components-symbolspan.md#effectstrategy) | 11 | 12 |
| SymbolSpan | [renderingStrategy](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/SymbolSpan/ts-basic-components-symbolspan.md#renderingstrategy) | 11 | 12 |
| ScrollableCommonAttribute | [onWillScroll](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/滚动组件通用接口/ts-container-scrollable-common.md#onwillscroll12) | 12 | 14 |
| ScrollableCommonAttribute | [onDidScroll](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/滚动组件通用接口/ts-container-scrollable-common.md#ondidscroll12) | 12 | 14 |
| TabContent | [onWillShow](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/TabContent/ts-container-tabcontent.md#onwillshow12) | 12 | 20 |
| TabContent | [onWillHide](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/TabContent/ts-container-tabcontent.md#onwillhide12) | 12 | 20 |
| Tabs | [edgeEffect](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#edgeeffect12) | 12 | 17 |
| Tabs | [customContentTransition](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#customcontenttransition11) | 11 | 20 |
| Tabs | [onContentWillChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#oncontentwillchange12) | 12 | 20 |
| Tabs | [barBackgroundBlurStyle](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#barbackgroundblurstyle11) | 11 | 12 |
| TextArea | [enterKeyType](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md#enterkeytype11) | 11 | 12 |
| Text | [enableHapticFeedback](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md#enablehapticfeedback13) | 13 | 18 |
| TextInput | [showCounter](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#showcounter11) | 11 | 12 |
| TextInput | [onSecurityStateChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md#onsecuritystatechange12) | 12 | 20 |
| TextPicker | [onScrollStop14+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md#onscrollstop14) | 14 | 20 |
| TextPicker | [onScrollStop18+](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md#onscrollstop18) | 18 | 20 |
| TextTimer | [textShadow](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/TextTimer/ts-basic-components-texttimer.md#textshadow11) | 11 | 12 |
| TimePicker | [enableHapticFeedback](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md#enablehapticfeedback12) | 12 | 18 |
| TimePicker | [onChange](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md#onchange18) | 18 | 20 |
| Video | [enableAnalyzer](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Video/ts-media-components-video.md#enableanalyzer12) | 12 | 20 |
| Video | [analyzerConfig](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Video/ts-media-components-video.md#analyzerconfig12) | 12 | 20 |
| Video | [onError](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Video/ts-media-components-video.md#onerror) | 7 | 20 |
| WaterFlow | [onScrollIndex](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md#onscrollindex11) | 11 | 20 |
