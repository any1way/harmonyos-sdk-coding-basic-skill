---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-login-state
title: 订阅华为账号的登录/登出事件
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 订阅华为账号的登录/登出事件
category: harmonyos-guides
scraped_at: 2026-06-01T14:59:07+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:862cc74dd6cdeffea433ef613376c60b5adac2bf3f6bbcb0b6dd8b60974eab12
---
## 场景介绍

应用在前台时可以订阅Account Kit提供的华为账号登录/登出广播事件，来感知华为账号的登录状态，实现用户登录/登出应用的逻辑。应用也可通过[getHuaweiIDState](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#gethuaweiidstate>)实时查询华为账号登录状态。

## 事件说明

以下是华为账号登录/登出发送的广播事件。

| 事件名称 | 描述 |
| --- | --- |
| [COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/系统定义的公共事件/commoneventmanager-definitions.md#common_event_distributed_account_login>) | 表示分布式账号登录成功的动作。华为账号登录成功也会发这个广播事件。 |
| [COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/系统定义的公共事件/commoneventmanager-definitions.md#common_event_distributed_account_logout>) | 表示分布式账号登出成功的动作。华为账号登出成功也会发这个广播事件。 |

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](../../开发准备/配置签名和指纹/account-sign-fingerprints.md)、[配置Client ID](<../../开发准备/配置Client ID/account-client-id.md>)。此场景无需申请账号权限。

## 开发步骤

1. 导入[commonEventManager](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/@ohos.commonEventManager (公共事件模块)/js-apis-commoneventmanager.md>)模块及相关公共模块。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 创建订阅者，并处理订阅结果。

   ```
   1. // 订阅者信息
   2. const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
   3. events: [commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN,
   4. commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT]
   5. };
   6. let subscriber: commonEventManager.CommonEventSubscriber;

   8. // 创建订阅者
   9. commonEventManager.createSubscriber(subscribeInfo)
   10. .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
   11. subscriber = commonEventSubscriber;
   12. // 订阅公共事件
   13. commonEventManager.subscribe(subscriber,
   14. (error: BusinessError, data: commonEventManager.CommonEventData) => {
   15. if (error) {
   16. hilog.error(0x0000, 'testTag',
   17. `Failed to subscribe, code is ${error.code}, message is ${error.message}`);
   18. } else {
   19. hilog.info(0x0000, 'testTag', 'Succeeded in subscribing.');
   20. if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN) {
   21. // 订阅到华为账号登录事件
   22. }
   23. if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT) {
   24. // 订阅到华为账号登出事件
   25. }
   26. }
   27. });
   28. })
   29. .catch((err: BusinessError) => {
   30. hilog.error(0x0000, 'testTag', `Failed to createSubscriber. Code: ${err.code}, message: ${err.message}`);
   31. });
   ```
