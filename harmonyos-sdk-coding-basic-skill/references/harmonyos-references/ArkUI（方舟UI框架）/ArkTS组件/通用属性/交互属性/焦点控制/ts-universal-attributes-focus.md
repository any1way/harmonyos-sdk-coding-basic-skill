---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus
title: 焦点控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 焦点控制
category: harmonyos-references
scraped_at: 2026-06-11T15:44:48+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:d1cdb9544f77b411125666135fc5418512dcec2ae44eb6f3d5de1f8c2155e822
---
自定义组件的走焦效果，可设置组件是否走焦和具体的走焦顺序，使用TAB键或方向键切换焦点。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 自定义组件无获焦能力，当设置[focusable](ts-universal-attributes-focus.md#focusable)、[enabled](../禁用控制/ts-universal-attributes-enable.md#enabled)等属性为false，或者设置[visibility](../../基础属性/显隐控制/ts-universal-attributes-visibility.md#visibility)属性为Hidden、None时，也不影响其子组件的获焦。
* 组件主动获取焦点不受窗口焦点的控制。
* 焦点开发参考[支持焦点处理](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md>)。

## focusable

PhonePC/2in1TabletTVWearable

focusable(value: boolean): T

设置当前组件是否可以获焦。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否可以获焦，true表示组件可以获焦，false表示组件不可获焦。  **说明：**  存在默认交互逻辑的组件例如[Button](../../../按钮与选择/Button/ts-basic-components-button.md)、[TextInput](../../../文本与输入/TextInput/ts-basic-components-textinput.md)等，默认即为可获焦，[Text](../../../文本与输入/Text/ts-basic-components-text.md)、[Image](../../../图片与视频/Image/ts-basic-components-image.md)等组件则默认状态为不可获焦。不可获焦状态下，无法触发[焦点事件](../../../通用事件/交互响应事件/焦点事件/ts-universal-focus-event.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## tabIndex9+

PhonePC/2in1TabletTVWearable

tabIndex(index: number): T

自定义组件tab键走焦能力。当组件未设置tabIndex时，默认按照预设的焦点移动规则进行焦点移动。

说明

* tabIndex只能够自定义Tab键走焦，若想同时自定义方向键等走焦能力，建议使用[nextFocus](ts-universal-attributes-focus.md#nextfocus18)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 自定义组件tab键走焦能力。若有配置了tabIndex大于0的组件，则tab键走焦只会在tabIndex大于0的组件内按照tabIndex的值从小到大并循环依次走焦。若没有配置tabIndex大于0的组件，则tabIndex等于0的组件按照组件预设的走焦规则走焦。  [UiExtension](<../../../../ArkTS API/UI界面/@ohos.arkui.uiExtension (uiExtension)/js-apis-arkui-uiextension.md>)组件未适配tabIndex，在含有[UiExtension](<../../../../ArkTS API/UI界面/@ohos.arkui.uiExtension (uiExtension)/js-apis-arkui-uiextension.md>)组件的[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)使用tabIndex会导致走焦错乱。  - tabIndex >= 0：表示元素是可聚焦的，并且可以通过tab键走焦来访问到该元素。  - tabIndex < 0（通常是tabIndex = -1）：表示元素是可聚焦的，但是不能通过tab键走焦来访问到该元素。  **说明：**  tabIndex与focusScopeId不能混用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## defaultFocus9+

PhonePC/2in1TabletTVWearable

defaultFocus(value: boolean): T

设置当前组件是否为当前[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)上的默认焦点。当未设置defaultFocus时，组件默认不为当前层级页面的默认焦点。

说明

可以设置默认焦点的页面指的是支持页面路由或是弹窗类的容器组件，例如Page、NaviDestination、NavBar、PopUp、Dialog等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否为当前[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)上的默认焦点，仅在初次创建的[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)第一次进入时生效。  **说明：**  值为true则表示为默认焦点，值为false时无效。  若[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)内无任何组件设置defaultFocus(true)，API version 11及之前，[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)的默认焦点是当前[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)上首个可获焦的非容器组件，API version 11之后，[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)的默认焦点就是[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)的根容器。  若某[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)内有多个组件设置了defaultFocus(true)，则以组件树深度遍历找到的第一个组件为默认焦点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## groupDefaultFocus9+

PhonePC/2in1TabletTVWearable

groupDefaultFocus(value: boolean): T

设置当前组件是否为当前组件所在容器获焦时的默认焦点。当组件未设置groupDefaultFocus时，组件默认不为当前组件所在容器获焦时的默认焦点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否为当前组件所在容器获焦时的默认焦点，仅在初次创建容器节点第一次获焦时生效。true表示当前组件为所在容器获焦时的默认焦点，false表示当前组件不是所在容器获焦时的默认焦点。  **说明：**  必须与[tabIndex](ts-universal-attributes-focus.md#tabindex9)联合使用，当某个容器设置了tabIndex，且容器内某子组件或容器自身设置了groupDefaultFocus(true)，当该容器首次TAB键获焦时，会自动将焦点转移至该指定的组件上。若容器内（包含容器本身）有多个组件设置了groupDefaultFocus(true)，则以组件树深度遍历找到的第一个组件为最终结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## focusOnTouch9+

PhonePC/2in1TabletTVWearable

focusOnTouch(value: boolean): T

设置当前组件是否支持点击获焦能力。当组件未设置focusOnTouch时，组件默认不支持点击获焦能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否支持点击获焦能力。true表示组件支持点击获焦，false表示不支持点击获焦。  **说明：**  仅在组件可点击时才能正常获取焦点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## focusBox12+

PhonePC/2in1TabletTVWearable

focusBox(style: FocusBoxStyle): T

设置当前组件系统焦点框样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [FocusBoxStyle](ts-universal-attributes-focus.md#focusboxstyle12对象说明) | 是 | 设置当前组件系统焦点框样式。  **说明：**  仅影响走焦状态下展示了系统焦点框的组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## focusControl9+

PhonePC/2in1TabletTVWearable

焦点控制模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### requestFocus9+

PhonePC/2in1TabletTVWearable

requestFocus(value: string): boolean

方法语句中可使用的全局接口，调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。

如果需要指定组件立刻获焦，推荐使用FocusController中的焦点同步转移接口[requestFocus](<../../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (FocusController)/arkts-apis-uicontext-focuscontroller.md#requestfocus12>)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 目标组件使用接口key(value: string)或id(value: string)绑定的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回值表示是否成功给目标组件申请到焦点。若参数指向的目标组件存在且已挂载组件树，并具备获焦能力，则返回true，否则返回false。 |

说明

支持焦点控制的组件：[TextInput](../../../文本与输入/TextInput/ts-basic-components-textinput.md)、[TextArea](../../../文本与输入/TextArea/ts-basic-components-textarea.md)、[Search](../../../文本与输入/Search/ts-basic-components-search.md)、[Button](../../../按钮与选择/Button/ts-basic-components-button.md)、[Text](../../../文本与输入/Text/ts-basic-components-text.md)、[Image](../../../图片与视频/Image/ts-basic-components-image.md)、[List](../../../滚动与滑动/List/ts-container-list.md)、[Grid](../../../滚动与滑动/Grid/ts-container-grid.md)。焦点事件当前仅支持在真机上显示运行效果。

## FocusBoxStyle12+对象说明

PhonePC/2in1TabletTVWearable

设置当前组件系统焦点框样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | [LengthMetrics](<../../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | 是 | 焦点框相对组件边缘的距离。  正数代表外侧，负数代表内侧。不支持百分比。 |
| strokeColor | [ColorMetrics](<../../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#colormetrics12>) | 否 | 是 | 焦点框颜色。 |
| strokeWidth | [LengthMetrics](<../../../../ArkTS API/UI界面/arkui/Graphics/js-apis-arkui-graphics.md#lengthmetrics12>) | 否 | 是 | 焦点框宽度。  不支持负数与百分比。 |

## focusScopePriority12+

PhonePC/2in1TabletTVWearable

focusScopePriority(scopeId: string, priority?: FocusPriority): T

设置当前组件在指定容器内获焦的优先级。需要配合[focusScopeId](ts-universal-attributes-focus.md#focusscopeid12)一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scopeId | string | 是 | 当前组件设置的获焦优先级生效的容器组件的id标识。  **说明：**  1.当前组件必须在scopeId所标识的容器内，或其所属容器在scopeId所标识的容器内。  2.组件不可重复设置多个优先级。  3.设置了focusScopeId的容器组件不可设置优先级。 |
| priority | [FocusPriority](ts-universal-attributes-focus.md#focuspriority12) | 否 | 获焦优先级。  **说明：**  未设置priority时，默认为AUTO优先级。  优先级对走焦以及获焦组件的影响：  1.容器整体获焦（[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)切换/焦点切换到焦点组/容器组件使用requestFocus申请焦点）时，若容器内存在优先级为PREVIOUS的组件，则优先级为PREVIOUS的组件获焦，否则，由容器内上次获焦的组件获焦。  2.容器非整体获焦（非焦点组场景下使用tab键/方向键走焦）时，若容器为首次获焦，则容器内优先级最高的组件获焦，若容器非首次获焦，不考虑优先级按照位置顺序走焦。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

### FocusPriority12+

PhonePC/2in1TabletTVWearable

设置组件焦点的优先级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 默认的优先级，缺省时组件的获焦优先级。 |
| PRIOR | 2000 | 容器内优先获焦的优先级。优先级高于AUTO。 |
| PREVIOUS | 3000 | 上一次容器整体失焦时获焦节点的优先级。优先级高于PRIOR。 |

### KeyProcessingMode15+

PhonePC/2in1TabletTVWearable

设置按键事件处理的优先级。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOCUS\_NAVIGATION | 0 | 默认值，当前组件不消费按键时，tab/方向键优先在当前容器内走焦。 |
| ANCESTOR\_EVENT | 1 | 当前组件不消费按键时，tab/方向键优先冒泡给父组件。 |

## focusScopeId12+

PhonePC/2in1TabletTVWearable

focusScopeId(id: string, isGroup?: boolean): T

设置当前容器组件的id标识，以及是否为焦点组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 设置当前容器组件的id标识。  **说明：**  单个[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)下，id标识全局唯一，不可重复。 |
| isGroup | boolean | 否 | 设置当前容器组件是否为焦点组。true表示容器组件为焦点组，false表示容器组件不是焦点组。默认值为false。  **说明：**  焦点组不可嵌套，不可重复配置。  焦点组不能和tabIndex混用。  配置焦点组的目的是使得容器及容器内的元素可以按照焦点组规则走焦。焦点组走焦规则：  1.焦点组容器内只能通过方向键走焦，tab键会使焦点跳出焦点组容器。  2.通过方向键使焦点从焦点组容器外切换到焦点组容器内时，若焦点组容器内存在优先级为PREVIOUS的组件，则优先级为PREVIOUS的组件获焦，否则，由焦点组容器内上次获焦的组件获焦。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## focusScopeId14+

PhonePC/2in1TabletTVWearable

focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T

设置当前容器组件的id标识，以及是否为焦点组。新增参数arrowStepOut，用于设置能否使用方向键走焦出当前焦点组。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 设置当前容器组件的id标识。  **说明：**  单个[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)下，id标识全局唯一，不可重复。 |
| isGroup | boolean | 否 | 设置当前容器组件是否为焦点组。true表示容器组件为焦点组，false表示容器组件不是焦点组。默认值为false。  **说明：**  焦点组不可嵌套，不可重复配置。  焦点组不能和tabIndex混用。  配置焦点组的目的是使得容器及容器内的元素可以按照焦点组规则走焦。焦点组走焦规则：  1.焦点组容器内只能通过方向键走焦，tab键会使焦点跳出焦点组容器。  2.通过方向键使焦点从焦点组容器外切换到焦点组容器内时，若焦点组容器内存在优先级为PREVIOUS的组件，则优先级为PREVIOUS的组件获焦，否则，由焦点组容器内上次获焦的组件获焦。 |
| arrowStepOut | boolean | 否 | 设置能否使用方向键走焦出当前焦点组。true表示可以使用方向键走焦出当前焦点组，false表示不能使用方向键走焦出当前焦点组。默认值为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## tabStop14+

PhonePC/2in1TabletTVWearable

tabStop(isTabStop: boolean): T

设置当前容器组件的tabStop，可决定焦点在走焦时是否会停留在当前容器。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTabStop | boolean | 是 | 设置当前容器组件是否为走焦可停留容器。true表示当前容器组件为走焦可停留容器，false表示当前容器组件不是走焦可停留容器。  **说明：**  1.配置tabStop需要确保是容器组件且有可获焦的孩子组件，默认容器组件不能直接获焦。  2.通过[requestFocus](<../../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (FocusController)/arkts-apis-uicontext-focuscontroller.md#requestfocus12>)请求焦点，如果是容器组件且配置tabStop，焦点能够停留在容器组件，如果未配置tabStop，即使整条焦点链上有配置了tabStop的组件，该组件依然能获取到焦点。  3.配置tabStop的容器不允许嵌套超过2层。  tabStop走焦规则：  1.通过tab键和方向键走焦，焦点会停留在配置了tabStop的组件上，如果焦点停留在配置了tabStop的容器内部时，可以走焦到容器内部的下一个可获焦组件，如果焦点停留在配置了tabStop的容器外部时，可以走焦到容器外的下一个可获焦组件。  2.当焦点停留在tabStop上时，按Enter键可以走焦到内部第一个可获焦组件，按ESC能够将焦点退回到不超过当前[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)根容器的上一个配置了tabStop的组件，按空格键可以响应该容器的onClick事件。  3.不建议根容器配置tabStop。如果根容器配置了tabStop，通过[clearFocus](<../../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (FocusController)/arkts-apis-uicontext-focuscontroller.md#clearfocus12>)将焦点清理到根容器，再按Enter键会重新走回内部上一次获焦组件，通过ESC键将焦点清理到根容器，再按Enter键会走焦到内部第一个可获焦组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**描述走焦的时候的按键以及获焦组件**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/QbgAU89sQDCq8fCkk9hbYg/zh-cn_image_0000002592379924.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=41EE039BAF63CE6028B5FAD7B397AD01D1552F66A3080707D55B034114321546)

如果当前焦点停留在button2上，按下tab键将会走焦到Column3，再按下tab键会循环走焦到button1。

## nextFocus18+

PhonePC/2in1TabletTVWearable

nextFocus(nextStep: Optional<FocusMovement>): T

设置组件的自定义焦点走焦逻辑。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nextStep | Optional<[FocusMovement](ts-universal-attributes-focus.md#focusmovement18对象说明)> | 是 | 设置当前容器组件的自定义走焦规则。  **说明：**  默认值为重置nextStep为空。  没设置自定义走焦或者设置自定义组件容器不存在，仍进行默认走焦规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## FocusMovement18+对象说明

PhonePC/2in1TabletTVWearable

设置对应的按键对应的走焦目的组件，缺省则遵循默认走焦规则。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| forward | string | 否 | 是 | 通过tab键走焦到组件的id。  默认值为重置forward为空。 |
| backward | string | 否 | 是 | 通过shift+tab键走焦到组件的id。  默认值为重置backward为空。 |
| up | string | 否 | 是 | 通过方向键上键走焦到组件的id。  默认值为重置up为空。 |
| down | string | 否 | 是 | 通过方向键下键走焦到组件的id。  默认值为重置down为空。 |
| left | string | 否 | 是 | 通过方向键左键走焦到组件的id。  默认值为重置left为空。 |
| right | string | 否 | 是 | 通过方向键右键走焦到组件的id。  默认值为重置right为空。 |

说明

直接使用focusControl可能导致[UI上下文不明确](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI系统场景化能力/使用UI上下文接口操作界面（UIContext）/arkts-global-interface.md#ui上下文不明确>)的问题，建议使用getUIContext()获取[UIContext](<../../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)实例，并使用[getFocusController](<../../../../ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getfocuscontroller12>)获取绑定实例的focusControl。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件获焦和走焦的效果）

该示例通过配置[defaultFocus](ts-universal-attributes-focus.md#defaultfocus9)可以使绑定的组件成为[层级页面](<../../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加交互响应/支持焦点处理/arkts-common-events-focus-event.md#基础概念>)创建后首次获焦的焦点，配置[groupDefaultFocus](ts-universal-attributes-focus.md#groupdefaultfocus9)可以使绑定的组件成为tabIndex容器创建后首次获焦的焦点，配置[focusOnTouch](ts-universal-attributes-focus.md#focusontouch9)可以使绑定的组件点击后立即获焦。

```
1. // focusTest.ets
2. @Entry
3. @Component
4. struct FocusableExample {
5. @State inputValue: string = '';

7. build() {
8. Scroll() {
9. Row({ space: 20 }) {
10. Column({ space: 20 }) {
11. Column({ space: 5 }) {
12. Button('Group1')
13. .width(165)
14. .height(40)
15. .fontColor(Color.White)
16. .focusOnTouch(true) // 该Button组件点击后可获焦
17. Row({ space: 5 }) {
18. Button()
19. .width(80)
20. .height(40)
21. .fontColor(Color.White)
22. Button()
23. .width(80)
24. .height(40)
25. .fontColor(Color.White)
26. .focusOnTouch(true) // 该Button组件点击后可获焦
27. }

29. Row({ space: 5 }) {
30. Button()
31. .width(80)
32. .height(40)
33. .fontColor(Color.White)
34. Button()
35. .width(80)
36. .height(40)
37. .fontColor(Color.White)
38. }
39. }.borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)
40. .tabIndex(1) // 该Column组件为按TAB键走焦的第一个获焦的组件
41. Column({ space: 5 }) {
42. Button('Group2')
43. .width(165)
44. .height(40)
45. .fontColor(Color.White)
46. Row({ space: 5 }) {
47. Button()
48. .width(80)
49. .height(40)
50. .fontColor(Color.White)
51. Button()
52. .width(80)
53. .height(40)
54. .fontColor(Color.White)
55. .groupDefaultFocus(true) // 该Button组件上级Column组件获焦时获焦
56. }

58. Row({ space: 5 }) {
59. Button()
60. .width(80)
61. .height(40)
62. .fontColor(Color.White)
63. Button()
64. .width(80)
65. .height(40)
66. .fontColor(Color.White)
67. }
68. }.borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)
69. .tabIndex(2) // 该Column组件为按TAB键走焦的第二个获焦的组件
70. }

72. Column({ space: 5 }) {
73. TextInput({ placeholder: 'input', text: this.inputValue })
74. .onChange((value: string) => {
75. this.inputValue = value
76. })
77. .width(156)
78. .defaultFocus(true) // 该TextInput组件为层级页面的初始默认焦点
79. Button('Group3')
80. .width(165)
81. .height(40)
82. .fontColor(Color.White)
83. Row({ space: 5 }) {
84. Button()
85. .width(80)
86. .height(40)
87. .fontColor(Color.White)
88. Button()
89. .width(80)
90. .height(40)
91. .fontColor(Color.White)
92. }

94. Button()
95. .width(165)
96. .height(40)
97. .fontColor(Color.White)
98. Row({ space: 5 }) {
99. Button()
100. .width(80)
101. .height(40)
102. .fontColor(Color.White)
103. Button()
104. .width(80)
105. .height(40)
106. .fontColor(Color.White)
107. }

109. Button()
110. .width(165)
111. .height(40)
112. .fontColor(Color.White)
113. Row({ space: 5 }) {
114. Button()
115. .width(80)
116. .height(40)
117. .fontColor(Color.White)
118. Button()
119. .width(80)
120. .height(40)
121. .fontColor(Color.White)
122. }
123. }.borderWidth(2).borderColor(Color.Orange).borderStyle(BorderStyle.Dashed)
124. .tabIndex(3) // 该Column组件为按TAB键走焦的第三个获焦的组件
125. }.alignItems(VerticalAlign.Top)
126. }
127. }
128. }
```

示意图：

首次进入时，焦点默认在defaultFocus绑定的TextInput组件上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/lrsgg6MLTYmIeFqz6qoYIg/zh-cn_image_0000002622859433.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=6B6610A210608BD07D0F949B9DEDB22CA200E66E535B2D43D50600CA171EBE9C)

首次按TAB键，焦点切换到tabIndex(1)的容器上，且自动走焦到内部第一个可获焦组件上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/B3YpSasHRdmGNOgHOTFh1w/zh-cn_image_0000002622699553.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=7175F9AF9D437E085142D475B5DA3E268A41BA849D62992EDD456F0D7C34E027)

第二次按TAB键，焦点切换到tabIndex(2)的容器上，且自动走到其内部的groupDefaultFocus绑定的组件上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/F6HZrF0kTU-JIXbX5gdxdw/zh-cn_image_0000002592219992.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=BF5DA6E696D45ED264DBC82BD5B2889AC1F67F0C0F536F7976E9094DB765E234)

第三次按TAB键，焦点切换到tabIndex(3)的容器上，且自动走焦到内部配置了DefaultFocus的组件上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/S-OlFQD8RtmphKAMqYVF8g/zh-cn_image_0000002592379926.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=A31DE0FCB44BE50E976D37FDE4CDF5D7BAEC8A0E79460B274B9F7AF591A1AC90)

点击绑定了focusOnTouch的组件，组件自身获焦，焦点框被清除，再按下TAB键后，显示焦点框：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/0SgjdApwQwqaPXyBRGv3Fg/zh-cn_image_0000002622859435.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=7F453BB5D61A3C1E0999E99583806712F6B070DAE90522975ED1380CE372B405)

### 示例2（设置指定组件获焦）

该示例通过配置[focusControl.requestFocus](ts-universal-attributes-focus.md#requestfocus9)使指定组件获取焦点。

```
1. // requestFocus.ets
2. @Entry
3. @Component
4. struct RequestFocusExample {
5. @State idList: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'LastPageId'];
6. @State selectId: string = 'LastPageId';

8. build() {
9. Column({ space: 20 }) {
10. Row({ space: 5 }) {
11. Button("id: " + this.idList[0] + " focusable(false)")
12. .width(180)
13. .height(70)
14. .fontColor(Color.White)
15. .id(this.idList[0])
16. .focusable(false)
17. Button("id: " + this.idList[1])
18. .width(180).height(70).fontColor(Color.White)
19. .id(this.idList[1])
20. }

22. Row({ space: 5 }) {
23. Button("id: " + this.idList[2])
24. .width(180).height(70).fontColor(Color.White)
25. .id(this.idList[2])
26. Button("id: " + this.idList[3])
27. .width(180).height(70).fontColor(Color.White)
28. .id(this.idList[3])
29. }

31. Row({ space: 5 }) {
32. Button("id: " + this.idList[4])
33. .width(180).height(70).fontColor(Color.White)
34. .id(this.idList[4])
35. Button("id: " + this.idList[5])
36. .width(180).height(70).fontColor(Color.White)
37. .id(this.idList[5])
38. }

40. Row({ space: 5 }) {
41. Select([{ value: this.idList[0] },
42. { value: this.idList[1] },
43. { value: this.idList[2] },
44. { value: this.idList[3] },
45. { value: this.idList[4] },
46. { value: this.idList[5] },
47. { value: this.idList[6] }])
48. .value(this.selectId)
49. .onSelect((index: number) => {
50. this.selectId = this.idList[index]
51. })
52. Button("RequestFocus")
53. .width(180).height(70).fontColor(Color.White)
54. .onClick(() => {
55. // 建议使用this.getUIContext().getFocusController().requestFocus()
56. let res = focusControl.requestFocus(this.selectId) // 使选中的this.selectId的组件获焦
57. if (res) {
58. this.getUIContext().getPromptAction().showToast({ message: 'Request success' })
59. } else {
60. this.getUIContext().getPromptAction().showToast({ message: 'Request failed' })
61. }
62. })
63. }
64. }.width('100%').margin({ top: 20 })
65. }
66. }
```

示意图：

按下TAB键，激活焦点态显示。

申请不存在的组件获焦：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/L5023MEeQuOf6hvN3MXOZw/zh-cn_image_0000002622699555.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=973B613B4ED651A5F27B8AAE136B2B1EA22DA7FF8A902B00E7B7AEB26CA57C74)

申请不可获焦的组件获焦：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/p8shel8FS3OgNbwytsSX2w/zh-cn_image_0000002592219994.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=C5A512572EFB10324585B4EDE185EC0E0EE6FCEAD792906F71004E376671A7E5)

申请存在且可获焦的组件获焦：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Kbbigng_QXWUtz0wCDvblQ/zh-cn_image_0000002592379928.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=5AA3B20218A27989B61180A4B20C0CBD7E2BA13A09D6ADE2D9AD2862576B9324)

### 示例3（设置焦点框样式）

该示例通过配置[focusBox](ts-universal-attributes-focus.md#focusbox12)修改组件的焦点框样式。

```
1. import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct RequestFocusExample {
6. build() {
7. Column({ space: 30 }) {
8. Button("small black focus box")
9. .focusBox({
10. margin: new LengthMetrics(0),
11. strokeColor: ColorMetrics.rgba(0, 0, 0),
12. })
13. Button("large red focus box")
14. .focusBox({
15. margin: LengthMetrics.px(20),
16. strokeColor: ColorMetrics.rgba(255, 0, 0),
17. strokeWidth: LengthMetrics.px(10)
18. })
19. }
20. .alignItems(HorizontalAlign.Center)
21. .width('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/LV-xmtWiRIqsiMpeMz2Sjg/zh-cn_image_0000002622859437.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=70708BE8E4F7802BC8DDA044640BA6DA291C83EAA2C644778937F3DB8AEBF317)

### 示例4（设置焦点组走焦）

该示例通过配置[focusScopePriority](ts-universal-attributes-focus.md#focusscopepriority12)，可以使绑定的组件在所属容器首次获焦时成为焦点，配置[focusScopeId](ts-universal-attributes-focus.md#focusscopeid12)，可以使绑定的容器组件成为焦点组。

```
1. // focusTest.ets
2. @Entry
3. @Component
4. struct FocusableExample {
5. @State inputValue: string = '';

7. build() {
8. Scroll() {
9. Row({ space: 20 }) {
10. Column({ space: 20 }) { // 标记为Column1
11. Column({ space: 5 }) {
12. Button('Group1')
13. .width(165)
14. .height(40)
15. .fontColor(Color.White)
16. Row({ space: 5 }) {
17. Button()
18. .width(80)
19. .height(40)
20. .fontColor(Color.White)
21. Button()
22. .width(80)
23. .height(40)
24. .fontColor(Color.White)
25. }

27. Row({ space: 5 }) {
28. Button()
29. .width(80)
30. .height(40)
31. .fontColor(Color.White)
32. Button()
33. .width(80)
34. .height(40)
35. .fontColor(Color.White)
36. }
37. }.borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)

39. Column({ space: 5 }) {
40. Button('Group2')
41. .width(165)
42. .height(40)
43. .fontColor(Color.White)
44. Row({ space: 5 }) {
45. Button()
46. .width(80)
47. .height(40)
48. .fontColor(Color.White)
49. Button()
50. .width(80)
51. .height(40)
52. .fontColor(Color.White)
53. .focusScopePriority('ColumnScope1', FocusPriority.PRIOR) // Column1首次获焦时获焦
54. }

56. Row({ space: 5 }) {
57. Button()
58. .width(80)
59. .height(40)
60. .fontColor(Color.White)
61. Button()
62. .width(80)
63. .height(40)
64. .fontColor(Color.White)
65. }
66. }.borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)
67. }
68. .focusScopeId('ColumnScope1')

70. Column({ space: 5 }) { // 标记为Column2
71. TextInput({ placeholder: 'input', text: this.inputValue })
72. .onChange((value: string) => {
73. this.inputValue = value
74. })
75. .width(156)
76. Button('Group3')
77. .width(165)
78. .height(40)
79. .fontColor(Color.White)
80. Row({ space: 5 }) {
81. Button()
82. .width(80)
83. .height(40)
84. .fontColor(Color.White)
85. Button()
86. .width(80)
87. .height(40)
88. .fontColor(Color.White)
89. }

91. Button()
92. .width(165)
93. .height(40)
94. .fontColor(Color.White)
95. .focusScopePriority('ColumnScope2', FocusPriority.PREVIOUS) // Column2获焦时获焦
96. Row({ space: 5 }) {
97. Button()
98. .width(80)
99. .height(40)
100. .fontColor(Color.White)
101. Button()
102. .width(80)
103. .height(40)
104. .fontColor(Color.White)
105. }

107. Button()
108. .width(165)
109. .height(40)
110. .fontColor(Color.White)
111. Row({ space: 5 }) {
112. Button()
113. .width(80)
114. .height(40)
115. .fontColor(Color.White)
116. Button()
117. .width(80)
118. .height(40)
119. .fontColor(Color.White)
120. }
121. }.borderWidth(2).borderColor(Color.Orange).borderStyle(BorderStyle.Dashed)
122. .focusScopeId('ColumnScope2', true) // Column2为焦点组
123. }.alignItems(VerticalAlign.Top)
124. }
125. }
126. }
```

示意图：

首次按下TAB键时，焦点转移到容器1中绑定focusScopePriority的组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Q00Hw3dvRnmUPFio55t4hA/zh-cn_image_0000002622699557.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=73E8E653B9F49F946A47D57C11E031E130AF2E44F1D2A8DA2F5C5CAADEAC6618)

继续按下TAB键，焦点转移到容器1下一个组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/fv17aOUVRYS0O_QtHP4jEA/zh-cn_image_0000002592219996.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=1CB57E66B5420439058C1A33B7EEF46636F7CDA622C5F1891FDB4D23F235107C)

再次按下TAB键，焦点转移到容器1下一个组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/qkVl3huiTYS8W8g-bbo35Q/zh-cn_image_0000002592379930.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=42EE5C0474A8F303454949FD8A833353351B4A1AFB87B75B10498F957EAC6199)

继续按下TAB键，焦点转移到容器2中配置了focusScopePriority的组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/cYOa-1L8Q1CO9Npnm5xzrA/zh-cn_image_0000002622859439.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=118CBFD504692DA0AAB0E959EBC9CF329D6EFF95A13A317D2DCD0D559396828E)

继续按下TAB键，焦点转移到容器1中名为Group1的组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/C7gcQgIzQ8q_La1gfDRPRA/zh-cn_image_0000002622699559.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=B873F23847199A9C481030A74D0B0EE6F8FF7FD1A815160B7C8C19DE03CCA4B0)

### 示例5（设置tab走焦停留）

该示例通过配置[tabStop](ts-universal-attributes-focus.md#tabstop14)实现使用tab走焦停留在组件上。

```
1. import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TabStop {
6. build() {
7. Column({ space: 20 }) {
8. Column({ space: 20 }) {
9. Column({ space: 20 }) {
10. Row({ space: 5 }) {
11. Button("button 1")
12. .width(200).height(70).fontColor(Color.White)
13. .focusBox({
14. margin: LengthMetrics.px(20),
15. strokeColor: ColorMetrics.rgba(23, 169, 141),
16. strokeWidth: LengthMetrics.px(10)
17. })
18. }

20. Row({ space: 5 }) {
21. Button("button 2")
22. .width(200).height(70).fontColor(Color.White)
23. .focusBox({
24. margin: LengthMetrics.px(20),
25. strokeColor: ColorMetrics.rgba(23, 169, 141),
26. strokeWidth: LengthMetrics.px(10)
27. })
28. }
29. }.width('80%').margin({ top: 30 }).borderColor(Color.Black)
30. }.width('95%').margin({ top: 60 }).borderColor(Color.Black)

32. Column({ space: 20 }) {
33. Column({ space: 20 }) {
34. Row({ space: 5 }) {
35. Button("button 3")
36. .width(200)
37. .height('70%')
38. .fontColor(Color.White)
39. .focusBox({
40. margin: LengthMetrics.px(20),
41. strokeColor: ColorMetrics.rgba(23, 169, 141),
42. strokeWidth: LengthMetrics.px(10)
43. })
44. .margin({ top: 15 })
45. }
46. }
47. .width('80%')
48. .height('120')
49. .borderColor(Color.Black)
50. .margin({ top: 10 })
51. .tabStop(true)
52. .focusBox({
53. margin: LengthMetrics.px(20),
54. strokeColor: ColorMetrics.rgba(23, 169, 141),
55. strokeWidth: LengthMetrics.px(10)
56. })
57. .borderWidth(1)
58. }.width('95%').margin({ top: 50 }).borderColor(Color.Black)
59. }
60. }
61. }
```

示意图：

连续按下两次TAB键，焦点转移到button2上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/RYjuqvlwSTOF4ACrKVcisQ/zh-cn_image_0000002592219998.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=C52227EC52F742E6EAB5FA9084704862484F84F81468AFC67D3C8169242C3A53)

接着按下TAB键，焦点转移到配置了tabStop的组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/3WQoKKv5Tk2qQQYyo9p5Ew/zh-cn_image_0000002592379932.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=45557077AA431C73B241E399F723C4DD4CA3ABF79741DFF9DB4537F32D8DC27A)

再按下Enter键，焦点转移至内部button3上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/b3-qMqtdR-64bSreXcMewQ/zh-cn_image_0000002622859441.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=D752F5E961B86692B4A39EDDF565AF798C2542E75D6B699C64467C6074419FCA)

再按下ESC键，焦点转移到配置了tabStop的组件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_GvcbHziSke0tXeVBIh0Uw/zh-cn_image_0000002592379932.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=7858C77BF4285EB54EE7B9FE3FBC9680B0CE6E805D0B7AC7D346E285AB8C59CF)

再按下TAB键，焦点循环走焦到button1上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/rlyN3E-gTcmOTaGEHYr4Cg/zh-cn_image_0000002622699561.png?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=8E11C02D3EA706260D00D42ECCC2DB8000349523CDFCB6C48D00D60EFB7ABFDD)

### 示例6（设置自定义走焦）

从API version 18开始，该示例通过配置[nextFocus](ts-universal-attributes-focus.md#nextfocus18)实现自定义走焦规则。

如果不配置[nextFocus](ts-universal-attributes-focus.md#nextfocus18)，默认的点击tab的走焦顺序为：M->A->B->C；配置了[nextFocus](ts-universal-attributes-focus.md#nextfocus18)以后，走焦顺序变更为：M->D->F->B。

```
1. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
2. applyNormalAttribute(instance: ButtonAttribute): void {
3. instance.id('M')
4. instance.nextFocus({ forward: 'D', up: 'C', down: 'D' })
5. }
6. }

8. @Entry
9. @Component
10. struct Index {
11. @State modifier: MyButtonModifier = new MyButtonModifier();
12. @State idList: string[] = ['A', 'B', 'C', 'D', 'E', 'F'];

14. build() {
15. Column({ space: 10 }) {
16. Row({ space: 10 }) {
17. Button("id: M")
18. .attributeModifier(this.modifier)
19. Button("id: " + this.idList[0])
20. .id(this.idList[0])
21. .nextFocus({
22. forward: 'C',
23. backward: 'M',
24. up: 'E',
25. right: 'F',
26. down: 'B',
27. left: 'D'
28. });
29. Button("id: " + this.idList[1])
30. .id(this.idList[1])
31. }

33. Column({ space: 10 }) {
34. Button("id: " + this.idList[2])
35. .id(this.idList[2]);
36. Button("id: " + this.idList[3])
37. .id(this.idList[3])
38. .nextFocus({ forward: 'F' });
39. }

41. Row({ space: 10 }) {
42. Button("id: " + this.idList[4])
43. .id(this.idList[4]);
44. Button("id: " + this.idList[5])
45. .id(this.idList[5])
46. .nextFocus({ forward: 'B' });
47. }
48. }
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/mv_kAGMrROKvswp51FNoCQ/zh-cn_image_0000002592220000.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074446Z&HW-CC-Expire=86400&HW-CC-Sign=1313D7C61924DA0BE4FE320C5BAD5345F7EA503533EDF4CF969ACE8A2E758845)
