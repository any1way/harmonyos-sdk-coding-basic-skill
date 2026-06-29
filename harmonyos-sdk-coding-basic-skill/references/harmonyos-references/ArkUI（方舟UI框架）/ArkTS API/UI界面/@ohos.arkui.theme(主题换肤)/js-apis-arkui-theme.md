---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme
title: @ohos.arkui.theme(主题换肤)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.theme(主题换肤)
category: harmonyos-references
scraped_at: 2026-06-11T15:41:44+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:4bf134cecdaeba3880426bd13314fde465603be82ec5d347e351e4bfc5ee5272
---
支持自定义主题风格，实现App组件风格跟随Theme切换。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

## Theme

PhonePC/2in1TabletTVWearable

当前生效的主题风格对象，可从[onWillApplyTheme](../../../ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [Colors](js-apis-arkui-theme.md#colors) | 否 | 否 | 主题颜色资源。 |

## Colors

PhonePC/2in1TabletTVWearable

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

颜色对应的组件可参考[文本色与图标色](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164#section137153164914)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 品牌色。  **影响组件：** [TextInput](../../../ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、[Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md) |
| warning | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级警示色。  **影响组件：** [TipsDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#tipsdialog>)、[AlertDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#alertdialog>)、[CustomContentDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#customcontentdialog12>)、  [Badge](../../../ArkTS组件/信息展示/Badge/ts-container-badge.md)、[Button](../../../ArkTS组件/按钮与选择/Button/ts-basic-components-button.md) |
| alert | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级提示色。  **影响组件：** 暂无组件使用。 |
| confirm | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 确认色。  **影响组件：** 暂无组件使用。 |
| fontPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级文本字体颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[LoadingDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#loadingdialog>)、[TipsDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#tipsdialog>)、  [ConfirmDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#confirmdialog>)、[AlertDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#alertdialog>)、[SelectDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#selectdialog>)、  [CustomContentDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#customcontentdialog12>)、[Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)、[Text](../../../ArkTS组件/文本与输入/Text/ts-basic-components-text.md)、  [SubHeader](../../../ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md)、[ProgressButton](../../../ArkTS组件/系统预置UI组件库/ProgressButton/ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](../../../ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、  [Popup](../../../ArkTS组件/系统预置UI组件库/Popup/ohos-arkui-advanced-popup.md)、[Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、  [ToolBar](../../../ArkTS组件/系统预置UI组件库/ToolBar/ohos-arkui-advanced-toolbar.md)、[Menu](../../../ArkTS组件/菜单/Menu/ts-basic-components-menu.md)、[TextInput](../../../ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、  [Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md)、[Counter](../../../ArkTS组件/信息展示/Counter/ts-container-counter.md)、[TimePicker](../../../ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md)、[DatePicker](../../../ArkTS组件/按钮与选择/DatePicker/ts-basic-components-datepicker.md)、  [TextPicker](../../../ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md)、[ComposeListItem](../../../ArkTS组件/系统预置UI组件库/ComposeListItem/ohos-arkui-advanced-composelistitem.md)、[TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| fontSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级文本字体颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[AlertDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#alertdialog>)、[CustomContentDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#customcontentdialog12>)、  [SubHeader](../../../ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md)、[AlphabetIndexer](../../../ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、[Popup](../../../ArkTS组件/系统预置UI组件库/Popup/ohos-arkui-advanced-popup.md)、  [TextInput](../../../ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、[Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md)、[ComposeListItem](../../../ArkTS组件/系统预置UI组件库/ComposeListItem/ohos-arkui-advanced-composelistitem.md)、  [TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md)、[TextClock](../../../ArkTS组件/信息展示/TextClock/ts-basic-components-textclock.md)。 |
| fontTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级文本字体颜色。  **影响组件：** [ComposeListItem](../../../ArkTS组件/系统预置UI组件库/ComposeListItem/ohos-arkui-advanced-composelistitem.md) |
| fontFourth | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 四级文本字体颜色。  **影响组件：** 暂无组件使用。 |
| fontEmphasize | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 高亮字体颜色。  **影响组件：** [TipsDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#tipsdialog>)、[ConfirmDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#confirmdialog>)、[AlertDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#alertdialog>)、  [SelectDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#selectdialog>)、[CustomContentDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#customcontentdialog12>)、[SubHeader](../../../ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md)、  [AlphabetIndexer](../../../ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、[Popup](../../../ArkTS组件/系统预置UI组件库/Popup/ohos-arkui-advanced-popup.md)、[Button](../../../ArkTS组件/按钮与选择/Button/ts-basic-components-button.md)、  [Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[ToolBar](../../../ArkTS组件/系统预置UI组件库/ToolBar/ohos-arkui-advanced-toolbar.md)、[Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md)、  [TimePicker](../../../ArkTS组件/按钮与选择/TimePicker/ts-basic-components-timepicker.md)、[DatePicker](../../../ArkTS组件/按钮与选择/DatePicker/ts-basic-components-datepicker.md)、[TextPicker](../../../ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md) |
| fontOnPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级文本反转颜色，用于彩色背景。  **影响组件：** [Badge](../../../ArkTS组件/信息展示/Badge/ts-container-badge.md)、[Button](../../../ArkTS组件/按钮与选择/Button/ts-basic-components-button.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md) |
| fontOnSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| fontOnTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| fontOnFourth | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 四级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| iconPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级图标颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)、[ToolBar](../../../ArkTS组件/系统预置UI组件库/ToolBar/ohos-arkui-advanced-toolbar.md)、  [TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| iconSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级图标颜色。  **影响组件：** [LoadingDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#loadingdialog>)、[SubHeader](../../../ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md)、[LoadingProgress](../../../ArkTS组件/信息展示/LoadingProgress/ts-basic-components-loadingprogress.md)、  [Popup](../../../ArkTS组件/系统预置UI组件库/Popup/ohos-arkui-advanced-popup.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md)、  [TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| iconTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级图标颜色。  **影响组件：** [SubHeader](../../../ArkTS组件/系统预置UI组件库/SubHeader/ohos-arkui-advanced-subheader.md) |
| iconFourth | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 四级图标颜色。  **影响组件：** [Checkbox](../../../ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md)、[CheckboxGroup](../../../ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md)、[Radio](../../../ArkTS组件/按钮与选择/Radio/ts-basic-components-radio.md) |
| iconEmphasize | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 高亮图标颜色。  **影响组件：** [ToolBar](../../../ArkTS组件/系统预置UI组件库/ToolBar/ohos-arkui-advanced-toolbar.md) |
| iconSubEmphasize | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 高亮辅助图标颜色。  **影响组件：** 暂无组件使用。 |
| iconOnPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级图标反转颜色，用于彩色背景。  **影响组件：** [Checkbox](../../../ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md)、[CheckboxGroup](../../../ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md)、[Radio](../../../ArkTS组件/按钮与选择/Radio/ts-basic-components-radio.md) |
| iconOnSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级图标反转颜色，用于彩色背景。  **影响组件：** [Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md) |
| iconOnTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级图标反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| iconOnFourth | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 四级图标反转颜色，用于彩色背景。  **影响组件：** [ProgressButton](../../../ArkTS组件/系统预置UI组件库/ProgressButton/ohos-arkui-advanced-progressbutton.md) |
| backgroundPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 一级背景颜色（实色，不透明）。  **影响组件：** [TextInput](../../../ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、[QRCode](../../../ArkTS组件/信息展示/QRCode/ts-basic-components-qrcode.md) |
| backgroundSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundFourth | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 四级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundEmphasize | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 高亮背景颜色（实色，不透明）。  **影响组件：** [Progress](../../../ArkTS组件/信息展示/Progress/ts-basic-components-progress.md)、[Button](../../../ArkTS组件/按钮与选择/Button/ts-basic-components-button.md)、[Slider](../../../ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md) |
| compForegroundPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 前背景。  **影响组件：** [QRCode](../../../ArkTS组件/信息展示/QRCode/ts-basic-components-qrcode.md) |
| compBackgroundPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 白色背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundPrimaryTran | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 白色透明背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundPrimaryContrary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 常亮背景。  **影响组件：** [Toggle](../../../ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md)、[Slider](../../../ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md) |
| compBackgroundGray | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 灰色背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 二级背景。  **影响组件：** [Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)、[Slider](../../../ArkTS组件/按钮与选择/Slider/ts-basic-components-slider.md) |
| compBackgroundTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 三级背景。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[Progress](../../../ArkTS组件/信息展示/Progress/ts-basic-components-progress.md)、[AlphabetIndexer](../../../ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、  [Button](../../../ArkTS组件/按钮与选择/Button/ts-basic-components-button.md)、[Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Toggle](../../../ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md)、  [Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[TextInput](../../../ArkTS组件/文本与输入/TextInput/ts-basic-components-textinput.md)、[Search](../../../ArkTS组件/文本与输入/Search/ts-basic-components-search.md) |
| compBackgroundEmphasize | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 高亮背景。  **影响组件：** [Swiper](../../../ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)、[Toggle](../../../ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、  [Checkbox](../../../ArkTS组件/按钮与选择/Checkbox/ts-basic-components-checkbox.md)、[CheckboxGroup](../../../ArkTS组件/按钮与选择/CheckboxGroup/ts-basic-components-checkboxgroup.md)、[Radio](../../../ArkTS组件/按钮与选择/Radio/ts-basic-components-radio.md) |
| compBackgroundNeutral | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 黑色中性高亮背景颜色。  **影响组件：** [PatternLock](../../../ArkTS组件/信息展示/PatternLock/ts-basic-components-patternlock.md) |
| compEmphasizeSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 20%高亮背景颜色。  **影响组件：** [Progress](../../../ArkTS组件/信息展示/Progress/ts-basic-components-progress.md)、[ProgressButton](../../../ArkTS组件/系统预置UI组件库/ProgressButton/ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](../../../ArkTS组件/信息展示/AlphabetIndexer/ts-container-alphabet-indexer.md)、  [Select](../../../ArkTS组件/按钮与选择/Select/ts-basic-components-select.md)、[Toggle](../../../ArkTS组件/按钮与选择/Toggle/ts-basic-components-toggle.md) |
| compEmphasizeTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 10%高亮背景颜色。  **影响组件：** 暂无组件使用。 |
| compDivider | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用分割线颜色。  **影响组件：** [SelectDialog](<../../../ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md#selectdialog>)、[PatternLock](../../../ArkTS组件/信息展示/PatternLock/ts-basic-components-patternlock.md)、[Divider](../../../ArkTS组件/空白与分隔/Divider/ts-basic-components-divider.md) |
| compCommonContrary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用反转颜色。  **影响组件：** 暂无组件使用。 |
| compBackgroundFocus | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 获焦态背景颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedPrimary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 获焦态一级反转颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedSecondary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 获焦态二级反转颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedTertiary | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 获焦态三级反转颜色。  **影响组件：** [Scroll](../../../ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md) |
| interactiveHover | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用悬停交互式颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| interactivePressed | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用按压交互式颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| interactiveFocus | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用获焦交互式颜色。  **影响组件：** [EditableTitleBar](../../../ArkTS组件/系统预置UI组件库/EditableTitleBar/ohos-arkui-advanced-editabletitlebar.md)、[Chip](../../../ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| interactiveActive | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用激活交互式颜色。  **影响组件：** [TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| interactiveSelect | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用选择交互式颜色。  **影响组件：** [TreeView](../../../ArkTS组件/系统预置UI组件库/TreeView/ohos-arkui-advanced-treeview.md) |
| interactiveClick | [ResourceColor](../../../ArkTS组件/公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 否 | 通用点击交互式颜色。  **影响组件：** 暂无组件使用。 |

## CustomTheme

PhonePC/2in1TabletTVWearable

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义浅色主题颜色资源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| darkColors20+ | [CustomDarkColors](js-apis-arkui-theme.md#customdarkcolors20) | 否 | 是 | 自定义深色主题颜色资源。  **说明**：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## CustomColors

PhonePC/2in1TabletTVWearable

type CustomColors = Partial<Colors>

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义主题颜色资源类型。 |

## CustomDarkColors20+

PhonePC/2in1TabletTVWearable

type CustomDarkColors = Partial<Colors>

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义深色主题颜色资源类型。 |

## ThemeControl

PhonePC/2in1TabletTVWearable

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setDefaultTheme

PhonePC/2in1TabletTVWearable

setDefaultTheme(theme: [CustomTheme](js-apis-arkui-theme.md#customtheme)): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](<../../窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#loadcontent9>)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/主题设置/设置应用内主题换肤/theme_skinning.md#设置应用内组件自定义主题色>)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 是 | 表示设置的自定义主题风格。 |

**示例**

```
1. import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
2. // 自定义主题颜色
3. class BlueColors implements CustomColors {
4. fontPrimary = "#FF707070";
5. backgroundPrimary = "#FF2787D9";
6. brand = "#FFEEAAFF"; // 品牌色
7. }

9. class PageCustomTheme implements CustomTheme {
10. colors?: CustomColors;

12. constructor(colors: CustomColors) {
13. this.colors = colors;
14. }
15. }
16. // 创建实例
17. const BlueColorsTheme = new PageCustomTheme(new BlueColors());
18. // 在页面build之前执行ThemeControl.setDefaultTheme，设置App默认样式风格为BlueColorsTheme。
19. ThemeControl.setDefaultTheme(BlueColorsTheme);

21. @Entry
22. @Component
23. struct Index {

25. build() {
26. Row() {
27. Column() {
28. // 文本颜色应用fontPrimary
29. Text('这是一段文本')
30. .fontSize(30)
31. .fontWeight(FontWeight.Bold)
32. .margin('5%')
33. // 二维码背景色应用backgroundPrimary
34. QRCode('Hello')
35. .width(100)
36. .height(100)
37. // 输入框光标颜色应用brand
38. TextInput({placeholder: 'input your word...'})
39. .width('80%')
40. .height(40)
41. .margin(20)
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/JF2DHR2QTu61QpXZ4S5NAw/zh-cn_image_0000002592219868.png?HW-CC-KV=V1&HW-CC-Date=20260611T074142Z&HW-CC-Expire=86400&HW-CC-Sign=E16F9DE227CE03C6099E3A28CB6304B0A8426EDB9378D8B9628EC5199D01A600)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/5JVbt0ocT4eaaYjriyEHfA/zh-cn_image_0000002592379802.png?HW-CC-KV=V1&HW-CC-Date=20260611T074142Z&HW-CC-Expire=86400&HW-CC-Sign=EDB415AB2F927F7873BD8C0619671D15FD3AF8455338E9AAFAB94752655CE942)
