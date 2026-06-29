---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea
title: TextArea
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > TextArea
category: harmonyos-references
scraped_at: 2026-06-11T15:47:17+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:d3ec644f5a478d37db7c858d1bdda657e416e76e8e8b9411721ae4811e05cf5f
---
多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。

高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

TextArea(value?: TextAreaOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAreaOptions](ts-basic-components-textarea.md#textareaoptions对象说明) | 否 | TextArea组件参数。 |

## TextAreaOptions对象说明

PhonePC/2in1TabletTVWearable

TextArea初始化参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placeholder | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 设置无输入时的提示文本。输入内容后，提示文本不显示。  仅设置placeholder属性时，手柄依然跟随拖动，手柄松开后光标停留在文字开头位置。 |
| text | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | 是 | 设置输入框当前的文本内容。  建议通过onChange事件将状态变量与文本实时绑定，  避免组件刷新时TextArea中的文本内容异常。  从API version 10开始，该参数支持[$$](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/语法糖/$$语法：系统组件双向同步/arkts-two-way-sync.md>)双向绑定变量。  从API version 18开始，该参数支持[!!](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/语法糖/!!语法：双向绑定/arkts-new-binding.md#系统组件参数双向绑定>)双向绑定变量。 |
| controller8+ | [TextAreaController](ts-basic-components-textarea.md#textareacontroller8) | 否 | 是 | 设置TextArea控制器。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](../../通用属性/ts-component-general-attributes.md)，还支持以下属性：

说明

[通用属性padding](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#padding)的默认值为：

{

top: '8vp',

right: '16vp',

bottom: '8vp',

left: '16vp'

}

从API version 11开始，多行输入框可设置.width('auto')使组件宽度自适应文本宽度，自适应时组件宽度受constraintSize属性以及父容器传递的最大最小宽度限制，其余使用方式参考[尺寸设置](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md)。

### placeholderColor

PhonePC/2in1TabletTVWearable

placeholderColor(value: ResourceColor)

设置placeholder文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 是 | placeholder文本颜色。  默认值：跟随主题。 |

### placeholderFont

PhonePC/2in1TabletTVWearable

placeholderFont(value: Font)

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。

说明

可以使用[loadFontSync](<../../../../ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.text (文本模块)/js-apis-graphics-text.md#loadfontsync>)注册自定义字体。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](../../公共定义/基础类型定义/ts-types.md#font) | 是 | placeholder文本样式。 |

### textAlign

PhonePC/2in1TabletTVWearable

textAlign(value: TextAlign)

设置文本在输入框中的水平对齐方式。

支持TextAlign.Start、TextAlign.Center和TextAlign.End。从API version 11开始，新增TextAlign.JUSTIFY选项。

可通过[align](../../通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#align)属性控制文本段落在垂直方向上的位置，此组件中不可通过align属性控制文本段落在水平方向上的位置。

* Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对齐。
* Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。
* Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。

当textAlign属性设置为TextAlign.JUSTIFY时，最后一行文本不参与两端对齐，为水平对齐首部效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAlign](../../公共定义/枚举说明/ts-appendix-enums.md#textalign) | 是 | 文本在输入框中的水平对齐方式。  默认值：TextAlign.Start |

说明

textAlign只能调整文本整体的布局，不影响字符的显示顺序。若需要调整字符的显示顺序，请参考[镜像状态字符对齐](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI国际化/arkts-internationalization.md#镜像状态字符对齐>)。

### textDirection23+

PhonePC/2in1TabletTVWearable

textDirection(direction: TextDirection | undefined)

指定文本排版方向，未通过该接口设置时，默认文本排版方向遵循组件布局方向。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [TextDirection](../文本组件公共接口/ts-text-common.md#textdirection22) | undefined | 是 | 文本排版方向。  设置为undefined时，按照TextDirection.DEFAULT处理，表现为文本排版方向遵循组件布局方向。 |

### horizontalScrolling24+

PhonePC/2in1TabletTVWearable

horizontalScrolling(enabled: Optional<boolean>)

设置当文本宽度超过内容区宽度时是否启用水平滚动。未通过该接口设置时，禁用水平滚动。

说明

以下场景不支持水平滚动：设置[内联模式](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/使用文本/文本输入 (TextInputTextAreaSearch)/arkts-common-components-text-input.md#内联模式>)。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否启用水平滚动。  true表示启用水平滚动；false表示禁用水平滚动，文本将自动换行。 |

### caretColor

PhonePC/2in1TabletTVWearable

caretColor(value: ResourceColor)

设置输入框光标颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 是 | 输入框光标颜色。  默认值：'#007DFF' |

说明

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 是 | 字体颜色。 |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: Length)

设置字体大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../公共定义/基础类型定义/ts-types.md#length) | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp，Wearable设备上默认值为：18fp。不支持设置百分比字符串。 |

### fontStyle

PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle)

设置字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](../../公共定义/枚举说明/ts-appendix-enums.md#fontstyle) | 是 | 字体样式。  默认值：FontStyle.Normal |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | ResourceStr)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal  从API version 20开始，支持Resource类型。 |

### fontFamily

PhonePC/2in1TabletTVWearable

fontFamily(value: ResourceStr)

设置字体列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 是 | 字体列表。默认字体'HarmonyOS Sans'。  使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |

说明

可以使用[loadFontSync](<../../../../ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.text (文本模块)/js-apis-graphics-text.md#loadfontsync>)注册自定义字体。

### inputFilter8+

PhonePC/2in1TabletTVWearable

inputFilter(value: ResourceStr, error?: (value: string) => void)

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。

单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

从API version 11开始，设置inputFilter且输入的字符不为空字符，会导致[type](ts-basic-components-textarea.md#type11)接口附带的文本过滤效果失效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 是 | 正则表达式。 |
| error | (value: string) => void | 否 | 正则匹配失败时，返回被过滤的内容。正则匹配成功时，无返回。 |

### copyOption9+

PhonePC/2in1TabletTVWearable

copyOption(value: CopyOptions)

设置输入的文本是否可复制。设置CopyOptions.None时，只支持粘贴和全选。

设置CopyOptions.None时，不支持拖拽操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](../../公共定义/枚举说明/ts-appendix-enums.md#copyoptions9) | 是 | 输入的文本是否可复制。  默认值：CopyOptions.LocalDevice，支持设备内复制。 |

### maxLength10+

PhonePC/2in1TabletTVWearable

maxLength(value: number)

设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 文本的最大输入字符数。  当value<0时，按照默认值处理，不设限制。  默认值：uint32\_max，即2的32次方-1。 |

### showCounter10+

PhonePC/2in1TabletTVWearable

showCounter(value: boolean, options?: InputCounterOptions)

设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。未调用showCounter接口时，默认不显示计数器。

参数value为true时，才能设置options，文本框开启计数器功能，需要配合maxLength（设置最大字符限制）一起使用。字符计数器显示的效果是当前输入字符数/最大可输入字符数。

当输入字符数大于最大字符数乘百分比值时，显示字符计数器。如果用户设置计数器时不设置InputCounterOptions，那么当前输入字符数达到最大字符数时，边框和计数器下标将变为红色。用户同时设置参数value为true和InputCounterOptions，当thresholdPercentage数值在有效区间内，且输入字符数超过最大字符数时，边框和计数器下标将变为红色，框体抖动。highlightBorder设置为false，则不显示红色边框，计数器默认显示红色边框。内联模式下字符计数器不显示。

[示例2（设置计数器）](ts-basic-components-textarea.md#示例2设置计数器)展示了设置showCounter的效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示计数器。  true表示显示计数器，false表示不显示。 |
| options11+ | [InputCounterOptions](../输入框类组件通用接口/ts-universal-attributes-text-style.md#inputcounteroptions11对象说明) | 否 | 计数器的配置项。 |

### style10+

PhonePC/2in1TabletTVWearable

style(value: TextContentStyle)

设置文本框多态样式，内联输入风格只支持TextAreaType.NORMAL类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextContentStyle](../../公共定义/枚举说明/ts-appendix-enums.md#textcontentstyle10) | 是 | 文本框多态样式。  默认值：TextContentStyle.DEFAULT |

### enableKeyboardOnFocus10+

PhonePC/2in1TabletTVWearable

enableKeyboardOnFocus(value: boolean)

设置TextArea通过点击以外的方式获焦时，是否主动拉起软键盘。

从API version 10开始，获焦默认绑定输入法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 通过点击以外的方式获焦时，是否主动拉起软键盘。  true表示主动拉起，false表示不主动拉起。  默认值：true |

### selectionMenuHidden10+

PhonePC/2in1TabletTVWearable

selectionMenuHidden(value: boolean)

设置是否不弹出系统文本选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否不弹出系统文本选择菜单。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。  设置为false时，弹出系统文本选择菜单。  默认值：false |

### barState10+

PhonePC/2in1TabletTVWearable

barState(value: BarState)

设置输入框滚动条的显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](../../公共定义/枚举说明/ts-appendix-enums.md#barstate) | 是 | 输入框滚动条的显示模式。  默认值：BarState.Auto |

### maxLines10+

PhonePC/2in1TabletTVWearable

maxLines(value: number)

配置textOverflow一起使用时，maxLines为可显示行数，超出截断；未配置textOverflow时，内联模式获焦状态下内容超出maxLines时，文本可滚动显示，内联模式非获焦状态下不生效maxLines，非内联模式按行截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内联输入风格编辑态时文本可显示的最大行数。  默认值：3，非内联模式下，默认值为UINT32\_MAX。  取值范围：(0, UINT32\_MAX] |

### maxLines20+

PhonePC/2in1TabletTVWearable

maxLines(lines: number, options: MaxLinesOptions)

配置[textOverflow](ts-basic-components-textarea.md#textoverflow12)一起使用时，maxLines为可显示行数，超出可配置为截断或滚动。未配置textOverflow时，内联模式获焦状态下内容超出maxLines时，文本可滚动显示。内联模式非获焦状态下，maxLines不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lines | number | 是 | 内联输入风格编辑态时文本可显示的最大行数。  默认值：3，非内联模式下，默认值为+∞，不限制最大行数。  取值范围：(0, +∞) |
| options | [MaxLinesOptions](../文本组件公共接口/ts-text-common.md#maxlinesoptions20对象说明) | 是 | 文本超长时显示效果。  默认值：MaxLinesMode.CLIP |

### minLines20+

PhonePC/2in1TabletTVWearable

minLines(lines: Optional<number>)

设置最小行数。组件的高度将根据lines自动调整，确保显示高度不低于lines对应的高度。如果设置了[constraintSize](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#constraintsize)，那么组件最后显示高度会在[constraintSize](../../通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#constraintsize)约束内。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lines | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 最小行数。  默认值：1  取值范围：[1, INT32\_MAX]  如果lines的值小于1，取默认值。 |

### customKeyboard10+

PhonePC/2in1TabletTVWearable

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度则使用系统默认值。

自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景，不会对应用原始界面产生压缩或者上提。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[TextAreaController](ts-basic-components-textarea.md#textareacontroller8).[stopEditing](ts-basic-components-textarea.md#stopediting10)方法控制键盘关闭。

当设置自定义键盘时，可以通过绑定[onKeyPreIme](../../通用事件/基础输入事件/按键事件/ts-universal-events-key.md#onkeypreime12)事件规避物理键盘的输入。

从API version 23开始，自定义键盘可以通过[setCustomKeyboardContinueFeature](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature23>)开启接续，在切换至其他自定义键盘时，会直接切换，不会触发键盘关闭和拉起动画。

说明

该接口不支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](../../公共定义/基础类型定义/ts-types.md#custombuilder8) | [ComponentContent](<../../../ArkTS API/UI界面/arkui/ComponentContent/js-apis-arkui-componentcontent.md#componentcontent-1>)22+ | undefined22+ | 是 | 自定义键盘。设定值为undefined时，关闭自定义键盘。 |
| options12+ | [KeyboardOptions](../RichEditor/ts-basic-components-richeditor.md#keyboardoptions12) | 否 | 设置自定义键盘是否支持避让功能。 |

### type11+

PhonePC/2in1TabletTVWearable

type(value: TextAreaType)

设置输入框类型。

不同的TextAreaType会拉起对应类型的键盘，同时限制输入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAreaType](ts-basic-components-textarea.md#textareatype11枚举说明) | 是 | 输入框类型。  默认值：TextAreaType.NORMAL |

### enterKeyType11+

PhonePC/2in1TabletTVWearable

enterKeyType(value: EnterKeyType)

设置输入法回车键类型。

说明

从API version 12开始，该接口支持在[attributeModifier](../../通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EnterKeyType](../TextInput/ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 输入法回车键类型。  默认值：EnterKeyType.NEW\_LINE |

### enableAutoFill12+

PhonePC/2in1TabletTVWearable

enableAutoFill(value: boolean)

设置是否启用自动填充。典型场景参考[密码自动填充服务](../../../../../harmonyos-guides/系统/安全/密码自动填充服务/passwordvault.md)、[智能填充服务](<../../../../../harmonyos-guides/应用服务/Scenario Fusion Kit（融合场景服务）/智能填充服务/scenario-fusion-intelligent-filling.md>)。

具体使用场景请参考[账号密码填充](../../../../../harmonyos-guides/系统/安全/密码自动填充服务/应用接入密码保险箱/自动填充/账号密码填充/passwordvault-autofill-acc-password.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用自动填充。  true表示启用，false表示不启用。  默认值：true |

### enableSelectedDataDetector22+

PhonePC/2in1TabletTVWearable

enableSelectedDataDetector(enable: boolean | undefined)

设置是否对选中文本进行实体识别。该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableSelectedDataDetector设置为true时，默认识别所有类型的实体。

需要[CopyOptions](../../公共定义/枚举说明/ts-appendix-enums.md#copyoptions9)为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE时，本功能生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | undefined | 是 | 开启选中词文本识别。  true：开启识别，false：关闭识别。默认值为：true。 |

### contentType12+

PhonePC/2in1TabletTVWearable

contentType(contentType: ContentType)

设置自动填充类型。典型场景参考[智能填充服务](<../../../../../harmonyos-guides/应用服务/Scenario Fusion Kit（融合场景服务）/智能填充服务/scenario-fusion-intelligent-filling.md>)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentType | [ContentType](../TextInput/ts-basic-components-textinput.md#contenttype12枚举说明) | 是 | 自动填充类型。 |

### lineHeight12+

PhonePC/2in1TabletTVWearable

lineHeight(value: number | string | Resource)

设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | 文本的文本行高。需要显式指定[像素单位](../../公共定义/像素单位/ts-pixel-units.md)，如'10px'，也可设置百分比字符串，如'100%'。  **说明**：不指定像素单位时，默认单位fp，如'10'，等同于10。 |

说明

特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。

### decoration12+

PhonePC/2in1TabletTVWearable

decoration(value: TextDecorationOptions)

设置文本装饰线类型样式及其颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextDecorationOptions](../输入框类组件通用接口/ts-universal-attributes-text-style.md#textdecorationoptions12对象说明) | 是 | 文本装饰线对象。  默认值：{  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID  } |

说明

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

### letterSpacing12+

PhonePC/2in1TabletTVWearable

letterSpacing(value: number | string | Resource)

设置文本字符间距。设置该值为百分比时，按默认值显示。当设置该值为0时，使用默认值。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。

对每个字符生效，包括行尾字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | 文本字符间距。  单位：[fp](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位) |

### fontFeature12+

PhonePC/2in1TabletTVWearable

fontFeature(value: string)

设置文字特性效果，比如数字等宽的特性。

格式为：normal | <feature-tag-value>

<feature-tag-value>的格式为：<string> [ <integer> | on | off ]

<feature-tag-value>的个数可以有多个，中间用','隔开。

例如，使用等宽数字的输入格式为："ss01" on。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 文字特性效果。 |

Font Feature当前支持的属性参见[fontFeature](../Text/ts-basic-components-text.md#fontfeature12)属性列表。

设置Font Feature属性，Font Feature是OpenType字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。

更多Font Feature能力介绍可参考[font-feature-settings 属性](https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop)和[OpenType 字体功能的完整 CSS 演示](https://sparanoid.com/lab/opentype-features/)。

### wordBreak12+

PhonePC/2in1TabletTVWearable

wordBreak(value: WordBreak)

设置文本断行规则。该属性对placeholder文本无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WordBreak](../../公共定义/枚举说明/ts-appendix-enums.md#wordbreak11) | 是 | 文本断行规则。  默认值：WordBreak.BREAK\_WORD |

说明

组件不支持clip属性设置，设置该属性任意枚举值对组件文本截断无影响。

### selectedBackgroundColor12+

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 是 | 文本选中底板颜色。 |

### caretStyle12+

PhonePC/2in1TabletTVWearable

caretStyle(value: CaretStyle)

设置光标风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CaretStyle](../文本组件公共接口/ts-text-common.md#caretstyle10) | 是 | 光标的风格。 |

说明

当同时设置caretColor属性和caretStyle属性中的color参数时，遵循后设置生效原则。

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### textIndent12+

PhonePC/2in1TabletTVWearable

textIndent(value: Dimension)

设置首行文本缩进。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](../../公共定义/基础类型定义/ts-types.md#dimension10) | 是 | 首行文本缩进。  默认值：0  单位：[vp](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位)  取值范围：大于等于0。设置负数时，按默认值处理。 |

### textOverflow12+

PhonePC/2in1TabletTVWearable

textOverflow(value: TextOverflow)

设置文本超长时的显示方式。

内联模式，主动配置textOverflow才会生效按[maxLines](ts-basic-components-textarea.md#maxlines10)截断效果，不配置时，默认不截断。

文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，[wordBreak](../../公共定义/枚举说明/ts-appendix-enums.md#wordbreak11)属性可设置为WordBreak.BREAK\_ALL。

当textOverflow设置为TextOverflow.None、TextOverflow.Clip、TextOverflow.Ellipsis时，需配合[maxLines](ts-basic-components-textarea.md#maxlines10)使用，单独设置不生效。设置TextOverflow.None与TextOverflow.Clip效果一样。

说明

TextArea组件不支持设置TextOverflow.MARQUEE模式，当设置为TextOverflow.MARQUEE模式时，显示为TextOverflow.Clip。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextOverflow](../../公共定义/枚举说明/ts-appendix-enums.md#textoverflow) | 是 | 文本超长时的显示方式。  默认值：TextOverflow.Clip |

### minFontSize12+

PhonePC/2in1TabletTVWearable

minFontSize(value: number | string | Resource)

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[maxFontSize](ts-basic-components-textarea.md#maxfontsize12)以及[maxLines](ts-basic-components-textarea.md#maxlines10)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](ts-basic-components-textarea.md#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | 文本最小显示字号。  单位：[fp](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位) |

### maxFontSize12+

PhonePC/2in1TabletTVWearable

maxFontSize(value: number | string | Resource)

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[minFontSize](ts-basic-components-textarea.md#minfontsize12)以及[maxLines](ts-basic-components-textarea.md#maxlines10)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[fontSize](ts-basic-components-textarea.md#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 是 | 文本最大显示字号。  单位：[fp](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位) |

### heightAdaptivePolicy12+

PhonePC/2in1TabletTVWearable

heightAdaptivePolicy(value: TextHeightAdaptivePolicy)

设置文本自适应高度的方式。

当设置为TextHeightAdaptivePolicy.MAX\_LINES\_FIRST时，优先使用[maxLines](ts-basic-components-textarea.md#maxlines10)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](ts-basic-components-textarea.md#minfontsize12)和[maxFontSize](ts-basic-components-textarea.md#maxfontsize12)的范围内缩小字体以显示更多文本。

组件设置为内联输入风格，编辑态与非编辑态存在字体大小不一致情况。

当设置为TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST时，优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和maxFontSize的范围内增大字体并使用最大可能的字体大小。

当设置为TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST时，优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在minFontSize和maxFontSize的范围内缩小字体以满足布局约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextHeightAdaptivePolicy](../../公共定义/枚举说明/ts-appendix-enums.md#textheightadaptivepolicy10) | 是 | 文本自适应高度的方式。  默认值：TextHeightAdaptivePolicy.MAX\_LINES\_FIRST |

### lineSpacing12+

PhonePC/2in1TabletTVWearable

lineSpacing(value: LengthMetrics)

设置文本的行间距，设置值不大于0时，取默认值0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 是 | 文本的行间距。默认值：0 |

### lineSpacing20+

PhonePC/2in1TabletTVWearable

lineSpacing(value: LengthMetrics, options?: LineSpacingOptions)

设置文本的行间距。当不配置LineSpacingOptions时，首行上方和尾行下方默认会有行间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 是 | 文本的行间距。设置值不大于0时，取默认值0。 |
| options | [LineSpacingOptions](../文本组件公共接口/ts-text-common.md#linespacingoptions20对象说明) | 否 | 设置行间距配置项。  默认值：{ onlyBetweenLines: false } |

### lineBreakStrategy12+

PhonePC/2in1TabletTVWearable

lineBreakStrategy(strategy: LineBreakStrategy)

设置折行规则。该属性在[wordBreak](ts-basic-components-textarea.md#wordbreak12)不等于WordBreak.BREAK\_ALL的时候生效，不支持连词符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [LineBreakStrategy](../../公共定义/枚举说明/ts-appendix-enums.md#linebreakstrategy12) | 是 | 文本的折行规则。  默认值：LineBreakStrategy.GREEDY |

### editMenuOptions12+

PhonePC/2in1TabletTVWearable

editMenuOptions(editMenu: EditMenuOptions)

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

调用[disableMenuItems](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20>)或[disableSystemServiceMenuItems](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (TextMenuController)/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20>)接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法[onCreateMenu](../文本组件公共接口/ts-text-common.md#oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../文本组件公共接口/ts-text-common.md#editmenuoptions) | 是 | 扩展菜单选项。 |

### enablePreviewText12+

PhonePC/2in1TabletTVWearable

enablePreviewText(enable: boolean)

设置是否开启输入预上屏。

预上屏内容定义为文字暂存态，目前不支持文字拦截功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否开启输入预上屏。  true表示开启，false表示不开启。  默认值：true |

说明

“预上屏”描述的是一种文字暂存状态。需要在输入法中开启预上屏功能，在输入文本过程中，未确认输入候选词时，文本框中显示标记文本。例如，通过拼音输入中文时，未确定候选词之前，在输入框中显示拼音字母，该状态称为文字预上屏。

### enableHapticFeedback13+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(isEnabled: boolean)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的[module.json5](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中配置requestPermissions字段以开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE",
4. }
5. ]
```

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否开启触控反馈。  true表示开启，false表示不开启。  默认值：true |

### autoCapitalizationMode20+

PhonePC/2in1TabletTVWearable

autoCapitalizationMode(mode: AutoCapitalizationMode)

设置自动大小写模式的文本模式，只提供接口能力，具体实现以输入法应用为主。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AutoCapitalizationMode](../文本组件公共接口/ts-text-common.md#autocapitalizationmode20枚举说明) | 是 | 自动大小写模式，默认状态无效。 |

### keyboardAppearance15+

PhonePC/2in1TabletTVWearable

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

设置输入框拉起的键盘样式，需要输入法适配后生效。具体参考[输入法应用沉浸模式](<../../../../../harmonyos-guides/应用框架/IME Kit（输入法开发服务）/输入法应用沉浸模式/inputmethod-immersive-mode-guide.md>)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appearance | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<[KeyboardAppearance](../文本组件公共接口/ts-text-common.md#keyboardappearance15枚举说明)> | 是 | 键盘样式。  默认值：KeyboardAppearance.NONE\_IMMERSIVE |

### strokeWidth20+

PhonePC/2in1TabletTVWearable

strokeWidth(width: Optional<LengthMetrics>)

设置文本描边的宽度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>)> | 是 | 文本描边的宽度。如果LengthMetrics的unit值是PERCENT，当前设置不生效，按默认值处理。  若设置值小于0，显示实心字；若大于0，显示空心字。  默认值为0，不做描边处理。 |

### strokeColor20+

PhonePC/2in1TabletTVWearable

strokeColor(color: Optional<ResourceColor>)

设置文本描边的颜色。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor)> | 是 | 描边颜色。默认值为字体颜色，设置异常值时取默认值。 |

### stopBackPress15+

PhonePC/2in1TabletTVWearable

stopBackPress(isStopped: Optional<boolean>)

设置是否阻止返回键传递。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isStopped | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否阻止返回键。  true表示阻止，false表示不阻止。  默认值：true。异常值取默认值。 |

### halfLeading18+

PhonePC/2in1TabletTVWearable

halfLeading(halfLeading: Optional<boolean>)

设置文本在行内垂直居中，将行间距平分至行的顶部与底部。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| halfLeading | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置文本是否垂直居中。  true表示将行间距平分至行的顶部与底部，false则不平分。  默认值：false |

### minFontScale18+

PhonePC/2in1TabletTVWearable

minFontScale(scale: Optional<number | Resource>)

设置文本最小的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource)> | 是 | 文本最小的字体缩放倍数，支持undefined类型。  取值范围：[0, 1]  **说明：**  设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。  使用前需在工程中配置configuration.json文件和app.json5文件，具体详见[示例17（设置最小字体范围与最大字体范围）](ts-basic-components-textarea.md#示例17设置最小字体范围与最大字体范围)。 |

### maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: Optional<number | Resource>)

设置文本最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource)> | 是 | 文本最大的字体缩放倍数，支持undefined类型。  取值范围：[1, +∞)  **说明：**  设置的值小于1时，按值为1处理。异常值默认不生效。  使用前需在工程中配置configuration.json文件和app.json5文件，具体详见[示例17（设置最小字体范围与最大字体范围）](ts-basic-components-textarea.md#示例17设置最小字体范围与最大字体范围)。 |

### ellipsisMode18+

PhonePC/2in1TabletTVWearable

ellipsisMode(mode: Optional<EllipsisMode>)

设置省略位置。ellipsisMode属性需要配合[textOverflow](ts-basic-components-textarea.md#textoverflow12)设置为TextOverflow.Ellipsis以及[maxLines](ts-basic-components-textarea.md#maxlines10)使用，单独设置ellipsisMode属性不生效。

EllipsisMode.START和EllipsisMode.CENTER仅在[maxLines](ts-basic-components-textarea.md#maxlines10)设置为1生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<[EllipsisMode](../../公共定义/枚举说明/ts-appendix-enums.md#ellipsismode11)> | 是 | 省略位置。  默认值：EllipsisMode.END |

### enableAutoSpacing20+

PhonePC/2in1TabletTVWearable

enableAutoSpacing(enabled: Optional<boolean>)

设置是否开启中文与西文的自动间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启中文与西文的自动间距。  true为开启自动间距，false为不开启。  默认值：false |

### scrollBarColor22+

PhonePC/2in1TabletTVWearable

scrollBarColor(thumbColor: ColorMetrics | undefined)

设置滚动条的颜色。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thumbColor | [ColorMetrics](<../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | undefined | 是 | 滚动条的颜色。  默认值：'#66182431'，显示为灰色。 |

### compressLeadingPunctuation23+

PhonePC/2in1TabletTVWearable

compressLeadingPunctuation(enabled: Optional<boolean>)

设置是否开启行首标点符号压缩。

说明

* 行首标点符号默认不压缩。
* 支持压缩的标点符号，请参考[ParagraphStyle](<../../../../ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.text (文本模块)/js-apis-graphics-text.md#paragraphstyle>)的行首压缩的标点范围。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启行首标点符号压缩。  true表示开启行首标点符号压缩；false表示不开启行首标点符号压缩。 |

### includeFontPadding23+

PhonePC/2in1TabletTVWearable

includeFontPadding(include: Optional<boolean>)

设置是否在首行和尾行增加间距以避免文字截断。不通过该接口设置，默认不增加间距。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| include | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否在首行和尾行增加间距以避免文字截断。  true表示在首行和尾行增加间距；false表示在首行和尾行不增加间距。 |

### fallbackLineSpacing23+

PhonePC/2in1TabletTVWearable

fallbackLineSpacing(enabled: Optional<boolean>)

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。不通过该接口设置，默认行高不基于文字实际高度自适应。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](../../通用属性/动态属性与自定义/自定义属性设置/ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 行高是否基于文字实际高度自适应。  true表示行高基于文字实际高度自适应；false表示行高不基于文字实际高度自适应。 |

### selectedDragPreviewStyle23+

PhonePC/2in1TabletTVWearable

selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)

设置多行文本输入框内文本拖拽时的背板样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectedDragPreviewStyle](../文本组件公共接口/ts-text-common.md#selecteddragpreviewstyle23对象说明) | undefined | 是 | 文本拖拽时的背板样式。  设置为undefined时：背板颜色跟随主题，浅色模式显示白色，深色模式显示黑色。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](../../通用事件/ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: EditableTextOnChangeCallback)

输入内容发生变化时，触发该回调。

在本回调中，若执行了光标操作，需要开发者在预上屏场景下依据[EditableTextOnChangeCallback](../文本组件公共接口/ts-text-common.md#editabletextonchangecallback12)的previewText参数调整光标逻辑，以适应预上屏场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [EditableTextOnChangeCallback](../文本组件公共接口/ts-text-common.md#editabletextonchangecallback12) | 是 | 当前输入文本内容变化时的回调。 |

### onEditChange10+

PhonePC/2in1TabletTVWearable

onEditChange(callback: (isEditing: boolean) => void)

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEditing | boolean | 是 | 是否处于编辑态。  true：编辑态；false：非编辑态。 |

### onCopy8+

PhonePC/2in1TabletTVWearable

onCopy(callback: (value: string) => void)

进行复制操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 复制的文本内容。 |

### onCut8+

PhonePC/2in1TabletTVWearable

onCut(callback: (value: string) => void)

进行剪切操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 剪切的文本内容。 |

### onPaste

PhonePC/2in1TabletTVWearable

onPaste(callback: (value: string, event: PasteEvent) => void)

进行粘贴操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 粘贴的文本内容。 |
| event11+ | [PasteEvent](../RichEditor/ts-basic-components-richeditor.md#pasteevent11) | 是 | 用户自定义的粘贴事件。 |

### onTextSelectionChange10+

PhonePC/2in1TabletTVWearable

onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void)

文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 所选文本的起始位置，文字的起始位置为0。 |
| selectionEnd | number | 是 | 所选文本的结束位置。 |

### onContentScroll10+

PhonePC/2in1TabletTVWearable

onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void)

文本内容滚动时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalOffsetX | number | 是 | 文本在内容区的横坐标偏移。  单位：[px](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位) |
| totalOffsetY | number | 是 | 文本在内容区的纵坐标偏移。  单位：[px](../../公共定义/像素单位/ts-pixel-units.md#基本像素单位) |

### onSubmit11+

PhonePC/2in1TabletTVWearable

onSubmit(callback: (enterKey: EnterKeyType) => void)

按下软键盘输入法回车键时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](../TextInput/ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 输入法回车键类型，类型为EnterKeyType.NEW\_LINE时不触发onSubmit。 |

### onSubmit14+

PhonePC/2in1TabletTVWearable

onSubmit(callback: TextAreaSubmitCallback)

按下软键盘输入法回车键触发该回调事件，提交事件时提供保持TextArea编辑状态的方法。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextAreaSubmitCallback](ts-basic-components-textarea.md#textareasubmitcallback14) | 是 | 按下软键盘输入法回车键时的回调事件。 |

### onWillInsert12+

PhonePC/2in1TabletTVWearable

onWillInsert(callback: Callback<InsertValue, boolean>)

在将要输入时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InsertValue](../文本组件公共接口/ts-text-common.md#insertvalue12对象说明), boolean> | 是 | 在将要输入时调用的回调。  在返回true时，表示正常插入，返回false时，表示不插入。  在预上屏和候选词操作时，该回调不触发。  仅支持系统输入法输入的场景。 |

### onDidInsert12+

PhonePC/2in1TabletTVWearable

onDidInsert(callback: Callback<InsertValue>)

在输入完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InsertValue](../文本组件公共接口/ts-text-common.md#insertvalue12对象说明)> | 是 | 在输入完成时调用的回调。  仅支持系统输入法输入的场景。 |

### onWillDelete12+

PhonePC/2in1TabletTVWearable

onWillDelete(callback: Callback<DeleteValue, boolean>)

在将要删除时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DeleteValue](../文本组件公共接口/ts-text-common.md#deletevalue12对象说明), boolean> | 是 | 在将要删除时调用的回调。  在返回true时，表示正常删除，返回false时，表示不删除。  在预上屏删除操作时，该回调不触发。  仅支持系统输入法输入的场景。 |

### onDidDelete12+

PhonePC/2in1TabletTVWearable

onDidDelete(callback: Callback<DeleteValue>)

在删除完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DeleteValue](../文本组件公共接口/ts-text-common.md#deletevalue12对象说明)> | 是 | 在删除完成时调用的回调。  仅支持系统输入法输入的场景。 |

说明

点击清除按钮不触发onDidDelete回调。

### onWillChange15+

PhonePC/2in1TabletTVWearable

onWillChange(callback: Callback<EditableTextChangeValue, boolean>)

在文本内容将要发生变化时，触发该回调。

onWillChange的回调时序晚于onWillInsert、onWillDelete，早于onDidInsert、onDidDelete。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[EditableTextChangeValue](../文本组件公共接口/ts-text-common.md#editabletextchangevalue15), boolean> | 是 | 在文本内容将要发生变化时的回调。  返回true时，表示正常修改。返回false时，表示拦截此次触发。 |

### onWillAttachIME22+

PhonePC/2in1TabletTVWearable

onWillAttachIME(callback: Callback<IMEClient> | undefined)

在输入框将要绑定输入法前触发该回调。

从API version 22开始，调用[IMEClient](../文本组件公共接口/ts-text-common.md#imeclient20对象说明)的[setExtraConfig](../文本组件公共接口/ts-text-common.md#setextraconfig22)方法可以设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IMEClient](../文本组件公共接口/ts-text-common.md#imeclient20对象说明)> | undefined | 是 | 在输入框将要绑定输入法前触发该回调。 |

## TextAreaController8+

PhonePC/2in1TabletTVWearable

TextArea组件的控制器继承自[TextContentControllerBase](../输入框类组件通用接口/ts-universal-attributes-text-style.md#textcontentcontrollerbase)，涉及的接口有[getTextContentRect](../输入框类组件通用接口/ts-universal-attributes-text-style.md#gettextcontentrect)、[getTextContentLineCount](../输入框类组件通用接口/ts-universal-attributes-text-style.md#gettextcontentlinecount)、[getCaretOffset](../输入框类组件通用接口/ts-universal-attributes-text-style.md#getcaretoffset11)、[addText](../输入框类组件通用接口/ts-universal-attributes-text-style.md#addtext15)、[deleteText](../输入框类组件通用接口/ts-universal-attributes-text-style.md#deletetext15)、[getSelection](../输入框类组件通用接口/ts-universal-attributes-text-style.md#getselection15)、[clearPreviewText](../输入框类组件通用接口/ts-universal-attributes-text-style.md#clearpreviewtext17)、[setStyledPlaceholder](../输入框类组件通用接口/ts-universal-attributes-text-style.md#setstyledplaceholder22)、[deleteBackward](../输入框类组件通用接口/ts-universal-attributes-text-style.md#deletebackward23)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 导入对象

```
1. controller: TextAreaController = new TextAreaController()
```

### constructor8+

PhonePC/2in1TabletTVWearable

constructor()

TextAreaController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### caretPosition8+

PhonePC/2in1TabletTVWearable

caretPosition(value: number): void

设置输入光标的位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 从字符串开始到光标所在位置的字符长度。  当value<0时，按照0处理。当value>字符串长度时，按照字符串长度处理。 |

### setTextSelection10+

PhonePC/2in1TabletTVWearable

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 文本选择区域起始位置，文本框中文字的起始位置为0。  当selectionStart小于0时，按0处理；当selectionStart大于文字最大长度时，按照文字最大长度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectionEnd | number | 是 | 文本选择区域结束位置。  当selectionEnd小于0时，按0处理；当selectionEnd大于文字最大长度时，按照文字最大长度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| options12+ | [SelectionOptions](../输入框类组件通用接口/ts-universal-attributes-text-style.md#selectionoptions12对象说明) | 否 | 选中文字时的配置。  默认值：MenuPolicy.DEFAULT  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

说明

如果selectionMenuHidden被赋值为true或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。

如果选中的文本含有emoji表情时，表情的起始位置包含在设置的文本选中区域内就会被选中。

### stopEditing10+

PhonePC/2in1TabletTVWearable

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## TextAreaType11+枚举说明

PhonePC/2in1TabletTVWearable

多行文本输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 基本输入模式，无特殊限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER | 2 | 纯数字输入模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PHONE\_NUMBER | 3 | 电话号码输入模式。  支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EMAIL | 5 | 邮箱地址输入模式。  支持数字，字母，下划线、小数点、!、#、$、%、&、'、\*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER\_DECIMAL12+ | 12 | 带小数点的数字输入模式。  支持数字，小数点（只能存在一个小数点）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| URL12+ | 13 | 带URL的输入模式，无特殊限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ONE\_TIME\_CODE20+ | 14 | 验证码输入模式，无特殊限制。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## TextAreaSubmitCallback14+

PhonePC/2in1TabletTVWearable

type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void

软键盘按下回车键时的回调事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKeyType | [EnterKeyType](../TextInput/ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 软键盘输入法回车键类型。  类型为EnterKeyType.NEW\_LINE时不触发onSubmit。 |
| event | [SubmitEvent](../TextInput/ts-basic-components-textinput.md#submitevent11) | 否 | 提交事件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置与获取光标位置）

从API version 8开始，该示例通过[controller](ts-basic-components-textarea.md#textareacontroller8)实现了光标位置的设置与获取。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '';
6. @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
7. controller: TextAreaController = new TextAreaController();

9. build() {
10. Column() {
11. TextArea({
12. text: this.text,
13. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
14. controller: this.controller
15. })
16. .placeholderFont({ size: 16, weight: 400 })
17. .width(336)
18. .height(56)
19. .margin(20)
20. .fontSize(16)
21. .fontColor('#182431')
22. .backgroundColor('#FFFFFF')
23. .onChange((value: string) => {
24. this.text = value;
25. })
26. Text(this.text)
27. Button('Set caretPosition 1')
28. .backgroundColor('#007DFF')
29. .margin(15)
30. .onClick(() => {
31. // 设置光标位置到第一个字符后
32. this.controller.caretPosition(1);
33. })
34. Button('Get CaretOffset')
35. .backgroundColor('#007DFF')
36. .margin(15)
37. .onClick(() => {
38. this.positionInfo = this.controller.getCaretOffset();
39. })
40. }.width('100%').height('100%').backgroundColor('#F1F3F5')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/7uxjWZn8Q2qRLtiXq_Q9kQ/zh-cn_image_0000002622859655.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=AE4AB5314F38DB2029C9402C70C1747CCB1D74485B3CDCC2C6E35326107A0FD4)

### 示例2（设置计数器）

从API version 10开始，该示例通过[maxLength](ts-basic-components-textarea.md#maxlength10)、[showCounter](ts-basic-components-textarea.md#showcounter10)属性实现了计数器的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '';
6. controller: TextAreaController = new TextAreaController();

8. build() {
9. Column() {
10. TextArea({
11. text: this.text,
12. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
13. controller: this.controller
14. })
15. .placeholderFont({ size: 16, weight: 400 })
16. .width(336)
17. .height(56)
18. .margin(20)
19. .fontSize(16)
20. .fontColor('#182431')
21. .backgroundColor('#FFFFFF')
22. .maxLength(4)
23. .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })
24. // 计数器显示效果为用户当前输入字符数/最大字符限制数。最大字符限制数通过maxLength()接口设置。
25. // 如果用户当前输入字符数达到最大字符限制乘50%（thresholdPercentage）。字符计数器显示。
26. // 用户设置highlightBorder为false时，配置取消红色边框。不设置此参数时，默认为true。
27. .onChange((value: string) => {
28. this.text = value;
29. })
30. }.width('100%').height('100%').backgroundColor('#F1F3F5')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/jqPhkAUHRJ2fmOwbhfkNxA/zh-cn_image_0000002622699775.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=DD5733D2EAB5928FA8D274AE76FAC635EE28408BCB0BE6B7A114A6D6A11D316E)

### 示例3（设置自定义键盘）

该示例通过[customKeyboard](ts-basic-components-textarea.md#customkeyboard10)（从API version 10开始）属性分别将value中的入参类型设置为[CustomBuilder](../../公共定义/基础类型定义/ts-types.md#custombuilder8)和[ComponentContent](<../../../ArkTS API/UI界面/arkui/ComponentContent/js-apis-arkui-componentcontent.md#componentcontent-1>)，实现了自定义键盘的功能。

从API version 22开始[customKeyboard](ts-basic-components-textarea.md#customkeyboard10)属性新增了入参类型[ComponentContent](<../../../ArkTS API/UI界面/arkui/ComponentContent/js-apis-arkui-componentcontent.md#componentcontent-1>)。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. class BuilderParams {
4. inputValue: string;
5. controller: TextAreaController;

7. constructor(inputValue: string, controller: TextAreaController) {
8. this.inputValue = inputValue;
9. this.controller = controller;
10. }
11. }
12. @Builder
13. function CustomKeyboardBuilder(builderParams: BuilderParams) {
14. Column() {
15. Row() {
16. Button('x').onClick(() => {
17. // 关闭自定义键盘
18. builderParams.controller.stopEditing();
19. }).margin(10)
20. }

22. Grid() {
23. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
24. GridItem() {
25. Button(item + "")
26. .width(110).onClick(() => {
27. builderParams.inputValue += item;
28. })
29. }
30. })
31. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
32. }.backgroundColor(Color.Gray)
33. }
34. @Entry
35. @Component
36. struct TextAreaExample {
37. controller: TextAreaController = new TextAreaController();
38. @State inputValue: string = "";
39. @State componentContent ?: ComponentContent<BuilderParams> = undefined;
40. @State builderParam: BuilderParams = new BuilderParams(this.inputValue, this.controller);
41. @State supportAvoidance: boolean = true;

43. aboutToAppear(): void {
44. // 创建ComponentContent
45. this.componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(CustomKeyboardBuilder), this.builderParam);
46. }
47. build(){
48. Column() {
49. Text('Builder').margin(10).border({ width: 1 })
50. TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
51. .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
52. .margin(10).border({ width: 1 }).height('48vp')

54. Text('ComponentContent').margin(10).border({ width: 1 })
55. TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
56. .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
57. .margin(10).border({ width: 1 }).height('48vp')
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/BJbF7VqhR6Wb9yQhgWVV5Q/zh-cn_image_0000002592220214.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=A2CB2E6D4727022D41C718192920D98D0558C4550D479E88C08A97A463564ECC)

### 示例4（设置输入法回车键类型）

从API version 11开始，该示例通过[enterKeyType](ts-basic-components-textarea.md#enterkeytype11)属性实现了动态切换输入法回车键的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '';
6. @State enterTypes: Array<EnterKeyType> =
7. [EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next,
8. EnterKeyType.PREVIOUS, EnterKeyType.NEW_LINE];
9. @State index: number = 0;

11. build() {
12. Column({ space: 20 }) {
13. TextArea({ placeholder: '请输入用户名', text: this.text })
14. .width(380)
15. .enterKeyType(this.enterTypes[this.index])
16. .onChange((value: string) => {
17. this.text = value;
18. })
19. .onSubmit((enterKey: EnterKeyType) => {
20. console.info("trigger area onSubmit" + enterKey);
21. })
22. Button('改变EnterKeyType').onClick(() => {
23. this.index = (this.index + 1) % this.enterTypes.length;
24. })

26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/L6y97Qg5S5-OogwOIm-HUg/zh-cn_image_0000002592380148.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=B14385B9F5313A2B2D12D0F69E2D3842C0DA81847A70684AD29F167EEB8F695E)

### 示例5（设置文本断行规则）

从API version 12开始，该示例通过[wordBreak](ts-basic-components-textarea.md#wordbreak12)属性实现了TextArea不同断行规则下的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Column() {
7. Text("属性WordBreakType为NORMAL的样式：").fontSize(16).fontColor(0xFF0000)
8. TextArea({
9. text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
10. })
11. .fontSize(16)
12. .border({ width: 1 })
13. .wordBreak(WordBreak.NORMAL)
14. Text("英文文本，属性WordBreakType为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)
15. TextArea({
16. text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
17. })
18. .fontSize(16)
19. .border({ width: 1 })
20. .wordBreak(WordBreak.BREAK_ALL)
21. Text("中文文本，属性WordBreakType为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)
22. TextArea({
23. text: '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。'
24. })
25. .fontSize(16)
26. .border({ width: 1 })
27. .wordBreak(WordBreak.BREAK_ALL)
28. Text("属性WordBreakType为BREAK_WORD的样式：").fontSize(16).fontColor(0xFF0000)
29. TextArea({
30. text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
31. })
32. .fontSize(16)
33. .border({ width: 1 })
34. .wordBreak(WordBreak.BREAK_WORD)
35. }
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/zhruQnoNQE-FF7EawPKJzg/zh-cn_image_0000002622859657.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=954BA3AB604C99D3E352AC5766C5B5BA1544E25EBF457C4A2C4BEA4072DD284E)

### 示例6（设置文本样式）

从API version 12开始，该示例通过[lineHeight](ts-basic-components-textarea.md#lineheight12)、[letterSpacing](ts-basic-components-textarea.md#letterspacing12)、[decoration](ts-basic-components-textarea.md#decoration12)属性展示了不同样式的文本效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Row() {
7. Column() {
8. Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
9. TextArea({ text: 'lineHeight unset' })
10. .border({ width: 1 }).padding(10).margin(5)
11. TextArea({ text: 'lineHeight 15' })
12. .border({ width: 1 }).padding(10).margin(5).lineHeight(15)
13. TextArea({ text: 'lineHeight 30' })
14. .border({ width: 1 }).padding(10).margin(5).lineHeight(30)

16. Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
17. TextArea({ text: 'letterSpacing 0' })
18. .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)
19. TextArea({ text: 'letterSpacing 3' })
20. .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)
21. TextArea({ text: 'letterSpacing -1' })
22. .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)

24. Text('decoration').fontSize(9).fontColor(0xCCCCCC)
25. TextArea({ text: 'LineThrough, Red\nsecond line' })
26. .border({ width: 1 }).padding(5).margin(5)
27. .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
28. TextArea({ text: 'Overline, Red, DOTTED\nsecond line' })
29. .border({ width: 1 }).padding(5).margin(5)
30. .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DOTTED })
31. TextArea({ text: 'Underline, Red, WAVY\nsecond line' })
32. .border({ width: 1 }).padding(5).margin(5)
33. .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
34. }.height('90%')
35. }
36. .width('90%')
37. .margin(10)
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/_Hx2A_QiSrqX7TpegPUYKA/zh-cn_image_0000002622699777.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=C153D90D12CF9DC7FE278B1EA6CE0D78D5B0373645E6C80223159E589E64903A)

### 示例7（设置文字特性效果）

从API version 12开始，该示例通过[fontFeature](ts-basic-components-textarea.md#fontfeature12)属性实现了文本在不同文字特性下的展示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text1: string = 'This is ss01 on : 0123456789';
6. @State text2: string = 'This is ss01 off: 0123456789';

8. build() {
9. Column() {
10. TextArea({ text: this.text1 })
11. .fontSize(20)
12. .margin({ top: 200 })
13. .fontFeature("\"ss01\" on")
14. TextArea({ text: this.text2 })
15. .margin({ top: 10 })
16. .fontSize(20)
17. .fontFeature("\"ss01\" off")
18. }
19. .width("90%")
20. .margin("5%")
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VEgZpKISS6myeJ7R-r70rA/zh-cn_image_0000002592220216.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=4B7BCE322ACAB14633E6291AF40D8B4710C543396A06A41735D3407DE22AB3B6)

### 示例8（自定义键盘避让）

该示例通过[customKeyboard](ts-basic-components-textarea.md#customkeyboard10)（从API version 10开始）属性配置[KeyboardOptions](../RichEditor/ts-basic-components-richeditor.md#keyboardoptions12)（从API version 12开始）接口实现了自定义键盘避让的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. controller: TextAreaController = new TextAreaController();
6. @State inputValue: string = "";
7. @State height1: string | number = '80%';
8. @State height2: number = 100;
9. @State supportAvoidance: boolean = true;

11. // 自定义键盘组件
12. @Builder
13. CustomKeyboardBuilder() {
14. Column() {
15. Row() {
16. Button('x').onClick(() => {
17. // 关闭自定义键盘
18. this.controller.stopEditing();
19. }).margin(10)
20. }

22. Grid() {
23. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
24. GridItem() {
25. Button(item + "")
26. .width(110).onClick(() => {
27. this.inputValue += item;
28. })
29. }
30. })
31. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
32. }.backgroundColor(Color.Gray)
33. }

35. build() {
36. Column() {
37. Row() {
38. Button("20%")
39. .fontSize(24)
40. .onClick(() => {
41. this.height1 = "20%";
42. })
43. Button("80%")
44. .fontSize(24)
45. .margin({ left: 20 })
46. .onClick(() => {
47. this.height1 = "80%";
48. })
49. }
50. .justifyContent(FlexAlign.Center)
51. .alignItems(VerticalAlign.Bottom)
52. .height(this.height1)
53. .width("100%")
54. .padding({ bottom: 50 })

56. TextArea({ controller: this.controller, text: this.inputValue })// 绑定自定义键盘
57. .height(100)
58. .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
59. .margin(10)
60. .border({ width: 1 })
61. }
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Qpr3p3P3R32OgPvbtPomnw/zh-cn_image_0000002592380150.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=91785B07FAB19B662C1EE60B15D44940A5B8965DA3A20D181550DA4A3D471BCE)

### 示例9（设置文本自适应）

从API version 12开始，该示例通过[minFontSize](ts-basic-components-textarea.md#minfontsize12)、[maxFontSize](ts-basic-components-textarea.md#maxfontsize12)、[heightAdaptivePolicy](ts-basic-components-textarea.md#heightadaptivepolicy12)属性展示了文本自适应字号的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Row() {
7. Column() {
8. Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)
9. TextArea({text: 'This is the text with the height adaptive policy set'})
10. .width('80%').height(90).borderWidth(1).margin(1)
11. .minFontSize(4)
12. .maxFontSize(40)
13. .maxLines(3)
14. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
15. TextArea({text: 'This is the text with the height adaptive policy set'})
16. .width('80%').height(90).borderWidth(1).margin(1)
17. .minFontSize(4)
18. .maxFontSize(40)
19. .maxLines(3)
20. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
21. TextArea({text: 'This is the text with the height adaptive policy set'})
22. .width('80%').height(90).borderWidth(1).margin(1)
23. .minFontSize(4)
24. .maxFontSize(40)
25. .maxLines(3)
26. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
27. }.height('90%')
28. }
29. .width('90%')
30. .margin(10)
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/COgNxO59QSW2eyMejj-LOw/zh-cn_image_0000002622859659.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=9669DE1BE009C67D0154EBC07699D80889F83E2C8F06CC4F52450D21F779EC1D)

### 示例10（设置文本行间距）

从API version 12开始，该示例通过[lineSpacing](ts-basic-components-textarea.md#linespacing12)属性展示了文本在不同行间距下的展示效果，同时，配置[LineSpacingOptions](../文本组件公共接口/ts-text-common.md#linespacingoptions20对象说明)中的onlyBetweenLines（从API version 20开始）属性，可以设置文本的行间距，是否仅在行与行之间生效。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TextAreaExample {
7. build() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
9. Text('TextArea lineSpacing.').fontSize(9).fontColor(0xCCCCCC)
10. TextArea({ text: 'This is the TextArea with no lineSpacing set.' })
11. .fontSize(12)
12. TextArea({ text: 'This is the TextArea with lineSpacing set to 20_px.' })
13. .fontSize(12)
14. .lineSpacing(LengthMetrics.px(20))
15. TextArea({ text: 'This is the TextArea with lineSpacing set to 20_vp.' })
16. .fontSize(12)
17. .lineSpacing(LengthMetrics.vp(20))
18. TextArea({ text: 'This is the TextArea with lineSpacing set to 20_fp.' })
19. .fontSize(12)
20. .lineSpacing(LengthMetrics.fp(20))
21. TextArea({ text: 'This is the TextArea with lineSpacing set to 20_lpx.' })
22. .fontSize(12)
23. .lineSpacing(LengthMetrics.lpx(20))
24. TextArea({ text: 'This is the TextArea with lineSpacing set to 100%.' })
25. .fontSize(12)
26. .lineSpacing(LengthMetrics.percent(1))
27. TextArea({ text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.' })
28. .fontSize(12)
29. .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
30. }.height(600).width(350).padding({ left: 35, right: 35, top: 35 })
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/_fuh8Q4JT4uY8N7wUvwFzA/zh-cn_image_0000002622699779.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=EEAE1FC5BA6EC3E794F9D37707A4AE26C8003B9FBE830678B2C59A7A667C38AF)

### 示例11（设置自动填充）

从API version 12开始，该示例通过[contentType](ts-basic-components-textarea.md#contenttype12)、[enableAutoFill](ts-basic-components-textarea.md#enableautofill12)属性实现了文本自动填充的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '';

7. build() {
8. Column() {
9. // 邮箱地址自动填充类型
10. TextArea({ placeholder: 'input your email...' })
11. .width('95%')
12. .height(40)
13. .margin(20)
14. .contentType(ContentType.EMAIL_ADDRESS)
15. .enableAutoFill(true)
16. .maxLength(20)
17. // 街道地址自动填充类型
18. TextArea({ placeholder: 'input your street address...' })
19. .width('95%')
20. .height(40)
21. .margin(20)
22. .contentType(ContentType.FULL_STREET_ADDRESS)
23. .enableAutoFill(true)
24. .maxLength(20)
25. }.width('100%').height('100%').backgroundColor('#F1F3F5')
26. }
27. }
```

具体使用场景请参考[账号密码填充](../../../../../harmonyos-guides/系统/安全/密码自动填充服务/应用接入密码保险箱/自动填充/账号密码填充/passwordvault-autofill-acc-password.md)。

### 示例12（设置折行规则）

从API version 12开始，该示例通过[lineBreakStrategy](ts-basic-components-textarea.md#linebreakstrategy12)属性实现了TextArea不同折行规则下的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State message1: string =
6. "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +
7. "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effect of these components in method chaining mode," +
8. "page components are divided into independent UI units to implement independent creation development and reuse of different units on pages making pages more engineering-oriented.";
9. @State lineBreakStrategyIndex: number = 0;
10. @State lineBreakStrategy: LineBreakStrategy[] =
11. [LineBreakStrategy.GREEDY, LineBreakStrategy.HIGH_QUALITY, LineBreakStrategy.BALANCED];
12. @State lineBreakStrategyStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED'];

14. build() {
15. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
16. Text('lineBreakStrategy').fontSize(9).fontColor(0xCCCCCC)
17. TextArea({ text: this.message1 })
18. .fontSize(12)
19. .border({ width: 1 })
20. .padding(10)
21. .width('100%')
22. .lineBreakStrategy(this.lineBreakStrategy[this.lineBreakStrategyIndex])
23. Row() {
24. Button('当前lineBreakStrategy模式：' + this.lineBreakStrategyStr[this.lineBreakStrategyIndex]).onClick(() => {
25. this.lineBreakStrategyIndex++;
26. if (this.lineBreakStrategyIndex > (this.lineBreakStrategyStr.length - 1)) {
27. this.lineBreakStrategyIndex = 0;
28. }
29. })
30. }.padding({ top: 10 })
31. }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/cb4tg2tESfGgDr0BE-Jr5A/zh-cn_image_0000002592220218.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=BFF3F0EA105019399C0B813CA43465056232C92E5B55B4172C1C8AAB59966845)

### 示例13（支持插入和删除回调）

从API version 12开始，该示例通过[onWillInsert](ts-basic-components-textarea.md#onwillinsert12)、[onDidInsert](ts-basic-components-textarea.md#ondidinsert12)、[onWillDelete](ts-basic-components-textarea.md#onwilldelete12)、[onDidDelete](ts-basic-components-textarea.md#ondiddelete12)接口实现了插入和删除的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State insertValue: string = "";
6. @State deleteValue: string = "";
7. @State insertOffset: number = 0;
8. @State deleteOffset: number = 0;
9. @State deleteDirection: number = 0;
10. @State currentValue_1: string = "";
11. @State currentValue_2: string = "";

13. build() {
14. Row() {
15. Column() {
16. TextArea({ text: "TextArea支持插入回调文本" })
17. .width(300)
18. .height(60)
19. .onWillInsert((info: InsertValue) => {
20. this.insertValue = info.insertValue;
21. return true;
22. })
23. .onDidInsert((info: InsertValue) => {
24. this.insertOffset = info.insertOffset;
25. })
26. .onWillChange((info: EditableTextChangeValue) => {
27. this.currentValue_1 = info.content
28. return true
29. })

31. Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)
32. Text("currentValue_1:" + this.currentValue_1).height(30)

34. TextArea({ text: "TextArea支持删除回调文本b" })
35. .width(300)
36. .height(60)
37. .onWillDelete((info: DeleteValue) => {
38. this.deleteValue = info.deleteValue;
39. this.deleteDirection = info.direction;
40. return true;
41. })
42. .onDidDelete((info: DeleteValue) => {
43. this.deleteOffset = info.deleteOffset;
44. this.deleteDirection = info.direction;
45. })
46. .onWillChange((info: EditableTextChangeValue) => {
47. this.currentValue_2 = info.content
48. return true
49. })

51. Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)
52. Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)
53. Text("currentValue_2:" + this.currentValue_2).height(30)

55. }.width('100%')
56. }
57. .height('100%')
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/EHDMVmL7RJGZhI49L6X5zA/zh-cn_image_0000002592380152.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=DF511F3791E616A9953A556D8D26CFACD1D2AADA65A0FD9A07CC0DDC7DE3A728)

### 示例14（文本扩展自定义菜单）

从API version 12开始，该示例通过[editMenuOptions](ts-basic-components-textarea.md#editmenuoptions12)接口实现了文本设置自定义菜单扩展项的文本内容、图标以及回调的功能，同时，可以在[onPrepareMenu](../文本组件公共接口/ts-text-common.md#属性-1)（从API version 20开始）回调中，进行菜单数据的设置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = 'TextArea editMenuOptions';
6. @State endIndex: number = 0;
7. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
8. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
9. let item1: TextMenuItem = {
10. content: 'create1',
11. icon: $r('app.media.startIcon'),
12. id: TextMenuItemId.of('create1'),
13. };
14. let item2: TextMenuItem = {
15. content: 'create2',
16. id: TextMenuItemId.of('create2'),
17. icon: $r('app.media.startIcon'),
18. };
19. // 从API version 23开始支持TextMenuItemId.autoFill
20. let targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.autoFill));
21. if (targetIndex !== -1) {
22. menuItems.splice(targetIndex, 1); // 从目标索引删除1个元素
23. }
24. menuItems.push(item1);
25. menuItems.unshift(item2);
26. return menuItems;
27. }
28. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
29. if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
30. console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
31. return true;
32. }
33. if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
34. console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
35. return true;
36. }
37. if (menuItem.id.equals(TextMenuItemId.COPY)) {
38. console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
39. return true;
40. }
41. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
42. console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
43. return false;
44. }
45. return false;
46. }
47. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
48. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
49. let item1: TextMenuItem = {
50. content: 'prepare1_' + this.endIndex,
51. icon: $r('app.media.startIcon'),
52. id: TextMenuItemId.of('prepare1'),
53. };
54. menuItems.unshift(item1);
55. return menuItems;
56. }
57. @State editMenuOptions: EditMenuOptions = {
58. onCreateMenu: this.onCreateMenu,
59. onMenuItemClick: this.onMenuItemClick,
60. onPrepareMenu: this.onPrepareMenu
61. };

63. build() {
64. Column() {
65. TextArea({ text: this.text })
66. .width('95%')
67. .height(56)
68. .editMenuOptions(this.editMenuOptions)
69. .margin({ top: 100 })
70. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
71. this.endIndex = selectionEnd;
72. })
73. }
74. .width("90%")
75. .margin("5%")
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/saUNEvlcQFWXR5Zxn_j1qg/zh-cn_image_0000002622859661.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=266716FF3F621B9F752FAA82366B0624A7315ECC9275690AFD2A4C20F526DED2)

### 示例15（文本设置省略模式）

该示例通过[textOverflow](ts-basic-components-textarea.md#textoverflow12)、[ellipsisMode](ts-basic-components-textarea.md#ellipsismode18)、[maxLines](ts-basic-components-textarea.md#maxlines10)属性展示了文本超长省略以及调整省略位置的效果，通过MULTILINE\_START和MULTILINE\_CENTER两种类型实现了单行文本和多行文本场景下的省略号在行首和行中的效果。

从API version 10开始，通过[maxLines](ts-basic-components-textarea.md#maxlines10)属性设置文本显示的最大行数。

从API version 12开始，通过[textOverflow](ts-basic-components-textarea.md#textoverflow12)属性设置文本超长时的显示方式。

从API version 18开始，通过[ellipsisMode](ts-basic-components-textarea.md#ellipsismode18)属性设置省略号位置。

从API version 24开始，[EllipsisMode](../../公共定义/枚举说明/ts-appendix-enums.md#ellipsismode11)新增了MULTILINE\_START和MULTILINE\_CENTER枚举。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct EllipsisModeExample {
5. @State textIndex: number = 0;
6. @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
7. "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
8. " pink, and lavender, creating a breath taking tapestry that stretches as far as the eye can see." +
9. "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil.";
10. @State ellipsisModeIndex: number = 0;
11. @State ellipsisMode: (EllipsisMode | undefined | null)[] =
12. [EllipsisMode.START, EllipsisMode.END, EllipsisMode.CENTER, EllipsisMode.MULTILINE_START,
13. EllipsisMode.MULTILINE_CENTER, undefined, null]; // 从API version 24开始新增MULTILINE_START和MULTILINE_CENTER
14. @State ellipsisModeStr: string[] =
15. ['START ', 'END', 'CENTER', 'MULTILINE_START', 'MULTILINE_CENTER', 'undefined', 'null'];
16. @State textOverflowIndex: number = 0;
17. @State textOverflow: TextOverflow[] = [TextOverflow.Ellipsis, TextOverflow.Clip];
18. @State textOverflowStr: string[] = ['Ellipsis', 'Clip'];
19. @State maxLinesIndex: number = 0;
20. @State maxLines: number[] = [1, 2, 3];
21. @State maxLinesStr: string[] = ['1', '2', '3'];
22. @State styleAreaIndex: number = 0;
23. @State styleArea: TextContentStyle[] = [TextContentStyle.INLINE, TextContentStyle.DEFAULT];
24. @State styleAreaStr: string[] = ['INLINE', 'DEFAULT'];

26. build() {
27. Column({ space: 20 }) {
28. TextArea({ text: this.text })
29. .textOverflow(this.textOverflow[this.textOverflowIndex])
30. .ellipsisMode(this.ellipsisMode[this.ellipsisModeIndex])
31. .maxLines(this.maxLines[this.maxLinesIndex])
32. .style(this.styleArea[this.styleAreaIndex])
33. .fontSize(30)
34. .margin(30)

36. Button('更改ellipsisMode模式：' + this.ellipsisModeStr[this.ellipsisModeIndex]).onClick(() => {
37. this.ellipsisModeIndex++;
38. if (this.ellipsisModeIndex > (this.ellipsisModeStr.length - 1)) {
39. this.ellipsisModeIndex = 0;
40. }
41. }).fontSize(20)
42. Button('更改textOverflow模式：' + this.textOverflowStr[this.textOverflowIndex]).onClick(() => {
43. this.textOverflowIndex++;
44. if (this.textOverflowIndex > (this.textOverflowStr.length - 1)) {
45. this.textOverflowIndex = 0;
46. }
47. }).fontSize(20)
48. Button('更改maxLines大小：' + this.maxLinesStr[this.maxLinesIndex]).onClick(() => {
49. this.maxLinesIndex++;
50. if (this.maxLinesIndex > (this.maxLinesStr.length - 1)) {
51. this.maxLinesIndex = 0;
52. }
53. }).fontSize(20)
54. Button('更改Style大小：' + this.styleAreaStr[this.styleAreaIndex]).onClick(() => {
55. this.styleAreaIndex++;
56. if (this.styleAreaIndex > (this.styleAreaStr.length - 1)) {
57. this.styleAreaIndex = 0;
58. }
59. }).fontSize(20)
60. }.height(600).width('100%')
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/38svx8sITmaKJM6VQhjZHA/zh-cn_image_0000002622699781.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=3E2168D91A21F5A2B6553ABD432796137CAD3D91EF9AB446147CBAC14C1219D1)

### 示例16（自定义复制、剪切、粘贴）

该示例通过[onCopy](ts-basic-components-textarea.md#oncopy8)、[onCut](ts-basic-components-textarea.md#oncut8)、[onPaste](ts-basic-components-textarea.md#onpaste)展示如何监听文本选择菜单的复制、剪切、粘贴按钮，以及如何屏蔽系统粘贴功能并实现自定义的粘贴能力，同时，可以通过[maxFontScale](ts-basic-components-textarea.md#maxfontscale18)、[minFontScale](ts-basic-components-textarea.md#minfontscale18)属性设置文本最大和最小的字体缩放倍数。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '';
6. controller: TextAreaController = new TextAreaController();

8. build() {
9. Column() {
10. TextArea({
11. text: this.text,
12. placeholder: 'placeholder',
13. controller: this.controller
14. })
15. .placeholderColor(Color.Red)
16. .textAlign(TextAlign.Center)
17. .caretColor(Color.Green)
18. .caretStyle({ width: '2vp' })
19. .fontStyle(FontStyle.Italic)
20. .fontWeight(FontWeight.Bold)
21. .fontFamily('HarmonyOS Sans')
22. .inputFilter('[a-zA-Z]+', (value) => { // 只允许字母输入
23. console.error(`unsupported char ${value}`);
24. })
25. .copyOption(CopyOptions.LocalDevice)
26. .enableKeyboardOnFocus(false)
27. .selectionMenuHidden(false)
28. .barState(BarState.On)
29. .type(TextAreaType.NORMAL)
30. .selectedBackgroundColor(Color.Orange)
31. .textIndent(2)
32. .halfLeading(true)
33. .minFontScale(1)
34. .maxFontScale(2)
35. .enablePreviewText(true)
36. .enableHapticFeedback(true)
37. .stopBackPress(false)// 返回键交给其他组件处理
38. .width(336)
39. .height(56)
40. .margin(20)
41. .fontSize(16)
42. .onEditChange((isEditing: boolean) => {
43. console.info(`isEditing ${isEditing}`);
44. })
45. .onCopy((value) => {
46. console.info(`copy ${value}`);
47. })
48. .onCut((value) => {
49. console.info(`cut ${value}`);
50. })
51. .onPaste((value, event) => {
52. // 阻止系统粘贴功能，开发者可自行实现
53. if (event.preventDefault) {
54. event.preventDefault();
55. }
56. console.info(`paste:${value}`);
57. this.text = value;
58. })
59. .onTextSelectionChange((start: number, end: number) => {
60. console.info(`onTextSelectionChange start ${start}, end ${end}`);
61. })
62. .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
63. console.info(`onContentScroll offsetX ${totalOffsetX}, offsetY ${totalOffsetY}`);
64. })
65. }.width('100%').height('100%').backgroundColor('#F1F3F5')
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/2A0gfEO4TI62Ll_iEz8Y6g/zh-cn_image_0000002592220220.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=DFE2FAA74BED8D85548B8ED59776175A2CA3D53006FE8CB5C59A8E7B2D9BACC3)

### 示例17（设置最小字体范围与最大字体范围）

从API version 18开始，该示例通过[minFontScale](ts-basic-components-textarea.md#minfontscale18)、[maxFontScale](ts-basic-components-textarea.md#maxfontscale18)设置字体显示最小与最大范围。

```
1. // 开启应用缩放跟随系统
2. // AppScope/resources/base，新建文件夹profile。
3. // AppScope/resources/base/profile，新建文件configuration.json。
4. // AppScope/resources/base/profile/configuration.json，增加如下代码。
5. {
6. "configuration": {
7. "fontSizeScale": "followSystem",
8. "fontSizeMaxScale": "3.2"
9. }
10. }
```

```
1. // AppScope/app.json5，修改如下代码。
2. {
3. "app": {
4. "bundleName": "com.example.myapplication",
5. "vendor": "example",
6. "versionCode": 1000000,
7. "versionName": "1.0.0",
8. "icon": "$media:app_icon",
9. "label": "$string:app_name",
10. "configuration": "$profile:configuration"
11. }
12. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State minFontScale: number = 0.85;
6. @State maxFontScale: number = 2;

8. build() {
9. Column() {
10. Column({ space: 30 }) {
11. Text("通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。")
12. TextArea({
13. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
14. text: '通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。'
15. })
16. .minFontScale(this.minFontScale)// 设置最小字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
17. .maxFontScale(this.maxFontScale) // 设置最大字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
18. }.width('100%')
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/jhDlyl_3T62FLolras0lgQ/zh-cn_image_0000002592380154.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=737F35200C26FDC43E3223AAA4F61156B8465DA0ED5207060971C3398CB75040)

### 示例18（设置选中指定区域的文本内容）

从API version 10开始，该示例通过[setTextSelection](ts-basic-components-textarea.md#settextselection10)方法展示如何设置选中指定区域的文本内容以及菜单的显隐策略。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct TextAreaExample {
6. controller: TextAreaController = new TextAreaController();
7. @State startIndex: number = 0;
8. @State endIndex: number = 0;

10. build() {
11. Column({ space: 3 }) {
12. Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
13. TextArea({ text: 'Hello World', controller: this.controller })
14. .width('95%')
15. .height(80)
16. .margin(10)
17. .defaultFocus(true)
18. .enableKeyboardOnFocus(true)
19. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
20. this.startIndex = selectionStart;
21. this.endIndex = selectionEnd;
22. })

24. Button('setTextSelection [0,3], set menuPolicy is MenuPolicy.SHOW')
25. .onClick(() => {
26. this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9Ny8ZW5wTUadyVwP0acW5A/zh-cn_image_0000002622859663.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=350255D7398E8A3087DD3E21D176892D0985EEA882B6E0439356AC13AF6DD0F6)

### 示例19（设置文本描边）

从API version 20开始，该示例通过[strokeWidth](ts-basic-components-textarea.md#strokewidth20)和[strokeColor](ts-basic-components-textarea.md#strokecolor20)属性设置文本的描边宽度及颜色。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TextAreaExample {
7. build() {
8. Row() {
9. Column() {
10. Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

12. TextArea({ text: 'Text without stroke' })
13. .width('100%')
14. .height(60)
15. .borderWidth(1)
16. .fontSize(40)
17. TextArea({ text: 'Text with stroke' })
18. .width('100%')
19. .height(60)
20. .borderWidth(1)
21. .fontSize(40)
22. .strokeWidth(LengthMetrics.px(-3.0))
23. .strokeColor(Color.Red)
24. TextArea({ text: 'Text with stroke' })
25. .width('100%')
26. .height(60)
27. .borderWidth(1)
28. .fontSize(40)
29. .strokeWidth(LengthMetrics.px(3.0))
30. .strokeColor(Color.Red)
31. }.height('90%')
32. }
33. .width('90%')
34. .margin(10)
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/E6tBKVE0QjeHdUPrMc7JUA/zh-cn_image_0000002622699783.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=946F73ADFF69E9C2FFA97D402B22E2F139C033E9DB1C15FE17C711E95C02FC2D)

### 示例20（设置中西文自动间距）

从API version 20开始，该示例通过[enableAutoSpacing](ts-basic-components-textarea.md#enableautospacing20)属性设置中西文自动间距。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Row() {
7. Column() {
8. Text('开启中西文自动间距').margin(5)
9. TextArea({text: '中西文Auto Spacing自动间距'})
10. .enableAutoSpacing(true)
11. Text('关闭中西文自动间距').margin(5)
12. TextArea({text: '中西文Auto Spacing自动间距'})
13. .enableAutoSpacing(false)
14. }.height('100%')
15. }
16. .width('60%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/zbyoId8rSDORnnlxoZejJw/zh-cn_image_0000002592220222.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=C6612EC45926DFD73945E2C7AB70C493F59722A212CB914D5D8C4CE1A0BE579F)

### 示例21（设置最大行数）

从API version 20开始，该示例通过[maxLines](ts-basic-components-textarea.md#maxlines20)属性设置显示最大行数，超出最大行数后可滚动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Row() {
7. Column() {
8. TextArea({ text: '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20' })
9. .fontSize(50)
10. .width('50%')
11. .borderWidth(1)
12. .margin(100)
13. .textOverflow(TextOverflow.Clip)
14. .maxLines(3, { overflowMode: MaxLinesMode.SCROLL })
15. }.height('90%')
16. }
17. .width('90%')
18. .margin(10)
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/CQIOia07RfWp7NDEwMq5Dw/zh-cn_image_0000002592380156.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=58A0CAE771132301EDD63B756F0CD7FA555C51B099467D62DCAB93B3E296AE17)

### 示例22（设置最小行数）

从API version 20开始，该示例通过[minLines](ts-basic-components-textarea.md#minlines20)属性设置显示的最小行数。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'Hello World';

7. build() {
8. Row() {
9. Column() {
10. TextArea({ text: this.message })
11. .width('95%')
12. .fontSize(20)
13. .margin(10)
14. .minLines(3)
15. }
16. }
17. .width('90%')
18. .margin(10)
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/rJ0KzeqxScuOiMlOdmm0JA/zh-cn_image_0000002622859665.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=48481F9C165FBCA8FA22F12B77A2DCEE3DC0895F25380EBD8110C5655A94E20D)

### 示例23（设置字符计数颜色以及超出字符颜色）

从API version 22开始，该示例通过[showCounter](ts-basic-components-textarea.md#showcounter10)属性的counterTextColor和counterTextOverflowColor设置字符计数颜色以及超出字符颜色。

```
1. import { ColorMetrics } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct TextAreaExample {
7. @State text: string = '';
8. controller: TextAreaController = new TextAreaController();

10. build() {
11. Column() {
12. TextArea({
13. text: this.text,
14. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
15. controller: this.controller
16. })
17. .placeholderFont({ size: 16, weight: 400 })
18. .width(336)
19. .height(56)
20. .margin(20)
21. .fontSize(16)
22. .fontColor('#182431')
23. .backgroundColor('#FFFFFF')
24. .maxLength(4)
25. .showCounter(true, {
26. thresholdPercentage: 50,
27. highlightBorder: true,
28. counterTextColor: ColorMetrics.resourceColor(Color.Red),
29. counterTextOverflowColor: ColorMetrics.resourceColor(Color.Orange)
30. })
31. }.width('100%').height('100%').backgroundColor('#F1F3F5')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/wjy90Hb_RJKLL1A3NfTfKw/zh-cn_image_0000002622699785.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=225FBB1FB0625907FD5EDEB9EF740103C8CC23F32EBF5A8AFAE75802E6EE0B32)

### 示例24（设置滚动条颜色）

从API version 22开始，该示例通过[scrollBarColor](ts-basic-components-textarea.md#scrollbarcolor22)属性设置滚动条颜色。

```
1. // xxx.ets
2. import { ColorMetrics } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct Index {
6. controller: TextAreaController = new TextAreaController();
7. build() {
8. Column() {
9. TextArea({
10. text: "Hello World TextArea\nHello World TextArea\nHello World TextArea\nHello World TextArea",
11. placeholder: 'Type to text area...',
12. controller: this.controller
13. })
14. .width(336)
15. .height(56)
16. .margin({bottom:5})
17. .fontSize(16)
18. .fontColor('#182431')
19. .backgroundColor('#FFFFFF')
20. .barState(BarState.On)
21. .scrollBarColor(undefined)
22. TextArea({
23. text: "Hello World TextArea\nHello World TextArea\nHello World TextArea\nHello World TextArea",
24. placeholder: 'Type to text area...',
25. controller: this.controller
26. })
27. .width(336)
28. .height(56)
29. .margin({bottom:5})
30. .fontSize(16)
31. .fontColor('#182431')
32. .backgroundColor('#FFFFFF')
33. .barState(BarState.On)
34. .scrollBarColor(ColorMetrics.resourceColor(Color.Orange))
35. TextArea({
36. text: "Hello World TextArea\nHello World TextArea\nHello World TextArea\nHello World TextArea",
37. placeholder: 'Type to text area...',
38. controller: this.controller
39. })
40. .width(336)
41. .height(56)
42. .margin({bottom:5})
43. .fontSize(16)
44. .fontColor('#182431')
45. .backgroundColor('#FFFFFF')
46. .barState(BarState.On)
47. .scrollBarColor(ColorMetrics.rgba(255, 100, 255))
48. }
49. .backgroundColor(Color.Blue).width('100%').height('100%')
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ZbosUyxQSgOEYqVMq9tnzw/zh-cn_image_0000002592220224.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=634A03B7165786DA75D6865694A7EE37B0E5AB1D3D7D9560996786C5B8C1112A)

### 示例25（设置placeholder富文本样式）

从API version 22开始，该示例通过[setStyledPlaceholder](../输入框类组件通用接口/ts-universal-attributes-text-style.md#setstyledplaceholder22)接口设置placeholder富文本样式。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TextAreaExample {
7. styledString: MutableStyledString =
8. new MutableStyledString("段落标题\n正文第一段\n正文第二段indent 40 vp\n正文第三段textAlign居中对齐",
9. [
10. {
11. start: 0,
12. length: 4,
13. styledKey: StyledStringKey.FONT,
14. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
15. },
16. {
17. start: 5,
18. length: 5,
19. styledKey: StyledStringKey.FONT,
20. styledValue: new TextStyle({ fontColor: Color.Gray })
21. },
22. {
23. start: 11,
24. length: 1,
25. styledKey: StyledStringKey.PARAGRAPH_STYLE,
26. styledValue: new ParagraphStyle({
27. textIndent: LengthMetrics.vp(40),
28. maxLines: 1,
29. overflow: TextOverflow.Ellipsis
30. })
31. },
32. {
33. start: 29,
34. length: 1,
35. styledKey: StyledStringKey.PARAGRAPH_STYLE,
36. styledValue: new ParagraphStyle({
37. textAlign: TextAlign.Center
38. })
39. }
40. ]);
41. controller: TextAreaController = new TextAreaController();

43. aboutToAppear() {
44. this.controller.setStyledPlaceholder(this.styledString)
45. }

47. build() {
48. Scroll() {
49. Column() {
50. Text("TextArea placeholder富文本")
51. .fontSize(8)
52. TextArea({ controller: this.controller })
53. .width(200)
54. .fontSize(24)
55. .margin(10)
56. }
57. .width('100%')
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/V0Dwq_m5QJKQbxzQVYR_rA/zh-cn_image_0000002592380158.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=672414DB93CE78FC4A085B3F33AD1FBA50F991A75B52D1FC3B06C2604884A616)

### 示例26（设置输入法扩展信息）

从API version 22开始，该示例通过[IMEClient](../文本组件公共接口/ts-text-common.md#imeclient20对象说明)的setExtraConfig设置输入法扩展信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. build() {
6. Column() {
7. TextArea({ text: '拉起输入法前执行onWillAttachIME回调' })
8. .onWillAttachIME((client: IMEClient) => {
9. client.setExtraConfig({
10. customSettings: {
11. name: "TextArea", // 自定义属性
12. id: client.nodeId // 自定义属性
13. }
14. })
15. })
16. }.height('100%')
17. }
18. }
```

### 示例27（设置行首标点压缩）

该示例通过[compressLeadingPunctuation](ts-basic-components-textarea.md#compressleadingpunctuation23)接口设置行首标点压缩，左侧有间距的标点符号位于行首时，标点会直接压缩间距至左侧边界。

从API version 23开始，支持compressLeadingPunctuation接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column(){
7. TextArea({ text: "\u300C行首标点压缩打开" })
8. .compressLeadingPunctuation(true)
9. .margin(5)
10. .fontSize(30)
11. .width("90%")
12. TextArea({ text: "\u300C行首标点压缩关闭" })
13. .compressLeadingPunctuation(false)
14. .fontSize(30)
15. .width("90%")
16. }
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Asf_uUDaQBe2gzrJbD652A/zh-cn_image_0000002622859667.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=8D9445E5E105DA00CD5568529F358E2178864FA12C213F972268855FA75ED5A2)

### 示例28（设置自适应间距）

该示例通过[includeFontPadding](ts-basic-components-textarea.md#includefontpadding23)接口增加首行尾行间距和[fallbackLineSpacing](ts-basic-components-textarea.md#fallbacklinespacing23)接口设置自适应行间距。

从API version 23开始，新增[includeFontPadding](ts-basic-components-textarea.md#includefontpadding23)和[fallbackLineSpacing](ts-basic-components-textarea.md#fallbacklinespacing23)接口。

```
1. // xxx.ets

3. const UYGHUR_TEXT: string = 'ياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەن';
4. @Entry
5. @Component
6. struct Index {
7. @State include: boolean | null | undefined = false;
8. @State fallback: boolean | null | undefined = false;
9. @State displayText: string = UYGHUR_TEXT;

11. build() {
12. Column() {
13. TextArea({
14. text: this.displayText,
15. placeholder: '请输入内容...'
16. })
17. .includeFontPadding(this.include)
18. .fallbackLineSpacing(this.fallback)
19. .lineHeight(5)
20. .width('100%')
21. .height(100)
22. .backgroundColor('#eee')
23. .borderWidth(1)
24. .borderColor('#dddddd')

26. Scroll() {
27. Column() {
28. // --- IncludeFontPadding相关按钮 ---
29. Button('设置includePadding: ' + this.include)
30. .onClick(() => {
31. this.include = this.include === false ? true : false;
32. })
33. .margin({ bottom: 10 })

35. // --- FallbackLineSpacing相关按钮 ---
36. Button('设置fallbackLineSpacing: ' + this.fallback)
37. .onClick(() => {
38. this.fallback = this.fallback === false ? true : false;
39. })
40. .margin({ bottom: 10 })

42. }
43. .width('100%')
44. .padding(5)
45. }
46. .height(250)
47. .backgroundColor('transparent')
48. .scrollBarWidth(2)
49. .scrollBarColor('#888')

51. }
52. .width('100%')
53. .height('100%')
54. .padding(20)
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xFpTcHOESiKTl9qi331ffg/zh-cn_image_0000002622699787.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=91DC2807F9A4DBB77A890A3CDD255A2E59BE3F77CE3480E01BE1AE120047EB73)

### 示例29（设置文本拖拽时的背板样式）

该示例通过[selectedDragPreviewStyle](ts-basic-components-textarea.md#selecteddragpreviewstyle23)接口设置文本拖拽时的背板样式。

从API version 23开始，新增selectedDragPreviewStyle接口。

```
1. @Entry
2. @Component
3. struct TextAreaTest {
4. build() {
5. Column() {
6. TextArea({ text: 'HelloWorld', placeholder: 'please input words' })
7. .copyOption(CopyOptions.InApp)
8. .width(200)
9. .height(50)
10. .margin(150)
11. .draggable(true)
12. .selectedDragPreviewStyle({color: 'rgba(227, 248, 249, 1)'})
13. }
14. .height('100%')
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/dpOdWCXySQmRYdOmIoErVQ/zh-cn_image_0000002592220226.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=4E286045F61FB3A3C982AEEAF50F29ADF3E0C13D1C164C99FE9698724A614465)

### 示例30（删除文本框内的最后一个字符）

该示例通过调用[deleteBackward](../输入框类组件通用接口/ts-universal-attributes-text-style.md#deletebackward23)接口删除文本框内最后一个字符。

从API version 23开始，新增[deleteBackward](../输入框类组件通用接口/ts-universal-attributes-text-style.md#deletebackward23)接口。

```
1. @Entry
2. @Component
3. struct Page {
4. controller: TextAreaController = new TextAreaController();

6. build() {
7. Column() {
8. TextArea({ text: 'TextArea输入框Deletebackward示例', controller: this.controller })
9. Button('Delete backward')
10. .onClick(() => {
11. this.controller.deleteBackward();
12. })
13. }
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/fwDptul2Rq-Zf5TzXEXMHw/zh-cn_image_0000002592380160.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=CEA91A9AB269DFBC34782252379756C9EDD2B31F66A9546DA4ECFF79BC7D2811)

### 示例31（设置文本排版方向）

该示例通过[textDirection](ts-basic-components-textarea.md#textdirection23)接口设置文本排版方向。

从API version 23开始，新增textDirection接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = 'TextArea文本排版方向示例';

7. build() {
8. Column() {
9. Text('TextArea文本排版方向RTL，布局方向default')
10. .fontSize(12).width('90%')
11. TextArea({ text: this.text })
12. .width(336)
13. .height(56)
14. .margin(10)
15. .fontSize(16)
16. .textDirection(TextDirection.RTL)
17. .showCounter(true)
18. .maxLength(50)
19. Text('TextArea文本排版方向RTL，布局方向default，文本水平方向对齐方式LEFT')
20. .fontSize(12).width('90%')
21. TextArea({ text: this.text })
22. .width(336)
23. .height(56)
24. .margin(10)
25. .fontSize(16)
26. .textDirection(TextDirection.RTL)
27. .textAlign(TextAlign.LEFT)
28. .showCounter(true)
29. .maxLength(50)
30. Text('TextArea文本排版方向LTR，布局方向Rtl')
31. .fontSize(12).width('90%')
32. TextArea({ text: this.text })
33. .width(336)
34. .height(56)
35. .margin(10)
36. .fontSize(16)
37. .textDirection(TextDirection.LTR)
38. .direction(Direction.Rtl)
39. .maxLength(50)
40. .showCounter(true)
41. }.width('100%').height('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/jws4VZfvRUS8MBfrFfU1-w/zh-cn_image_0000002622859669.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=3431B3686BE11E0C4B97D1E34B745F65FF3CBF3CBF7386CA6316D50BFE490DA0)

### 示例32（将指定范围的文字滚动到可视区内）

本示例通过[scrollToVisible](../输入框类组件通用接口/ts-universal-attributes-text-style.md#scrolltovisible23)将可视区外的文本滚动到可视区内。

从API version 23开始，新增scrollToVisible接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextAreaExample {
5. @State text: string = '12345678913456789123456789123456789123456789123456789123456789123456789123456789123';
6. controller: TextAreaController = new TextAreaController();

8. build() {
9. Column() {
10. TextArea({ text: this.text, controller: this.controller })
11. .width(336)
12. .height(150)
13. Button("滚动文本到可视区").onClick(() => {
14. this.controller.scrollToVisible({ start: 110, end: 115 })
15. })
16. }.width('100%').height('100%').backgroundColor('#F1F3F5')
17. }

19. aboutToAppear(): void {
20. for (let i = 0; i < 5; i++) {
21. this.text += this.text
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZaI93JEETB69lSz3-40dkw/zh-cn_image_0000002622699789.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=29235124C00555F9118D5967B019AC9C90C90BDFAE6E3108F74E52E67B5110CB)

### 示例33（设置水平滚动）

本示例通过[horizontalScrolling](ts-basic-components-textarea.md#horizontalscrolling24)设置水平滚动。

从API version 24开始，新增horizontalScrolling接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = `Hello World Hello World Hello World Hello World Hello World\n
6. Hello World Hello World Hello World Hello World Hello World\n
7. Hello World Hello World Hello World Hello World Hello World\n
8. Hello World Hello World Hello World Hello World Hello World\n
9. Hello World Hello World Hello World Hello World Hello World\n
10. Hello World Hello World Hello World Hello World Hello World\n
11. Hello World Hello World Hello World Hello World Hello World\n
12. Hello World Hello World Hello World Hello World Hello World\n
13. `

15. build() {
16. Column() {
17. TextArea({ text: this.message })
18. .horizontalScrolling(true)
19. .width('200vp')
20. .height('150vp')
21. }
22. .height('100%')
23. .width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fccWHJX4Tb6AwhgSxvHTmA/zh-cn_image_0000002592220228.png?HW-CC-KV=V1&HW-CC-Date=20260611T074712Z&HW-CC-Expire=86400&HW-CC-Sign=DE186A20891A4F9598F005E0ACB261A5B266A5E80C9526C7B2E483ECFBF5135B)
