---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-scan
title: scan（星闪扫描能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > scan（星闪扫描能力）
category: harmonyos-references
scraped_at: 2026-06-11T16:14:48+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:d9fcc711d0d555df33bed74b0c17e851685b2ef17032f4a4c7e6282e54bff719
---
本模块提供了星闪扫描相关功能。

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { scan } from '@kit.NearLinkKit';
```

## startScan

PhonePC/2in1TabletTVWearable

startScan(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void>

发起星闪扫描。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<[ScanFilters](nearlink-scan.md#scanfilters)> | 是 | 表示扫描过滤器，配置期望扫描的设备名称、地址等信息。其中表示过滤条件的ScanFilters中全部字段均为可选字段，所有字段都未配置的ScanFilters代表一组空过滤器，视为无效过滤器而忽略。不允许filters中的所有ScanFilters都配置为空过滤器，否则返回错误码401。 |
| options | [ScanOptions](nearlink-scan.md#scanoptions) | 否 | 表示扫描选项。默认为低功耗模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```
1. import { scan } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scanFilter: scan.ScanFilters = {
5. address: '11:22:33:44:AA:FF', // 期望扫描到的外围设备地址
6. deviceName: 'device name' // 期望扫描到的外围设备名称
7. };
8. let scanOptions: scan.ScanOptions = {
9. scanMode: scan.ScanMode.SCAN_MODE_LOW_POWER
10. }
11. try {
12. scan.startScan([scanFilter], scanOptions).then(() => {
13. console.info("start scan success");
14. });
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
```

## stopScan

PhonePC/2in1TabletTVWearable

stopScan(): Promise<void>

停止星闪扫描。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```
1. import { scan } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. scan.stopScan().then(() => {
6. console.info("stop scan success");
7. });
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## on( 'deviceFound')

PhonePC/2in1TabletTVWearable

on(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void

订阅星闪扫描结果。回调函数携带远端设备的随机地址。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceFound'，表示星闪设备扫描结果上报事件。  当[scan.startScan](nearlink-scan.md#startscan)调用完成，发起星闪扫描，若扫描到星闪设备，触发该事件。 |
| callback | Callback‌<‌Array‌<‌[ScanResults](nearlink-scan.md#scanresults)‌>‌> | 是 | 回调函数，返回星闪扫描结果数组对象。扫描结果携带远端设备的随机地址。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```
1. import { scan } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onReceiveEvent:(data: Array<scan.ScanResults>) => void = (data: Array<scan.ScanResults>) => {
5. console.info('scan result addr:' + data[0].address + 'name:' + data[0].deviceName);
6. }
7. try {
8. scan.on('deviceFound', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## off( 'deviceFound')

PhonePC/2in1TabletTVWearable

off(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void

取消订阅星闪扫描结果。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceFound'，表示星闪设备扫描结果上报事件。 |
| callback | Callback<Array<‌[ScanResults](nearlink-scan.md#scanresults)‌>> | 否 | 回调函数，返回星闪扫描结果数组对象。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/nearlink-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```
1. import { scan } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. scan.off('deviceFound');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## ScanResults

PhonePC/2in1TabletTVWearable

表示扫描结果。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示扫描到设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备rssi值，取值范围[-128, 127]，单位dBm，其中127表示无效值。 |
| data | ArrayBuffer | 否 | 否 | 表示广播包数据。 |
| deviceName | string | 否 | 否 | 表示扫描到的设备名称。字符串长度范围[0, 30]。 |
| isConnectable | boolean | 否 | 否 | 表示扫描到的广播是否可连接。true：可连接，false：不可连接 |
| deviceClass | [constant.DeviceClass](../constant（星闪公共常量定义）/nearlink-constant.md#deviceclass) | 否 | 是 | 表示扫描到的设备类型  **起始版本：** 5.1.0(18) |

## ScanFilters

PhonePC/2in1TabletTVWearable

表示扫描过滤条件。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 是 | 表示设备地址，若未配置则默认不过滤该字段。地址格式参考："11:22:33:AA:BB:FF"。 |
| deviceName | string | 否 | 是 | 表示设备名称，字符串长度范围[0, 30]。若未配置则默认不过滤该字段。 |
| manufacturerId | number | 否 | 是 | 表示厂商ID，取值范围[1, 65535]，若未配置则默认不过滤该字段。 |
| manufacturerData | ArrayBuffer | 否 | 是 | 表示厂商数据，若未配置则默认不过滤该字段。配置该字段需同时配置manufacturerId。 |
| manufacturerDataMask | ArrayBuffer | 否 | 是 | 表示厂商数据掩码，若未配置则默认不过滤该字段。配置该字段需同时配置manufacturerData，且二者长度必须一致。 |

## ScanOptions

PhonePC/2in1TabletTVWearable

表示扫描选项。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanMode | [ScanMode](nearlink-scan.md#scanmode) | 否 | 是 | 表示扫描模式。默认值为"SCAN\_MODE\_LOW\_POWER" |
| duration | number | 否 | 是 | 表示扫描持续时间。单位second，取值范围[10, 60]，默认值为全时段扫描 |

## ScanMode

PhonePC/2in1TabletTVWearable

表示扫描模式，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_LOW\_POWER | 0 | 表示低功耗扫描模式，扫描频率低，功耗低。默认值。 |
| SCAN\_MODE\_BALANCED | 1 | 表示均衡扫描模式，扫描频率中等，功耗中等。 |
