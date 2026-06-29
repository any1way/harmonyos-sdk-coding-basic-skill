---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-intro
title: HiTraceChain介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 分布式调用链跟踪 > HiTraceChain介绍
category: harmonyos-guides
scraped_at: 2026-06-11T14:52:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b6685bcdd9ec2e97f39e0f12cd7e33a1aacf6e057f0a3502e94d2d7e7328c551
---
## 简介

HiTraceChain是基于分布式跟踪调用链思想，在端侧业务流程（涉及跨线程、跨进程、跨设备）中的一种轻量级分布式跟踪的实现。HiTraceChain在业务流程中生成和传递唯一跟踪标识，在业务流程输出的各类信息中（包括HiTraceMeter打点、应用事件、hilog日志等）记录该跟踪标识。在调试、问题定位的过程中，开发者可以通过该唯一跟踪标识将本次业务流程端到端的各类信息快速关联起来。HiTraceChain为开发者提供业务流程调用链跟踪的维测接口，帮助开发者迅速获取指定业务流程调用链的运行日志，定位跨设备/跨进程/跨线程的故障问题。

## 基本概念

**HiTraceId**：HiTraceChain提供的唯一跟踪标识，用于跟踪业务流程的调用链。

**chainId**：跟踪链标识，属于HiTraceId的一部分，用于标识当前跟踪的业务流程。

**spanId**：分支标识，属于HiTraceId的一部分，用于标识业务流程在某个服务中的一个具体任务，可以为每个任务创建一个唯一的spanId，用于区分不同的任务。默认值为0，当调用接口创建spanId或自动传递机制传递HiTraceId时，会生成新的spanId。

**parentSpanId**：父分支标识，属于HiTraceId的一部分，用于标识当前任务的父任务，可以建立不同任务之间的层级关系，显示任务之间的从属关系。默认值为0，创建新的spanId时，先将当前spanId赋值给parentSpanId，再生成新的spanId。

## 实现原理

1. **生成唯一跟踪标识**：启用HiTraceChain跟踪后，会在当前线程的TLS（Thread Local Storage，线程本地存储）生成一个全局唯一跟踪标识HiTraceId。
2. **获取HiTraceId**：Native层直接获取TLS中的HiTraceId；ArkTS层通过NAPI接口调用获取Native层TLS中的HiTraceId。
3. **传递HiTraceId**：随着业务流程的推进，开发者可取出当前线程TLS中的HiTraceId，在不同的线程（如thread1, thread2）、进程（如APP1, APP2）以及设备（如Device1, Device2）之间传递，并将HiTraceId设置到其他线程的TLS中，确保在同一个业务流程中，所有相关线程都能访问到这个唯一的跟踪标识。
4. **信息记录**：对于启用HiTraceChain的业务流程，其输出的各类信息中（包括HiTraceMeter打点、应用事件、hilog日志等）都会记录该跟踪标识，开发者可以通过HiTraceId将这些信息关联起来，从而实现端到端的调用链跟踪。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/m0hnp2goTPuYYRax-E9Trw/zh-cn_image_0000002592218928.png?HW-CC-KV=V1&HW-CC-Date=20260611T065238Z&HW-CC-Expire=86400&HW-CC-Sign=EEF2BEDC38FF8BC5653BAA08B6846947533C6DAC2263C197532D30BDFA98D50B)

## 约束与限制

通过设置[HiTraceFlag](<../../../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiTraceChain (分布式跟踪)/js-apis-hitracechain.md#hitraceflag>)以启用异步调用跟踪，HiTraceId可在HiTraceChain的自动传递机制中自动传递。

下表列举了一些常见的支持与不支持HiTraceChain自动传递的机制，不支持HiTraceChain自动传递的机制无法传递HiTraceId到创建的异步任务、线程或进程中，会导致HiTraceChain调用链中断，需要开发者手动传递并设置HiTraceId，以实现完整的调用链跟踪。

| 场景 | 异步任务 | 跨线程 | 跨进程 | 跨设备 |
| --- | --- | --- | --- | --- |
| 支持HiTraceChain自动传递的机制 | [async/await](<../../../../../应用框架/ArkTS（方舟编程语言）/ArkTS并发/异步并发 (Promise和asyncawait)/async-concurrency-overview.md#asyncawait>)  [Promise](<../../../../../应用框架/ArkTS（方舟编程语言）/ArkTS并发/异步并发 (Promise和asyncawait)/async-concurrency-overview.md#promise>) | [HiAppEvent](../../事件订阅/HiAppEvent介绍/hiappevent-intro.md)  [napi\_async\_work](../../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API典型使用场景/使用Node-API接口进行异步任务开发/use-napi-asynchronous-task.md)  [FFRT](<../../../../基础功能/Function Flow Runtime Kit（任务并发调度服务）/Function Flow Runtime Kit概述/ffrt-overview.md>) | [IPC](<../../../../../应用框架/IPC Kit（进程间通信服务）/IPC Kit简介/ipc-rpc-overview.md>) | [RPC](<../../../../../应用框架/IPC Kit（进程间通信服务）/IPC Kit简介/ipc-rpc-overview.md>) |
| 不支持HiTraceChain自动传递的机制 | 宏任务及其异步任务（例如[setTimeout](<../../../../../../harmonyos-references/ArkTS API/Timer (定时器)/js-apis-timer.md#settimeout>)、[setInterval](<../../../../../../harmonyos-references/ArkTS API/Timer (定时器)/js-apis-timer.md#setinterval>)等） | [TaskPool](../../../../../应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/TaskPool简介/taskpool-introduction.md)  [Worker](../../../../../应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/Worker简介/worker-introduction.md)  C++标准库std::thread、pthread\_create、std::async等创建的线程 | [Socket](<../../../../网络/Network Kit（网络服务）/访问网络/使用Socket访问网络/socket-connection.md>)  [Ashmem](<../../../../../../harmonyos-references/IPC Kit（进程间通信服务）/ArkTS API/@ohos.rpc (RPC通信)/js-apis-rpc.md#ashmem8>) | - |
