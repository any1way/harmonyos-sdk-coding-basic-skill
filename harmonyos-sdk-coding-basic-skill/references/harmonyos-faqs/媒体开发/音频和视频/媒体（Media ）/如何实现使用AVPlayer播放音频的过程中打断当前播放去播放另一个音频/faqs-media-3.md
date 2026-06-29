---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-3
title: 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:699027ca6d7f415996bead6f55d1fa343082a5e50481ecc20567417f3a07880a
---
需要先调用[reset()](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md#reset9>)打断前一个音频，然后切换音频源。因为reset()是异步的，所以调用reset()的语句需加上await关键字。
