---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-4
title: 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3066d7333c37ede358596e01abff0e4f6e2da04a1d824ed166254c0df7a69016
---
在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法[avPlayer.play()](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md#play9>)，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法[avPlayer.pause()](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md#pause9>)即可。
