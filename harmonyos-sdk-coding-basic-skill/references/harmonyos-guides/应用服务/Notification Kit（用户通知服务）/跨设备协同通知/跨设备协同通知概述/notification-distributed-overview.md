---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-distributed-overview
title: 跨设备协同通知概述
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 跨设备协同通知 > 跨设备协同通知概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:11:11+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:d65a9dabc60063333743675dd0503709f7f32ac16d793442bb12de09ea57bf46
---
跨设备协同通知旨在以手机为中心，实现与手表等其他设备的通知消息协同交互。典型场景如下：

* [清除跨设备场景下的重复通知](../清除跨设备场景下的重复通知/notification-distributed-messageid.md)：清除跨设备协同消息和本地设备发布的重复消息，避免多源通知重复打扰用户。

## 约束条件

* 跨设备协同支持的设备：从API version 18开始，支持Phone与Wearable之间通知消息的协同；从API version 20开始，支持Phone与Tablet、PC/2in1设备之间通知消息的协同。
* 跨设备协同支持的[通知渠道](<../../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/@ohos.notificationManager (NotificationManager模块)/js-apis-notificationmanager.md#slottype>)：
  + Wearable：带快捷回复的社交通信类通知（社交通信）、实况窗。
  + Tablet：社交通信、服务提醒、实况窗、客服消息。
  + PC/2in1：社交通信、服务提醒、客服消息。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Em9Jlzu8Q7mu-tKA-i557g/zh-cn_image_0000002622699059.png?HW-CC-KV=V1&HW-CC-Date=20260611T071110Z&HW-CC-Expire=86400&HW-CC-Sign=121BA3A7422E77E616B7D6DEF68D27D22F719F3FC900A0354122389A1B9212FF)
