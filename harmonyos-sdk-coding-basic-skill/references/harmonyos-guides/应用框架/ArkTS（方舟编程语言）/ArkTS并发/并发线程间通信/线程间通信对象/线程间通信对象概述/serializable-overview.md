---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview
title: 线程间通信对象概述
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > 线程间通信对象概述
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bacbedbdc7de8c7c2286701dae6ebb785d356a40710fd46bac41c1d5fd701f8a
---
在多线程并发场景中，例如通过TaskPool或Worker创建后台线程，不同线程间需要进行数据交互。由于线程间内存隔离，线程间通信对象必须通过序列化实现值拷贝或内存共享。

说明

* 单次序列化传输的数据量大小限制为16MB。
* 序列化不支持使用[@State装饰器](<../../../../../ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@State装饰器：组件内状态/arkts-state.md>)、[@Prop装饰器](<../../../../../ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Prop装饰器：父子单向同步/arkts-prop.md>)、[@Link装饰器](<../../../../../ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Link装饰器：父子双向同步/arkts-link.md>)等装饰器修饰的复杂类型。

目前ArkTS支持线程间通信的对象有以下几种：

* [普通对象](../普通对象/normal-object.md)：可直接传递基本数据类型及自定义对象（需满足序列化规范）。
* [容器类对象](../容器类对象/container-object.md)：可直接传递已经支持的容器类对象（需满足序列化规范）。
* [ArrayBuffer对象](../ArrayBuffer对象/arraybuffer-object.md)：用于二进制数据的高效传递，适用于大段连续内存数据（如图片、音频原始数据）。
* [SharedArrayBuffer对象](../SharedArrayBuffer对象/shared-arraybuffer-object.md)：支持多线程共享内存，允许线程间直接访问同一块内存区域，提升数据传递效率。
* [Transferable对象（NativeBinding对象）](<../Transferable对象 (NativeBinding对象)/transferabled-object.md>)：支持跨线程转移对象所有权（如文件描述符、图形资源等），转移后原线程不再拥有访问权限。
* [Sendable对象](../Sendable对象/Sendable对象简介/arkts-sendable.md)：符合ArkTS语言规范的可共享对象，需通过[@Sendable装饰器](../Sendable对象/Sendable对象简介/arkts-sendable.md#sendable装饰器)标记，并且满足Sendable约束，详情可查[Sendable使用规则与约束](../Sendable对象/Sendable使用规则与约束/sendable-constraints.md)。
