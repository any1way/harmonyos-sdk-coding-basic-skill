---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-9
title: 静音播放音频时，如何做到不抢音频焦点
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 静音播放音频时，如何做到不抢音频焦点
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4768651af30db8487cb37525e3536b48c46846879c582dbe954b0bf13fa8cfdf
---
若应用以静音状态开始播放音频或视频，并且希望静音阶段不影响其他音频，后续解除静音时，再以正常策略申请音频焦点，可以调用静音并发播放模式的相关接口。

* 若使用[AVPlayer开发音频播放功能(ArkTS)](<../../../../../harmonyos-guides/媒体/Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放音频(ArkTS)/using-avplayer-for-playback.md>)，可以调用[setMediaMuted](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md#setmediamuted12>)函数。
* 若使用[AudioRenderer开发音频播放功能](<../../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/音频播放/使用AudioRenderer开发音频播放功能(ArkTs)/using-audiorenderer-for-playback.md>)，可调用[setSilentModeAndMixWithOthers](<../../../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioRenderer)/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12>)函数。
* 若使用WebView开发音频播放功能，播放前将流音量设为0，系统默认优先与其他音频流并发，解除静音时申请音频焦点。
