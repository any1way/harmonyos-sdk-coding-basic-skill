---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-mainthread-consumption-detection
title: 主线程超时类问题检测方法
breadcrumb: 最佳实践 > 性能 > 性能检测 > 运行态性能检测 > 主线程超时类问题检测方法
category: best-practices
scraped_at: 2026-06-01T16:59:41+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a0579ee686b5322cf533b27cd4b5434f79a7e4628b734ea41d814edcb0ea6029
---
当应用的主线程执行耗时任务时，用户会感觉到应用卡顿，但若未达到卡死的时间限制，则不会生成故障日志，这给开发者定位问题带来了不便。为此，系统提供了[任务超时检测](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/任务超时检测/apptask-timeout-guidelines.md>)机制，能够生成采样调用栈文件或trace文件，帮助开发者定位和分析主线程任务的执行情况。开发者可以通过HiAppEvent接口订阅[主线程超时事件](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/事件订阅/使用HiAppEvent订阅事件/系统事件/主线程超时事件/main-thread-jank-events.md>)，以获取维护和测试信息。
