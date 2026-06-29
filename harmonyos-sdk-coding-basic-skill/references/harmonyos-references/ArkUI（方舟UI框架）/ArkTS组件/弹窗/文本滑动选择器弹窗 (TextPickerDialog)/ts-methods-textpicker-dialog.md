---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-textpicker-dialog
title: 文本滑动选择器弹窗 (TextPickerDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 文本滑动选择器弹窗 (TextPickerDialog)
category: harmonyos-references
scraped_at: 2026-06-11T15:49:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e02eb07f14dceac0b9aa650b9cfbcfb04309c1a82316019ea1d57ab1d066ef57
---
根据指定的选择范围创建文本选择器，展示在弹窗上。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI系统场景化能力/使用UI上下文接口操作界面（UIContext）/arkts-global-interface.md#ui上下文不明确>)的地方使用，参见[UIContext](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)说明。
* 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。

## TextPickerDialog

PhonePC/2in1TabletTVWearable

### show(deprecated)

PhonePC/2in1TabletTVWearable

static show(options?: TextPickerDialogOptions)

定义文本滑动选择器弹窗并弹出。

说明

从API version 8开始支持，从API version 18开始废弃，建议使用[showTextPickerDialog](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#showtextpickerdialog>)替代。showTextPickerDialog需先获取[UIContext](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)中的[showTextPickerDialog](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#showtextpickerdialog>)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextPickerDialogOptions](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明) | 否 | 配置文本选择器弹窗的参数。 |

## TextPickerDialogOptions对象说明

PhonePC/2in1TabletTVWearable

文本选择器弹窗的参数继承自[TextPickerOptions](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultPickerItemHeight | number | string | 否 | 是 | 设置选择器中选项的高度。number类型取值范围：[0, +∞)，string类型仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。设置该参数后，选中项与非选中项的高度均为所设置的值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| disappearTextStyle10+ | [PickerTextStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle10+ | [PickerTextStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedTextStyle10+ | [PickerTextStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| canLoop10+ | boolean | 否 | 是 | 设置是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](<../警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md#dialogalignment枚举说明>) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](../../公共定义/基础类型定义/ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](<../警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md#rectangle8类型说明>) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAccept | (value: [TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)) => void | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | () => void | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | (value: [TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)) => void | 否 | 是 | 滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调。  回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用onEnterSelectedArea接口。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onScrollStop14+ | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 滑动弹窗中的选择器的选择列停止时，触发该回调。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | () => void | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | () => void | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | () => void | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | () => void | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](../../通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 设置悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| disableTextStyleAnimation15+ | boolean | 否 | 是 | 设置是否关闭滑动过程中文本样式变化的动效。  - true：关闭文本样式变化动效。  - false：不关闭文本样式变化动效。  默认值：false  **说明：**  设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为defaultTextStyle属性设置的样式。如未设置defaultTextStyle，则显示为[Text](../../文本与输入/Text/ts-basic-components-text.md)组件默认样式。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| defaultTextStyle15+ | [TextPickerTextStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 否 | 是 | 设置关闭滑动过程中文本样式变化动效时的各个选项的文本样式，仅当disableTextStyleAnimation为true时生效。  默认值：与[Text](../../文本与输入/Text/ts-basic-components-text.md)组件默认值相同。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| onEnterSelectedArea18+ | Callback<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。  **说明：**  在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  **元服务API**： 从API version 18开始，该接口支持在元服务中使用。  **说明**：  1. 设置为true后，其生效情况取决于系统的硬件是否支持。  2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |
| selectedBackgroundStyle20+ | [PickerBackgroundStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#pickerbackgroundstyle20) | 否 | 是 | 设置选中项背景样式。  默认值：  {  color: $r('sys.color.comp\_background\_tertiary'),  borderRadius: $r('sys.float.corner\_radius\_level12')  }  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## TextPickerDialogOptionsExt20+对象说明

PhonePC/2in1TabletTVWearable

文本选择器弹窗的参数继承自[TextPickerOptions](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickeroptions对象说明)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultPickerItemHeight | number | string | 否 | 是 | 设置选择器中选项的高度。number类型取值范围：[0, +∞)，string类型仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。设置该参数后，选中项与非选中项的高度均为所设置的值。 |
| acceptButtonStyle | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)。 |
| cancelButtonStyle | [PickerDialogButtonStyle](../../按钮与选择/选择器（Picker）公共接口/ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](../../按钮与选择/Button/ts-basic-components-button.md#buttontype枚举说明)。 |
| canLoop | boolean | 否 | 是 | 设置是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true |
| alignment | [DialogAlignment](<../警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md#dialogalignment枚举说明>) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default |
| offset | [Offset](../../公共定义/基础类型定义/ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 } |
| maskRect | [Rectangle](<../警告弹窗 (AlertDialog)/ts-methods-alert-dialog-box.md#rectangle8类型说明>) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' } |
| onAccept | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。 |
| onCancel | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。 |
| onChange | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调。  回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用onEnterSelectedArea接口。 |
| onScrollStop | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 滑动弹窗中的选择器的选择列停止时，触发该回调。 |
| backgroundColor | [ResourceColor](../../公共定义/基础类型定义/ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。 |
| backgroundBlurStyle | [BlurStyle](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。 |
| backgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundEffect | [BackgroundEffectOptions](../../通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。 |
| onDidAppear | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。 |
| onDidDisappear | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。 |
| onWillAppear | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 |
| onWillDisappear | [VoidCallback](../../公共定义/基础类型定义/ts-types.md#voidcallback12) | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 |
| shadow | [ShadowOptions](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](../../通用属性/视效与模糊/图像效果/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM |
| enableHoverMode | boolean | 否 | 是 | 是否响应悬停态。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false |
| hoverModeArea | [HoverModeAreaType](../../通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 设置悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN |
| disableTextStyleAnimation | boolean | 否 | 是 | 设置是否关闭滑动过程中文本样式变化的动效。  - true：关闭文本样式变化动效。  - false：不关闭文本样式变化动效。  默认值：false  **说明：**  设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为defaultTextStyle属性设置的样式。如未设置defaultTextStyle，则显示为[Text](../../文本与输入/Text/ts-basic-components-text.md)组件默认样式。 |
| defaultTextStyle | [TextPickerTextStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 否 | 是 | 设置关闭滑动过程中文本样式变化动效时的各个选项的文本样式，仅当disableTextStyleAnimation为true时生效。  默认值：与[Text](../../文本与输入/Text/ts-basic-components-text.md)组件默认值相同。 |
| onEnterSelectedArea | [Callback](../../公共定义/基础类型定义/ts-types.md#callback12)<[TextPickerResult](ts-methods-textpicker-dialog.md#textpickerresult对象说明)> | 否 | 是 | 滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。  **说明：**  在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。 |
| enableHapticFeedback | boolean | 否 | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  **说明**：  1. 设置为true后，其生效情况取决于系统的硬件是否支持。  2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |
| selectedBackgroundStyle | [PickerBackgroundStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#pickerbackgroundstyle20) | 否 | 是 | 设置选中项背景样式。  默认值：  {  color: $r('sys.color.comp\_background\_tertiary'),  borderRadius: $r('sys.float.corner\_radius\_level12')  } |
| disappearTextStyle | [TextPickerTextStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.CLIP  } |
| textStyle | [TextPickerTextStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.CLIP  } |
| selectedTextStyle | [TextPickerTextStyle](../../按钮与选择/TextPicker/ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.CLIP  } |

## TextPickerResult对象说明

PhonePC/2in1TabletTVWearable

文本选择器结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | string []10+ | 否 | 否 | 选中项的文本内容。  **说明**：当显示文本或图片加文本列表时，value值为选中项中的文本值。（文本选择器显示多列时，value为数组类型。）  当显示图片列表时，value值为空。  value值不支持包含转义字符'\'。 |
| index | number | number []10+ | 否 | 否 | 选中项在选择范围数组中的索引值，索引从0开始。（文本选择器显示多列时，index为数组类型。） |

## 示例

PhonePC/2in1TabletTVWearable

说明

推荐通过使用[UIContext](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)中的[showTextPickerDialog](<../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#showtextpickerdialog>)来明确UI的执行上下文。

### 示例1（弹出文本选择弹窗）

该示例通过点击按钮弹出文本选择弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. value: this.selectedValue,
19. defaultPickerItemHeight: 40,
20. onAccept: (value: TextPickerResult) => {
21. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
22. this.select = value.index;
23. console.info(this.select + '');
24. // 点击确定后，被选到的文本数据展示到页面
25. this.selectedValue = value.value as string;
26. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
27. },
28. onCancel: () => {
29. console.info('TextPickerDialog:onCancel()');
30. },
31. onChange: (value: TextPickerResult) => {
32. console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
33. },
34. onScrollStop: (value: TextPickerResult) => {
35. console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
36. },
37. onDidAppear: () => {
38. console.info('TextPickerDialog:onDidAppear()');
39. },
40. onDidDisappear: () => {
41. console.info('TextPickerDialog:onDidDisappear()');
42. },
43. onWillAppear: () => {
44. console.info('TextPickerDialog:onWillAppear()');
45. },
46. onWillDisappear: () => {
47. console.info('TextPickerDialog:onWillDisappear()');
48. }
49. });
50. })
51. }.width('100%')
52. }.height('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/az71pdCBRXSosiLxw2uFkA/zh-cn_image_0000002592220534.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=D95D3FD07BC30DC8B182391C629E514822477301C2AA4760CF56961D92D3C4FA)

### 示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本和按钮样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. disappearTextStyle: { color: '#297bec', font: { size: 15, weight: FontWeight.Lighter } },
19. textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
20. selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
21. acceptButtonStyle: {
22. type: ButtonType.Normal,
23. style: ButtonStyleMode.NORMAL,
24. role: ButtonRole.NORMAL,
25. fontColor: 'rgb(81, 81, 216)',
26. fontSize: '26fp',
27. fontWeight: FontWeight.Bolder,
28. fontStyle: FontStyle.Normal,
29. fontFamily: 'sans-serif',
30. backgroundColor: '#A6ACAF',
31. borderRadius: 20
32. },
33. cancelButtonStyle: {
34. type: ButtonType.Normal,
35. style: ButtonStyleMode.NORMAL,
36. role: ButtonRole.NORMAL,
37. fontColor: Color.Blue,
38. fontSize: '16fp',
39. fontWeight: FontWeight.Normal,
40. fontStyle: FontStyle.Italic,
41. fontFamily: 'sans-serif',
42. backgroundColor: '#50182431',
43. borderRadius: 10
44. },
45. onAccept: (value: TextPickerResult) => {
46. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
47. this.select = value.index;
48. console.info(this.select + '');
49. // 点击确定后，被选到的文本数据展示到页面
50. this.selectedValue = value.value as string;
51. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
52. },
53. onCancel: () => {
54. console.info('TextPickerDialog:onCancel()');
55. },
56. onChange: (value: TextPickerResult) => {
57. console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
58. },
59. onScrollStop: (value: TextPickerResult) => {
60. console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
61. },
62. onDidAppear: () => {
63. console.info('TextPickerDialog:onDidAppear()');
64. },
65. onDidDisappear: () => {
66. console.info('TextPickerDialog:onDidDisappear()');
67. },
68. onWillAppear: () => {
69. console.info('TextPickerDialog:onWillAppear()');
70. },
71. onWillDisappear: () => {
72. console.info('TextPickerDialog:onWillDisappear()');
73. }
74. });
75. })
76. }.width('100%')
77. }.height('100%')
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/7SsQajirSXK6M--qwQzivg/zh-cn_image_0000002592380466.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=5EC30D5A9111E370472085DE916BD983F3278E88DD194069743E397F4AE9FB4B)

### 示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. @Entry
2. @Component
3. struct TextPickerDialogExample {
4. private select: number | number[] = 0;
5. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
6. @State selectedValue: string = '';

8. build() {
9. Row() {
10. Column() {
11. Button('TextPickerDialog:' + this.selectedValue)
12. .margin(20)
13. .onClick(() => {
14. this.getUIContext().showTextPickerDialog({
15. range: this.fruits,
16. selected: this.select,
17. disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter }},
18. textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal }},
19. selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder }},
20. onAccept: (value: TextPickerResult) => {
21. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
22. this.select = value.index;
23. console.info(this.select + '');
24. // 点击确定后，被选到的文本数据展示到页面
25. this.selectedValue = value.value as string;
26. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
27. },
28. onCancel: () => {
29. console.info('TextPickerDialog:onCancel()');
30. },
31. onChange: (value: TextPickerResult) => {
32. console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
33. },
34. onScrollStop: (value: TextPickerResult) => {
35. console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
36. },
37. onDidAppear: () => {
38. console.info('TextPickerDialog:onDidAppear()');
39. },
40. onDidDisappear: () => {
41. console.info('TextPickerDialog:onDidDisappear()');
42. },
43. onWillAppear: () => {
44. console.info('TextPickerDialog:onWillAppear()');
45. },
46. onWillDisappear: () => {
47. console.info('TextPickerDialog:onWillDisappear()');
48. },
49. enableHoverMode: true,
50. hoverModeArea: HoverModeAreaType.TOP_SCREEN
51. });
52. })
53. }.width('100%')
54. }.height('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/R2A46V3BQOmUaA-QU9Vi8w/zh-cn_image_0000002622859977.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=E08EE17B2087076DCA7CA9686F3FC3BFE6CC8FCF1A2BE19A2B4D81298F932C29)

### 示例4（设置弹窗位置）

该示例通过alignment、offset设置弹窗的位置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. alignment: DialogAlignment.Center,
19. offset: { dx: 20, dy: 0 },
20. onAccept: (value: TextPickerResult) => {
21. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
22. this.select = value.index;
23. console.info(this.select + '');
24. // 点击确定后，被选到的文本数据展示到页面
25. this.selectedValue = value.value as string;
26. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
27. }
28. });
29. })
30. }.width('100%')
31. }.height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/2ew7S9qRTRumTLPWcMStqA/zh-cn_image_0000002622700095.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=AA081A6AB9ED48226BDC089C0DB8EBF9E82F2F0046897EDCD2C44E2C42ED43C8)

### 示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. maskRect: {
19. x: 30,
20. y: 60,
21. width: '100%',
22. height: '60%'
23. },
24. onAccept: (value: TextPickerResult) => {
25. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
26. this.select = value.index;
27. console.info(this.select + '');
28. // 点击确定后，被选到的文本数据展示到页面
29. this.selectedValue = value.value as string;
30. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
31. }
32. });
33. })
34. }.width('100%')
35. }.height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/tZnToVaRRmmwNGjqqt9EJw/zh-cn_image_0000002592220536.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=0F7A27A88A32F10CD93769ABBE82C13A76FB1643AD190DC4CAFAD66A03207B30)

### 示例6（设置弹窗背板）

该示例通过backgroundColor、backgroundBlurStyle和shadow设置弹窗背板。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. backgroundColor: 'rgb(204, 226, 251)',
19. backgroundBlurStyle: BlurStyle.NONE,
20. shadow: ShadowStyle.OUTER_FLOATING_SM,
21. onAccept: (value: TextPickerResult) => {
22. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
23. this.select = value.index;
24. console.info(this.select + '');
25. // 点击确定后，被选到的文本数据展示到页面
26. this.selectedValue = value.value as string;
27. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
28. }
29. });
30. })
31. }.width('100%')
32. }.height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-WdKEctLQdGsFAE6Ie1o4g/zh-cn_image_0000002592380468.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=83C8D06E1E42C14A70DAAFE6D477061D6137B4E349B0E41693991939CE0EA488)

### 示例7（设置循环滚动）

该示例通过配置canLoop设置是否循环滚动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerDialogExample {
5. private select: number | number[] = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
7. @State selectedValue: string = '';

9. build() {
10. Row() {
11. Column() {
12. Button('TextPickerDialog:' + this.selectedValue)
13. .margin(20)
14. .onClick(() => {
15. this.getUIContext().showTextPickerDialog({
16. range: this.fruits,
17. selected: this.select,
18. value: this.selectedValue,
19. canLoop: false,
20. onAccept: (value: TextPickerResult) => {
21. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
22. this.select = value.index;
23. console.info(this.select + '');
24. // 点击确定后，被选到的文本数据展示到页面
25. this.selectedValue = value.value as string;
26. console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
27. }
28. });
29. })
30. }.width('100%')
31. }.height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/oWoiXuOoT7yjpQ41ieUdBw/zh-cn_image_0000002622859979.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=5B2FB5B1EFA4ED43F9291E00068D21AE7EEF47ACD4748E067E9413C0CB469BD0)

### 示例8（设置选中项的背景样式）

该示例通过selectedBackgroundStyle属性设置文本选择器选中项的背景样式。

从API version 20开始，新增了[TextPickerDialogOptions](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明)的selectedBackgroundStyle属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private showText1: string [] = ['Text1', 'Text1', 'Text1', 'Text1']
6. build() {
7. Column() {
8. Row() {
9. Button('TextPickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTextPickerDialog({
13. range: this.showText1,
14. selectedBackgroundStyle: {
15. borderRadius: {
16. topLeft:15,
17. topRight:15,
18. bottomLeft:15,
19. bottomRight:15
20. },
21. color: 'FFC3C3C3'
22. }
23. })
24. })
25. }
26. }.height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/iuenJHLbSmuGtB5q7y2etg/zh-cn_image_0000002622700097.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=9C4C1755288B13B8BE1FE32EC967F37987F6A886CF9190501726E9A68302AFAD)

### 示例9（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明)，实现自定义背景模糊效果。

```
1. @Entry
2. @Component
3. struct TextPickerExample {
4. private showText1: string [] = ['Text1', 'Text1', 'Text1', 'Text1']

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. Column() {
11. Button('TextPickerDialog')
12. .margin(20)
13. .onClick(() => {
14. this.getUIContext().showTextPickerDialog({
15. range: this.showText1,
16. backgroundColor: undefined,
17. backgroundBlurStyle: BlurStyle.Thin,
18. backgroundBlurStyleOptions: {
19. colorMode: ThemeColorMode.LIGHT,
20. adaptiveColor: AdaptiveColor.AVERAGE,
21. scale: 1,
22. blurOptions: { grayscale: [20, 20] },
23. },
24. })
25. })
26. }.width('100%')
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/xGVSLXjsRe-pCnueU9Yxag/zh-cn_image_0000002592220538.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=CA132880A916AA5DB8AFEFB6C10B66513B38FED3AFAE0DC14E1BABB3DD017F43)

### 示例10（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明)，实现自定义背景效果。

```
1. @Entry
2. @Component
3. struct TextPickerExample {
4. private showText1: string [] = ['Text1', 'Text1', 'Text1', 'Text1']

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. Column() {
11. Button('TextPickerDialog')
12. .margin(20)
13. .onClick(() => {
14. this.getUIContext().showTextPickerDialog({
15. range: this.showText1,
16. backgroundColor: undefined,
17. backgroundBlurStyle: BlurStyle.Thin,
18. backgroundEffect: {
19. radius: 60,
20. saturation: 0,
21. brightness: 1,
22. color: Color.White,
23. blurOptions: { grayscale: [20, 20] }
24. },
25. })
26. })
27. }.width('100%')
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/11D5K6J_R0aQdvtSf2gkNg/zh-cn_image_0000002592380470.png?HW-CC-KV=V1&HW-CC-Date=20260611T074917Z&HW-CC-Expire=86400&HW-CC-Sign=04894B046E0DF4EBACB9739E19079316C71DEC6361F5924C31DB40C853B52149)
