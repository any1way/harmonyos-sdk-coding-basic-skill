---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d4326a7dd3accbe51596e1764f5ffeb054ffb54f17bf946d40563ffc6db8dd12
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/sFTDHA5aTDuoabvx9K9RSQ/zh-cn_image_0000002592379076.png?HW-CC-KV=V1&HW-CC-Date=20260611T070125Z&HW-CC-Expire=86400&HW-CC-Sign=1F13FC3684AD23FA57A0405BCD0300FD5D5AFF0B0E44048786E07C243A713502)
