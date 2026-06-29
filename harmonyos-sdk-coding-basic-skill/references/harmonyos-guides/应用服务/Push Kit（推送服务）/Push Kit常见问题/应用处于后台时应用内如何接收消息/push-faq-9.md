---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-9
title: 应用处于后台时应用内如何接收消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 应用处于后台时应用内如何接收消息
category: harmonyos-guides
scraped_at: 2026-06-01T15:09:57+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d59626397385d9ed96afa5bc801ff726086fdf51336c31da7a488beead4f6ab4
---
应用处于后台时仅有如下两个场景可以在应用内接收消息：

* 若应用需要实现语音播报等能力时，服务端可发送**语音播报消息**（即[push-type](<../../../../../harmonyos-references/Push Kit（推送服务）/REST API/场景化消息/功能介绍/push-scenariozed-api-intro.md#场景介绍>)为**2**）。该场景中客户端应用内消息接收请参考RemoteNotificationExtensionAbility中[接口调用示例](<../../../../../harmonyos-references/Push Kit（推送服务）/ArkTS API/RemoteNotificationExtensionAbility（通知扩展Ability）/push-remote-notification-extension-ability.md#onreceivemessage>)。
* 若应用需要实现网络音视频通话能力时，服务端可发送**应用内通话消息**（即push-type为**10**）。该场景中客户端应用内消息接收请参考VoIPExtensionAbility中[接口调用示例](<../../../../../harmonyos-references/Push Kit（推送服务）/ArkTS API/VoIPExtensionAbility（应用内通话消息扩展Ability）/push-voip-ability.md#onreceivemessage>)。

当应用处于内容不频繁更新，不会显示通知、播放铃声或改变应用角标场景时，服务端可发送**后台消息**（即push-type为**6**），若[proxyData](<../../../../../harmonyos-references/Push Kit（推送服务）/REST API/场景化消息/请求体参数说明/push-scenariozed-api-request-param.md#backgroundpayload-后台消息>)为“ENABLE”时，Push Kit将后台消息写入到数据库中，不会拉起应用进程。
