---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-unsubscription
title: 取消动态订阅公共事件
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 取消动态订阅公共事件
category: harmonyos-guides
scraped_at: 2026-06-01T11:21:44+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:027569ff7ce5cd5c5dba1ed7fdae533c739e4a53afd27dc29a107a4ff4e49456
---
## 场景介绍

动态订阅者完成业务需求后，应主动取消订阅。通过调用[unsubscribe()](<../../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe>)方法，取消订阅事件。

## 接口说明

| 接口名 | 接口描述 |
| --- | --- |
| [unsubscribe](<../../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe>)(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>) | 取消订阅公共事件。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG: string = 'ProcessModel';
   5. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L15-L21)
2. 根据[动态订阅公共事件](../动态订阅公共事件/common-event-subscription.md)章节的步骤来订阅某个事件。
3. 调用CommonEvent中的[unsubscribe()](<../../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe>)方法取消订阅某事件。

   ```
   1. // subscriberCustom为订阅事件时创建的订阅者对象
   2. if (subscriberCustom !== null) {
   3. commonEventManager.unsubscribe(subscriberCustom, (err: BusinessError) => {
   4. if (err) {
   5. hilog.error(DOMAIN_NUMBER, TAG,
   6. `Failed to unsubscribe. code is ${err.code}, message is ${err.message}`);
   7. } else {
   8. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in unsubscribing.`);
   9. subscriberCustom = null;
   10. }
   11. })
   12. }
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L96-L109)
