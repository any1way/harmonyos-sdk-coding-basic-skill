---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-basic-syntax-overview
title: 基本语法概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 基本语法概述
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:23+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:809028a9d8e9dcb446264689c97ee46e0c4eca15f878faa55201c7a840e1b3c9
---
在初步了解ArkTS语言后，本指南将以具体的示例来说明ArkTS的基本组成。

如下图所示，点击“按钮”时，文本内容从“Hello World”变为“Hello ArkUI”。

**图1** 示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/UCp6OJuoS_qMD6h-5WfUgw/zh-cn_image_0000002622697503.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062822Z&HW-CC-Expire=86400&HW-CC-Sign=3D08072121C8E0C7B3C4E1B107D274F93DE98D382F7E9472FF0BDE924D0781FF)

本示例中，ArkTS的基本组成如下所示。

**图2** ArkTS的基本组成

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/XyrFYjhTTDqIIJShs_8q-A/zh-cn_image_0000002592217942.png?HW-CC-KV=V1&HW-CC-Date=20260611T062822Z&HW-CC-Expire=86400&HW-CC-Sign=94F2FC7106EAD157ED07EDCBC26F8EF918AB10DC0A38F3CDFE5171D953DCF8CD)

说明

自定义变量不能与基础通用属性/事件名重复。

* [UI装饰器](../UI装饰器总览/arkts-decorator-overview.md)： 用于装饰类、结构、方法以及变量，并赋予其特殊的含义。如上述示例中@Entry、@Component和@State都是装饰器，[@Component](../自定义组件/创建自定义组件/arkts-create-custom-components.md#component)表示自定义组件，[@Entry](../自定义组件/创建自定义组件/arkts-create-custom-components.md#entry)表示该自定义组件为入口组件，[@State](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md)表示组件中的状态变量，状态变量变化会触发UI刷新。
* [UI描述](../声明式UI描述/arkts-declarative-ui-description.md)：以声明式的方式来描述UI的结构，例如build()方法中的代码块。
* [自定义组件](../自定义组件/创建自定义组件/arkts-create-custom-components.md)：可复用的UI单元，可组合其他组件，如上述被@Component装饰的struct Hello。
* 系统组件：ArkUI框架中默认内置的基础和容器组件，可以直接调用，例如示例中的Column、Text、Divider、Button。
* [属性方法](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/ts-component-general-attributes.md)：组件可以通过链式调用配置多项属性，如fontSize()、width()、height()、backgroundColor()等。
* [事件方法](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/ts-component-general-events.md)：组件可以通过链式调用设置多个事件的响应逻辑，如跟随在Button后面的onClick()。

除此之外，ArkTS扩展了多种语法范式来使开发更加便捷：

* [@Builder](../组件扩展/@Builder装饰器：自定义构建函数/arkts-builder.md)/[@BuilderParam](../组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md)：特殊的封装UI描述的方法，细粒度的封装和复用UI描述。
* [@Extend](../组件扩展/@Extend装饰器：定义扩展组件样式/arkts-extend.md)/[@Styles](../组件扩展/@Styles装饰器：定义组件重用样式/arkts-style.md)：扩展系统组件和封装属性样式，更灵活地组合系统组件。
* [stateStyles](../组件扩展/stateStyles：多态样式/arkts-statestyles.md)：多态样式，可以依据组件的内部状态的不同，设置不同样式。
