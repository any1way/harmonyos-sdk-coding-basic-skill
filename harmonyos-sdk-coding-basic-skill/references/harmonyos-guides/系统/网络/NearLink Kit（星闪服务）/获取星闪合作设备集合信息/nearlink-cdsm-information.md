---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-cdsm-information
title: 获取星闪合作设备集合信息
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 获取星闪合作设备集合信息
category: harmonyos-guides
scraped_at: 2026-06-01T11:19:57+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:0666e212cc2ec6fbd9f4e9f0caae6a328e6361cd70455da241b76b1cabae7640
---
## 场景介绍

从6.1.1(24)开始支持获取星闪合作设备集合信息。

合作设备集合是由多个成员设备协同提供特定服务的整体，例如一副星闪耳机包含左右两个耳机单元。当配对的外设属于某个合作设备集合时，通过[getPairedDevices](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/manager（星闪开关能力）/nearlink-manager.md#getpaireddevices>)接口仅能获取该集合中首个配对的成员设备，无法直接获取其他成员设备信息。作为集合使用者，可通过主动查询或订阅通知的方式，获取该合作设备集合内所有成员设备的完整信息。

更多技术细节可参考[星闪标准](https://www.isla.org.cn/trial)《星闪无线通信系统 基础应用层 合作设备集合管理》。

## 接口说明

提供2种获取星闪开关状态的方式，主动查询和订阅状态变化。

| 接口名 | 描述 |
| --- | --- |
| [createCdsmClient](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#createcdsmclient>)(address: string): [CdsmClient](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#cdsmclient>) | 创建合作设备集合客户端实例。 |
| [getCdsmInfo](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#getcdsminfo>)(): [CdsmInfo](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#cdsminfo>) | 主动查询合作设备集合里所有成员设备的信息。 |
| [onCdsmInfoChange](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#oncdsminfochange>)(callback: Callback<CdsmInfo>): void | 订阅合作设备集合成员设备的信息变化事件。 |
| [offCdsmInfoChange](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md#offcdsminfochange>)(callback?: Callback<CdsmInfo>): void | 取消订阅合作设备集合成员设备的信息变化事件。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { cdsm } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { Callback } from '@kit.BasicServicesKit';
   ```
2. 创建合作设备集合客户端实例，参数addr是通过[getPairedDevices](<../../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/manager（星闪开关能力）/nearlink-manager.md#getpaireddevices>)获取的设备地址，并且此设备是合作设备集合的成员设备。

   ```
   1. let addr: string = '00:11:22:33:AA:FF';
   2. let client: cdsm.CdsmClient;
   3. try {
   4. client = cdsm.createCdsmClient(addr);
   5. console.info('client: ' + JSON.stringify(client));
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
3. 主动查询合作设备集合里所有成员设备的信息。

   ```
   1. try {
   2. let cdsmInformation: cdsm.CdsmInfo = client.getCdsmInfo();
   3. console.info('cdsmInformation:' + JSON.stringify(cdsmInformation));
   4. } catch (err) {
   5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   6. }
   ```
4. 通过注册的方式订阅合作设备集合成员设备的信息变化。

   ```
   1. let callback: Callback<cdsm.CdsmInfo> = (data: cdsm.CdsmInfo) => {
   2. console.info('CdsmInfo:' + JSON.stringify(data));
   3. };

   5. try {
   6. client.onCdsmInfoChange(callback);
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
5. 取消订阅合作设备集合成员设备的信息变化。

   ```
   1. try {
   2. client.offCdsmInfoChange(callback);
   3. } catch (err) {
   4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   5. }
   ```
