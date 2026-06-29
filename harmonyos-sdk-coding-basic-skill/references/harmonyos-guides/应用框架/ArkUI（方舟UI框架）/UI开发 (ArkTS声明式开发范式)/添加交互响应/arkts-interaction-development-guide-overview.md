---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-overview
title: 添加交互响应
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:43+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:ba314c32e487578f8e3f9e5a969ab857c49bae8c9882f8d3c4e7f059996d40ae
---
ArkUI框架提供了丰富的接口，用于处理用户通过不同外设生成的基础输入事件，同时提供了高级接口封装，以响应用户归一化的交互行为，如手势、拖拽、焦点等。

相较于基础输入事件，应优先采用手势处理用户交互，因为手势作为用户交互的识别结果，能够屏蔽不同基础事件的差异。例如，点击操作既可通过手指触控实现，也可通过鼠标点击完成，应用程序只需对接一个[TapGesture](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/基础手势/TapGesture/ts-basic-gestures-tapgesture.md)即可在各类输入设备上支持点击交互。

[交互基础机制说明](交互基础机制说明/arkts-interaction-basic-principles.md)：交互处理的基本概念和原理。

[输入设备与事件](输入设备与事件/arkts-interaction-raw-input-event.md)：不同的输入设备会产生哪些基础输入事件，以及如何处理它们。

[添加手势响应](添加手势响应/arkts-interaction-support-gesture.md)：处理归一化手势交互。

[支持统一拖拽](支持统一拖拽/arkts-common-events-drag-event.md)：了解如何适配统一拖拽。

[支持焦点处理](支持焦点处理/arkts-common-events-focus-event.md)：了解如何控制和管理界面中的组件焦点。

通过以下链接了解使用NDK开发UI界面时，如何为组件添加交互响应：

* [绑定基础输入事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-input-events)：通过NDK为组件添加基础输入事件响应。
* [绑定手势事件](<../../UI开发 (基于NDK构建UI)/添加交互事件/绑定手势事件/ndk-bind-gesture-events.md>)：通过NDK为组件添加手势交互。
* [绑定拖拽事件](<../../UI开发 (基于NDK构建UI)/添加交互事件/拖拽事件/ndk-drag-event.md>)：通过NDK为组件支持统一拖拽。

* **[交互响应概述](交互响应概述/arkts-interaction-capability-overview.md)**
* **[交互基础机制说明](交互基础机制说明/arkts-interaction-basic-principles.md)**
* **[输入设备与事件](输入设备与事件/arkts-interaction-raw-input-event.md)**
* **[添加手势响应](添加手势响应/arkts-interaction-support-gesture.md)**
* **[支持统一拖拽](支持统一拖拽/arkts-common-events-drag-event.md)**
* **[支持焦点处理](支持焦点处理/arkts-common-events-focus-event.md)**
