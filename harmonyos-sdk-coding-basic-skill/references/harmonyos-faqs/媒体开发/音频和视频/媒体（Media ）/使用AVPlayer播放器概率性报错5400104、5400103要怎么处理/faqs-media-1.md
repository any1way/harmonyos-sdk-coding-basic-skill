---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-1
title: 使用AVPlayer播放器概率性报错5400104、5400103要怎么处理
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用AVPlayer播放器概率性报错5400104、5400103要怎么处理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:22+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c228585c28835a2b5ce4644c0648a633f8e420bdcf862bf95e9919b7867388d9
---
**问题现象**

5400103：媒体与其他模块（图形、音频、网络、HDI、相机）的数据交互出现问题，可能与服务器限流有关。

5400104：网络超时或访问其他模块超时。默认网络超时时间是15秒，从开始缓存事件上报时开始计时，超时后将上报该错误信息。

**解决措施**

1. 确认网络连接是否正常。
2. 销毁当前实例，并重新创建。如果重新创建失败，则停止相关操作。
3. 尝试优化流所对应的服务器限流情况，以规避系统播放器的严格条件。

**参考链接**

[错误码5400103](<../../../../../harmonyos-references/Media Kit（媒体服务）/错误码/Media错误码/errorcode-media.md#section5400103-出现io错误>)

[错误码5400104](<../../../../../harmonyos-references/Media Kit（媒体服务）/错误码/Media错误码/errorcode-media.md#section5400104-操作超时>)
