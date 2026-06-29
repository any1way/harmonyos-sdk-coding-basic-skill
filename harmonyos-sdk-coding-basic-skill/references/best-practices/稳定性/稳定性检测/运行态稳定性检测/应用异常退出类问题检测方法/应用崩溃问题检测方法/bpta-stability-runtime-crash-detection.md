---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-runtime-crash-detection
title: 应用崩溃问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 运行态稳定性检测 > 应用异常退出类问题检测方法 > 应用崩溃问题检测方法
category: best-practices
scraped_at: 2026-06-01T17:02:22+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1016a7d10ed7678aef27f5b52f4e083a948e4a6386665e564a1d75378f0fceb5
---
应用崩溃是指应用进程在运行过程中发生不可恢复的异常，最终导致进程非预期的退出。目前有以下两类场景应用会发生崩溃：

1. Native代码未处理崩溃异常信号会生成CPP Crash日志。检测方法详见[Cpp Crash（进程崩溃）检测](<../../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/崩溃检测/Cpp Crash（进程崩溃）检测/cppcrash-guidelines.md>)，崩溃异常信号详见[系统处理的崩溃信号](<../../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/崩溃检测/Cpp Crash（进程崩溃）检测/cppcrash-guidelines.md#系统处理的崩溃信号>)。
2. ArkTS/JS代码未处理异常会生成JS Crash日志，检测方法详见[JS Crash（进程崩溃）检测](<../../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/崩溃检测/JS Crash（进程崩溃）检测/jscrash-guidelines.md>)。
