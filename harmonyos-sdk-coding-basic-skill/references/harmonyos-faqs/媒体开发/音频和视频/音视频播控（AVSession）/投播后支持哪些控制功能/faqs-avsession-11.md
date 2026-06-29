---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-11
title: 投播后支持哪些控制功能
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 投播后支持哪些控制功能
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d55cc2bd014c875a818b8766b9c958c2b36e430fbcca7f3c91d63e5108cc4284
---
投播成功后，目前在本端支持的功能有：播放、暂停、下一首/曲、上一首/曲、快进、快退、进度控制、音量控制。

对端大屏设备支持的功能有：播放、暂停、下一首/曲、上一首/曲、快进、快退、进度控制。

目前不支持清晰度切换、音轨切换、倍速、弹幕等功能。

支持的接口：[sendControlCommand](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSessionController)/arkts-apis-avsession-avsessioncontroller.md#sendcontrolcommand10>)(command: AVCastControlCommand, callback: AsyncCallback<void>): void。
