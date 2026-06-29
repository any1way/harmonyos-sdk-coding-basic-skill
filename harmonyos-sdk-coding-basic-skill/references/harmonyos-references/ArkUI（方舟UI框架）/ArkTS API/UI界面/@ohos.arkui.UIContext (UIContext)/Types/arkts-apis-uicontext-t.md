---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-t
title: Types
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Types
category: harmonyos-references
scraped_at: 2026-06-01T15:37:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b5b7ce2aa074d71c27f6ec07fc97c4c4f53ceaec5231fbd587ff6b552a06c6bf
---
说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## CustomBuilderWithId18+

PhonePC/2in1TabletTVWearable

type CustomBuilderWithId = (id: number) => void

组件属性、方法参数可使用CustomBuilderWithId类型来自定义UI描述，并且可以指定组件ID生成用户自定义组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 组件ID。 |

## ClickEventListenerCallback12+

PhonePC/2in1TabletTVWearable

type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void

定义了用于在UIObserver中监听点击事件的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ClickEvent](../../../../ArkTS组件/通用事件/交互响应事件/点击事件/ts-universal-events-click.md#clickevent) | 是 | 触发事件监听的点击事件的相关信息。 |
| node | [FrameNode](../../arkui/FrameNode/js-apis-arkui-framenode.md) | 否 | 触发事件监听的点击事件所绑定的组件。 |

## PanListenerCallback19+

PhonePC/2in1TabletTVWearable

type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void

Pan手势事件监听函数类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [GestureEvent](../../../../ArkTS组件/手势处理/手势公共接口/ts-gesture-common.md#gestureevent对象说明) | 是 | 触发事件监听的手势事件的相关信息。 |
| current | [GestureRecognizer](../../../../ArkTS组件/手势处理/手势公共接口/ts-gesture-common.md#gesturerecognizer12) | 是 | 触发事件监听的手势识别器的相关信息。 |
| node | [FrameNode](../../arkui/FrameNode/js-apis-arkui-framenode.md) | 否 | 触发事件监听的手势事件所绑定的组件。 |

## GestureEventListenerCallback12+

PhonePC/2in1TabletTVWearable

type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void

定义了用于在UIObserver中监听手势的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [GestureEvent](../../../../ArkTS组件/手势处理/手势公共接口/ts-gesture-common.md#gestureevent对象说明) | 是 | 触发事件监听的手势事件的相关信息。 |
| node | [FrameNode](../../arkui/FrameNode/js-apis-arkui-framenode.md) | 否 | 触发事件监听的手势事件所绑定的组件。 |

## NodeIdentity20+

PhonePC/2in1TabletTVWearable

type NodeIdentity = string | number

组件标识。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| string | 指定组件id，该id通过通用属性[id](../../../../ArkTS组件/通用属性/基础属性/组件标识/ts-universal-attributes-component-id.md#id)设置。 |
| number | 系统分配的唯一标识的节点UniqueID，可通过[getUniqueId](../../arkui/FrameNode/js-apis-arkui-framenode.md#getuniqueid12)获取。 |

## NodeRenderStateChangeCallback20+

PhonePC/2in1TabletTVWearable

type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void

定义了用于在UIObserver中监控某个特定节点渲染状态的回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [NodeRenderState](../Enums/arkts-apis-uicontext-e.md#noderenderstate20) | 是 | 触发事件监听的手势事件的相关信息。 |
| node | [FrameNode](../../arkui/FrameNode/js-apis-arkui-framenode.md) | 否 | 触发事件监听的手势事件所绑定的组件，如果组件被释放将返回null。 |

## GestureListenerCallback20+

PhonePC/2in1TabletTVWearable

type GestureListenerCallback = (info: GestureTriggerInfo) => void

定义了用于在UIObserver中监控特定手势触发信息的回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [GestureTriggerInfo](<../Interfaces (其他)/arkts-apis-uicontext-i.md#gesturetriggerinfo20>) | 是 | 交互触发的手势详情。 |

## PointerStyle12+

PhonePC/2in1TabletTV

type PointerStyle = pointer.PointerStyle

光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

| 类型 | 说明 |
| --- | --- |
| [pointer.PointerStyle](<../../../../../基础功能/Input Kit（多模输入服务）/ArkTS API/@ohos.multimodalInput.pointer (鼠标光标)/js-apis-pointer.md#pointerstyle>) | 光标样式。 |

## Context12+

PhonePC/2in1TabletTVWearable

type Context = common.Context

当前组件所在Ability的上下文。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [common.Context](<../../../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.common (Ability公共模块)/js-apis-app-ability-common.md#context>) | Context的具体类型为当前Ability关联的Context对象。 |
