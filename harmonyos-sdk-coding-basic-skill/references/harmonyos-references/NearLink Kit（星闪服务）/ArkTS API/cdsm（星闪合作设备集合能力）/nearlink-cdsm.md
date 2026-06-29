---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-cdsm
title: cdsm（星闪合作设备集合能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > cdsm（星闪合作设备集合能力）
category: harmonyos-references
scraped_at: 2026-06-11T16:14:54+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:4b410185a8f479cd833eed065c548cf7b325d140dcb33e48473e1035314aecc4
---
本模块提供了查询星闪合作设备集合信息的功能。

**起始版本：** 6.1.1(24)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { cdsm } from '@kit.NearLinkKit';
```

## createCdsmClient

PhonePC/2in1TabletTVWearable

createCdsmClient(address: string): CdsmClient

创建cdsm客户端实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 已配对连接的合作设备集合的成员设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CdsmClient](nearlink-cdsm.md#cdsmclient) | cdsm客户端实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because the chip does not support it. |
| 1009700003 | Nearlink is off. |
| 1009700050 | Coordinated Devices Set Management not supported. |
| 1009700099 | Operation failed. |

**示例：**

```
1. import { cdsm } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
5. let client: cdsm.CdsmClient;
6. try {
7. client = cdsm.createCdsmClient(addr);
8. console.info('client: ' + JSON.stringify(client));
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## CdsmClient

PhonePC/2in1TabletTVWearable

提供获取远端设备的合作设备集合信息的方法，使用前需要使用cdsm.createCdsmClient方法创建一个CdsmClient实例。

一个应用针对一个远端设备只需要创建一次实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

### getCdsmInfo

PhonePC/2in1TabletTVWearable

getCdsmInfo(): CdsmInfo

查询远端设备的合作设备集合信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CdsmInfo](nearlink-cdsm.md#cdsminfo) | 远端设备的合作设备集合信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```
1. import { cdsm } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
5. let client: cdsm.CdsmClient;
6. try {
7. client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. let cdsmInformation: cdsm.CdsmInfo = client.getCdsmInfo();
9. console.info('cdsmInformation:' + JSON.stringify(cdsmInformation));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### onCdsmInfoChange

PhonePC/2in1TabletTVWearable

onCdsmInfoChange(callback: Callback<CdsmInfo>): void

订阅远端设备合作设备集合信息变化事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CdsmInfo](nearlink-cdsm.md#cdsminfo)> | 是 | 表示远端设备合作设备集合信息变化回调函数的入参。回调函数由用户创建，通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { cdsm } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<cdsm.CdsmInfo> = (data: cdsm.CdsmInfo) => {
6. console.info('CdsmInfo:' + JSON.stringify(data));
7. };

9. let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
10. let client: cdsm.CdsmClient;
11. try {
12. client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
13. client.onCdsmInfoChange(callback);
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

### offCdsmInfoChange

PhonePC/2in1TabletTVWearable

offCdsmInfoChange(callback?: Callback<CdsmInfo>): void

取消订阅远端设备合作设备集合信息变化事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CdsmInfo](nearlink-cdsm.md#cdsminfo)> | 否 | 回调函数，返回合作设备集合信息。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { cdsm } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<cdsm.CdsmInfo> = (data: cdsm.CdsmInfo) => {
6. console.info('CdsmInfo:' + JSON.stringify(data));
7. };

9. let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
10. let client: cdsm.CdsmClient;
11. try {
12. client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
13. client.onCdsmInfoChange(callback);
14. client.offCdsmInfoChange(callback);
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
```

## CdsmInfo

PhonePC/2in1TabletTVWearable

表示合作设备集合信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| members | Array<[CdsmMemberInfo](nearlink-cdsm.md#cdsmmemberinfo)> | 否 | 否 | 合作设备集合信息。 |

## CdsmMemberInfo

PhonePC/2in1TabletTVWearable

表示合作设备集合的成员信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 成员设备地址。 |
| state | [CdsmConnectionState](nearlink-cdsm.md#cdsmconnectionstate) | 否 | 否 | 成员设备连接状态。 |

## CdsmConnectionState

PhonePC/2in1TabletTVWearable

表示和远端设备的合作设备集合连接状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 表示已断连。 |
| CONNECTED | 1 | 表示已连接。 |
