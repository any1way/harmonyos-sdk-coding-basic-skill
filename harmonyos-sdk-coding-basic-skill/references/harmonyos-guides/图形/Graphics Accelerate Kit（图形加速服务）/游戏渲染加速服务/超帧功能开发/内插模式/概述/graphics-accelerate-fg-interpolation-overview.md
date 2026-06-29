---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-interpolation-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 内插模式 > 概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ce6d196f8b4ba2c93322b0cf8c7224ce2b70e95a02480bab37c12b4941b0e58b
---

超帧内插模式是利用相邻两个真实渲染帧进行超帧计算生成中间的预测帧，即利用第N-1帧和第N帧真实渲染帧预测第N-0.5帧预测帧，如下图所示。由于中间预测帧的像素点通常能在前后两帧中找到对应位置，因此内插模式的预测帧效果较外插模式更优。由于第N帧真实渲染帧需要等待第N-0.5帧预测帧生成并送显后才能最终送显，因此会新增1~2帧的响应时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ARs0kCRYTOa41E6GbJGPKA/zh-cn_image_0000002592379072.png?HW-CC-KV=V1&HW-CC-Date=20260611T070114Z&HW-CC-Expire=86400&HW-CC-Sign=E39BA2D0205663F67ABF1264CDDD07FA4C5D259DCB25A63B9051FBE4E0986555)
