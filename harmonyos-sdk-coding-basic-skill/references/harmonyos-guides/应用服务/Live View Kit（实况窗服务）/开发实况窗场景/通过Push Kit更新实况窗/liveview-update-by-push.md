---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-update-by-push
title: 通过Push Kit更新实况窗
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发实况窗场景 > 通过Push Kit更新实况窗
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a8b2d4da1c42057631af6f41bb3d58faf92adc7061e1ec3fc6fbdc4ea7a81654
---
## 场景介绍

本地实况窗的更新依赖于应用进程的存活，为了让实况窗在生命周期内正常完成更新和结束，我们更推荐开发者使用Push Kit实时更新实况窗状态。

通过Push Kit更新实况窗的流程如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/IGUkV6O0RKy5wfyYVinJ8w/zh-cn_image_0000002622858863.png?HW-CC-KV=V1&HW-CC-Date=20260611T070915Z&HW-CC-Expire=86400&HW-CC-Sign=619727A33DB16298C78F53FFE6A4AEFBF5406F2F3604BB3C1466B24A00570892)

1. 使用Push Kit，获取Push Token。
2. 使用Live View Kit创建实况窗成功后，开发者需要将实况窗id、pushToken、实况窗场景event以及业务服务的相关的状态属性保存到业务服务端。
3. 当业务服务的用户订单状态发生变化时，通过Push Kit通道推送更新消息，更新/结束实况窗。

详细开发流程请参见Push Kit[推送实况窗消息](<../../../Push Kit（推送服务）/推送场景化消息/推送实况窗消息/push-update-liveview.md>)。
