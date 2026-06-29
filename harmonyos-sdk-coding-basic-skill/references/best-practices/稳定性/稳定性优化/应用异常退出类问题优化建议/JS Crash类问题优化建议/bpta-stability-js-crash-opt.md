---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-crash-opt
title: JS Crash类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用异常退出类问题优化建议 > JS Crash类问题优化建议
category: best-practices
scraped_at: 2026-06-01T17:02:51+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e9daccd8c97f201cd8067d95c96d6cb56a5c1104eddd7261be123d516920153f
---
## 优化建议1：Source Maps归档保存

生产环境归档SourceMap便于后续源码还原，遇到JS Crash应先进行[堆栈轨迹分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ide-release-app-stack-analysis-V5)。

说明

编译时SourceMap的获取位置详见：[sourceMap归档位置介绍](../../../../../harmonyos-guides/编写与调试应用/日志与故障分析/故障分析/异常堆栈解析原理/ide-exception-stack-parsing-principle.md#section666114451518)。

## 优化建议2：崩溃预防机制

可使用errorManager注册错误观测器。注册后可以捕获到应用产生的JS Crash，应用崩溃时进程不会退出。详见[errorManager使用指导](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/错误管理及应用恢复/错误管理开发指导/errormanager-guidelines.md>)。
