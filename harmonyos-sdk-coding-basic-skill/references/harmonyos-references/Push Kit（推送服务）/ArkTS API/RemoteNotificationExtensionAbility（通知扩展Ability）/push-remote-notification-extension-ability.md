---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-remote-notification-extension-ability
title: RemoteNotificationExtensionAbility（通知扩展Ability）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > RemoteNotificationExtensionAbility（通知扩展Ability）
category: harmonyos-references
scraped_at: 2026-06-11T16:49:44+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:85c8aaf13699652f251deb7133e7cd1d506f260a31fbda91d4810cbf43b18408
---
RemoteNotificationExtensionAbility为通知扩展Ability，提供获取场景化消息数据和生命周期结束的回调。有如下约束：

* RemoteNotificationExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。
* 不允许调用通知API、卡片API、窗口API、弹窗API、实况窗API。
* 生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详请参见[ArkTS API错误码](<../ArkTS API错误码/push-error-code.md>)。

若应用进程在前台，Push Kit将不会弹出通知提醒，开发者可以在应用进程中调用[pushService.receiveMessage](../pushService（推送服务基础能力）/push-pushservice.md#pushservicereceivemessage)接收消息内容并自行完成业务处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [RemoteNotificationExtensionContext](../RemoteNotificationExtensionContext（通知扩展Context）/push-remote-notification-extension-context.md) | 否 | 否 | RemoteNotificationExtensionAbility的上下文环境，继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。 |

## onReceiveMessage

PhonePC/2in1TabletTVWearable

onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent>

应用继承RemoteNotificationExtensionAbility后接收通知扩展数据的接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| remoteNotificationInfo | pushCommon.[RemoteNotificationInfo](../pushCommon（推送服务公共信息）/push-pushcommon.md#remotenotificationinfo) | 是 | 通知扩展数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<pushCommon.[RemoteNotificationContent](../pushCommon（推送服务公共信息）/push-pushcommon.md#remotenotificationcontent)> | Promise对象，返回通知扩展替换内容。 |

**示例：**

```
1. import { RemoteNotificationExtensionAbility, pushCommon } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
5. export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
6. // remoteNotificationInfo为场景化消息数据
7. async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
8. hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
9. return {
10. title: 'Default replace title.',
11. text: 'Default replace text.',
12. badgeNumber: 1,
13. wantAgent: {
14. abilityName: 'DemoAbility',
15. parameters: {
16. key: 'Default value'
17. }
18. }
19. }
20. }
21. }
```

## onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

当RemoteNotificationExtensionAbility生命周期结束时，会执行该回调，建议在该方法中执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
5. export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
6. onDestroy(): void {
7. hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onDestroy.');
8. }
9. }
```
