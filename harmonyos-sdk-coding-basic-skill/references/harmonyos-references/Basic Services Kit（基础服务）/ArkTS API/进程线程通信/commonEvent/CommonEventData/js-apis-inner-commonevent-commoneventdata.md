---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata
title: CommonEventData
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > commonEvent > CommonEventData
category: harmonyos-references
scraped_at: 2026-06-11T16:17:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:18130558425ea9ed11da72641eb7a7ce651b58a3287b446f73b31f381ae1593a
---
表示公共事件的数据。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | string | 否 | 否 | 表示当前接收的公共事件名称。 |
| bundleName | string | 否 | 是 | 表示包名称，默认为空字符串。 |
| code | number | 否 | 是 | 表示订阅者接收到的公共事件数据（number类型）。该字段取值与发布者使用[commonEventManager.publish](<../../@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerpublish-1>)发布公共事件时，通过[CommonEventPublishData](../CommonEventPublishData/js-apis-inner-commonevent-commoneventpublishdata.md)中的code字段传递的数据一致。默认值为0。 |
| data | string | 否 | 是 | 表示订阅者接收到的公共事件数据（string类型）。该字段取值与发布者使用[commonEventManager.publish](<../../@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerpublish-1>)发布公共事件时，通过[CommonEventPublishData](../CommonEventPublishData/js-apis-inner-commonevent-commoneventpublishdata.md)中的data字段传递的数据一致。 |
| parameters | {[key: string]: any} | 否 | 是 | 表示订阅者接收到的公共事件的附加信息。该字段取值与发布者使用[commonEventManager.publish](<../../@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerpublish-1>)发布公共事件时，通过[CommonEventPublishData](../CommonEventPublishData/js-apis-inner-commonevent-commoneventpublishdata.md)中的parameters字段传递的数据一致。 |
