---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-5
title: 如何实现录音监听
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何实现录音监听
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1b3f9ca3f98e8fdbc7605aac56ef3db30e8af57e2dfa9332f0003a9136d73770
---
系统音频监听功能在AudioStreamManager内，录音监听可以通过on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void订阅接口实现。详细可参考链接：[on('audioCapturerChange')](<../../../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioStreamManager)/arkts-apis-audio-audiostreammanager.md#onaudiocapturerchange9>)。
