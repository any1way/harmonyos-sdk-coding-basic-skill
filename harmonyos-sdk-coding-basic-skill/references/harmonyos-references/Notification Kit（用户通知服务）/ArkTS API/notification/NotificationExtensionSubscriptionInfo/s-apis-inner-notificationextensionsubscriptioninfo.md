---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo
title: NotificationExtensionSubscriptionInfo
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationExtensionSubscriptionInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:36:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cc168d2cb65fe97d27d0f808890be22c0645e7c00a7bb17e299f6092071f65d8
---
用于描述通知扩展订阅的信息。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationExtensionSubscriptionInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [notificationExtensionSubscription.SubscribeType](<../../@ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)/js-apis-n_26046847.md#subscribetype>) | 否 | 否 | 表示订阅的类型，包括通过蓝牙订阅通知。 |
| addr | string | 否 | 否 | 表示设备的唯一标识符。例如："11:22:33:AA:BB:FF" |
