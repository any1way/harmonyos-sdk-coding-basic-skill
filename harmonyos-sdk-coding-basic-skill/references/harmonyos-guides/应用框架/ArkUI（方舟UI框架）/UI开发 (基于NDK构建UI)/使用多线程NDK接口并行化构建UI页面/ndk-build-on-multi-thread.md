---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-on-multi-thread
title: 使用多线程NDK接口并行化构建UI页面
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用多线程NDK接口并行化构建UI页面
category: harmonyos-guides
scraped_at: 2026-06-01T11:07:17+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:8a5564e2db47b7559c7bfa3f930fa2d83fe17c390649543e864888ec1c05ede2
---
## 概述

在API version 22之前，UI组件的创建与属性设置等操作必须在应用的UI线程中执行。这导致开发者在使用NDK接口时，需将组件创建与属性设置等操作通过任务队列提交至UI线程执行，限制了组件创建过程的灵活性及应用的性能。

随着应用程序功能的日益复杂，应用页面内需要动态创建大量UI组件，这些组件的创建任务堆积在单一的UI线程中执行，会导致应用启动缓慢、动画丢帧及页面卡顿，直接影响用户体验。

针对这些问题，在API version 22，NDK接口引入了多线程支持能力，为开发者带来了以下提升：

* **简化调用流程：** 开发者无需通过任务队列将组件创建任务提交至UI线程执行，可以在任意线程中直接调用组件创建和属性设置等接口，减少线程上下文切换次数，简化UI框架与应用间的交互逻辑。
* **性能与体验显著优化：** 组件创建和属性设置等接口支持多线程并发调用，能够充分利用设备的多核CPU，降低页面创建阶段的总体耗时。UI线程专注于动画渲染与用户输入，确保界面流畅及交互及时。
* **为后续功能扩展提供更好的灵活性：** 组件创建和属性设置等接口支持多线程调用，不仅能够解决应用当前的性能瓶颈问题，还为未来开发更复杂、高负载的UI页面提供扩展空间，帮助开发者在设计时拥有更多的灵活性，为持续提升用户体验创造条件。

综上所述，在复杂业务场景中，多线程NDK接口将为开发者带来高性能的UI页面创建体验。

## 多线程NDK接口使用方式

* 在使用多线程NDK接口前，建议开发者先阅读[NDK接口概述](../基于NDK构建UI概述/ndk-build-ui-overview.md)，掌握使用NDK接口必备的基本概念和基础知识。
* 为降低开发者适配多线程NDK接口的成本，多线程NDK接口的获取和使用方式与现有NDK接口保持一致。只需要调用[OH\_ArkUI\_GetModuleInterface](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_interface.h/capi-native-interface-h.md#oh_arkui_getmoduleinterface>)接口，入参传入[ARKUI\_MULTI\_THREAD\_NATIVE\_NODE](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_interface.h/capi-native-interface-h.md#arkui_nativeapivariantkind>)即可获取多线程NDK接口集合。例如：

  ```
  1. ArkUI_NativeNodeAPI_1 *multiThreadNodeAPI = nullptr;
  2. // 获取多线程NDK接口集合。
  3. OH_ArkUI_GetModuleInterface(ARKUI_MULTI_THREAD_NATIVE_NODE, ArkUI_NativeNodeAPI_1, multiThreadNodeAPI);

  5. if (!multiThreadNodeAPI) {
  6. return;
  7. }
  8. // 调用集合中支持多线程的createNode接口创建UI组件。
  9. auto node = multiThreadNodeAPI->createNode(ARKUI_NODE_COLUMN);
  ```

支持多线程调用的全量NDK接口请参考[多线程NDK接口集合规格](ndk-build-on-multi-thread.md#多线程ndk接口集合规格)。

开发者可以使用多线程NDK接口在任意线程创建UI组件并设置属性，但是必须在UI线程中，把UI组件挂载到UI主树上。可以通过如下接口完成多线程UI组件创建任务的分发和执行。

* 对于可以在非UI线程执行的任务（如组件创建、属性设置等），可以使用[OH\_ArkUI\_PostAsyncUITask](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postasyncuitask>)接口，将组件创建和属性设置等任务调度到系统线程池中执行，之后将组件挂载到主树的任务提交到UI线程执行。
* 当开发者需要在自己创建的非UI线程中创建UI组件时，使用[OH\_ArkUI\_PostUITask](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postuitask>)接口将组件挂载到主树的任务提交到UI线程执行。
* 开发者在多线程创建UI组件的过程中需要执行只支持UI线程的任务时，使用[OH\_ArkUI\_PostUITaskAndWait](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postuitaskandwait>)接口将任务提交到UI线程执行，调用此接口的非UI线程等待函数执行完成后继续创建组件。当UI线程负载很高时，调用此接口的非UI线程可能长时间阻塞，会影响多线程创建UI组件的性能收益，不建议频繁使用。

## 多线程NDK接口适配说明

1. 多线程NDK接口适用于页面跳转和列表滑动等高负载且性能敏感的场景，此类场景下UI线程需要执行耗时从几ms到几十ms的组件创建任务，开发者可以将组件创建任务拆分成多个子任务，分派给多个线程并发执行，以降低UI线程负载，提高页面启动与更新流畅度。
2. 当开发者在自己创建的线程中创建UI组件时，基于设备CPU核数等客观条件，建议并行的线程数量不要超过4个，以避免线程调度带来的性能开销。
3. 开发者可以在非UI线程预创建常用组件树，为性能敏感场景提供更好的用户体验。

## 多线程NDK接口调用规范

框架将UI组件划分为Free（游离）和Attached（已挂载）两种状态。

使用多线程[createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>)接口创建的UI组件初始为Free状态，且可以在Free和Attached两种状态间进行转换，使用其他方式创建的UI组件初始为Attached状态且状态不可转换。

说明

* 开发者可以在任意线程使用多线程NDK接口操作处于Free状态的组件，为保证应用功能正常和线程安全，需遵守如下使用约束：

  + 禁止多线程同时操作同一个处于Free状态的组件或组件树，处于Free状态的组件内部是无锁的，多线程同时访问会出现稳定性问题。
  + 禁止使用[多线程NDK接口集合](ndk-build-on-multi-thread.md#多线程ndk接口集合规格)外的其他NDK接口操作处于Free状态的组件，需先将组件转换为Attach状态后才可以在UI线程使用其他NDK接口，否则接口功能会出现异常。
* 为兼顾性能，上述约束框架侧无运行时校验，需要开发者自行保证。
* 为保证接口多线程安全，处于Free状态的组件的一部分属性通过[setAttribute](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute>)设置后，无法立即通过[getAttribute](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getattribute>)接口读取到，需要将组件转换为Attached状态后才能读取到正确的属性值。

当开发者进行如下操作后，UI组件状态从Free转换为Attached：

* 使用多线程[markDirty](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#markdirty>)、[measureNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#measurenode>)或[layoutNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#layoutnode>)接口对Free组件进行标脏、测量或布局后，此组件所在组件树内所有处于Free状态的组件转换为Attached状态。
* 使用多线程[组件树操作](ndk-build-on-multi-thread.md#组件树操作)接口将处于Free状态的组件挂载为Attached组件的子组件，此组件所在组件树内所有处于Free状态的组件转换为Attached状态。
* 使用多线程[组件树操作](ndk-build-on-multi-thread.md#组件树操作)接口把Attached组件挂载为处于Free状态的组件的子组件，此组件所在组件树内所有处于Free状态的组件转换为Attached状态。

对于状态可转换的Attached组件，当开发者进行如下操作后，UI组件状态从Attached转换为Free：

* 使用多线程[组件树操作](ndk-build-on-multi-thread.md#组件树操作)接口将组件从组件树上移除，且移除后的组件所在组件树不包含不可转换的Attached组件，此组件所在组件树内所有组件转换为Free状态。

基于上述状态转换规则，每个UI组件树内所有组件都处于相同状态。

## 多线程NDK接口的错误与异常

多线程NDK接口调用规范请参考[多线程NDK接口集合规格](ndk-build-on-multi-thread.md#多线程ndk接口集合规格)。调用多线程NDK接口时必须检查接口返回值，如下两种情况接口会返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。

* 在非UI线程中调用集合中不支持多线程的接口。
* 在非UI线程调用多线程NDK接口操作处于Attached状态的组件。

多线程NDK适配过程中遇到的更多问题可以参考[UI并行化常见问题](../../UI开发调试调优/UI开发常见问题/UI并行化常见问题/multi-thread-ui-build-faq.md)。

## 多线程NDK接口集合规格

集合中支持多线程调用的接口包括：[组件创建销毁](ndk-build-on-multi-thread.md#组件创建销毁)，[组件属性读写](ndk-build-on-multi-thread.md#组件属性读写)，[组件事件注册解注册](ndk-build-on-multi-thread.md#组件事件注册解注册)，[组件树操作](ndk-build-on-multi-thread.md#组件树操作)和[组件自定义数据读写](ndk-build-on-multi-thread.md#组件自定义数据读写)。

集合中仅支持UI线程调用的接口包括：[全局事件注册解注册](ndk-build-on-multi-thread.md#全局事件注册解注册)和[组件测算布局](ndk-build-on-multi-thread.md#组件测算布局)。

### 组件创建销毁

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [createNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode>) )([ArkUI\_NodeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodetype>) type) | 基于[ArkUI\_NodeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodetype>)生成对应的Free节点并返回Free节点对象指针。 | 支持 | 支持在任意线程调用。 |
| void(\* [disposeNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#disposenode>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 销毁节点指针指向的节点对象。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口调用无效。 |

### 组件属性读写

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| int32\_t(\* [setAttribute](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>) attribute, const [ArkUI\_AttributeItem](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_AttributeItem/capi-arkui-nativemodule-arkui-attributeitem.md>) \*item) | 设置node节点的属性。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| const [ArkUI\_AttributeItem](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_AttributeItem/capi-arkui-nativemodule-arkui-attributeitem.md>) \*(\* [getAttribute](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getattribute>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>) attribute) | 获取node节点的属性。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |
| int32\_t(\* [resetAttribute](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#resetattribute>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeAttributeType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>) attribute) | 重置node节点的属性为默认值。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [setLengthMetricUnit](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_LengthMetricUnit](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_lengthmetricunit>) unit) | 指定node节点的单位。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |

### 组件事件注册解注册

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| int32\_t(\* [registerNodeEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeEventType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeeventtype>) eventType, int32\_t targetId, void \*userData) | 向node节点注册事件。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| void(\* [unregisterNodeEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodeevent>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeEventType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeeventtype>) eventType) | node节点解注册事件。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口调用无效。 |
| int32\_t(\* [registerNodeCustomEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomevent>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeCustomEventType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodecustomeventtype>) eventType, int32\_t targetId, void \*userData) | 向node节点注册自定义事件。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| void(\* [unregisterNodeCustomEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodecustomevent>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeCustomEventType](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodecustomeventtype>) eventType) | node节点解注册自定义事件。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口调用不生效。 |
| int32\_t(\* [addNodeEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodeeventreceiver>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, void(\*eventReceiver)([ArkUI\_NodeEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeEvent/capi-arkui-nativemodule-arkui-nodeevent.md>) \*event)) | 向node节点注册事件回调函数，用于接收该组件产生的组件事件。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [removeNodeEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodeeventreceiver>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, void(\*eventReceiver)([ArkUI\_NodeEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeEvent/capi-arkui-nativemodule-arkui-nodeevent.md>) \*event)) | 删除node节点上注册的事件回调函数。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [addNodeCustomEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodecustomeventreceiver>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, void(\*eventReceiver)([ArkUI\_NodeCustomEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeCustomEvent/capi-arkui-nativemodule-arkui-nodecustomevent.md>) \*event)) | 向node节点注册自定义事件回调函数，用于接收该组件产生的自定义事件（如布局事件，绘制事件）。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [removeNodeCustomEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodecustomeventreceiver>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, void(\*eventReceiver)([ArkUI\_NodeCustomEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeCustomEvent/capi-arkui-nativemodule-arkui-nodecustomevent.md>) \*event)) | 删除node节点上注册的自定义事件回调函数。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |

### 组件树操作

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| int32\_t(\* [addChild](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addchild>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) child) | 将child节点挂载到parent节点的子节点列表中。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [removeChild](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removechild>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) child) | 将child节点从parent节点的子节点列表中移除。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [insertChildAfter](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildafter>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) child, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) sibling) | 将child节点挂载到parent节点的子节点列表中，挂载位置在sibling节点之后。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [insertChildBefore](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildbefore>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) child, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) sibling) | 将child节点挂载到parent节点的子节点列表中，挂载位置在sibling节点之前。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [insertChildAt](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#insertchildat>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent, [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) child, int32\_t position) | 将child节点挂载到parent节点的子节点列表中，挂载位置由position指定。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getParent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getparent>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的父节点。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [removeAllChildren](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removeallchildren>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) parent) | 移除node节点的所有子节点。 | 支持 | 在非UI线程调用函数操作Attached节点节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| uint32\_t(\* [getTotalChildCount](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#gettotalchildcount>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的子节点个数。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回0。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getChildAt](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getchildat>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, int32\_t position) | 获取node节点的子节点指针，位置由position指定。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getFirstChild](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getfirstchild>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的第一个子节点指针。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getLastChild](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getlastchild>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的最后一个子节点指针。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getPreviousSibling](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getprevioussibling>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的上一个兄弟节点指针。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |
| [ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>)(\* [getNextSibling](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getnextsibling>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点的下一个兄弟节点指针。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |

### 组件自定义数据读写

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| int32\_t(\* [setUserData](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setuserdata>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, void \*userData) | 在node节点上保存自定义数据。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| void \*(\* [getUserData](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getuserdata>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点上保存的自定义数据。 | 支持 | 在非UI线程调用函数操作Attached节点时，接口返回空指针。 |

### 全局事件注册解注册

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| void(\* [registerNodeEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver>) )(void(\*eventReceiver)([ArkUI\_NodeEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeEvent/capi-arkui-nativemodule-arkui-nodeevent.md>) \*event)) | 注册节点事件回调统一入口函数。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口不生效。 |
| void(\* [unregisterNodeEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodeeventreceiver>) )() | 解注册节点事件回调统一入口函数。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口不生效。 |
| void(\* [registerNodeCustomEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomeventreceiver>) )(void(\*eventReceiver)([ArkUI\_NodeCustomEvent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NodeCustomEvent/capi-arkui-nativemodule-arkui-nodecustomevent.md>) \*event)) | 注册节点自定义事件回调统一入口函数。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口不生效。 |
| void(\* [unregisterNodeCustomEventReceiver](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodecustomeventreceiver>) )() | 解注册节点自定义事件回调统一入口函数。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口不生效。 |

### 组件测算布局

| 接口名 | 描述 | 非UI线程调用 | 多线程规格 |
| --- | --- | --- | --- |
| int32\_t(\* [setMeasuredSize](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setmeasuredsize>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, int32\_t width, int32\_t height) | 在测算回调函数中设置组件测算完成后的宽和高。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [setLayoutPosition](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlayoutposition>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, int32\_t positionX, int32\_t positionY) | 在布局回调函数中设置组件的位置。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| [ArkUI\_IntSize](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_IntSize/capi-arkui-nativemodule-arkui-intsize.md>)(\* [getMeasuredSize](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getmeasuredsize>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点测算完成后的宽高尺寸。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回默认值。 |
| [ArkUI\_IntOffset](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_IntOffset/capi-arkui-nativemodule-arkui-intoffset.md>)(\* [getLayoutPosition](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getlayoutposition>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node) | 获取node节点布局完成后的位置。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回默认值。 |
| int32\_t(\* [measureNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#measurenode>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_LayoutConstraint](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_LayoutConstraint/capi-arkui-nativemodule-arkui-layoutconstraint.md>) \*Constraint) | 对node节点进行测算，可以通过getMeasuredSize获取测算后的大小。节点所在组件树内所有Free节点的状态转换为Attached。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| int32\_t(\* [layoutNode](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#layoutnode>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, int32\_t positionX, int32\_t positionY) | 对node节点进行布局并传递该组件相对父组件的期望位置。节点所在组件树内所有Free节点的状态转换为Attached。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口返回错误码[ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_errorcode>)。 |
| void(\* [markDirty](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeNodeAPI_1/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#markdirty>) )([ArkUI\_NodeHandle](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_Node/capi-arkui-nativemodule-arkui-node8h.md>) node, [ArkUI\_NodeDirtyFlag](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodedirtyflag>) dirtyFlag) | 强制标记node节点重新执行测量、布局或者绘制的区域。节点所在组件树内所有Free节点的状态转换为Attached。 | 不支持 | 只支持UI线程调用，在非UI线程调用接口调用不生效。 |

## 多线程NDK接口使用示例

此示例构造了一个多线程创建UI组件的场景，页面显示的Button组件在非UI线程被并行创建。

点击CreateNodeTree按钮触发在多个非UI线程并行创建Button组件，之后在UI线程将创建完成的Button组件挂载到UI主树上，使组件显示在页面上。点击DisposeNodeTree按钮将已创建的组件从UI主树上卸载并销毁，清空页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/TGkq8vUXTuq8vfCg7oDm7g/zh-cn_image_0000002583118656.gif?HW-CC-KV=V1&HW-CC-Date=20260601T030716Z&HW-CC-Expire=86400&HW-CC-Sign=451B1DD562F3806174D5110D47E3446E355F1D6BF0AD24E93CAEE5B8B6693272)

示例主要展示了如何获取和使用多线程NDK接口，并使用[OH\_ArkUI\_PostAsyncUITask](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postasyncuitask>)、[OH\_ArkUI\_PostUITask](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postuitask>)和[OH\_ArkUI\_PostUITaskAndWait](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_postuitaskandwait>)等接口将组件创建和属性设置等任务分发到多线程并行执行。

为简化编程和工程管理，在开始编写并行化组件创建代码前，请先参考[接入ArkTS页面](../接入ArkTS页面/ndk-access-the-arkts-page.md)指导文档，在Native侧使用面向对象的方式将ArkUI\_NodeHandle封装为ArkUINode对象。

```
1. // index.ets
2. import { NodeContent } from '@kit.ArkUI';
3. import entry from 'libentry.so';

5. @Component
6. struct CAPIComponent {
7. private rootSlot = new NodeContent();

9. aboutToAppear(): void {
10. // 页面显示前多线程创建Native组件。
11. entry.createNodeTreeOnMultiThread(this.rootSlot, this.getUIContext());
12. }

14. aboutToDisappear(): void {
15. // 页面销毁前释放已创建的Native组件。
16. entry.disposeNodeTreeOnMultiThread(this.rootSlot);
17. }

19. build() {
20. Column() {
21. // Native组件挂载点。
22. ContentSlot(this.rootSlot)
23. }
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State isShow: boolean = false;
31. @State message: string = "CreateNodeTree";

33. build() {
34. Flex() {
35. Column() {
36. Text('CreateNodeTreeOnMultiThread')
37. .fontSize(18)
38. .fontWeight(FontWeight.Bold)
39. Button(this.message)
40. .onClick(() => {
41. this.isShow = !this.isShow;
42. if (this.isShow) {
43. this.message = "DisposeNodeTree"
44. } else {
45. this.message = "CreateNodeTree"
46. }
47. })
48. if (this.isShow) {
49. CAPIComponent()
50. }
51. }.width('100%')
52. }.width('100%')
53. }
54. }
```

```
1. // index.d.ts
2. // entry/src/main/cpp/types/libentry/Index.d.ts
3. export const createNativeRoot: (content: Object) => void;
4. export const destroyNativeRoot: () => void;
5. export const createNodeTreeOnMultiThread: (content1: Object, content2: Object) => void;
6. export const disposeNodeTreeOnMultiThread: (content1: Object) => void;
```

```
1. # CMakeLists.txt
2. # the minimum version of CMake.
3. cmake_minimum_required(VERSION 3.5.0)
4. project(ndk_build_on_multi_thread)

6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

8. if(DEFINED PACKAGE_FIND_FILE)
9. include(${PACKAGE_FIND_FILE})
10. endif()

12. include_directories(${NATIVERENDER_ROOT_PATH}
13. ${NATIVERENDER_ROOT_PATH}/include)

15. add_library(entry SHARED napi_init.cpp NativeEntry.cpp NativeModule.h ArkUIBaseNode.h ArkUINode.h ArkUIListNode.h ArkUIListItemNode.h ArkUITextNode.h NormalTextListExample.h CreateNode.h CreateNode.cpp)
16. target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libhilog_ndk.z.so)
```

```
1. // NativeModule.h
2. #ifndef MYAPPLICATION_NATIVEMODULE_H
3. #define MYAPPLICATION_NATIVEMODULE_H

5. #include <arkui/native_node.h>
6. #include <arkui/native_interface.h>
7. #include <cassert>

9. namespace NativeModule {

11. class NativeModuleInstance {
12. public:
13. static NativeModuleInstance *GetInstance() {
14. static NativeModuleInstance instance;
15. return &instance;
16. }

18. NativeModuleInstance() {
19. // 获取多线程NDK接口的函数指针结构体对象，用于后续操作。
20. OH_ArkUI_GetModuleInterface(ARKUI_MULTI_THREAD_NATIVE_NODE, ArkUI_NativeNodeAPI_1, arkUINativeNodeApi_);
21. assert(arkUINativeNodeApi_);
22. }
23. // 暴露给其他模块使用。
24. ArkUI_NativeNodeAPI_1 *GetNativeNodeAPI() { return arkUINativeNodeApi_; }

26. private:
27. ArkUI_NativeNodeAPI_1 *arkUINativeNodeApi_ = nullptr;
28. };
29. } // namespace NativeModule

31. #endif // MYAPPLICATION_NATIVEMODULE_H
```

```
1. // CreateNode.h
2. #ifndef MYAPPLICATION_CREATENODE_H
3. #define MYAPPLICATION_CREATENODE_H

5. // 封装的ArkUINode对象，参考接入ArkTS页面指导文档。
6. #include "ArkUINode.h"

8. #include <js_native_api.h>

10. namespace NativeModule {
11. // 封装Button组件。
12. class ArkUIButtonNode: public ArkUINode {
13. public:
14. ArkUIButtonNode() :
15. ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_BUTTON)) {}
16. int32_t SetLabel(ArkUI_AttributeItem& label_item) {
17. return nativeModule_->setAttribute(handle_, NODE_BUTTON_LABEL, &label_item);
18. }
19. int32_t SetMargin(ArkUI_AttributeItem& item) {
20. return nativeModule_->setAttribute(handle_, NODE_MARGIN, &item);
21. }
22. };

24. // 封装Row组件。
25. class ArkUIRowNode: public ArkUINode {
26. public:
27. ArkUIRowNode() :
28. ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_ROW)) {}
29. };

31. // 封装Scroll组件。
32. class ArkUIScrollNode: public ArkUINode {
33. public:
34. ArkUIScrollNode() :
35. ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_SCROLL)) {}
36. };

38. // 封装Column组件。
39. class ArkUIColumnNode: public ArkUINode {
40. public:
41. ArkUIColumnNode() :
42. ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_COLUMN)) {}
43. };

45. // 多线程创建组件。
46. napi_value CreateNodeTreeOnMultiThread(napi_env env, napi_callback_info info);
47. // 释放多线程创建的组件。
48. napi_value DisposeNodeTreeOnMultiThread(napi_env env, napi_callback_info info);
49. } // namespace NativeModule

51. #endif // MYAPPLICATION_CREATENODE_H
```

```
1. // CreateNode.cpp
2. #include "CreateNode.h"

4. #include <cstdint>
5. #include <hilog/log.h>
6. #include <map>
7. #include <string>
8. #include <thread>
9. #include <napi/native_api.h>
10. #include <arkui/native_node_napi.h>

12. namespace NativeModule {
13. #define FRAMEWORK_NODE_TREE_NUMBER 4 // 在框架线程创建组件树的数量。
14. #define USER_NODE_TREE_NUMBER 3 // 在开发者线程创建组件树的数量。
15. struct AsyncData {
16. napi_env env;
17. std::shared_ptr<ArkUINode> parent = nullptr;
18. std::shared_ptr<ArkUINode> child = nullptr;
19. std::string label = "";
20. };

22. // 保存ArkTs侧NodeContent指针与Native侧节点树根节点的对应关系。
23. std::map<ArkUI_NodeContentHandle, std::shared_ptr<ArkUIBaseNode>> g_nodeMap;
24. ArkUI_ContextHandle g_contextHandle = nullptr;

26. // 创建组件树。
27. void CreateNodeTree(void *asyncUITaskData) {
28. auto asyncData = static_cast<AsyncData*>(asyncUITaskData);
29. if (!asyncData) {
30. return;
31. }
32. // 创建组件树根节点。
33. auto rowNode = std::make_shared<ArkUIRowNode>();
34. asyncData->child = rowNode;

36. // 创建button组件。
37. auto buttonNode1 = std::make_shared<ArkUIButtonNode>();
38. ArkUI_AttributeItem label_item = { .string = asyncData->label.c_str() };
39. // 设置button组件的label属性。
40. int32_t result = buttonNode1->SetLabel(label_item);
41. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
42. OH_LOG_ERROR(LOG_APP, "Button SetLabel Failed %{public}d", result);
43. }
44. ArkUI_NumberValue value[] = {{.f32 = 5}, {.f32 = 5}, {.f32 = 5}, {.f32 = 5}};
45. ArkUI_AttributeItem item = {value, 4};
46. // 设置button组件的margin属性。
47. result = buttonNode1->SetMargin(item);
48. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
49. OH_LOG_ERROR(LOG_APP, "Button SetMargin Failed %{public}d", result);
50. }
51. // 设置button组件的width属性。
52. buttonNode1->SetWidth(150);

54. // 创建button组件。
55. auto buttonNode2 = std::make_shared<ArkUIButtonNode>();
56. ArkUI_AttributeItem label_item2 = { .string = asyncData->label.c_str() };
57. // 设置button组件的label属性。
58. result = buttonNode2->SetLabel(label_item2);
59. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
60. OH_LOG_ERROR(LOG_APP, "Button SetLabel Failed %{public}d", result);
61. }
62. ArkUI_NumberValue value2[] = {{.f32 = 5}, {.f32 = 5}, {.f32 = 5}, {.f32 = 5}};
63. ArkUI_AttributeItem item2 = {value2, 4};
64. // 设置button组件的margin属性。
65. result = buttonNode1->SetMargin(item2);
66. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
67. OH_LOG_ERROR(LOG_APP, "Button SetMargin Failed %{public}d", result);
68. }
69. // 设置button组件的width属性。
70. buttonNode2->SetWidth(150);

72. // 把组件挂载到组件树上。
73. rowNode->AddChild(buttonNode1);
74. rowNode->AddChild(buttonNode2);
75. }

77. // 把组件树挂载到UI组件主树上。
78. void MountNodeTree(void *asyncUITaskData) {
79. auto asyncData = static_cast<AsyncData*>(asyncUITaskData);
80. if (!asyncData) {
81. return;
82. }
83. auto parent = asyncData->parent;
84. auto child = asyncData->child;
85. // 把组件树挂载到UI组件主树上。
86. parent->AddChild(child);
87. delete asyncData;
88. }

90. void CreateNodeOnFrameworkThread(ArkUI_ContextHandle contextHandle, std::shared_ptr<ArkUIColumnNode> parent) {
91. for (int i = 0; i < FRAMEWORK_NODE_TREE_NUMBER; i++) {
92. // UI线程创建子树根节点，保证scroll的子节点顺序。
93. auto columnItem = std::make_shared<ArkUIColumnNode>();
94. parent->AddChild(columnItem);
95. AsyncData* asyncData = new AsyncData();
96. asyncData->parent = columnItem;
97. asyncData->label = "OnFwkThread";
98. // 使用框架提供的非UI线程创建组件树，创建完成后回到UI线程挂载到主树上。
99. int32_t result = OH_ArkUI_PostAsyncUITask(contextHandle, asyncData, CreateNodeTree, MountNodeTree);
100. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
101. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_PostAsyncUITask Failed %{public}d", result);
102. delete asyncData;
103. }
104. }
105. }

107. void CreateNodeOnUserThread(ArkUI_ContextHandle contextHandle, std::shared_ptr<ArkUIColumnNode> parent) {
108. auto columnItem = std::make_shared<ArkUIColumnNode>();
109. parent->AddChild(columnItem);
110. // 在开发者创建的非UI线程上创建组件树。
111. std::thread userThread([columnItem, contextHandle]() {
112. for (int i = 0; i < USER_NODE_TREE_NUMBER; i++) {
113. AsyncData* asyncData = new AsyncData();
114. asyncData->parent = columnItem;
115. asyncData->label = "OnUserThread1";
116. CreateNodeTree(asyncData);
117. // 组件树创建完成后回到UI线程挂载到主树上。
118. int32_t result = OH_ArkUI_PostUITask(contextHandle, asyncData, MountNodeTree);
119. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
120. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_PostUITask Failed %{public}d", result);
121. delete asyncData;
122. }
123. }
124. });
125. userThread.detach();
126. }

128. void CreateNodeOnUserThreadAndWait(ArkUI_ContextHandle contextHandle, std::shared_ptr<ArkUIColumnNode> parent) {
129. auto columnItem = std::make_shared<ArkUIColumnNode>();
130. parent->AddChild(columnItem);
131. // 在开发者创建的非UI线程上创建组件树。
132. std::thread userThread([columnItem, contextHandle]() {
133. for (int i = 0; i < USER_NODE_TREE_NUMBER; i++) {
134. AsyncData* asyncData = new AsyncData();
135. asyncData->parent = columnItem;
136. asyncData->label = "OnUserThread2";
137. CreateNodeTree(asyncData);
138. // 组件树创建完成后回到UI线程挂载到主树上，等待挂载完成后继续创建剩余组件。
139. int32_t result = OH_ArkUI_PostUITaskAndWait(contextHandle, asyncData, MountNodeTree);
140. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
141. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_PostUITask Failed %{public}d", result);
142. delete asyncData;
143. }
144. }
145. });
146. userThread.detach();
147. }

149. napi_value CreateNodeTreeOnMultiThread(napi_env env, napi_callback_info info) {
150. size_t argc = 2;
151. napi_value args[2] = { nullptr, nullptr };
152. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

154. // 获取ArkTs侧组件挂载点。
155. ArkUI_NodeContentHandle contentHandle;
156. int32_t result = OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
157. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
158. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_GetNodeContentFromNapiValue Failed %{public}d", result);
159. return nullptr;
160. }

162. // 获取上下文对象指针。
163. if (!g_contextHandle) {
164. result = OH_ArkUI_GetContextFromNapiValue(env, args[1], &g_contextHandle);
165. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
166. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_GetContextFromNapiValue Failed %{public}d", result);
167. delete g_contextHandle;
168. g_contextHandle = nullptr;
169. return nullptr;
170. }
171. }

173. // 创建Native侧组件树根节点。
174. auto scrollNode = std::make_shared<ArkUIScrollNode>();
175. // 将Native侧组件树根节点挂载到UI主树上。
176. result = OH_ArkUI_NodeContent_AddNode(contentHandle, scrollNode->GetHandle());
177. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
178. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_NodeContent_AddNode Failed %{public}d", result);
179. return nullptr;
180. }
181. // 保存Native侧组件树。
182. g_nodeMap[contentHandle] = scrollNode;

184. auto columnNode = std::make_shared<ArkUIColumnNode>();
185. scrollNode->AddChild(columnNode);
186. // 在框架提供的线程池中创建组件。
187. CreateNodeOnFrameworkThread(g_contextHandle,columnNode);
188. // 在开发者创建的非UI线程中创建组件。
189. CreateNodeOnUserThread(g_contextHandle,columnNode);
190. CreateNodeOnUserThreadAndWait(g_contextHandle,columnNode);
191. return nullptr;
192. }

194. napi_value DisposeNodeTreeOnMultiThread(napi_env env, napi_callback_info info)
195. {
196. size_t argc = 1;
197. napi_value args[1] = { nullptr };
198. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

200. // 获取ArkTs侧组件挂载点。
201. ArkUI_NodeContentHandle contentHandle;
202. int32_t result = OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
203. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
204. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_GetNodeContentFromNapiValue Failed %{public}d", result);
205. return nullptr;
206. }

208. auto it = g_nodeMap.find(contentHandle);
209. if (it == g_nodeMap.end()) {
210. return nullptr;
211. }
212. auto rootNode = it->second;
213. // 将Native侧组件树根节点从UI主树上卸载。
214. result = OH_ArkUI_NodeContent_RemoveNode(contentHandle, rootNode->GetHandle());
215. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
216. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_NodeContent_RemoveNode Failed %{public}d", result);
217. return nullptr;
218. }
219. // 释放Native侧组件树。
220. g_nodeMap.erase(contentHandle);
221. return nullptr;
222. }
223. } // namespace NativeModule
```

```
1. // napi_init.cpp
2. #include "napi/native_api.h"
3. #include "NativeEntry.h"
4. #include "CreateNode.h"

6. EXTERN_C_START
7. static napi_value Init(napi_env env, napi_value exports)
8. {
9. // 绑定Native侧的创建组件和销毁组件。
10. napi_property_descriptor desc[] = {
11. {"createNativeRoot", nullptr,
12. NativeModule::CreateNativeRoot, nullptr, nullptr,
13. nullptr, napi_default, nullptr},

15. {"destroyNativeRoot", nullptr,
16. NativeModule::DestroyNativeRoot, nullptr, nullptr,
17. nullptr, napi_default, nullptr},

19. {"createNodeTreeOnMultiThread", nullptr,
20. NativeModule::CreateNodeTreeOnMultiThread, nullptr, nullptr,
21. nullptr, napi_default, nullptr},

23. {"disposeNodeTreeOnMultiThread", nullptr,
24. NativeModule::DisposeNodeTreeOnMultiThread, nullptr, nullptr,
25. nullptr, napi_default, nullptr}
26. };
27. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
28. return exports;
29. }
30. EXTERN_C_END

32. static napi_module demoModule = {
33. .nm_version = 1,
34. .nm_flags = 0,
35. .nm_filename = nullptr,
36. .nm_register_func = Init,
37. .nm_modname = "entry",
38. .nm_priv = ((void *)0),
39. .reserved = {0},
40. };

42. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

## 示例代码

如下实例展示了在高负载组件创建场景下如何使用多线程NDK接口，将组件创建任务拆分成多个子任务，分派给多个线程并发执行来优化页面跳转场景的响应时延和完成时延。

[使用NDK多线程创建UI组件](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkBuildOnMultiThread)
