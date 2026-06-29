---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-461
title: AppStorage里面存储数据，如何保证不会有内存泄漏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > AppStorage里面存储数据，如何保证不会有内存泄漏
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2aec01fb4686b27bf5c27871ab418506cdd745a48ee505cb2598997cbe8b00a2
---
**问题描述**

在entryability里用AppStorage存储数据，'当需要访问数据时进行读取会存在内存泄漏吗？

**解决措施**

AppStorage是在应用启动时创建的单例，用于提供应用状态数据的中心存储，这些状态数据在应用级别可访问。AppStorage在应用运行过程中保留其属性，开发者自行管理AppStorage里面的变量生命周期，如不使用可以通过[delete接口](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/应用级变量的状态管理/ts-state-management.md#delete10)删掉。
