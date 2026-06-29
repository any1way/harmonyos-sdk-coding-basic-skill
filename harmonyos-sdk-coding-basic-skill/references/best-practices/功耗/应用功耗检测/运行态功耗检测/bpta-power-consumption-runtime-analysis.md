---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-power-consumption-runtime-analysis
title: 运行态功耗检测
breadcrumb: 最佳实践 > 功耗 > 应用功耗检测 > 运行态功耗检测
category: best-practices
scraped_at: 2026-06-01T17:01:09+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7a2d4c3f48299cd71031876d76a00c44fe3711eff4c93d32a701d140875844fa
---
运行态功耗检测主要基于[HiAppEvent事件订阅](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/事件订阅/hiappevent.md>)，这是一种系统层面为应用开发者提供的事件打点机制，用于帮助应用记录运行过程中发生的故障信息、统计信息、安全信息及用户行为信息，支持开发者分析应用的运行状况。

详细检测能力介绍可参考[功耗检测](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/功耗检测/power-detection.md>)文档。

运行态功耗检测支持通过HiAppEvent订阅[CPU高负载事件](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/事件订阅/使用HiAppEvent订阅事件/系统事件/CPU高负载事件/high-cpu-load-event.md>)和[24h功耗器件分解统计事件](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/事件订阅/使用HiAppEvent订阅事件/系统事件/24h功耗器件分解统计事件/24-hour-battery-usage-event.md>)。
