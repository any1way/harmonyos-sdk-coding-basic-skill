---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notification-notificationactionbutton
title: NotificationActionButton
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationActionButton
category: harmonyos-references
scraped_at: 2026-06-01T16:36:46+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f404bf1510cfa6f84f40c805ea3dbf8fc5b37fc1e6a11046d6fa717c4b06f061
---
描述通知中显示的操作按钮。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationActionButton

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮标题。字符串长度不超过200字节，超出部分会被截断；也不可为空字符串。 |
| wantAgent | [WantAgent](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.wantAgent (WantAgent模块)/js-apis-app-ability-wantagent.md>) | 否 | 否 | 点击按钮时触发的WantAgent。 |
| extras | { [key: string]: any } | 否 | 是 | 按钮扩展信息。预留能力，暂未支持。 |
| userInput8+ | [NotificationUserInput](../NotificationUserInput/js-apis-inner-notification-notificationuserinput.md) | 否 | 是 | 用户输入对象实例，默认为空。表示用户输入时的标识。 |
