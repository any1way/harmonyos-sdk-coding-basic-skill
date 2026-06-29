---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule
title: ArkUI_NativeModule
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 模块 > ArkUI_NativeModule
category: harmonyos-references
scraped_at: 2026-06-11T15:53:59+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:59da75338c6f033a8b4b9144af946dfe8d9d5be23914715e35a6e9346ef7ca12
---
## 概述

PhonePC/2in1TabletTVWearable

提供ArkUI在Native侧的通用拖拽及主动发起拖拽能力。更多详细介绍请参考[绑定拖拽事件](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (基于NDK构建UI)/添加交互事件/拖拽事件/ndk-drag-event.md>)。

提供ArkUI在Native侧的通用按键事件能力。

提供ArkUI在Native侧的注册手势回调的能力。更多详细介绍请参考[绑定手势事件](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (基于NDK构建UI)/添加交互事件/绑定手势事件/ndk-bind-gesture-events.md>)。

提供ArkUI在Native侧使用动画回调的能力。更多详细介绍请参考[使用动画](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (基于NDK构建UI)/使用动画/ndk-use-animation.md>)。

提供ArkUI在Native侧的UI能力，如UI组件创建销毁、树节点操作、属性设置、事件监听等。更多详细介绍请参考[接入ArkTS页面](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (基于NDK构建UI)/接入ArkTS页面/ndk-access-the-arkts-page.md>)。

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [drag\_and\_drop.h](../../头文件/drag_and_drop.h/capi-drag-and-drop-h.md) | 提供NativeDrag相关接口定义。 |
| [drawable\_descriptor.h](../../头文件/drawable_descriptor.h/capi-drawable-descriptor-h.md) | 提供NativeDrawableDescriptor接口的类型定义。 |
| [native\_animate.h](../../头文件/native_animate.h/capi-native-animate-h.md) | 提供ArkUI在Native侧的动画接口定义集合。 |
| [native\_dialog.h](../../头文件/native_dialog.h/capi-native-dialog-h.md) | 提供ArkUI在Native侧的自定义弹窗接口定义集合。 |
| [native\_gesture.h](../../头文件/native_gesture.h/capi-native-gesture-h.md) | 提供NativeGesture接口的类型定义。 |
| [native\_interface.h](../../头文件/native_interface.h/capi-native-interface-h.md) | 提供NativeModule接口的统一入口函数。 |
| [native\_interface\_focus.h](../../头文件/native_interface_focus.h/capi-native-interface-focus-h.md) | 定义焦点管理的相关接口，主要用于主动转移焦点或管理控制焦点转移默认行为，控制焦点激活态。 |
| [native\_key\_event.h](../../头文件/native_key_event.h/capi-native-key-event-h.md) | 提供NativeKeyEvent相关接口定义。 |
| [native\_node.h](../../头文件/native_node.h/capi-native-node-h.md) | 提供NativeNode接口的类型定义。 |
| [native\_node\_napi.h](../../头文件/native_node_napi.h/capi-native-node-napi-h.md) | 提供ArkTS侧的FrameNode转换NodeHandle的方式。 |
| [native\_type.h](../../头文件/native_type.h/capi-native-type-h.md) | 提供NativeModule公共的类型定义。 |
| [styled\_string.h](../../头文件/styled_string.h/capi-styled-string-h.md) | 提供ArkUI在Native侧的属性字符串能力。 |
