---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview
title: 状态管理概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理概述
category: harmonyos-guides
scraped_at: 2026-06-11T14:28:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5408bad137240ebfcdda5840bdb249a9e6bec1ab078e91af939f3234bada0794
---
在前文的描述中，构建的页面主要为静态界面。如果要构建一个动态的、有交互的界面，就需要引入“状态”的概念。

**图1** 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7r4js4JTTN6XlV24AaAcXg/zh-cn_image_0000002622697503.gif?HW-CC-KV=V1&HW-CC-Date=20260611T062858Z&HW-CC-Expire=86400&HW-CC-Sign=3BA5CED72B75CAA88518394E9716D7960DBD4B78944B9AA2746987A6CC3BE432)

上面的示例中，用户与应用程序的交互触发了文本状态变更，状态变更引起了UI渲染，UI从“Hello World”变更为“Hello ArkUI”。

在声明式UI编程框架中，UI是程序状态的运行结果，用户构建了一个UI模型，其中应用的运行时状态作为参数。当参数改变时，UI作为返回结果，也将进行对应的改变。这些运行时的状态变化导致的UI重新渲染，在ArkUI中统称为状态管理机制。

自定义组件中的变量，必须使用装饰器装饰，才能成为状态变量，状态变量的改变会引起UI的渲染刷新。如果不使用状态变量，UI只能在初始化时渲染，后续将不会再刷新。下图展示了State和View（UI）之间的关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SHgSHvKsSOO0PbSmNTaQIQ/zh-cn_image_0000002592217978.png?HW-CC-KV=V1&HW-CC-Date=20260611T062858Z&HW-CC-Expire=86400&HW-CC-Sign=41A02B7558F543EB7847667B6274378BB54CC9CB7FD7BEA91EFD0FB8A9AEED63)

* View(UI)：UI渲染，指将build方法内的UI描述和@Builder装饰的方法内的UI描述映射到界面。
* State：状态，指驱动UI更新的数据。通过触发组件的事件方法，改变状态数据。状态数据的改变，引起UI的重新渲染。

在阅读状态管理文档前，开发者需要了解UI范式基本语法。建议提前阅读[基本语法概述](../../学习UI范式基本语法/基本语法概述/arkts-basic-syntax-overview.md)、[声明式UI描述](../../学习UI范式基本语法/声明式UI描述/arkts-declarative-ui-description.md)、[状态管理术语](../状态管理术语/arkts-state-management-glossary.md)和[自定义组件-创建自定义组件](../../学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md)。

说明

当前状态管理的功能仅支持在UI主线程使用，不能在子线程、Worker、TaskPool中使用。

## 状态管理版本介绍

当前状态管理分为V1、V2两个版本。

1. V2是V1的增强版本，正在持续迭代优化来为开发者提供更多功能和灵活性。
2. 对于新开发的应用，建议直接使用V2版本范式来进行开发。
3. 对于已经使用V1的应用，如果V1的功能和性能已能满足需求，则不必立即切换到V2。

## 状态管理（V1）

开发者可以选择使用状态管理V1版本进行应用开发。

### 装饰器总览

ArkUI状态管理V1提供了多种装饰器，通过使用这些装饰器，状态变量不仅可以观察组件内的改变，还可以在不同组件层级间传递，比如父子组件、跨组件层级，也可以观察全局范围内的变化。根据状态变量的影响范围，将所有的装饰器可以大致分为：

* 管理组件内状态的装饰器：组件级别的状态管理，可以观察同一个组件树上（即同一个页面内）组件内或不同组件层级的变量变化。
* 管理应用级状态的装饰器：应用级别的状态管理，可以观察不同页面，甚至不同UIAbility的状态变化，是应用内全局的状态管理。

装饰器可按数据传递形式和同步类型分为：只读的单向传递和可变更的双向传递。

图示如下，具体装饰器的介绍，可详见[管理组件拥有的状态](../状态管理（V1）/管理组件拥有的状态/arkts-v1-component-state-management.md)和[管理应用拥有的状态](../状态管理（V1）/管理应用拥有的状态/arkts-v1-application-state-management.md)。开发者可以利用这些能力来实现数据和UI的联动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/gxDb0b1pRxiADXGpVmWNKw/zh-cn_image_0000002592377912.png?HW-CC-KV=V1&HW-CC-Date=20260611T062858Z&HW-CC-Expire=86400&HW-CC-Sign=0AD6550EBF806CB4350FFD7C13919B33CD55C85A4DFC12D9B489CB84AC33FF59)

上图中，Components部分的装饰器为组件级别的状态管理，Application部分为应用的状态管理。开发者可以通过[@StorageLink](../状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storagelink)/[@LocalStorageLink](../状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstoragelink)实现应用和组件状态的双向同步，通过[@StorageProp](../状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storageprop)/[@LocalStorageProp](../状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstorageprop)实现应用和组件状态的单向同步。

[管理组件拥有的状态](../状态管理（V1）/管理组件拥有的状态/arkts-v1-component-state-management.md)，即图中Components级别的状态管理：

* [@State](../状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md)：@State装饰的变量拥有其所属组件的状态，可以作为其子组件单向和双向同步的数据源。当其数值改变时，会引起相关组件的渲染刷新。
* [@Prop](../状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md)：@Prop装饰的变量可以和父组件建立单向同步关系，@Prop装饰的变量是可变的，但修改不会同步回父组件。
* [@Link](../状态管理（V1）/管理组件拥有的状态/@Link装饰器：父子双向同步/arkts-link.md)：@Link装饰的变量可以和父组件建立双向同步关系，子组件中@Link装饰变量的修改会同步给父组件中建立双向数据绑定的数据源，父组件的更新也会同步给@Link装饰的变量。
* [@Provide/@Consume](../状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md)：@Provide/@Consume装饰的变量用于跨组件层级（多层组件）同步状态变量，可以不需要通过参数命名机制传递，通过alias（别名）或者属性名绑定。
* [@Observed](../状态管理（V1）/管理组件拥有的状态/@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化/arkts-observed-and-objectlink.md)：@Observed装饰class，需要观察多层嵌套场景的class需要被@Observed装饰。单独使用@Observed没有任何作用，需要和@ObjectLink、@Prop联用。
* [@ObjectLink](../状态管理（V1）/管理组件拥有的状态/@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化/arkts-observed-and-objectlink.md)：@ObjectLink装饰的变量接收@Observed装饰的class的实例，应用于观察多层嵌套场景，和父组件的数据源构建双向同步。

说明

仅[@Observed/@ObjectLink](../状态管理（V1）/管理组件拥有的状态/@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化/arkts-observed-and-objectlink.md)可以观察嵌套场景，其他的状态变量仅能观察第一层，详情见各个装饰器章节的“观察变化和行为表现”小节。

[管理应用拥有的状态](../状态管理（V1）/管理应用拥有的状态/arkts-v1-application-state-management.md)，即图中Application级别的状态管理：

* [AppStorage](../状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md)是应用程序中的一个特殊的单例[LocalStorage](../状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md)对象，是应用级的数据库，和进程绑定，通过[@StorageProp](../状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storageprop)和[@StorageLink](../状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storagelink)装饰器可以和组件联动。
* AppStorage是应用状态的“中枢”，将需要与组件（UI）交互的数据存入AppStorage，比如持久化数据[PersistentStorage](../状态管理（V1）/管理应用拥有的状态/PersistentStorage：持久化存储UI状态/arkts-persiststorage.md)和环境变量[Environment](../状态管理（V1）/管理应用拥有的状态/Environment：设备环境查询/arkts-environment.md)。UI再通过AppStorage提供的装饰器或API接口访问这些数据。
* 框架还提供了LocalStorage，AppStorage是LocalStorage特殊的单例。LocalStorage是应用程序声明的应用状态的内存“数据库”，通常用于页面级的状态共享，通过[@LocalStorageProp](../状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstorageprop)和[@LocalStorageLink](../状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstoragelink)装饰器可以和UI联动。

### 其他状态管理V1功能

[@Watch](../状态管理（V1）/管理组件拥有的状态/@Watch装饰器：状态变量更改通知/arkts-watch.md)用于监听状态变量的变化。

[$$运算符](../语法糖/$$语法：系统组件双向同步/arkts-two-way-sync.md)：给系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。

## 状态管理（V2）

为了增强状态管理V1版本的部分能力，例如深度观察、属性级更新等，ArkUI推出状态管理V2供开发者使用。

### 状态管理V1现状以及V2优点

状态管理V1使用代理观察数据，创建状态变量时，会同时创建一个数据代理观察者。该观察者可以感知代理变化，但无法感知实际数据变化，因此存在以下限制：

* 状态变量不能独立于UI存在，同一个数据被多个视图代理时，其中一个视图的更改不会通知其他视图更新。
* 只能感知对象属性第一层的变化，无法做到深度观测和深度监听。
* 在更改对象中属性以及更改数组中元素的场景下存在冗余更新的问题。
* 装饰器间配合使用限制多，不易用。组件中没有明确状态变量的输入与输出，不利于组件化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/jGOhQkIJRhaZLfjIexDJ3A/zh-cn_image_0000002622857419.png?HW-CC-KV=V1&HW-CC-Date=20260611T062858Z&HW-CC-Expire=86400&HW-CC-Sign=BF07186BBC121A791AA2BAEE08BA3F6CEB0394F1C3E4CD4D7ADE3521B9268468)

状态管理V2增强了数据的观察能力，使数据本身可观察。更改数据时，会触发相应视图的更新。相较于状态管理V1，状态管理V2有如下优点：

* 状态变量独立于UI，更改数据会触发相应视图的更新。
* 支持对象的深度观测和深度监听，且深度观测机制不影响观测性能。
* 支持对象中属性级精准更新及数组中元素的最小化更新。
* 装饰器易用性高、拓展性强，在组件中明确输入与输出，有利于组件化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/FZcq9i3sShmcDh6x-kuDrA/zh-cn_image_0000002622697541.png?HW-CC-KV=V1&HW-CC-Date=20260611T062858Z&HW-CC-Expire=86400&HW-CC-Sign=2AE4F1DC409A7AB991E9E726BAA4AD7D10CB7D81071F466822BE075DEBB843B4)

### 装饰器总览

状态管理（V2）提供了一套全新的装饰器。

* [@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)：@ObservedV2装饰器装饰class，使得被装饰的class具有深度监听的能力。@ObservedV2和@Trace配合使用可以使class中的属性具有深度观测的能力。
* [@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)：@Trace装饰器装饰被@ObservedV2装饰的class中的属性，被装饰的属性具有深度观测的能力。
* [@ComponentV2](../../学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2)：使用@ComponentV2装饰的struct中能使用新的装饰器。例如：@Local、@Param、@Event、@Once、@Monitor、@Provider、@Consumer。
* [@Local](../状态管理（V2）/管理组件拥有的状态/@Local装饰器：组件内部状态/arkts-new-local.md)：@Local装饰的变量为组件内部状态，无法从外部初始化。
* [@Param](../状态管理（V2）/管理组件拥有的状态/@Param：组件外部输入/arkts-new-param.md)：@Param装饰的变量作为组件的输入，可以接受从外部传入初始化并同步。
* [@Once](../状态管理（V2）/管理组件拥有的状态/@Once：初始化同步一次/arkts-new-once.md)：@Once装饰的变量仅初始化时同步一次，需要与@Param一起使用。
* [@Event](../状态管理（V2）/管理组件拥有的状态/@Event装饰器：规范组件输出/arkts-new-event.md)：@Event装饰方法类型，作为组件输出，可以通过该方法影响父组件中变量。
* [@Monitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor)：@Monitor装饰器用于@ComponentV2装饰的自定义组件或@ObservedV2装饰的类中，能够对状态变量进行深度监听。
* [@Provider和@Consumer](../状态管理（V2）/管理组件拥有的状态/@Provider装饰器和@Consumer装饰器：跨组件层级双向同步/arkts-new-provider-and-consumer.md)：用于跨组件层级双向同步。
* [@Computed](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed)：计算属性，在被计算的值变化的时候，只会计算一次。主要应用于解决UI多次重用该属性从而重复计算导致的性能问题。
* [!!语法](../语法糖/!!语法：双向绑定/arkts-new-binding.md)：双向绑定语法糖。

### 状态管理V1与V2能力对比

| V1能力 | V2能力 | 说明 |
| --- | --- | --- |
| @Observed | @ObservedV2 | 表明当前对象为可观察对象。但两者能力并不相同。  @Observed可观察第一层的属性，需要搭配@ObjectLink使用才能生效。  @ObservedV2本身无观察能力，仅代表当前class可被观察，如果要观察其属性，需要搭配@Trace使用。 |
| @Track | @Trace | V1装饰器@Track为精确观察，可以不依赖@Observed单独使用。不使用则无法做到类属性的精准观察。  V2@Trace装饰的属性可以被精确跟踪观察。 |
| @Component | @ComponentV2 | @Component为搭配V1状态变量使用的自定义组件装饰器。  @ComponentV2为搭配V2状态变量使用的自定义组件装饰器。 |
| @State | 无外部初始化：@Local  外部初始化一次：@Param@Once | @State和@Local类似都是数据源的概念，区别是@State可以外部传入初始化，而@Local无法外部传入初始化。 |
| @Prop | @Param | @Prop和@Param类似都是自定义组件参数的概念。当输入参数为复杂类型时，@Prop为深拷贝，@Param为引用。 |
| @Link | @Param@Event | @Link是框架自己封装实现的双向同步，对于V2开发者可以通过@Param@Event自己实现双向同步。 |
| @ObjectLink | @Param | 直接兼容，@ObjectLink需要被@Observed装饰的class的实例初始化，@Param没有此限制。 |
| @Provide | @Provider | 兼容。 |
| @Consume | @Consumer | 兼容。 |
| @Watch | @Monitor | @Watch用于监听V1状态变量的变化，具有监听状态变量本身和其第一层属性变化的能力。状态变量可观察到的变化会触发其@Watch监听事件。  @Monitor用于监听V2状态变量的变化，搭配@Trace使用，可有深层监听的能力。状态变量在一次事件中多次变化时，仅会以最终的结果判断是否触发@Monitor监听事件。 |
| LocalStorage | 全局@ObservedV2@Trace | 兼容。 |
| AppStorage | AppStorageV2 | 兼容。 |
| Environment | 调用Ability接口获取系统环境变量 | Environment获取环境变量能力和AppStorage耦合。在V2中可直接调用Ability接口获取系统环境变量。 |
| PersistentStorage | PersistenceV2 | PersistentStorage持久化能力和AppStorage耦合，PersistenceV2持久化能力可独立使用。 |
| 自定义组件生命周期 | 自定义组件生命周期 | 均支持。[aboutToAppear](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttoappear)、[onDidBuild](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#ondidbuild12)、[aboutToDisappear](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttodisappear)。 |
| 页面生命周期 | 页面生命周期 | 均支持。[onPageShow](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#onpageshow)、[onPageHide](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#onpagehide)、[onBackPress](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#onbackpress)。 |
| @Reusable | @ReusableV2 | 组件复用。包括：[aboutToReuse](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttoreuse10)、[aboutToRecycle](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttorecycle10)。 |
| $$ | !! | 双向绑定。V2建议使用!!实现双向绑定。 |
| @CustomDialog | [openCustomDialog](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (PromptAction)/arkts-apis-uicontext-promptaction.md#opencustomdialog12>)接口 | 自定义弹窗。V2建议使用openCustomDialog实现自定义弹窗功能。 |
| WithTheme | WithTheme | 主题。用于设置应用局部页面自定义主题风格。包括：[onWillApplyTheme](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#onwillapplytheme12)。  从API version 18开始，该接口支持在状态管理V2组件中使用。 |
| 系统预置UI组件库 | 系统预置UI组件库 | 系统预置UI组件库 。支持V1的系统预置UI组件，例如：[Dialog](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/弹出框 (Dialog)/ohos-arkui-advanced-dialog.md>)、[ProgressButton](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ProgressButton/ohos-arkui-advanced-progressbutton.md)、[SegmentButton](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SegmentButton/ohos-arkui-advanced-segmentbutton.md)。  从API version 18开始，系统预置UI组件支持在状态管理V2组件中使用，例如：[DialogV2](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/DialogV2/ohos-arkui-advanced-dialogv2.md)、[ProgressButtonV2](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ProgressButtonV2/ohos-arkui-advanced-progressbuttonv2.md)、[SegmentButtonV2](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SegmentButtonV2/ohos-arkui-advanced-segmentbuttonv2.md)。 |
| animateTo | 部分场景不支持 | 当前某些场景下，在状态管理V2中使用animateTo动画，会产生异常效果，详见：[在状态管理V2中使用animateTo动画效果异常](../状态管理（V2）/管理组件拥有的状态/@Local装饰器：组件内部状态/arkts-new-local.md#在状态管理v2中使用animateto动画效果异常)。 |

有关V1向V2的迁移可参考[迁移指导](../状态管理V1-V2迁移指导/V1-V2迁移概述/arkts-v1-v2-migration.md)，有关V1与V2的混用可参考[状态管理V1和V2混用场景](../状态管理V1-V2迁移指导/状态管理V1和V2混用场景/v1v2-mixing.md)。
