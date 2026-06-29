---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-27
title: TaskPool和Worker的异同点
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > TaskPool和Worker的异同点
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:12+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d90a40791b333e0c81ea91b14b589da6592d2d88cf29cd708a078257812ef5ed
---
* 不同点：Worker 和 TaskPool 是不同颗粒度的并发 API。Worker 类似于 Thread 或 Service 维度，而 TaskPool 则是单一任务维度。TaskPool 简化了并发程序的开发，支持优先级和任务取消，并通过统一管理节省系统资源，优化调度。
* 相同点：JS相关的线程间交互都基于内存隔离模型，参数与数据范围的限制相同，并且都存在开销。

**参考链接**

[TaskPool和Worker的对比 (TaskPool和Worker)](<../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/多线程并发/TaskPool和Worker的对比 (TaskPool和Worker)/taskpool-vs-worker.md>)
