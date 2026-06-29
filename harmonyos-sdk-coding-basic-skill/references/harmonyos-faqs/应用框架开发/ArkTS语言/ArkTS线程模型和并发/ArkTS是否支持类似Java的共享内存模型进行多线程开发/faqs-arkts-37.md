---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-37
title: ArkTS是否支持类似Java的共享内存模型进行多线程开发
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS是否支持类似Java的共享内存模型进行多线程开发
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:83ee7e51f8662b94e7296894c85ed5eea1dbdd12f71eedd8d66715b35109af00
---
无法通过加锁的方式实现多个线程同时对同一个内存对象进行操作。

ArkTS采用Actor并发模型，线程间内存隔离，目前仅支持SharedArrayBuffer和Native层对象的共享。

**参考链接**

[多线程并发概述](../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/多线程并发概述/multi-thread-concurrency-overview.md)
