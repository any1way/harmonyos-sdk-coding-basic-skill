---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-decorator-overview
title: UI装饰器总览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > UI装饰器总览
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:24+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:0c3ea5e2d5f18e1cf36221a323e09adb99346c349ef881e5e4f8ccdf93732803
---
在声明式UI开发范式中，UI是程序状态的运行结果，状态的变化会驱动UI的刷新。ArkUI提供了一套装饰器机制，使开发者能够便捷地定义和管理状态变量，实现数据与UI的联动。

ArkUI包含的V2状态管理装饰器列表如下：

| V2状态管理装饰器 | 装饰器说明 |
| --- | --- |
| [@ComponentV2](../自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2) | 创建自定义组件。 |
| [@Local](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Local装饰器：组件内部状态/arkts-new-local.md) | 组件内部状态。 |
| [@Param](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Param：组件外部输入/arkts-new-param.md) | 组件外部输入。 |
| [@Once](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Once：初始化同步一次/arkts-new-once.md) | 初始化同步一次。 |
| [@Event](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Event装饰器：规范组件输出/arkts-new-event.md) | 规范组件输出。 |
| [@Provider](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Provider装饰器和@Consumer装饰器：跨组件层级双向同步/arkts-new-provider-and-consumer.md) | 与后代状态双向同步。 |
| [@Consumer](../../学习UI范式状态管理/状态管理（V2）/管理组件拥有的状态/@Provider装饰器和@Consumer装饰器：跨组件层级双向同步/arkts-new-provider-and-consumer.md) | 与祖先状态双向同步。 |
| [@Monitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor) | 状态变量修改异步监听。 |
| [@SyncMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-syncmonitor) | 状态变量修改同步监听。 |
| [@Computed](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed) | 计算属性。 |
| [@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace) | 标记类可观察。 |
| [@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace) | 标记类属性可观察。 |
| [@Type](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-type) | 标记类属性的类型。 |
| [@ReusableV2](../自定义组件/自定义组件复用/@ReusableV2装饰器：V2组件复用/arkts-new-reusablev2.md) | 标记组件可复用。 |

ArkUI包含的V1状态管理装饰器列表如下：

| V1状态管理装饰器 | 装饰器说明 |
| --- | --- |
| [@Component](../自定义组件/创建自定义组件/arkts-create-custom-components.md#component) | 创建自定义组件。 |
| [@State](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md) | 基础状态变量。 |
| [@Prop](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md) | 建立父子状态单向同步。 |
| [@Link](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Link装饰器：父子双向同步/arkts-link.md) | 建立父子状态双向同步。 |
| [@ObjectLink](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化/arkts-observed-and-objectlink.md) | 嵌套类对象属性变化观察。 |
| [@Provide](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md) | 与后代状态双向同步。 |
| [@Consume](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md) | 与祖先状态双向同步。 |
| [@Watch](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Watch装饰器：状态变量更改通知/arkts-watch.md) | 状态变量变化监听。 |
| [@StorageLink](../../学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storagelink) | 与AppStorage中对应的属性建立双向数据同步。 |
| [@StorageProp](../../学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storageprop) | 与AppStorage中对应的属性建立单向数据同步。 |
| [@LocalStorageLink](../../学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstoragelink) | 与LocalStorage中对应的属性建立双向数据同步。 |
| [@LocalStorageProp](../../学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstorageprop) | 与LocalStorage中对应的属性建立单向数据同步。 |
| [@Observed](../../学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化/arkts-observed-and-objectlink.md) | 标记类可观察。 |
| [@Track](../../学习UI范式状态管理/状态管理（V1）/管理数据对象的状态/@Track装饰器：class对象属性级更新/arkts-track.md) | 类对象属性级更新。 |
| [@Reusable](../自定义组件/自定义组件复用/@Reusable装饰器：V1组件复用/arkts-reusable.md) | 标记组件可复用。 |

ArkUI包含的通用UI装饰器列表如下：

| 通用装饰器 | 装饰器说明 |
| --- | --- |
| [@Entry](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/@Entry：页面入口/ts-universal-entry.md#entry) | 标记页面入口。 |
| [@Builder](../组件扩展/@Builder装饰器：自定义构建函数/arkts-builder.md) | 自定义构建函数。 |
| [@LocalBuilder](<../组件扩展/@LocalBuilder装饰器： 维持组件关系/arkts-localbuilder.md>) | 维持组件关系。 |
| [@BuilderParam](../组件扩展/@BuilderParam装饰器：引用@Builder函数/arkts-builderparam.md) | 引用@Builder函数。 |
| [@Styles](../组件扩展/@Styles装饰器：定义组件重用样式/arkts-style.md) | 定义组件重用样式。 |
| [@Extend](../组件扩展/@Extend装饰器：定义扩展组件样式/arkts-extend.md) | 定义扩展组件样式。 |
| [@AnimatableExtend](../组件扩展/@AnimatableExtend装饰器：定义可动画属性/arkts-animatable-extend.md) | 定义可动画属性。 |
| [@Require](../@Require装饰器：校验构造传参/arkts-require.md) | 校验构造传参。 |
| [@Env](../../学习响应式环境变量/@Env：环境变量/arkts-env-system-property.md) | 环境变量。 |
