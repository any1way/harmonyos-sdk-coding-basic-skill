---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common
title: 选择器（Picker）公共接口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > 选择器（Picker）公共接口
category: harmonyos-references
scraped_at: 2026-06-01T15:42:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14cad00fde95f9987d9b763a183b3d0e3ef6418f741e89025657db92cd792c6b
---
选择器组件公共接口。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## PickerTextStyle对象说明

PhonePC/2in1TabletTVWearable

选择器组件的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。 |
| font | [Font](../../公共定义/基础类型定义/ts-types.md#font) | 否 | 是 | 文本样式。 |

## PickerDialogButtonStyle12+对象说明

PhonePC/2in1TabletTVWearable

选择器弹窗的按钮样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ButtonType](../Button/ts-basic-components-button.md#buttontype枚举说明) | 否 | 是 | 按钮显示样式。 |
| style | [ButtonStyleMode](../Button/ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式和重要程度。 |
| role | [ButtonRole](../Button/ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | Button组件的角色。 |
| fontSize | [Length](../../公共定义/基础类型定义/ts-types.md#length) | 否 | 是 | 文本显示字号。 |
| fontColor | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 文本显示颜色。 |
| fontWeight | [FontWeight](../../公共定义/枚举说明/ts-appendix-enums.md#fontweight) | number | string | 否 | 是 | 文本的字体粗细。number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"200"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 |
| fontStyle | [FontStyle](../../公共定义/枚举说明/ts-appendix-enums.md#fontstyle) | 否 | 是 | 文本的字体样式。 |
| fontFamily | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | string | 否 | 是 | 字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和[注册自定义字体](<../../../ArkTS API/UI界面/@ohos.font (注册自定义字体)/js-apis-font.md>)。 |
| backgroundColor | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 按钮背景色。 |
| borderRadius | [Length](../../公共定义/基础类型定义/ts-types.md#length) | [BorderRadiuses](../../公共定义/基础类型定义/ts-types.md#borderradiuses9) | 否 | 是 | 圆角半径。 |
| primary | boolean | 否 | 是 | 弹出弹窗后，未使用Tab键切换焦点时，Enter键是否默认由该按钮响应。  true：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键会触发该按钮绑定的事件。  false：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键不会触发该按钮绑定的事件。  默认值：false |

## DateRange19+对象说明

PhonePC/2in1TabletTVWearable

日期区间，用于描述起止日期区间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | Date | 否 | 是 | 设置日期区间的开始日期。 |
| end | Date | 否 | 是 | 设置日期区间的结束日期。 |
