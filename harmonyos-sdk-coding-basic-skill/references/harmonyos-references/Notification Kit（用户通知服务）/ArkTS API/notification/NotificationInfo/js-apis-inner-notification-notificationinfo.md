---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationinfo
title: NotificationInfo
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:47:35+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:99ade123c4307978a50b89feb6f452fbb9807ed26fce91ee056d2801d219d785
---
通知订阅扩展能力中[onReceiveMessage](<../../@ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)/js-apis-notificatio_96645684.md#onreceivemessage>)回调的通知信息。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationInfo

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hashCode | string | 是 | 否 | 通知的唯一标识符。 |
| notificationSlotType | [notificationManager.SlotType](<../../@ohos.notificationManager (NotificationManager模块)/js-apis-notificationmanager.md#slottype>) | 是 | 否 | 通知渠道类型。 |
| content | [NotificationExtensionContent](../NotificationExtensionContent/js-apis-notif-notificationextensioncontent.md) | 是 | 否 | 通知内容。 |
| bundleName | string | 是 | 否 | 创建通知的包名。 |
| appIndex | number | 是 | 否 | 创建通知的应用包的分身索引标识，仅在分身应用中生效。 |
| appName | string | 是 | 是 | 创建通知的应用程序名称。 |
| deliveryTime | number | 是 | 是 | 通知发布的时间戳。  数据格式：时间戳。  单位：ms。 |
| groupName | string | 是 | 是 | 通知组名称。默认情况下此参数为空。 |
