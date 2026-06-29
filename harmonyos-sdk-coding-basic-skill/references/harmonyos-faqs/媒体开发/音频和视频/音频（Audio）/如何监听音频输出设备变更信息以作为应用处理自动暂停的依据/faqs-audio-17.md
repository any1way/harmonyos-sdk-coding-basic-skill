---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-17
title: 如何监听音频输出设备变更信息以作为应用处理自动暂停的依据
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何监听音频输出设备变更信息以作为应用处理自动暂停的依据
category: harmonyos-faqs
scraped_at: 2026-06-12T10:39:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0226919ce33565e70419216d5a10dae856523ef37eeaccc32ab139949468b947
---
**问题现象**

使用audioRoutingManager.on('deviceChange')监听设备连接状态变化，导致正常播放时，应用无故自动暂停。

**问题原因**

错误使用监听音频输出设备变化的接口，audioRoutingManager.on('deviceChange')监听的是全局输入和输出设备的连接状态变化，不与音频流绑定。因此，不建议作为应用处理自动暂停的依据。

**解决措施**

开发者可使用[audioRenderer.on('outputDeviceChangeWithInfo')](<../../../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioRenderer)/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11>)，用于监听该音频流输出设备变化及原因。当系统出现音频输出设备的上下线、用户强选、设备抢占或设备选择策略变更等情况，导致音频流输出设备变更时，系统将通过该接口通知应用当前音频流设备变更信息，包含当前音频流输出设备信息和设备变更原因。应用可根据变更原因做相应业务处理，具体详情参考[音频流输出设备变更原因](<../../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/音频设备路由管理/响应输出设备变更时合理暂停/audio-output-device-change.md#音频流输出设备变更原因>)。
