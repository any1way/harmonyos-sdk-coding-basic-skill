---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location
title: 位置设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 位置设置
category: harmonyos-references
scraped_at: 2026-06-11T15:44:19+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:9ac3ab62148e15295debd4ffce2a124ded9796fb0cd48755668c64d76c8d5315
---
设置组件对齐方式、布局方向及显示位置。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## align

PhonePC/2in1TabletTVWearable

align(value: Alignment): T

设置当前组件绘制区域内的子组件的对齐方式，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Alignment](../../../公共定义/枚举说明/ts-appendix-enums.md#alignment) | 是 | 设置当前组件绘制区域内的子组件的对齐方式。  只在[Stack](../../../行列与堆叠/Stack/ts-container-stack.md)、[FolderStack](../../../系统预置UI组件库/FolderStack/ts-container-folderstack.md)、[Shape](../../../图形绘制/Shape/ts-drawing-components-shape.md)、[Button](../../../按钮与选择/Button/ts-basic-components-button.md)、[Marquee](../../../信息展示/Marquee/ts-basic-components-marquee.md)、[StepperItem](../../../已停止维护的组件与接口/StepperItem/ts-basic-components-stepperitem.md)、[Text](../../../文本与输入/Text/ts-basic-components-text.md)、[TextArea](../../../文本与输入/TextArea/ts-basic-components-textarea.md)、[TextInput](../../../文本与输入/TextInput/ts-basic-components-textinput.md)、[RichEditor](../../../文本与输入/RichEditor/ts-basic-components-richeditor.md)、[Hyperlink](../../../文本与输入/Hyperlink/ts-container-hyperlink.md)、[SymbolGlyph](../../../文本与输入/SymbolGlyph/ts-basic-components-symbolglyph.md)、[ListItem](../../../滚动与滑动/ListItem/ts-container-listitem.md)、[GridItem](../../../滚动与滑动/GridItem/ts-container-griditem.md)、[Scroll](../../../滚动与滑动/Scroll/ts-container-scroll.md)、[FlowItem](../../../滚动与滑动/FlowItem/ts-container-flowitem.md)、[ImageAnimator](../../../图片与视频/ImageAnimator/ts-basic-components-imageanimator.md)、[LoadingProgress](../../../信息展示/LoadingProgress/ts-basic-components-loadingprogress.md)、[PatternLock](../../../信息展示/PatternLock/ts-basic-components-patternlock.md)、[Progress](../../../信息展示/Progress/ts-basic-components-progress.md)、[QRCode](../../../信息展示/QRCode/ts-basic-components-qrcode.md)、[TextClock](../../../信息展示/TextClock/ts-basic-components-textclock.md)、[TextTimer](../../../信息展示/TextTimer/ts-basic-components-texttimer.md)、[MenuItem](../../../菜单/MenuItem/ts-basic-components-menuitem.md)、[Toggle](../../../按钮与选择/Toggle/ts-basic-components-toggle.md)、[Checkbox](../../../按钮与选择/Checkbox/ts-basic-components-checkbox.md)、[NodeContainer](../../../自定义占位组件/NodeContainer/ts-basic-components-nodecontainer.md)中生效，其中和文本相关的组件Marquee、Text、TextArea、TextInput、RichEditor、Hyperlink的align结果参考[textAlign](../../../文本与输入/Text/ts-basic-components-text.md#textalign)。  不支持textAlign属性的组件则无法设置水平方向的文字对齐。  默认值：Alignment.Center  **说明：**  该属性在[Stack](../../../行列与堆叠/Stack/ts-container-stack.md)组件上支持镜像能力，在其他组件上不支持镜像能力。  在Stack中该属性与alignContent效果一致，只能设置子组件在当前组件内的对齐方式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## align20+

PhonePC/2in1TabletTVWearable

align(alignment: Alignment | LocalizedAlignment): T

设置当前组件绘制区域内的子组件的对齐方式，增加支持镜像的能力，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | [Alignment](../../../公共定义/枚举说明/ts-appendix-enums.md#alignment) | [LocalizedAlignment](../../../公共定义/枚举说明/ts-appendix-enums.md#localizedalignment20) | 是 | 设置当前组件绘制区域内的子组件的对齐方式，增加支持镜像的能力。  LocalizedAlignment只在[Shape](../../../图形绘制/Shape/ts-drawing-components-shape.md)、[Button](../../../按钮与选择/Button/ts-basic-components-button.md)、[GridItem](../../../滚动与滑动/GridItem/ts-container-griditem.md)、[FlowItem](../../../滚动与滑动/FlowItem/ts-container-flowitem.md)、[ImageAnimator](../../../图片与视频/ImageAnimator/ts-basic-components-imageanimator.md)、[LoadingProgress](../../../信息展示/LoadingProgress/ts-basic-components-loadingprogress.md)、[PatternLock](../../../信息展示/PatternLock/ts-basic-components-patternlock.md)、[Progress](../../../信息展示/Progress/ts-basic-components-progress.md)、[QRCode](../../../信息展示/QRCode/ts-basic-components-qrcode.md)、[TextClock](../../../信息展示/TextClock/ts-basic-components-textclock.md)、[TextTimer](../../../信息展示/TextTimer/ts-basic-components-texttimer.md)、[StepperItem](../../../已停止维护的组件与接口/StepperItem/ts-basic-components-stepperitem.md)、[MenuItem](../../../菜单/MenuItem/ts-basic-components-menuitem.md)、[Toggle](../../../按钮与选择/Toggle/ts-basic-components-toggle.md)、[Checkbox](../../../按钮与选择/Checkbox/ts-basic-components-checkbox.md)、[ListItem](../../../滚动与滑动/ListItem/ts-container-listitem.md)中有效果。  其中，除[ListItem](../../../滚动与滑动/ListItem/ts-container-listitem.md)与Alignment的效果保持一致以外，其他组件镜像切换均生效；其他设置LocalizedAlignment无效果的组件按其默认效果显示。  默认值：Alignment.Center、LocalizedAlignment.CENTER  设置异常值按默认值处理，效果为居中显示。  **说明：**  Alignment类型不支持镜像能力；LocalizedAlignment类型支持镜像能力，选择LocalizedAlignment中的枚举值，根据direction或系统语言方向的改变实现镜像切换。其中direction的优先级高于系统语言方向，当设置direction且不为auto时，LocalizedAlignment的镜像按照direction进行布局；当设置direction为auto或未设置时，LocalizedAlignment的镜像按照系统语言方向进行布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## direction

PhonePC/2in1TabletTVWearable

direction(value: Direction): T

设置当前组件绘制区域内主轴方向上的布局，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Direction](../../../公共定义/枚举说明/ts-appendix-enums.md#direction) | 是 | 设置当前组件绘制区域内主轴方向上的布局。  属性配置为auto的时候，按照系统语言方向进行布局。  该属性在Column组件上不生效。  默认值：Direction.Auto  direction取undefined或null时按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## position

PhonePC/2in1TabletTVWearable

position(value: Position | Edges | LocalizedEdges): T

绝对定位，确定子组件相对父组件内容区的位置，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

说明

* position对位置的影响作用在组件的尺寸测量完成之后。
* 当父组件为[Row](../../../行列与堆叠/Row/ts-container-row.md)、[Column](../../../行列与堆叠/Column/ts-container-column.md)或[Flex](../../../行列与堆叠/Flex/ts-container-flex.md)时，设置position的子组件不占位。在上述场景中，如果父组件包含的所有子组件均设置了position，此时父组件尺寸无法通过其他子组件确定，将基于尺寸(0, 0)进行布局测算。
* Position类型基于父组件内容区左上角确定位置；Edges类型基于父组件内容区四边确定位置，top/left/right/bottom分别为组件各边距离父组件内容区相应边的边距，通过边距来确定组件相对于父组件内容区的位置；LocalizedEdges类型基于父组件内容区四边确定位置，支持镜像模式。
* 本属性适用于置顶显示、悬浮按钮等组件在父组件中位置固定的场景。
* 本属性不支持在宽高为零的布局组件上设置。
* 当父组件为[RelativeContainer](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)，且子组件设置了alignRules属性时，子组件的position属性不生效。
* 若本属性所在组件的父组件未设置固定宽高，那么本组件会参考第一个设置固定宽高的祖先组件进行绝对定位。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](../../../公共定义/基础类型定义/ts-types.md#position) | [Edges12+](../../../公共定义/基础类型定义/ts-types.md#edges12) | [LocalizedEdges12+](../../../公共定义/基础类型定义/ts-types.md#localizededges12) | 是 | 绝对定位，确定子组件相对父组件内容区的位置，父组件内容区的大小为父组件大小减去[border](../边框设置/ts-universal-attributes-border.md#border)、[padding](../尺寸设置/ts-universal-attributes-size.md#padding)、[safeAreaPadding](../尺寸设置/ts-universal-attributes-size.md#safeareapadding14)后提供给子组件可布局的内容区域大小。  设置异常值时该属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## markAnchor

PhonePC/2in1TabletTVWearable

markAnchor(value: Position | LocalizedPosition): T

设置元素在位置定位时的锚点，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](../../../公共定义/基础类型定义/ts-types.md#position) | [LocalizedPosition12+](../../../公共定义/基础类型定义/ts-types.md#localizedposition12) | 是 | 设置元素在位置定位时的锚点，基于position或offset的初始位置，进行进一步的偏移调整。  设置.position({x: value1, y: value2}).markAnchor({x: value3, y: value4})，效果等于设置.position({x: value1 - value3, y: value2 - value4})，offset同理。  单独设置.markAnchor({x: value1, y: value2})，效果等于设置.offset({x: -value1, y: -value2})。  API version 9及以前，默认值为：{x: 0, y: 0}  API version 10：无默认值。  设置异常值时该属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## offset

PhonePC/2in1TabletTVWearable

offset(value: Position | Edges | LocalizedEdges): T

相对偏移，组件相对原本的布局位置进行偏移。和position一起使用时，position生效，offset不生效，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](../../../公共定义/基础类型定义/ts-types.md#position) | [Edges12+](../../../公共定义/基础类型定义/ts-types.md#edges12) | [LocalizedEdges12+](../../../公共定义/基础类型定义/ts-types.md#localizededges12) | 是 | 相对偏移，组件基于原本的布局位置进行偏移。offset属性不影响父组件布局，仅在绘制时调整位置。  Position类型基于组件自身左上角偏移，Edges类型基于组件自身四边偏移。 offset属性设置{x: x, y: y}与设置{left: x, top: y}以及{right: -x, bottom: -y}效果相同，类型LocalizedEdges支持镜像模式：LTR模式下start等同于x，RTL模式下start等同于-x。  API version 9及以前，默认值为：{x: 0, y: 0}  默认单位：vp  API version 10：无默认值。  设置异常值时该属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## alignRules9+

PhonePC/2in1TabletTVWearable

alignRules(value: AlignRuleOption): T

指定设置在相对布局组件中子组件的对齐规则，仅当父组件为[RelativeContainer](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)时生效，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AlignRuleOption](ts-universal-attributes-location.md#alignruleoption9对象说明) | 是 | 指定设置在相对布局组件中子组件的对齐规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## alignRules12+

PhonePC/2in1TabletTVWearable

alignRules(alignRule: LocalizedAlignRuleOptions): T

指定设置在相对布局组件中子组件的对齐规则，仅当父组件为[RelativeContainer](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)时生效。该方法水平方向上以start和end分别替代原方法的left和right，以便在RTL模式下能镜像显示，建议使用该方法指定设置在相对布局组件中子组件的对齐规则，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignRule | [LocalizedAlignRuleOptions](ts-universal-attributes-location.md#localizedalignruleoptions12对象说明) | 是 | 指定设置在相对布局组件中子组件的对齐规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## layoutGravity20+

PhonePC/2in1TabletTVWearable

layoutGravity(alignment: LocalizedAlignment): T

单独设置Stack组件中子组件的对齐规则，仅当父组件为Stack时生效。与align属性同时使用时，layoutGravity优先级更高，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | [LocalizedAlignment](../../../公共定义/枚举说明/ts-appendix-enums.md#localizedalignment20) | 是 | 指定设置在Stack组件中子组件的对齐规则。  默认值：LocalizedAlignment.CENTER 。说明：当传入异常值时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AlignRuleOption9+对象说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | [HorizontalAlignParam](ts-universal-attributes-location.md#horizontalalignparam23对象说明) | 否 | 是 | 设置左对齐参数。  API version 23之前，入参类型为{ anchor: string, align: [HorizontalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#horizontalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| right | [HorizontalAlignParam](ts-universal-attributes-location.md#horizontalalignparam23对象说明) | 否 | 是 | 设置右对齐参数。  API version 23之前，入参类型为{ anchor: string, align: [HorizontalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#horizontalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| middle | [HorizontalAlignParam](ts-universal-attributes-location.md#horizontalalignparam23对象说明) | 否 | 是 | 设置横向居中对齐方式的参数。  API version 23之前，入参类型为{ anchor: string, align: [HorizontalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#horizontalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| top | [VerticalAlignParam](ts-universal-attributes-location.md#verticalalignparam23对象说明) | 否 | 是 | 设置顶部对齐的参数。  API version 23之前，入参类型为{ anchor: string, align: [VerticalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#verticalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| bottom | [VerticalAlignParam](ts-universal-attributes-location.md#verticalalignparam23对象说明) | 否 | 是 | 设置底部对齐的参数。  API version 23之前，入参类型为{ anchor: string, align: [VerticalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#verticalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| center | [VerticalAlignParam](ts-universal-attributes-location.md#verticalalignparam23对象说明) | 否 | 是 | 设置纵向居中对齐方式的参数。  API version 23之前，入参类型为{ anchor: string, align: [VerticalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#verticalalign) }。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| bias11+ | [Bias](../../../公共定义/基础类型定义/ts-types.md#bias对象说明) | 否 | 是 | 设置组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## HorizontalAlignParam23+对象说明

PhonePC/2in1TabletTVWearable

定义在相对布局组件中子组件在水平方向上的对齐规则。

说明

为规范匿名对象的定义，从API version 23开始，修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| anchor9+ | string | 否 | 否 | 设置作为锚点的组件的id值。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| align9+ | [HorizontalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#horizontalalign) | 否 | 否 | 设置相对于锚点组件的横向对齐方式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## VerticalAlignParam23+对象说明

PhonePC/2in1TabletTVWearable

定义在相对布局组件中子组件在垂直方向上的对齐规则。

说明

为规范匿名对象的定义，从API version 23开始，修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| anchor9+ | string | 否 | 否 | 设置作为锚点的组件的id值。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| align9+ | [VerticalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#verticalalign) | 否 | 否 | 设置相对于锚点组件的纵向对齐方式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## LocalizedAlignRuleOptions12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [LocalizedHorizontalAlignParam](ts-universal-attributes-location.md#localizedhorizontalalignparam12对象说明) | 否 | 是 | 设置横向对齐方式的参数，LTR模式时为左对齐，RTL模式时为右对齐。 |
| end | [LocalizedHorizontalAlignParam](ts-universal-attributes-location.md#localizedhorizontalalignparam12对象说明) | 否 | 是 | 设置横向对齐方式的参数，LTR模式时为右对齐，RTL模式时为左对齐。 |
| middle | [LocalizedHorizontalAlignParam](ts-universal-attributes-location.md#localizedhorizontalalignparam12对象说明) | 否 | 是 | 设置横向居中对齐方式的参数。 |
| top | [LocalizedVerticalAlignParam](ts-universal-attributes-location.md#localizedverticalalignparam12对象说明) | 否 | 是 | 设置纵向顶部对齐的参数。 |
| bottom | [LocalizedVerticalAlignParam](ts-universal-attributes-location.md#localizedverticalalignparam12对象说明) | 否 | 是 | 设置纵向底部对齐的参数。 |
| center | [LocalizedVerticalAlignParam](ts-universal-attributes-location.md#localizedverticalalignparam12对象说明) | 否 | 是 | 设置纵向居中对齐方式的参数。 |
| bias | [Bias](../../../公共定义/基础类型定义/ts-types.md#bias对象说明) | 否 | 是 | 设置组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。 |

## LocalizedHorizontalAlignParam12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| anchor | string | 否 | 否 | 设置作为锚点的组件的id值。 |
| align | [HorizontalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#horizontalalign) | 否 | 否 | 设置相对于锚点组件的横向对齐方式。 |

## LocalizedVerticalAlignParam12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| anchor | string | 否 | 否 | 设置作为锚点的组件的id值。 |
| align | [VerticalAlign](../../../公共定义/枚举说明/ts-appendix-enums.md#verticalalign) | 否 | 否 | 设置相对于锚点组件的纵向对齐方式。 |

## chainMode12+

PhonePC/2in1TabletTVWearable

chainMode(direction: Axis, style: ChainStyle): T

指定以该组件为链头所构成的链的参数，仅当父组件为[RelativeContainer](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)时生效。链头指满足成链规则时链的第一个组件（水平方向从左边起始，镜像语言下从右边起始；竖直方向从上边起始）。

详细用法请参考[RelativeContainer示例7（设置链）](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md#示例7设置链)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [Axis](../../../公共定义/枚举说明/ts-appendix-enums.md#axis) | 是 | 链的方向。 |
| style | [ChainStyle](ts-universal-attributes-location.md#chainstyle12) | 是 | 链的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ChainStyle12+

PhonePC/2in1TabletTVWearable

定义链的风格，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPREAD | 0 | 组件在约束锚点间均匀分布。详细用法请参考[RelativeContainer示例7（设置链）](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md#示例7设置链)。 |
| SPREAD\_INSIDE | 1 | 除首尾2个子组件的其他组件在约束锚点间均匀分布。详细用法请参考[RelativeContainer示例7（设置链）](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md#示例7设置链)。 |
| PACKED | 2 | 链内子组件无间隙。详细用法请参考[RelativeContainer示例7（设置链）](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md#示例7设置链)。 |

说明

使用链时，RelativeContainer会为链中的相互依赖的组件定义一个大小计算顺序，大小计算完成后再确定使用ChainStyle的位置。因此使用SPREAD或PACKED风格时，只以链头组件为锚点进行布局的非链组件A和链中其他节点有相同布局优先级，当组件A的id的字典排序靠前时，此时组件A的alignRules先于链的ChainStyle生效。

## chainWeight14+

PhonePC/2in1TabletTVWearable

chainWeight(chainWeight: ChainWeightOptions): T

对形成链的组件进行重新布局。仅当父组件为[RelativeContainer](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md)时生效。

说明

从API version 23开始，支持[attributeModifier](../../动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chainWeight | [ChainWeightOptions](../../../公共定义/基础类型定义/ts-types.md#chainweightoptions14对象说明) | 是 | 设置了chainWeight属性的组件与同一条链上的兄弟组件在水平或竖直方向的尺寸会按照设置的权重进行分配，分配时会忽略组件本身尺寸设置，按分配的权重自适应占满剩余空间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**示例：**

具体示例请参考[示例10（设置链中节点权重）](../../../行列与堆叠/RelativeContainer/ts-container-relativecontainer.md#示例10设置链中节点权重)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（对齐方式和主轴方向上的布局）

设置内容在元素内的对齐方式和子元素在父组件主轴方向上的布局。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PositionExample1 {
5. build() {
6. Column() {
7. Column({ space: 10 }) {
8. // 元素内容<元素宽高，设置内容在与元素内的对齐方式
9. Text('align').fontSize(9).fontColor(0xCCCCCC).width('90%')
10. Stack() {
11. Text('First show in bottom end').height('65%').backgroundColor(0xD2B48C)
12. Text('Second show in bottom end').backgroundColor(0xF5DEB3).opacity(0.9)
13. }.width('90%').height(50).margin({ top: 5 }).backgroundColor(0xFFE4C4)
14. .align(Alignment.BottomEnd)
15. Stack() {
16. Text('top start')
17. }.width('90%').height(50).margin({ top: 5 }).backgroundColor(0xFFE4C4)
18. .align(Alignment.TopStart)

20. // 父组件设置direction为Direction.Ltr，子元素从左到右排列
21. Text('direction').fontSize(9).fontColor(0xCCCCCC).width('90%')
22. Row() {
23. Text('1').height(50).width('25%').fontSize(16).backgroundColor(0xF5DEB3)
24. Text('2').height(50).width('25%').fontSize(16).backgroundColor(0xD2B48C)
25. Text('3').height(50).width('25%').fontSize(16).backgroundColor(0xF5DEB3)
26. Text('4').height(50).width('25%').fontSize(16).backgroundColor(0xD2B48C)
27. }
28. .width('90%')
29. .direction(Direction.Ltr)
30. // 父组件设置direction为Direction.Rtl，子元素从右到左排列
31. Row() {
32. Text('1').height(50).width('25%').fontSize(16).backgroundColor(0xF5DEB3).textAlign(TextAlign.End)
33. Text('2').height(50).width('25%').fontSize(16).backgroundColor(0xD2B48C).textAlign(TextAlign.End)
34. Text('3').height(50).width('25%').fontSize(16).backgroundColor(0xF5DEB3).textAlign(TextAlign.End)
35. Text('4').height(50).width('25%').fontSize(16).backgroundColor(0xD2B48C).textAlign(TextAlign.End)
36. }
37. .width('90%')
38. .direction(Direction.Rtl)
39. }
40. }
41. .width('100%').margin({ top: 5 })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/qXNM71djQs2VVJ9Sgt7NHw/zh-cn_image_0000002622859397.png?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=26AE9140ABBB0F0BD2E1F8F517EB7301A6F64772E04250C00F5A3643631D4367)

### 示例2（位置偏移）

基于父组件、相对定位、锚点作出位置偏移。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PositionExample2 {
5. build() {
6. Column({ space: 20 }) {
7. // 设置子组件左上角相对于父组件左上角的偏移位置
8. Text('position').fontSize(12).fontColor(0xCCCCCC).width('90%')
9. Row() {
10. Text('1').size({ width: '30%', height: '50' }).backgroundColor(0xdeb887).border({ width: 1 }).fontSize(16)
11. .textAlign(TextAlign.Center)
12. Text('2 position(30, 10)')
13. .size({ width: '60%', height: '30' })
14. .backgroundColor(0xbbb2cb)
15. .border({ width: 1 })
16. .fontSize(16)
17. .align(Alignment.Start)
18. .position({ x: 30, y: 10 })
19. Text('3').size({ width: '45%', height: '50' }).backgroundColor(0xdeb887).border({ width: 1 }).fontSize(16)
20. .textAlign(TextAlign.Center)
21. Text('4 position(50%, 70%)')
22. .size({ width: '50%', height: '50' })
23. .backgroundColor(0xbbb2cb)
24. .border({ width: 1 })
25. .fontSize(16)
26. .position({ x: '50%', y: '70%' })
27. }.width('90%').height(100).border({ width: 1, style: BorderStyle.Dashed })

29. // 相对于起点偏移，其中x为最终定位点距离起点水平方向间距，x>0往左，反之向右。
30. // y为最终定位点距离起点垂直方向间距，y>0向上，反之向下
31. Text('markAnchor').fontSize(12).fontColor(0xCCCCCC).width('90%')
32. Stack({ alignContent: Alignment.TopStart }) {
33. Row()
34. .size({ width: '100', height: '100' })
35. .backgroundColor(0xdeb887)
36. Text('text')
37. .fontSize('30px')
38. .textAlign(TextAlign.Center)
39. .size({ width: 25, height: 25 })
40. .backgroundColor(Color.Green)
41. .markAnchor({ x: 25, y: 25 })
42. Text('text')
43. .fontSize('30px')
44. .textAlign(TextAlign.Center)
45. .size({ width: 25, height: 25 })
46. .backgroundColor(Color.Green)
47. .markAnchor({ x: -100, y: -25 })
48. Text('text')
49. .fontSize('30px')
50. .textAlign(TextAlign.Center)
51. .size({ width: 25, height: 25 })
52. .backgroundColor(Color.Green)
53. .markAnchor({ x: 25, y: -25 })
54. }.margin({ top: 25 }).border({ width: 1, style: BorderStyle.Dashed })

56. // 相对定位，x>0向右偏移，反之向左，y>0向下偏移，反之向上
57. Text('offset').fontSize(12).fontColor(0xCCCCCC).width('90%')
58. Row() {
59. Text('1').size({ width: '15%', height: '50' }).backgroundColor(0xdeb887).border({ width: 1 }).fontSize(16)
60. .textAlign(TextAlign.Center)
61. Text('2  offset(15, 30)')
62. .size({ width: 120, height: '50' })
63. .backgroundColor(0xbbb2cb)
64. .border({ width: 1 })
65. .fontSize(16)
66. .align(Alignment.Start)
67. .offset({ x: 15, y: 30 })
68. Text('3').size({ width: '15%', height: '50' }).backgroundColor(0xdeb887).border({ width: 1 }).fontSize(16)
69. .textAlign(TextAlign.Center)
70. Text('4 offset(-5%, 20%)')
71. .size({ width: 100, height: '50' })
72. .backgroundColor(0xbbb2cb)
73. .border({ width: 1 })
74. .fontSize(16)
75. .offset({ x: '-5%', y: '20%' })
76. }.width('90%').height(100).border({ width: 1, style: BorderStyle.Dashed })
77. }
78. .width('100%').margin({ top: 25 })
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/uR-0Uz82TDys8YfxSgWLvw/zh-cn_image_0000002622699517.png?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=2834704A19C1AD85321135756C338E6D96E82F1F3DAEC430F0E753F99EB3477A)

### 示例3（绝对定位和相对偏移）

使用position设置绝对定位，确定子组件相对父组件的位置。使用offset设置相对偏移，组件相对原本的布局位置进行偏移。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example3 {
5. build() {
6. Column({ space: 20 }) {
7. Text('position use Edges').fontSize(12).fontColor(0xCCCCCC).width('90%')
8. Row() {
9. Text('bottom:0, right:0')
10. .size({ width: '30%', height: '50' })
11. .backgroundColor(0xdeb887)
12. .border({ width: 1 })
13. .fontSize(16)
14. .textAlign(TextAlign.Center)
15. .position({ bottom: 0, right: 0 })
16. Text('top:0, left:0')
17. .size({ width: '30%', height: '50' })
18. .backgroundColor(0xdeb887)
19. .border({ width: 1 })
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .position({ top: 0, left: 0 })
23. Text('top:10%, left:50%')
24. .size({ width: '50%', height: '30' })
25. .backgroundColor(0xbbb2cb)
26. .border({ width: 1 })
27. .fontSize(16)
28. .textAlign(TextAlign.Center)
29. .position({ top: '10%', left: '50%' })
30. Text('bottom:0, left:30')
31. .size({ width: '50%', height: '30' })
32. .backgroundColor(0xbbb2cb)
33. .border({ width: 1 })
34. .fontSize(16)
35. .textAlign(TextAlign.Center)
36. .position({ bottom: 0, left: 30 })
37. }.width('90%').height(100).border({ width: 1, style: BorderStyle.Dashed })

40. Text('offset use Edges').fontSize(12).fontColor(0xCCCCCC).width('90%')
41. Row() {
42. Text('1')
43. .size({ width: '25%', height: 50 })
44. .backgroundColor(0xdeb887)
45. .border({ width: 1 })
46. .fontSize(16)
47. .textAlign(TextAlign.Center)
48. Text('2 top:30, left:0')
49. .size({ width: '25%', height: 50 })
50. .backgroundColor(0xbbb2cb)
51. .border({ width: 1 })
52. .fontSize(16)
53. .textAlign(TextAlign.Center)
54. .offset({ top: 30, left: 0 })
55. Text('3')
56. .size({ width: '25%', height: 50 })
57. .backgroundColor(0xdeb887)
58. .border({ width: 1 })
59. .fontSize(16)
60. .textAlign(TextAlign.Center)
61. Text('4 bottom:10, right:30')
62. .size({ width: '25%', height: 50 })
63. .backgroundColor(0xbbb2cb)
64. .border({ width: 1 })
65. .fontSize(12)
66. .textAlign(TextAlign.Center)
67. .offset({ bottom: 10, right: 30 })
68. }.width('90%').height(150).border({ width: 1, style: BorderStyle.Dashed })
69. }.width('100%').margin({ top: 25 })
70. }
71. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/dH0VzeqLTE60G2pwFGJULA/zh-cn_image_0000002592219956.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=D6C5FDB0484697788D4FC722D17ADCA978D41231DCD9F210751504AFD4ED3B8B)

### 示例4（镜像效果）

通用布局属性支持[使用镜像能力](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI国际化/arkts-internationalization.md#使用镜像能力>)。下述示例从上到下依次通过[position](ts-universal-attributes-location.md#position)、[offset](ts-universal-attributes-location.md#offset)和[markAnchor](ts-universal-attributes-location.md#markanchor)实现镜像效果，为对比镜像前后的差异，浅蓝色对应镜像前效果，深蓝色对应镜像后效果。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Example4 {
7. private scroller: Scroller = new Scroller()

9. build() {
10. Column() {
11. Stack({ alignContent: Alignment.End }) {
12. Scroll(this.scroller) {
13. Flex({ direction: FlexDirection.Column }) {
14. RelativeContainer() {
15. Row() {
16. }
17. .position({ start: LengthMetrics.px(200), top: LengthMetrics.px(100) }) // position接口中的参数使用LocalizedEdges类型，支持镜像翻转效果
18. .width("30%")
19. .height("20%")
20. .backgroundColor('rgb(0, 74, 175)')
21. .padding(50)
22. .margin(50)

24. Row() {
25. }
26. .position({ left: '200px', top: '100px' }) // position接口中的参数使用Edges类型，不支持镜像翻转效果
27. .width("30%")
28. .height("20%")
29. .backgroundColor('rgb(39, 135, 217)')
30. .padding(50)
31. .margin(50)

33. Row() {
34. }
35. .offset({ start: LengthMetrics.vp(100), top: LengthMetrics.vp(200) }) // offset接口中的参数使用LocalizedEdges类型，支持镜像翻转效果
36. .width("30%")
37. .height("20%")
38. .backgroundColor('rgb(0, 74, 175)')
39. .padding(50)
40. .margin(50)

42. Row() {
43. }
44. .offset({ left: 100, top: 200 }) // offset接口中的参数使用Edges类型，不支持镜像翻转效果
45. .width("30%")
46. .height("20%")
47. .backgroundColor('rgb(39, 135, 217)')
48. .padding(50)
49. .margin(50)

51. Row() {
52. }
53. .markAnchor({
54. start: LengthMetrics.fp(100),
55. top: LengthMetrics.fp(-350)
56. }) // markAnchor接口中的参数使用LocalizedPosition类型，支持镜像翻转效果
57. .width("30%")
58. .height("20%")
59. .backgroundColor('rgb(0, 74, 175)')
60. .padding(50)
61. .margin(50)

63. Row() {
64. }
65. .markAnchor({ x: '100fp', y: '-350fp' }) // markAnchor接口中的参数使用Position类型，不支持镜像翻转效果
66. .width("30%")
67. .height("20%")
68. .backgroundColor('rgb(39, 135, 217)')
69. .padding(50)
70. .margin(50)
71. }
72. .backgroundColor(Color.White)
73. .padding(50)
74. .margin(50)
75. }
76. }
77. .width('100%')
78. .scrollBar(BarState.Off)
79. .scrollable(ScrollDirection.Vertical)

81. ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
82. Text()
83. .width(20)
84. .height(100)
85. .borderRadius(10)
86. .backgroundColor('#C0C0C0')
87. }.width(20).backgroundColor('#ededed')
88. }
89. }.height('90%')
90. }
91. }
```

镜像前效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/TXj85JCRR8uUKbB2QIqbhA/zh-cn_image_0000002592379890.png?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=250A4B41A80597484F3059BE23104D11F9D1D84AE5AB804912F47BD52F68A5CF)

镜像后效果如下，镜像生效条件请参考[使用镜像能力](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI国际化/arkts-internationalization.md#使用镜像能力>)：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/x3cGIPHcR2yyVmV46Kex7A/zh-cn_image_0000002622859399.png?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=FCBC6F26862825DDD36AD63A68F0D37CE2F356E82E220DBACEAC45E2004CBE40)

### 示例5（align属性适配镜像特性）

设置内容在元素内的对齐方式和子元素在父组件主轴方向上的布局。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct buttonTestDemo {
5. @State isLocalizedAlignment: LocalizedAlignment[] =
6. [LocalizedAlignment.TOP_START, LocalizedAlignment.TOP, LocalizedAlignment.TOP_END, LocalizedAlignment.START,
7. LocalizedAlignment.CENTER, LocalizedAlignment.END, LocalizedAlignment.BOTTOM_START, LocalizedAlignment.BOTTOM,
8. LocalizedAlignment.BOTTOM_END]
9. @State isLocalizedAlignmentIndex: number = 4
10. @State isDirection: Direction[] = [Direction.Ltr, Direction.Rtl, Direction.Auto]
11. @State isDirectionIndex: number = 0

13. build() {
14. Row() {
15. Column() {

17. Row({ space: 5 }) {
18. Button('START')
19. .onClick(() => {
20. this.isLocalizedAlignmentIndex = 3
21. })
22. Button('CENTER')
23. .onClick(() => {
24. this.isLocalizedAlignmentIndex = 4
25. })
26. Button('END')
27. .onClick(() => {
28. this.isLocalizedAlignmentIndex = 5
29. })
30. }.margin(20)

32. Row({ space: 5 }) {
33. Button('Ltr')
34. .onClick(() => {
35. this.isDirectionIndex = 0
36. })
37. Button('Rtl')
38. .onClick(() => {
39. this.isDirectionIndex = 1
40. })
41. Button('Auto')
42. .onClick(() => {
43. this.isDirectionIndex = 2
44. })
45. }.margin(20)

47. Row() {
48. Button('OK', { type: ButtonType.Capsule, stateEffect: true })
49. .backgroundColor(0x317aff)
50. .width(200)
51. .height(100)
52. .direction(this.isDirection[this.isDirectionIndex])
53. .align(this.isLocalizedAlignment[this.isLocalizedAlignmentIndex])
54. }.margin(20)
55. }
56. .width('100%')
57. }
58. .height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/LUblML5MTfazjADFIrkVxw/zh-cn_image_0000002622699519.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=6257098F6244A5761BBDA17E16C0B4EBA88D33B54951F8F92CD2833C90C37F53)

### 示例6（layoutGravity属性单独设置Stack组件中子组件的对齐规则）

更改Stack中Text的位置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index5 {
5. private layoutGravityArr: LocalizedAlignment[] = [
6. LocalizedAlignment.TOP_START, LocalizedAlignment.TOP, LocalizedAlignment.TOP_END,
7. LocalizedAlignment.START, LocalizedAlignment.CENTER, LocalizedAlignment.END,
8. LocalizedAlignment.BOTTOM_START, LocalizedAlignment.BOTTOM, LocalizedAlignment.BOTTOM_END];
9. @State layoutGravityIndex: number = 0;
10. private directionArr: Direction[] = [Direction.Ltr, Direction.Rtl, Direction.Auto];
11. @State directionIndex: number = 0;

13. build() {
14. Row() {
15. Column() {
16. Stack({
17. alignContent: Alignment.TopStart
18. }) {
19. Text('StackChildAlign_TopStart').fontSize(15)
20. Text('Child Text')
21. .width(150)
22. .height(150)
23. .backgroundColor(Color.Yellow)
24. .fontSize(15)
25. .layoutGravity(this.layoutGravityArr[this.layoutGravityIndex])
26. }
27. .width('100%')
28. .height(400)
29. .backgroundColor(Color.Grey)
30. .margin({ top: 10, bottom: 10 })
31. .direction(this.directionArr[this.directionIndex])

33. Button("LayoutGravity: " + this.layoutGravityArr[this.layoutGravityIndex])
34. .width(300)
35. .fontSize(16)
36. .onClick(() => {
37. this.layoutGravityIndex = ++this.layoutGravityIndex % this.layoutGravityArr.length;
38. })
39. .margin({ bottom: 10 })

41. Button("Direction: " + this.directionArr[this.directionIndex])
42. .width(150)
43. .fontSize(16)
44. .onClick(() => {
45. this.directionIndex = ++this.directionIndex % this.directionArr.length;
46. })
47. .margin({ bottom: 10 })
48. }
49. .width('100%')
50. }
51. .height('100%')
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/0EGDfCc1TyOLZNmUJZUmLQ/zh-cn_image_0000002592219958.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074417Z&HW-CC-Expire=86400&HW-CC-Sign=0F3578C3710D7194D8F180D954AAFACF5934C10C49430786412944EAE70F04F1)
