---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbuttonv2
title: SegmentButtonV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SegmentButtonV2
category: harmonyos-references
scraped_at: 2026-06-11T15:50:19+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:bc0b3c3cfc503d9e912f1158cffcea7d047f7114f36fb66e9064a6e41e0cf1a1
---
分段按钮组件用于创建页签型、单选或多选的胶囊型分段按钮。

说明

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](../../通用属性/ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](../../通用事件/ts-component-general-events.md)。

## TabSegmentButtonV2

PhonePC/2in1TabletTVWearable

```
1. TabSegmentButtonV2({
2. items: SegmentButtonV2Items,
3. selectedIndex: number,
4. $selectedIndex?: OnSelectedIndexChange,
5. onItemClicked?: Callback<number>,
6. itemMinFontScale?: number | Resource,
7. itemMaxFontScale?: number | Resource,
8. itemSpace?: LengthMetrics,
9. itemFontSize?: LengthMetrics,
10. itemSelectedFontSize?: LengthMetrics,
11. itemFontColor?: ColorMetrics,
12. itemSelectedFontColor?: ColorMetrics,
13. itemFontWeight?: FontWeight,
14. itemSelectedFontWeight?: FontWeight,
15. itemBorderRadius?: LengthMetrics,
16. itemSelectedBackgroundColor?: ColorMetrics,
17. itemIconSize?: SizeT<LengthMetrics>,
18. itemIconFillColor?: ColorMetrics,
19. itemSelectedIconFillColor?: ColorMetrics,
20. itemSymbolFontSize?: LengthMetrics,
21. itemSymbolFontColor?: ColorMetrics,
22. itemSelectedSymbolFontColor?: ColorMetrics,
23. itemMinHeight?: LengthMetrics,
24. itemPadding?: LocalizedPadding,
25. itemShadow?: ShadowOptions | ShadowStyle,
26. buttonBackgroundColor?: ColorMetrics,
27. buttonBackgroundBlurStyle?: BlurStyle,
28. buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
29. buttonBackgroundEffect?: BackgroundEffectOptions,
30. buttonBorderRadius?: LengthMetrics,
31. buttonMinHeight?: LengthMetrics,
32. buttonPadding?: LengthMetrics,
33. languageDirection?: Direction,
34. enableStateAnimation?: boolean
35. })
```

**装饰器类型：** @ComponentV2

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | [SegmentButtonV2Items](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2items) | 是 | @Require  @Param | 配置分段按钮的选项集合信息。  值为undefined时，不显示选项信息。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 是 | @Require  @Param | 配置分段按钮被选中的选项下标，第一项的编号为0，之后顺序增加。  值为undefined时，不选中任何选项，其他非正数值，默认选项下标为0。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| $selectedIndex | [OnSelectedIndexChange](ohos-arkui-advanced-segmentbuttonv2.md#onselectedindexchange) | 否 | @Event | 配置分段按钮选中项变更时触发的回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onItemClicked | Callback<number> | 否 | @Event | 配置分段按钮选项被单击时触发的回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮背板颜色。  默认值：$r('sys.color.segment\_button\_v2\_tab\_button\_background')  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundBlurStyle | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | @Param | 配置分段按钮背板模糊材质。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | @Param | 配置分段按钮背板模糊材质配置参数。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundEffect | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | @Param | 配置分段按钮背板模糊配置参数。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBorderRadius | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮背板的圆角大小。  取值范围：[0, +∞)  默认值：$r('sys.float.segment\_button\_v2\_background\_corner\_radius')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonMinHeight | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮最小高度。  取值范围：[0, +∞)  默认值：只有纯文本或者纯图标选项时：$r('sys.float.segment\_button\_v2\_singleline\_background\_height')；有图文混合的选项时：$r('sys.float.segment\_button\_v2\_doubleline\_background\_height')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonPadding | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮内边距。  取值范围：[0, +∞)  默认值：$r('sys.float.padding\_level1')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项背景颜色。  默认值：$r('sys.color.segment\_button\_v2\_tab\_selected\_item\_background')  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMinHeight | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项最小高度。  取值范围：[0, +∞)  默认值：  只有纯文本或者纯图标选项时：$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')；有图文混合的选项时：$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemPadding | [LocalizedPadding](../../公共定义/基础类型定义/ts-types.md#localizedpadding12) | 否 | @Param | 配置分段按钮选项内边距。  默认值：{ top: LengthMetrics.resource($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4')) }  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemShadow | [ShadowOptions](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | @Param | 配置分段按钮选项阴影。  默认值：ShadowStyle.OUTER\_DEFAULT\_XS  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSpace | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项之间的间隔。  取值范围：[0, +∞)  默认值：LengthMetrics.vp(0)  **说明：**  不支持设置百分比类型，异常值按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMinFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最小字体缩放倍数。  取值范围：[0, 1]  默认值：0  **说明：**  设置的值小于 0 时，按值为 0 处理，设置的值大于 1，按值为 1 处理，异常值默认不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMaxFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最大放大倍数。  取值范围：[1, 2]  默认值：1  **说明：**  设置的值小于 1 时，按值为 1 处理，设置的值大于 2，按值为 2 处理，异常值默认不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮非选中选项的字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选中项的字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemSelectedFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中选项的字体颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中项的字体颜色。  默认值：$r('sys.color.font\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemSelectedFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮非选中选项的字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemFontWeight不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮选中项的字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemSelectedFontWeight不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemBorderRadius | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项的圆角大小。  取值范围：[0, +∞)  默认值：$r('sys.float.segment\_button\_v2\_selected\_corner\_radius')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemIconSize | [SizeT](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#sizett12>)<[LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>)> | 否 | @Param | 配置分段按钮选项中Image类型的图标大小。  取值范围：[0, +∞)  默认值：{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }  超出取值范围按默认值处理。  **说明：**  items设置iconModifier的width、height属性值时，itemIconSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项图标颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemIconFillColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项图标颜色。  默认值：$r('sys.color.font\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemSelectedIconFillColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSymbolFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项中HM Symbol类型图标大小。  取值范围：[0, +∞)  默认值：20fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置symbolModifier的fontSize属性值时，itemSymbolFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中选项HM Symbol类型图标的颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSymbolFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中选项的HM Symbol类型图标颜色。  默认值：$r('sys.color.font\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSelectedSymbolFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| languageDirection | [Direction](../../公共定义/枚举说明/ts-appendix-enums.md#direction) | 否 | @Param | 配置分段按钮的布局方向。  默认值：Direction.Auto  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableStateAnimation24+ | boolean | 否 | @Param | 设置当通过变量修改selectedIndex值时，是否开启分段按钮的属性动画。  true表示开启分段按钮的属性动画；未配置该属性或值为false时表示不开启分段按钮的属性动画，使用原有动画。  默认值：false  该成员只读，不支持更改。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## CapsuleSegmentButtonV2

PhonePC/2in1TabletTVWearable

```
1. CapsuleSegmentButtonV2({
2. items: SegmentButtonV2Items,
3. selectedIndex: number,
4. $selectedIndex?: OnSelectedIndexChange,
5. onItemClicked?: Callback<number>,
6. itemMinFontScale?: number | Resource,
7. itemMaxFontScale?: number | Resource,
8. itemSpace?: LengthMetrics,
9. itemFontSize?: LengthMetrics,
10. itemSelectedFontSize?: LengthMetrics,
11. itemFontColor?: ColorMetrics,
12. itemSelectedFontColor?: ColorMetrics,
13. itemFontWeight?: FontWeight,
14. itemSelectedFontWeight?: FontWeight,
15. itemBorderRadius?: LengthMetrics,
16. itemSelectedBackgroundColor?: ColorMetrics,
17. itemIconSize?: SizeT<LengthMetrics>,
18. itemIconFillColor?: ColorMetrics,
19. itemSelectedIconFillColor?: ColorMetrics,
20. itemSymbolFontSize?: LengthMetrics,
21. itemSymbolFontColor?: ColorMetrics,
22. itemSelectedSymbolFontColor?: ColorMetrics,
23. itemMinHeight?: LengthMetrics,
24. itemPadding?: LocalizedPadding,
25. itemShadow?: ShadowOptions | ShadowStyle,
26. buttonBackgroundColor?: ColorMetrics,
27. buttonBackgroundBlurStyle?: BlurStyle,
28. buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
29. buttonBackgroundEffect?: BackgroundEffectOptions,
30. buttonBorderRadius?: LengthMetrics,
31. buttonMinHeight?: LengthMetrics,
32. buttonPadding?: LengthMetrics,
33. languageDirection?: Direction,
34. enableStateAnimation?: boolean
35. })
```

**装饰器类型：** @ComponentV2

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | [SegmentButtonV2Items](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2items) | 是 | @Require  @Param | 配置分段按钮的选项集合信息。  值为undefined时，不显示选项信息。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 是 | @Require  @Param | 配置分段按钮被选中的选项下标，第一项的编号为0，之后顺序增加。  值为undefined时，不选中任何选项，其他非正数值，默认选项下标为0。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| $selectedIndex | [OnSelectedIndexChange](ohos-arkui-advanced-segmentbuttonv2.md#onselectedindexchange) | 否 | @Event | 配置分段按钮选中项变更时的回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onItemClicked | Callback<number> | 否 | @Event | 配置分段按钮选项被单击时触发的回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮背板颜色。  默认值：$r('sys.color.segment\_button\_v2\_tab\_button\_background')  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundBlurStyle | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | @Param | 配置分段按钮背板模糊材质。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | @Param | 配置分段按钮背板模糊材质配置参数。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBackgroundEffect | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | @Param | 配置分段按钮背板模糊配置参数。  默认值：undefined  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonBorderRadius | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮背板的圆角大小。  取值范围：[0, +∞)  默认值：$r('sys.float.segment\_button\_v2\_background\_corner\_radius')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonMinHeight | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮最小的高度。  取值范围：[0, +∞)  默认值：只有纯文本或者纯图标选项时：$r('sys.float.segment\_button\_v2\_singleline\_background\_height')；有图文混合的选项时：$r('sys.float.segment\_button\_v2\_doubleline\_background\_height')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buttonPadding | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮的内边距。  取值范围：[0, +∞)  默认值：$r('sys.float.padding\_level1')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项背景颜色。  默认值：$r('sys.color.comp\_background\_emphasize')  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMinHeight | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项的最小高度。  取值范围：[0, +∞)  默认值：  只有纯文本或者纯图标选项时：$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')；有图文混合的选项时：$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemPadding | [LocalizedPadding](../../公共定义/基础类型定义/ts-types.md#localizedpadding12) | 否 | @Param | 配置分段按钮选项的内边距。  默认值：{ top: LengthMetrics.resource($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4')) }  值为undefined时，按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemShadow | [ShadowOptions](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | @Param | 配置分段按钮选项的阴影。  默认值：ShadowStyle.OUTER\_DEFAULT\_XS  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSpace | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项之间的间隔。  取值范围：[0, +∞)  默认值：LengthMetrics.vp(0)  **说明：**  不支持设置百分比类型，异常值按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMinFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最小字体缩放倍数。  取值范围：[0, 1]  默认值：0  **说明：**  设置的值小于 0 时，按值为 0 处理，设置的值大于 1，按值为 1 处理，异常值默认不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemMaxFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最大字体放大倍数。  取值范围：[1, 2]  默认值：1  **说明：**  设置的值小于 1 时，按值为 1 处理，设置的值大于 2，按值为 2 处理，异常值默认不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮非选中的选项字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选中的选项字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemSelectedFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项字体颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项字体颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemSelectedFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮非选中的选项字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemFontWeight不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮选中的选项字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemSelectedFontWeight不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemBorderRadius | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项的圆角大小。  取值范围：[0, +∞)  默认值：$r('sys.float.segment\_button\_v2\_selected\_corner\_radius')  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemIconSize | [SizeT](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#sizett12>)<[LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>)> | 否 | @Param | 配置分段按钮选项中Image类型图标大小。  取值范围：[0, +∞)  默认值：{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }  超出取值范围按默认值处理。  **说明：**  items设置iconModifier的width、height属性值时，itemIconSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项图标颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemIconFillColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项图标颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemSelectedIconFillColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSymbolFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项中HM Symbol类型图标大小。  取值范围：[0, +∞)  默认值：20fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置symbolModifier的fontSize属性值时，itemSymbolFontSize不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项中HM Symbol类型图标颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSymbolFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| itemSelectedSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项中HM Symbol类型图标颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSelectedSymbolFontColor不生效。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| languageDirection | [Direction](../../公共定义/枚举说明/ts-appendix-enums.md#direction) | 否 | @Param | 配置分段按钮的布局方向。  默认值：Direction.Auto  超出取值范围按默认值处理。  该成员只读，不支持更改。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableStateAnimation24+ | boolean | 否 | @Param | 设置当通过变量修改selectedIndex时，是否开启分段按钮的属性动画。  true表示开启分段按钮的属性动画；未配置该属性或值为false时表示不开启分段按钮的属性动画，使用原有动画。  默认值：false  该成员只读，不支持更改。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## MultiCapsuleSegmentButtonV2

PhonePC/2in1TabletTVWearable

```
1. MultiCapsuleSegmentButtonV2({
2. items: SegmentButtonV2Items,
3. selectedIndexes: number[],
4. $selectedIndexes: OnSelectedIndexesChange,
5. onItemClicked?: Callback<number>,
6. itemMinFontScale?: number | Resource,
7. itemMaxFontScale?: number | Resource,
8. itemSpace?: LengthMetrics,
9. itemFontColor?: ColorMetrics,
10. itemSelectedFontColor?: ColorMetrics,
11. itemFontSize?: LengthMetrics,
12. itemSelectedFontSize?: LengthMetrics,
13. itemFontWeight?: FontWeight,
14. itemSelectedFontWeight?: FontWeight,
15. itemBorderRadius?: LengthMetrics,
16. itemBackgroundColor?: ColorMetrics,
17. itemBackgroundEffect?: BackgroundEffectOptions,
18. itemBackgroundBlurStyle?: BlurStyle,
19. itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
20. itemSelectedBackgroundColor?: ColorMetrics,
21. itemIconSize?: SizeT<LengthMetrics>,
22. itemIconFillColor?: ColorMetrics,
23. itemSelectedIconFillColor?: ColorMetrics,
24. itemSymbolFontSize?: LengthMetrics,
25. itemSymbolFontColor?: ColorMetrics,
26. itemSelectedSymbolFontColor?: ColorMetrics,
27. itemMinHeight?: LengthMetrics,
28. itemPadding?: LocalizedPadding,
29. languageDirection?: Direction
30. })
```

**装饰器类型：** @ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | [SegmentButtonV2Items](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2items) | 是 | @Require  @Param | 配置分段按钮的选项集合信息。  值为undefined时，不显示选项信息。  该成员只读，不支持更改。 |
| selectedIndexes | number[] | 是 | @Require  @Param | 配置分段按钮被选中的选项下标集合，第一项的编号为0，之后顺序增加。  值为undefined时，不选中任何选项。  **说明：**  仅支持有效的按钮编号（第一个按钮编号为0，之后按顺序累加），如没有选中项可传入空数组[]。  该成员只读，不支持更改。 |
| $selectedIndexes | [OnSelectedIndexesChange](ohos-arkui-advanced-segmentbuttonv2.md#onselectedindexeschange) | 是 | @Event | 配置分段按钮选中项变更时的回调函数。 |
| onItemClicked | Callback<number> | 否 | @Event | 配置分段按钮选项被单击时触发的回调函数。 |
| itemBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项背板颜色。  默认值：$r('sys.color.segment\_button\_v2\_multi\_capsule\_button\_background')  值为undefined时，按默认值处理。  该成员只读，不支持更改。 |
| itemBackgroundEffect | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | @Param | 配置分段按钮选项的背板效果。  默认值：undefined  该成员只读，不支持更改。 |
| itemBackgroundBlurStyle | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | @Param | 配置分段按钮选项的模糊材质。  默认值：undefined  该成员只读，不支持更改。 |
| itemBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | @Param | 配置分段按钮选项的模糊材质配置参数。  默认值：undefined  该成员只读，不支持更改。 |
| itemSelectedBackgroundColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项背景颜色。  默认值：$r('sys.color.comp\_background\_emphasize')  值为undefined时，按默认值处理。  该成员只读，不支持更改。 |
| itemMinHeight | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项的最小高度。  取值范围：[0, +∞)  默认值：  只有纯文本或者纯图标选项时：$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')；有图文混合的选项时：$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')  超出取值范围按默认值处理。  该成员只读，不支持更改。 |
| itemPadding | [LocalizedPadding](../../公共定义/基础类型定义/ts-types.md#localizedpadding12) | 否 | @Param | 配置分段按钮选项的内边距。  默认值：{ top: LengthMetrics.resource($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4')) }  值为undefined时，按默认值处理。  该成员只读，不支持更改。 |
| itemSpace | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项之间的间隔。  取值范围：[0, +∞)  默认值：LengthMetrics.vp(1)  **说明：**  不支持设置百分比类型，异常值按默认值处理。  该成员只读，不支持更改。 |
| itemMinFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最小缩放倍数。  取值范围：[0, 1]  默认值：0  **说明：**  设置的值小于 0 时，按值为 0 处理，设置的值大于 1，按值为 1 处理，异常值默认不生效。  该成员只读，不支持更改。 |
| itemMaxFontScale | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | @Param | 配置分段按钮选项文字大小的最大放大倍数。  取值范围：[1, 2]  默认值：1  **说明：**  设置的值小于 1 时，按值为 1 处理，设置的值大于 2，按值为 2 处理，异常值默认不生效。  该成员只读，不支持更改。 |
| itemSelectedFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选中的选项字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemSelectedFontSize不生效。  该成员只读，不支持更改。 |
| itemFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项字体颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemFontColor不生效。  该成员只读，不支持更改。 |
| itemFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮非选中的选项字体大小。  取值范围：[0, +∞)  默认值：14fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置textModifier的fontSize属性值时，itemFontSize不生效。  该成员只读，不支持更改。 |
| itemSelectedFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项字体颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置textModifier的fontColor属性值时，itemSelectedFontColor不生效。  该成员只读，不支持更改。 |
| itemFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮非选中的选项字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemFontWeight不生效。  该成员只读，不支持更改。 |
| itemSelectedFontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | 否 | @Param | 配置分段按钮选中的选项字体字重。  默认值：FontWeight.Medium  超出取值范围按默认值处理。  **说明：**  items设置textModifier的fontWeight属性值时，itemSelectedFontWeight不生效。  该成员只读，不支持更改。 |
| itemBorderRadius | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项的圆角大小。  取值范围：[0, +∞)  默认值：$r('sys.float.segment\_button\_v2\_multi\_corner\_radius')  超出取值范围按默认值处理。  该成员只读，不支持更改。 |
| itemIconSize | [SizeT](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#sizett12>)<[LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>)> | 否 | @Param | 配置分段按钮选项中Image类型图标大小。  取值范围：[0, +∞)  默认值：{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }  超出取值范围按默认值处理。  **说明：**  items设置iconModifier的width、height属性值时，itemIconSize不生效。  该成员只读，不支持更改。 |
| itemIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项图标颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemIconFillColor不生效。  该成员只读，不支持更改。 |
| itemSelectedIconFillColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项图标颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置iconModifier的fillColor属性值时，itemSelectedIconFillColor不生效。  该成员只读，不支持更改。 |
| itemSymbolFontSize | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | @Param | 配置分段按钮选项中HM Symbol类型图标大小。  取值范围：[0, +∞)  默认值：20fp  **说明：**  不支持设置百分比类型，异常值按默认值处理。  items设置symbolModifier的fontSize属性值时，itemSymbolFontSize不生效。  该成员只读，不支持更改。 |
| itemSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮非选中的选项中HM Symbol类型图标颜色。  默认值：$r('sys.color.font\_secondary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSymbolFontColor不生效。  该成员只读，不支持更改。 |
| itemSelectedSymbolFontColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | @Param | 配置分段按钮选中的选项中HM Symbol类型图标颜色。  默认值：$r('sys.color.font\_on\_primary')  值为undefined时，按默认值处理。  **说明：**  items设置symbolModifier的fontColor属性值时，itemSelectedSymbolFontColor不生效。  该成员只读，不支持更改。 |
| languageDirection | [Direction](../../公共定义/枚举说明/ts-appendix-enums.md#direction) | 否 | @Param | 配置分段按钮的布局方向。  默认值：Direction.Auto  超出取值范围按默认值处理。  该成员只读，不支持更改。 |

## SegmentButtonV2Items

PhonePC/2in1TabletTVWearable

分段按钮选项集合。

继承自 Array<[SegmentButtonV2Item](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2item)>

**装饰器类型：** @ObservedV2

### constructor

PhonePC/2in1TabletTVWearable

constructor(items: SegmentButtonV2ItemOptions[])

构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SegmentButtonV2ItemOptions](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2itemoptions)[] | 是 | 分段按钮选项配置参数集合。 |

### hasHybrid

PhonePC/2in1TabletTVWearable

get hasHybrid():boolean

是否支持图文混合选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持图文混合选项。  true：有图文混合选项；false：无图文混合选项。 |

## SegmentButtonV2Item

PhonePC/2in1TabletTVWearable

**装饰器类型：** @ObservedV2

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项文本。  默认值：undefined  装饰器类型：@Trace |
| icon | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项图片类型图标。  默认值：undefined  装饰器类型：@Trace |
| symbol | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | 是 | 分段按钮选项的HM Symbol类型图标。  默认值：undefined  装饰器类型：@Trace |
| enabled | boolean | 否 | 否 | 分段按钮选项是否可用。  默认值：true  true：可用；false：不可用。  值为undefined时，按默认值处理。  装饰器类型：@Trace |
| textModifier | [TextModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 分段按钮选项文本属性样式修改器。  默认值：undefined  装饰器类型：@Trace |
| iconModifier | [ImageModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 分段按钮选项图片类型图标属性的样式修改器。  默认值：undefined  装饰器类型：@Trace |
| symbolModifier | [SymbolGlyphModifier](../../通用属性/动态属性与自定义/动态SymbolGlyphModifier属性设置/ts-attr-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 分段按钮选项HM Symbol类型图标属性样式修改器。  默认值：undefined  装饰器类型：@Trace |
| accessibilityText | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项的无障碍文本[accessibilityText](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitytext)。  默认值：""  值为undefined时，按默认值处理。  装饰器类型：@Trace |
| accessibilityDescription | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项的无障碍说明[accessibilityDescription](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitydescription)。  默认值：""  值为undefined时，按默认值处理。  装饰器类型：@Trace |
| accessibilityLevel | string | 否 | 是 | 分段按钮选项的无障碍重要性[accessibilityLevel](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitylevel)。  默认值："auto"  值为undefined时，按默认值处理。  装饰器类型：@Trace |

说明

1. 当配置了symbol和icon 时，symbol的显示优先级更高。
2. 当symbol和symbolModifier 同时设置HM Symbol资源时，symbolModifier设置的资源具有更高的显示优先级。

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: SegmentButtonV2ItemOptions)

构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SegmentButtonV2ItemOptions](ohos-arkui-advanced-segmentbuttonv2.md#segmentbuttonv2itemoptions) | 是 | 分段按钮选项配置参数。 |

### isHybrid

PhonePC/2in1TabletTVWearable

get isHybrid():boolean

检查分段按钮选项是否已配置文本和图标。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 选项是否有图文混合配置。  true：有图文混合配置；false：无图文混合配置。 |

## SegmentButtonV2ItemOptions

PhonePC/2in1TabletTVWearable

配置分段按钮选项参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项文本。  默认值：undefined |
| icon | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项图标。  默认值：undefined |
| symbol | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | 是 | 分段按钮选项图标，HM Symbol类型 。  默认值：undefined |
| enabled | boolean | 否 | 是 | 分段按钮选项是否可用。  默认值：true  true：分段按钮选项可用；false：分段按钮选项不可用。  值为undefined时，按默认值处理。 |
| textModifier | [TextModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 分段按钮选项文本属性样式修改器。  默认值：undefined |
| iconModifier | [ImageModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 修改分段按钮选项图片类型的图标属性样式。  默认值：undefined |
| symbolModifier | [SymbolGlyphModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 分段按钮选项HM Symbol类型图标属性样式修改器。  默认值：undefined |
| accessibilityText | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项无障碍文本[accessibilityText](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitytext)。  默认值：""  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 分段按钮选项无障碍说明[accessibilityDescription](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitydescription)。  默认值：""  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 分段按钮选项无障碍重要性[accessibilityLevel](../../通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitylevel)。  默认值："auto"  值为undefined时，按默认值处理。 |

说明

1. 当配置symbol和icon时，symbol的显示优先级更高。
2. 当symbol和symbolModifier同时设置HM Symbol资源时，symbolModifier设置的资源具有更高的显示优先级。

## OnSelectedIndexChange

PhonePC/2in1TabletTVWearable

type OnSelectedIndexChange = (selectedIndex: number) => void

单选分段按钮选中项变更时调用的回调函数类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | number | 是 | 分段按钮选项下标。 |

## OnSelectedIndexesChange

PhonePC/2in1TabletTVWearable

type OnSelectedIndexesChange = (selectedIndexes: number[]) => void

多选分段按钮选中项变更时调用的回调函数类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndexes | number[] | 是 | 分段按钮选项下标集合。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例 1（页签型分段按钮）

此示例说明页签型分段按钮的基本用法。

```
1. import { SegmentButtonV2Items, TabSegmentButtonV2 } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct TabSegmentButtonV2Example {
6. @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items([
7. { text: '手机' },
8. { text: '平板' },
9. { text: '2in1' },
10. { text: '智能穿戴' },
11. ]);
12. @Local textSelectedIndex: number = 0;
13. @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items([
14. { icon: $r('sys.media.ohos_ic_public_device_phone') },
15. { icon: $r('sys.media.ohos_ic_public_device_pad') },
16. { icon: $r('sys.media.ohos_ic_public_device_matebook') },
17. { icon: $r('sys.media.ohos_ic_public_device_watch') },
18. ]);
19. @Local imageSelectedIndex: number = 0;
20. @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items([
21. { symbol: $r('sys.symbol.phone') },
22. { symbol: $r('sys.symbol.pad') },
23. { symbol: $r('sys.symbol.matebook') },
24. { symbol: $r('sys.symbol.watch') },
25. ]);
26. @Local symbolSelectedIndex: number = 0;
27. @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items([
28. { text: '手机', symbol: $r('sys.symbol.phone') },
29. { text: '平板', symbol: $r('sys.symbol.pad') },
30. { text: '2in1', symbol: $r('sys.symbol.matebook') },
31. { text: '智能穿戴', symbol: $r('sys.symbol.watch') },
32. ]);
33. @Local hybridSelectedIndex: number = 0;
34. @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items([
35. { text: '年' },
36. { text: '月' },
37. { text: '周' },
38. { text: '日' },
39. { icon: $r('sys.media.ohos_ic_public_search_filled') },
40. ]);
41. @Local freeSelectedIndex: number = 0;

43. build() {
44. Scroll() {
45. Column({ space: 12 }) {
46. VCard({ title: '纯文本选项' }) {
47. TabSegmentButtonV2({
48. items: this.textItems,
49. selectedIndex: this.textSelectedIndex!!,
50. })
51. }

53. VCard({ title: '纯图标选项（Image）' }) {
54. TabSegmentButtonV2({
55. items: this.imageItems,
56. selectedIndex: this.imageSelectedIndex!!,
57. })
58. }

60. VCard({ title: '纯图标选项（Symbol）' }) {
61. TabSegmentButtonV2({
62. items: this.symbolItems,
63. selectedIndex: this.symbolSelectedIndex!!,
64. })
65. }

67. VCard({ title: '图文混合选项' }) {
68. TabSegmentButtonV2({
69. items: this.hybridItems,
70. selectedIndex: this.hybridSelectedIndex!!,
71. })
72. }

74. VCard({ title: '自由选项' }) {
75. TabSegmentButtonV2({
76. items: this.freeItems,
77. selectedIndex: this.freeSelectedIndex!!,
78. })
79. }

81. Button(`isHybrid接口用法说明，${this.textItems[0].isHybrid}`) // 纯文本选项未配置图标，显示false。
82. .width('70%')

84. Button(`isHybrid接口用法说明，${this.hybridItems[0].isHybrid}`) // 图文混合选项已配置文本和图标，显示true。
85. .width('70%')

87. Button(`hasHybrid接口用法说明，${this.textItems.hasHybrid}`) // 分段按钮无图文混合选项，显示false。
88. .width('70%')

90. Button(`hasHybrid接口用法说明，${this.hybridItems.hasHybrid}`) // 分段按钮有图文混合选项，显示true。
91. .width('70%')
92. }
93. .constraintSize({ minHeight: '100%' })
94. .justifyContent(FlexAlign.Start)
95. .padding(16)
96. }
97. .backgroundColor('#f1f3f5')
98. .width('100%')
99. .height('100%')
100. }
101. }

103. @Builder
104. function Noop() {
105. }

107. @Component
108. export struct VCard {
109. @Prop
110. title: ResourceStr;
111. @BuilderParam
112. content: () => void = Noop;

114. build() {
115. Column({ space: 8 }) {
116. if (this.title) {
117. Text(this.title)
118. .maxLines(1)
119. .textOverflow({ overflow: TextOverflow.Ellipsis })
120. .constraintSize({ maxWidth: '80%' })
121. }
122. this.content()
123. }
124. .backgroundColor(Color.White)
125. .borderRadius(8)
126. .padding(8)
127. .width('100%')
128. }
129. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/_TV96YcKRemIOm8jrlGaCA/zh-cn_image_0000002592380528.gif?HW-CC-KV=V1&HW-CC-Date=20260611T075017Z&HW-CC-Expire=86400&HW-CC-Sign=1D62A4865A6928458CAFA994B52A55A8DD735C1110036171B528EF9500CDA072)

### 示例 2（单选的胶囊型分段按钮）

该示例介绍单选胶囊型分段按钮的基本用法。

```
1. import { CapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct CapsuleSegmentButtonV2Example {
6. @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items([
7. // 设置分段按钮选项文本。
8. { text: '手机' },
9. { text: '平板' },
10. { text: '2in1' },
11. { text: '智能穿戴' },
12. ]);
13. @Local textSelectedIndex: number = 0;
14. @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items([
15. // 设置分段按钮选项图标。
16. { icon: $r('sys.media.ohos_ic_public_device_phone') },
17. { icon: $r('sys.media.ohos_ic_public_device_pad') },
18. { icon: $r('sys.media.ohos_ic_public_device_matebook') },
19. { icon: $r('sys.media.ohos_ic_public_device_watch') },
20. ]);
21. @Local imageSelectedIndex: number = 0;
22. @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items([
23. // 分段按钮选项图标，Symbol类型。
24. { symbol: $r('sys.symbol.phone') },
25. { symbol: $r('sys.symbol.pad') },
26. { symbol: $r('sys.symbol.matebook') },
27. { symbol: $r('sys.symbol.watch') },
28. ]);
29. @Local symbolSelectedIndex: number = 0;
30. @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items([
31. { text: '手机', symbol: $r('sys.symbol.phone') },
32. { text: '平板', symbol: $r('sys.symbol.pad') },
33. { text: '2in1', symbol: $r('sys.symbol.matebook') },
34. { text: '智能穿戴', symbol: $r('sys.symbol.watch') },
35. ]);
36. @Local hybridSelectedIndex: number = 0;
37. @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items([
38. { text: '年' },
39. { text: '月' },
40. { text: '周' },
41. { text: '日' },
42. { icon: $r('sys.media.ohos_ic_public_search_filled') },
43. ]);
44. @Local freeSelectedIndex: number = 0;

46. build() {
47. Scroll() {
48. Column({ space: 12 }) {
49. VCard({ title: '纯文本选项' }) {
50. CapsuleSegmentButtonV2({
51. items: this.textItems,
52. selectedIndex: this.textSelectedIndex!!,
53. })
54. }

56. VCard({ title: '纯图标选项（Image）' }) {
57. CapsuleSegmentButtonV2({
58. items: this.imageItems,
59. selectedIndex: this.imageSelectedIndex!!,
60. })
61. }

63. VCard({ title: '纯图标选项（Symbol）' }) {
64. CapsuleSegmentButtonV2({
65. items: this.symbolItems,
66. selectedIndex: this.symbolSelectedIndex!!,
67. })
68. }

70. VCard({ title: '图文混合选项' }) {
71. CapsuleSegmentButtonV2({
72. items: this.hybridItems,
73. selectedIndex: this.hybridSelectedIndex!!,
74. })
75. }

77. VCard({ title: '自由选项' }) {
78. CapsuleSegmentButtonV2({
79. items: this.freeItems,
80. selectedIndex: this.freeSelectedIndex!!,
81. })
82. }
83. }
84. .constraintSize({ minHeight: '100%' })
85. .justifyContent(FlexAlign.Start)
86. .padding(16)
87. }
88. .backgroundColor('#f1f3f5')
89. .width('100%')
90. .height('100%')
91. }
92. }

94. @Builder
95. function Noop() {
96. }

98. @Component
99. export struct VCard {
100. @Prop
101. title: ResourceStr;
102. @BuilderParam
103. content: () => void = Noop;

105. build() {
106. Column({ space: 8 }) {
107. // 判断title是否存在，不存在不显示。
108. if (this.title) {
109. Text(this.title)
110. .maxLines(1)
111. .textOverflow({ overflow: TextOverflow.Ellipsis })
112. .constraintSize({ maxWidth: '80%' })
113. }
114. this.content()
115. }
116. .backgroundColor(Color.White)
117. .borderRadius(8)
118. .padding(8)
119. .width('100%')
120. }
121. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/TlV3qq4zTM2qpzRcWTkc9w/zh-cn_image_0000002622860039.gif?HW-CC-KV=V1&HW-CC-Date=20260611T075017Z&HW-CC-Expire=86400&HW-CC-Sign=DD616B84112032C9125612E0F5814273C068A040E55C798756A5BC4691BE135A)

### 示例 3（多选的胶囊型分段按钮）

该示例介绍多选胶囊型分段按钮的基本用法。

```
1. import { MultiCapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct MultiCapsuleSegmentButtonV2Example {
6. @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items([
7. // 设置分段按钮选项文本。
8. { text: '手机' },
9. { text: '平板' },
10. { text: '2in1' },
11. { text: '智能穿戴' },
12. ]);
13. @Local textSelectedIndexes: number[] = [0];
14. @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items([
15. // 设置分段按钮选项图标。
16. { icon: $r('sys.media.ohos_ic_public_device_phone') },
17. { icon: $r('sys.media.ohos_ic_public_device_pad') },
18. { icon: $r('sys.media.ohos_ic_public_device_matebook') },
19. { icon: $r('sys.media.ohos_ic_public_device_watch') },
20. ]);
21. @Local imageSelectedIndexes: number[] = [0];
22. @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items([
23. // 分段按钮选项图标，Symbol类型。
24. { symbol: $r('sys.symbol.phone') },
25. { symbol: $r('sys.symbol.pad') },
26. { symbol: $r('sys.symbol.matebook') },
27. { symbol: $r('sys.symbol.watch') },
28. ]);
29. @Local symbolSelectedIndexes: number[] = [0];
30. @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items([
31. { text: '手机', symbol: $r('sys.symbol.phone') },
32. { text: '平板', symbol: $r('sys.symbol.pad') },
33. { text: '2in1', symbol: $r('sys.symbol.matebook') },
34. { text: '智能穿戴', symbol: $r('sys.symbol.watch') },
35. ]);
36. @Local hybridSelectedIndexes: number[] = [0];
37. @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items([
38. { text: '年' },
39. { text: '月' },
40. { text: '周' },
41. { text: '日' },
42. { icon: $r('sys.media.ohos_ic_public_search_filled') },
43. ]);
44. @Local freeSelectedIndexes: number[] = [0];

46. build() {
47. Scroll() {
48. Column({ space: 12 }) {
49. VCard({ title: '纯文本选项' }) {
50. MultiCapsuleSegmentButtonV2({
51. items: this.textItems,
52. selectedIndexes: this.textSelectedIndexes!!,
53. })
54. }

56. VCard({ title: '纯图标选项（Image）' }) {
57. MultiCapsuleSegmentButtonV2({
58. items: this.imageItems,
59. selectedIndexes: this.imageSelectedIndexes!!,
60. })
61. }

63. VCard({ title: '纯图标选项（Symbol）' }) {
64. MultiCapsuleSegmentButtonV2({
65. items: this.symbolItems,
66. selectedIndexes: this.symbolSelectedIndexes!!,
67. })
68. }

70. VCard({ title: '图文混合选项' }) {
71. MultiCapsuleSegmentButtonV2({
72. items: this.hybridItems,
73. selectedIndexes: this.hybridSelectedIndexes!!,
74. })
75. }

77. VCard({ title: '自由选项' }) {
78. MultiCapsuleSegmentButtonV2({
79. items: this.freeItems,
80. selectedIndexes: this.freeSelectedIndexes!!,
81. })
82. }
83. }
84. .constraintSize({ minHeight: '100%' })
85. .justifyContent(FlexAlign.Start)
86. .padding(16)
87. }
88. .backgroundColor('#f1f3f5')
89. .width('100%')
90. .height('100%')
91. }
92. }

94. @Builder
95. function Noop() {
96. }

98. @Component
99. export struct VCard {
100. @Prop
101. title: ResourceStr;
102. @BuilderParam
103. content: () => void = Noop;

105. build() {
106. Column({ space: 8 }) {
107. // 判断title是否存在，不存在不显示。
108. if (this.title) {
109. Text(this.title)
110. .maxLines(1)
111. .textOverflow({ overflow: TextOverflow.Ellipsis })
112. .constraintSize({ maxWidth: '80%' })
113. }
114. this.content()
115. }
116. .backgroundColor(Color.White)
117. .borderRadius(8)
118. .padding(8)
119. .width('100%')
120. }
121. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1EAQm2_XQGyoN80DTvq-PQ/zh-cn_image_0000002622700157.gif?HW-CC-KV=V1&HW-CC-Date=20260611T075017Z&HW-CC-Expire=86400&HW-CC-Sign=3D1612AE790A8DB0C34246E00FEEBA5F998A49B28764703820B70F2EBD638320)

### 示例4（分段按钮Modifier的基本用法）

该示例介绍页签型分段按钮，单选的胶囊型分段按钮，多选的胶囊型分段按钮Modifier的基本用法。

```
1. import {
2. SegmentButtonV2Items,
3. TabSegmentButtonV2,
4. CapsuleSegmentButtonV2,
5. MultiCapsuleSegmentButtonV2,
6. TextModifier,
7. ImageModifier,
8. SymbolGlyphModifier
9. } from '@kit.ArkUI';

11. @Entry
12. @ComponentV2
13. struct SegmentButtonV2Example {
14. @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items([
15. { text: '手机', textModifier: new TextModifier().fontSize(20) }, // textModifier: 分段按钮选项文本属性样式修改器。
16. { text: '平板' },
17. // iconModifier: 修改分段按钮选项图片类型的图标属性样式。
18. { icon: $r('sys.media.ohos_ic_public_device_phone'), iconModifier: new ImageModifier().height(17).width(17) },
19. { icon: $r('sys.media.ohos_ic_public_device_pad') },
20. // symbolModifier: 分段按钮选项Symbol类型图标属性样式修改器。
21. { symbol: $r('sys.symbol.phone'), symbolModifier: new SymbolGlyphModifier().fontColor([Color.Pink]) },
22. { symbolModifier: new SymbolGlyphModifier($r('sys.symbol.pad')).fontColor([Color.Orange]) },
23. { symbol: $r('sys.symbol.matebook') },
24. ]);
25. @Local textSelectedIndex: number = 0;
26. @Local freeSelectedIndex: number[] = [0];

28. build() {
29. Column() {
30. VCard({ title: 'TabSegmentButtonV2' }) {
31. TabSegmentButtonV2({
32. items: this.textItems,
33. selectedIndex: this.textSelectedIndex!!,
34. })
35. }

37. VCard({ title: 'CapsuleSegmentButtonV2' }) {
38. CapsuleSegmentButtonV2({
39. items: this.textItems,
40. selectedIndex: this.textSelectedIndex!!,
41. })
42. }

44. VCard({ title: 'MultiCapsuleSegmentButtonV2' }) {
45. MultiCapsuleSegmentButtonV2({
46. items: this.textItems,
47. selectedIndexes: this.freeSelectedIndex!!,
48. })
49. }

51. }
52. .constraintSize({ minHeight: '100%' })
53. .justifyContent(FlexAlign.Start)
54. .padding(16)

56. }
57. }

59. @Builder
60. function Noop() {
61. }

63. @Component
64. export struct VCard {
65. @Prop
66. title: ResourceStr;
67. @BuilderParam
68. content: () => void = Noop;

70. build() {
71. Column({ space: 8 }) {
72. // 判断title是否存在，不存在不显示。
73. if (this.title) {
74. Text(this.title)
75. .maxLines(1)
76. .textOverflow({ overflow: TextOverflow.Ellipsis })
77. .constraintSize({ maxWidth: '80%' })
78. }
79. this.content()
80. }
81. .backgroundColor(Color.White)
82. .borderRadius(8)
83. .padding(8)
84. .width('100%')
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/RZAqSiSvSR6VDUbZc9HB5Q/zh-cn_image_0000002592220598.png?HW-CC-KV=V1&HW-CC-Date=20260611T075017Z&HW-CC-Expire=86400&HW-CC-Sign=067561E6202B0087A5F2C89487BB7C9DD75BE4E8A4672D9D07F3AFEAA1CC6ACC)

### 示例5（开启SegmentButtonV2的属性动画）

此示例展示了SegmentButtonV2开启enableStateAnimation后，在通过状态变量修改selectedIndexes的值时，按钮切换也具有动画效果。

从API version 24开始，[TabSegmentButtonV2](ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)和[CapsuleSegmentButtonV2](ohos-arkui-advanced-segmentbuttonv2.md#capsulesegmentbuttonv2)新增enableStateAnimation属性。

```
1. import { TabSegmentButtonV2, CapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct SegmentButtonV2Example {
6. @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items([
7. { text: '手机' },
8. { text: '平板' },
9. { text: '2in1' },
10. { text: '智能穿戴' },
11. ]);
12. @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items([
13. { icon: $r('sys.media.ohos_ic_public_device_phone') },
14. { icon: $r('sys.media.ohos_ic_public_device_pad') },
15. { icon: $r('sys.media.ohos_ic_public_device_matebook') },
16. { icon: $r('sys.media.ohos_ic_public_device_watch') },
17. ]);
18. @Local textSelectedIndex: number = 0;
19. @Local imageSelectedIndex: number = 0;
20. @Local currentSelectedIndex: number = 0; // 切换选中项的索引计数器

22. build() {
23. Scroll() {
24. Column({ space: 12 }) {
25. VCard({ title: 'TabSegmentButtonV2' }) {
26. TabSegmentButtonV2({
27. items: this.textItems,
28. selectedIndex: this.textSelectedIndex!!,
29. enableStateAnimation: true // 开启TabSegmentButtonV2的属性动画
30. })
31. }

33. VCard({ title: 'CapsuleSegmentButtonV2' }) {
34. CapsuleSegmentButtonV2({
35. items: this.imageItems,
36. selectedIndex: this.imageSelectedIndex!!,
37. enableStateAnimation: true // 开启CapsuleSegmentButtonV2的属性动画
38. })
39. }

41. Button('ChangeSelectedIndex').onClick((event: ClickEvent) => {
42. // 通过状态变量自增修改选中项的索引值，若超出最大索引则重置为0
43. this.currentSelectedIndex = this.currentSelectedIndex < 3 ? this.currentSelectedIndex + 1 : 0;
44. this.textSelectedIndex = this.currentSelectedIndex;
45. this.imageSelectedIndex = this.currentSelectedIndex;
46. })
47. }
48. .constraintSize({ minHeight: '100%' })
49. .justifyContent(FlexAlign.Start)
50. .padding(16)
51. }
52. .backgroundColor('#f1f3f5')
53. .width('100%')
54. .height('100%')
55. }
56. }

58. @Builder
59. function Noop() {
60. }

62. @Component
63. export struct VCard {
64. @Prop
65. title: ResourceStr;
66. @BuilderParam
67. content: () => void = Noop;

69. build() {
70. Column({ space: 8 }) {
71. if (this.title) {
72. Text(this.title)
73. .maxLines(1)
74. .textOverflow({ overflow: TextOverflow.Ellipsis })
75. .constraintSize({ maxWidth: '80%' })
76. }
77. this.content()
78. }
79. .backgroundColor(Color.White)
80. .borderRadius(8)
81. .padding(8)
82. .width('100%')
83. }
84. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/hsXoEMmJRyG3f3fvJYnmDQ/zh-cn_image_0000002592380530.gif?HW-CC-KV=V1&HW-CC-Date=20260611T075017Z&HW-CC-Expire=86400&HW-CC-Sign=E5BCF8893156FD528DB90512BFA029EEBA430E8B2BAECAEA1D6724E011E53519)
