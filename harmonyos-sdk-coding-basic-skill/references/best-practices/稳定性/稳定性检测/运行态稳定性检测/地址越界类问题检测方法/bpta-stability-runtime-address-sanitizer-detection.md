---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-runtime-address-sanitizer-detection
title: 地址越界类问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 运行态稳定性检测 > 地址越界类问题检测方法
category: best-practices
scraped_at: 2026-06-01T17:02:17+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:946e492a1fbfd4c2ecd6fd1d7b39248baf9bcb2ece2a780c41f8c98c26203efa
---
## 地址越界定义

地址越界是指程序访问了本不属于自己的内存区域，导致数据被意外修改、程序崩溃、产生不可预期的行为。这种错误通常发生在对不属于当前进程的内存进行读写操作时，主要涉及全局存储区（.data/.bss）、堆内存和栈内存三种类型。

## 检测原理与使用方法

可参看[地址越界类问题检测](../../开发态稳定性检测/地址越界类问题检测/bpta-stability-ram-detection.md)。

## 订阅地址越界事件

发生地址越界事件后，可参看[地址越界事件](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/事件订阅/使用HiAppEvent订阅事件/系统事件/地址越界事件/address-sanitizer-events.md>)。
