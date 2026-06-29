---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-13
title: 音频焦点如何适配
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 音频焦点如何适配
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:13+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:6288e0ed8c3f4ba637db3db945ab1ec5212f1bcbc2fa1581d1c71602621565c2
---
为确保应用提供良好的音频焦点体验，需要注意：

（1）应用在启动播放或录制前，需根据音频用途，正确指定StreamUsage或SourceType。

（2）应用需监听音频焦点事件，并在收到音频焦点事件时做出必要响应。

（3）若应用需要对音频焦点进行主动管理，可以使用音频会话（AudioSession）相关接口。

**参考链接**

[音频焦点和音频会话介绍](<../../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/音频焦点和音频会话管理/音频焦点介绍/audio-playback-concurrency.md>)
