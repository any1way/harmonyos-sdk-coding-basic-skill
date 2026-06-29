---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-8
title: 播放短促提示音（如点赞、收藏、新消息等场景的提示音或音效），应该如何处理
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 播放短促提示音（如点赞、收藏、新消息等场景的提示音或音效），应该如何处理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:58882088b0af4d7e1cc78dd47f43fba4a9876f9a503ed854e15c302cc4873b48
---
* 推荐优先使用[SoundPool](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/multimedia/SoundPool (音频池)/js-apis-inner-multimedia-soundpool.md>)，若应用使用SoundPool开发音频播放功能，且StreamUsage指定为Music、Movie、AudioBook等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。
* 若应用不希望使用SoundPool，并且当前使用的流类型会打断其他音频播放，推荐使用[AudioSession](<../../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/音频焦点和音频会话管理/音频焦点介绍/audio-playback-concurrency.md>)相关接口，指定为MIX\_WITH\_OTHERS策略。
