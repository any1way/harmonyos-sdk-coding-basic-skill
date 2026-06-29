---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-9
title: 是否可以申请长时任务，在游戏前台下载资源包过程中切后台时免冻结并继续下载资源包
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 是否可以申请长时任务，在游戏前台下载资源包过程中切后台时免冻结并继续下载资源包
category: harmonyos-guides
scraped_at: 2026-06-01T14:58:20+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:c391778cc2b7f5e4185361401f7b3fa5ebf46b1e710bc70f3c15d4be8bd9567a
---
可以。

游戏可以申请[dataTransfer类型的长时任务](<../../../../../应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)，在游戏前台切后台后，游戏可以保持免冻结并继续下载资源包。
