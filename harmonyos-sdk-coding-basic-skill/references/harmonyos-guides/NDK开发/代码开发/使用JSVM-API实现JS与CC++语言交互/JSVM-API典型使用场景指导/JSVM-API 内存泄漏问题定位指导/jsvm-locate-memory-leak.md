---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-locate-memory-leak
title: JSVM-API 内存泄漏问题定位指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API 内存泄漏问题定位指导
category: harmonyos-guides
scraped_at: 2026-06-01T15:16:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8f325ad7154efc5a157d42753c91c40a601861e19b20614d03d842ad99411463
---
JSVM的内存占用包括Native内存占用(C/C++侧的内存占用)和底层的JS引擎的堆内存占用，JS引擎会维护一个堆来管理其生成的JS对象，其生命周期由JS引擎维护，除此之外的内存我们归为Native内存。用户在使用JSVM时，可能碰到这两种内存异常增长的情况。

本文先介绍如何定性分析，然后分两个部分介绍如何定位Native内存泄漏和JS引擎堆内存泄漏。

## 定性分析

可以通过hdc连接设备，执行如下命令行的方式对目标应用的内存进行采样，比较一段时间内的内存变化情况，从而定性分析是Native内存泄漏还是JS内存。下图中Pss Total列，native heap对应Native内存占用，AnonPage other对应js堆内存占用。

```
1. hidumper --mem $(pidof dest_app)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JJMb6J_lQ5ClzJbkuNMSOA/zh-cn_image_0000002613519881.png?HW-CC-KV=V1&HW-CC-Date=20260601T071631Z&HW-CC-Expire=86400&HW-CC-Sign=8EAF0277DAE21627D833B72DDE5345EC7F2EE5D49E01A7FD56E0B4D1DC904C7F)

## Native内存泄漏定位

### 典型场景

1. OH\_JSVM\_CreateReference 和 OH\_JSVM\_DeleteReference 接口没有成对调用，导致Reference没有被释放。

```
1. JSVM_Value obj = nullptr;
2. OH_JSVM_CreateObject(env, &obj);
3. // 创建引用
4. JSVM_Ref reference;
5. OH_JSVM_CreateReference(env, obj, 1, &reference);

7. // 使用引用
8. JSVM_Value result;
9. OH_JSVM_GetReferenceValue(env, reference, &result);

11. // 未释放引用
12. // OH_JSVM_DeleteReference(env, reference);
```

### 定位步骤

为了分析Native内存泄漏，可以借助DevEco Studio的内存分析模块，具体参考文档：[内存分析及优化](../../../../../优化应用性能/基础内存：Allocation分析/内存分析介绍/ide-insight-session-allocations-memory.md)。

1. 使用Profiler的Allocation模块记录一段时间内的Native内存信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0DaFKSoPRkOyeS6GWm7ZWw/zh-cn_image_0000002582960080.png?HW-CC-KV=V1&HW-CC-Date=20260601T071631Z&HW-CC-Expire=86400&HW-CC-Sign=9A964258017B866366F85CAF9531E5581E5B9FD1F94A7BB7C3D2C26244AB7095)
2. 比较这段时间内"Created & Existing"的内存变化情况，如果存在占比较大且Count较大的未释放内存，则怀疑存在内存泄漏，展开进一步查看调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Nu7y6PhsQfmJqQRH-QRgcQ/zh-cn_image_0000002583120006.png?HW-CC-KV=V1&HW-CC-Date=20260601T071631Z&HW-CC-Expire=86400&HW-CC-Sign=6C4F76225A49A9B2B192173700649D36A803F5904CD3474FAD532DF13ECDB35D)

## JS引擎堆内存泄漏定位

### 典型场景

1. 全局变量滥用，导致DOM元素未释放。

```
1. const elements = [];
2. function createElements() {
3. for (let i = 0; i < 1000; i++) {
4. const el = document.createElement('div');
5. document.body.appendChild(el);
6. elements.push(el); // 即使从 DOM 移除，数组仍保留引用
7. }
8. }
```

### 定位步骤

JSVM目前提供了OH\_JSVM\_OpenInspector开启inspector，参考[使用OH\_JSVM\_OpenInspector](../JSVM-API调试&定位/jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-oh_jsvm_openinspector),在此基础上可以[使用 Chrome inspect 页面进行调试](../JSVM-API调试&定位/jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-chrome-inspect-页面进行调试)。

通过使用DevTools工具，对目标场景内的堆内存进行快照（快照前先点击上方的垃圾回收按钮进行垃圾回收），利用快照对比功能，找到未释放的JS对象和其所在源码中的位置，进一步指导定位堆内存未释放的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/MSkmHXifRRWtEgAuE3Si8g/zh-cn_image_0000002613639773.png?HW-CC-KV=V1&HW-CC-Date=20260601T071631Z&HW-CC-Expire=86400&HW-CC-Sign=60AC9ED847A293C5738824756CCB2CC4A3090C7559D849EFB9F52FBCAD9DD68A)
