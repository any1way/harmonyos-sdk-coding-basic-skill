---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-issupported
title: 查询是否支持星闪
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 查询是否支持星闪
category: harmonyos-guides
scraped_at: 2026-06-01T11:19:51+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:8663f13218f6ab598056c4564c15de09a98cbf25d294d691af5424e335172b1e
---
## 场景介绍

从6.1.0(23)版本开始，新增查询是否支持星闪的能力。由于并非所有设备都支持星闪，使用星闪相关功能前可以主动查询当前设备是否支持星闪。

## 接口说明

提供查询当前设备是否支持星闪的方式。

| 接口名 | 描述 |
| --- | --- |
| [isNearLinkSupported](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/manager（星闪开关能力）/nearlink-manager.md#isnearlinksupported>)(): boolean | 主动查询当前设备是否支持星闪。 |

## 开发步骤

说明

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，查看当前设备是否支持星闪。

如果在不支持星闪的设备上调用星闪相关接口，可能会返回[801](../../../../../harmonyos-references/通用错误码/errorcode-universal.md#section801-该设备不支持此api)错误码。

1. 导入相关模块。

   ```
   1. import { manager } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 发起当前设备是否支持星闪的状态查询。

   ```
   1. try {
   2. let isSupported: boolean = manager.isNearLinkSupported();
   3. if (isSupported) {
   4. console.info('NearLink is supported on this device.');
   5. } else {
   6. console.info('NearLink is not supported on this device.');
   7. }
   8. } catch (err) {
   9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   10. }
   ```
