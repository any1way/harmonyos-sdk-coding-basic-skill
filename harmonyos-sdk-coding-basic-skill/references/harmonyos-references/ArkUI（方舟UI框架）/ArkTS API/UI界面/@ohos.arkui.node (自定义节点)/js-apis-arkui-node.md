---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node
title: @ohos.arkui.node (自定义节点)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.node (自定义节点)
category: harmonyos-references
scraped_at: 2026-06-01T15:36:46+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:9df6863e0a48a942da2e426725572b5d6fd8ac8c14b8b9943b5d0f0bcb591ef1
---
Node将自定义节点的二级模块API组织在一起，方便开发者进行导出使用。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当前不支持在预览器中使用自定义节点。

## BuilderNode

PhonePC/2in1TabletTVWearable

[BuilderNode](../arkui/BuilderNode/js-apis-arkui-buildernode.md)模块提供能够挂载系统组件的自定义节点BuilderNode。不建议将BuilderNode作为子节点挂载到其他自定义节点上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## FrameNode

PhonePC/2in1TabletTVWearable

[FrameNode](../arkui/FrameNode/js-apis-arkui-framenode.md)模块提供自定义节点FrameNode，表示组件树的实体节点。[NodeController](../arkui/NodeController/js-apis-arkui-nodecontroller.md)可通过[BuilderNode](../arkui/BuilderNode/js-apis-arkui-buildernode.md)持有的FrameNode将其挂载到[NodeContainer](../../../ArkTS组件/自定义占位组件/NodeContainer/ts-basic-components-nodecontainer.md)上，也可通过FrameNode获取[RenderNode](../arkui/RenderNode/js-apis-arkui-rendernode.md)，挂载到其他FrameNode上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NodeController

PhonePC/2in1TabletTVWearable

[NodeController](../arkui/NodeController/js-apis-arkui-nodecontroller.md)模块提供NodeController，用于实现自定义节点的创建、显示、更新等操作，并负责将自定义节点挂载到[NodeContainer](../../../ArkTS组件/自定义占位组件/NodeContainer/ts-basic-components-nodecontainer.md)上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Graphics

PhonePC/2in1TabletTVWearable

[Graphics](../arkui/Graphics/js-apis-arkui-graphics.md)模块：提供自定义节点相关属性设置的定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RenderNode

PhonePC/2in1TabletTVWearable

[RenderNode](../arkui/RenderNode/js-apis-arkui-rendernode.md)模块提供自绘制渲染节点RenderNode，支持开发者通过C API进行开发，完成自定义绘制需求。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## XComponentNode

PhonePC/2in1TabletTVWearable

[XComponentNode](../../已停止维护的接口/XComponentNode/js-apis-arkui-xcomponentnode.md)模块提供XComponent节点XComponentNode，表示组件树中的XComponent组件，用于EGL/OpenGLES和媒体数据写入，并支持动态修改节点渲染类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## UIContext获取方法

PhonePC/2in1TabletTVWearable

1.使用ohos.window中的[getUIContext()](<../../窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getuicontext10>)方法获取UIContext实例。

2.可以通过自定义组件内置方法[getUIContext()](../../../ArkTS组件/自定义组件/自定义组件内置方法/ts-custom-component-api.md#getuicontext)获取。

3.可以在[NodeController](../arkui/NodeController/js-apis-arkui-nodecontroller.md)的[makeNode](../arkui/NodeController/js-apis-arkui-nodecontroller.md#makenode)回调方法中获取。
