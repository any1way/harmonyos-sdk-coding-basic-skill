---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-unsubscribe-event
title: 取消订阅空间事件
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 取消订阅空间事件
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d28fc322d1a3809ce3eaa08e00132a1baffba71dd9e886655fd89dcbce541c16
---
## 场景介绍

Enterprise Space Kit为应用提供取消订阅空间事件的能力，支持应用在特定场景下灵活管理空间事件的订阅状态。例如，当应用需要关闭、某个功能模块不再使用时，可通过调用该方法主动取消对特定空间事件的订阅。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#unsubscribeevent>)。

| 接口名 | 描述 |
| --- | --- |
| [unsubscribeEvent](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#unsubscribeevent>)(subscribeId:number): void | 取消订阅空间事件，在相关事件触发时，不再通知应用侧。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[unsubscribeEvent](<../../../../../harmonyos-references/Enterprise Space Kit（企业数字空间服务）/ArkTS API/spaceManager (空间管理)/enterprisespace-spacemanager.md#unsubscribeevent>)接口，取消订阅空间事件，并查看打印信息。

   ```
   1. const subscribeId: number = 100;
   2. try {
   3. spaceManager.unsubscribeEvent(subscribeId);
   4. console.info('Succeeded in unsubscribing event');
   5. } catch (err) {
   6. console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
