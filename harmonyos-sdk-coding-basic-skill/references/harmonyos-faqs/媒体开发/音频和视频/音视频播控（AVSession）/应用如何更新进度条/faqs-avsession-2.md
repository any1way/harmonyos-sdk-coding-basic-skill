---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-2
title: 应用如何更新进度条
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 应用如何更新进度条
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:19a003ca4cd3023d05bb9784df16213688bb509d113caed4daf9418a97cd8815
---
如果应用希望在播控中心支持进度显示和控制，需要将资源的时长信息设置给AVSession，并注册seek的回调接口以响应系统的进度控制。应用可以在倍速或播放状态发生变化时更新进度条，以节约系统资源。

**参考链接**

[进度控制](<../../../../../harmonyos-guides/媒体/AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md#进度控制>)
