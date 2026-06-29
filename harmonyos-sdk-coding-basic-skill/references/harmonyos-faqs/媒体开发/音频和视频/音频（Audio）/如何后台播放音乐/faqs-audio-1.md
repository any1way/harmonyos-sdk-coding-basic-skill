---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-1
title: 如何后台播放音乐
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何后台播放音乐
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aa945909d1df5685da9adf1556a2f25e1f7b7b59a5d0868830abee835bca4298
---
AVSession管控媒体播放。当第三方应用从前台切换到后台或进入锁屏状态时，媒体播放会强制暂停，且应用不会感知。若需开发后台播放功能，应在后台任务管理中启动长时任务播放音乐，并接入AVSession能力，允许控制中心的播控面板控制第三方应用的播放功能。

**参考链接**

[backgroundTaskManager.startBackgroundRunning](<../../../../../harmonyos-references/Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.resourceschedule.backgroundTaskManager (后台任务管理)/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12>)

[媒体会话提供方](<../../../../../harmonyos-guides/媒体/AVSession Kit（音视频播控服务）/本地媒体会话/媒体会话提供方(ArkTS)/using-avsession-developer.md>)
