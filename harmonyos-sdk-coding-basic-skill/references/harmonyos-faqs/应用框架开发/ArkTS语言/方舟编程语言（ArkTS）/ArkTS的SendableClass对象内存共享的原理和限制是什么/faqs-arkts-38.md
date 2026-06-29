---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-38
title: ArkTS的SendableClass对象内存共享的原理和限制是什么
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS的SendableClass对象内存共享的原理和限制是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:44+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:84a830a4c80b0de4d5adf87c64588b14b9ab92edfd5572b1697d3dcb60bcf132
---
SendableClass基于Actor内存隔离并发模型扩展，Sendable对象的内存由线程间共享，需确保单线程无锁化运行。因此，同一Sendable实例不能多线程并发访问，开发者应通过同步机制保证线程安全。

Sendable对象需要满足一定的规格。

1. 成员属性为 Sendable 类或基础类型（如 string、number、boolean 等）。
2. 成员属性必须显式初始化。
3. 成员函数不能使用闭包，只能使用入参、this成员或import导入的变量。
4. 只允许Sendable类继承Sendable类。
5. @Sendable 只能写在 ArkTS（.ets）文件中。
6. 不支持定义私有属性，应使用public。
7. 导出 Sendable 类的文件时，不能导出非 Sendable 属性。

**参考链接**

[多线程并发概述](../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/多线程并发概述/multi-thread-concurrency-overview.md)
