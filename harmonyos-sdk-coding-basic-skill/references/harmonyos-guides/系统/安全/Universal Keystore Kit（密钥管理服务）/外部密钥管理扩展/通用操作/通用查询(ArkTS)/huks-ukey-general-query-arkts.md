---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-general-query-arkts
title: 通用查询(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 通用查询(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3020b581dc5f905e0f9b1c016181611a274b9c1b05e929dbeef215183256d36
---
从API 22开始，huksExternalCrypto提供通用查询功能接口。该接口可以用于从UKey中获取设备标识、App标识以及其他通用属性信息，完成属性查询操作。具体的场景介绍请参考[获取属性介绍及规格](../通用查询介绍及规格/huks-ukey-general-query-overview.md)。

## 开发步骤

**获取属性**

1. 通过证书管理系统能力提供的[证书选择接口](<../../../../../../../harmonyos-references/安全/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.certManagerDialog (证书管理对话框模块)/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22>)获取[keyUri](<../../../../../../../harmonyos-references/安全/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.certManagerDialog (证书管理对话框模块)/js-apis-certmanagerdialog.md#certreference22>)作为resourceId，并[打开资源](../../资源管理/打开资源关闭资源(CC++)/huks-open-close-resource-ndk.md#打开资源)。
2. 构造输入参数propertyId和可选输入参数[param](<../../../../../../../harmonyos-references/安全/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huksExternalCrypto (外部密钥管理)/js-apis-huksexternalcrypto.md#huksexternalcryptoparam>)。
3. 调用[getProperty](<../../../../../../../harmonyos-references/安全/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huksExternalCrypto (外部密钥管理)/js-apis-huksexternalcrypto.md#huksexternalcryptogetproperty>)获取属性信息。

## 开发案例

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function getProperty(): Promise<Array<huksExternalCrypto.HuksExternalCryptoParam>> {
5. // 1. 获取resourceId, 假设获取的resourceId如下，并已经打开该资源
6. const testResourceId = JSON.stringify({
7. providerName: "testProviderName",
8. bundleName: "com.example.cryptoapplication",
9. abilityName: "CryptoExtension",
10. index: {
11. key: "testKey"
12. } as ESObject
13. });

15. // 2. 构造输入参数propertyId和可选参数param
16. let propertyId = "SKF_EnumDev";
17. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

19. // 3. 调用getProperty获取属性信息
20. console.info(`promise: await huksExternalCrypto getProperty`);
21. try {
22. await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
23. .then((data) => {
24. console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
25. }).catch((error: BusinessError) => {
26. console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
27. })
28. } catch (error) {
29. console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
30. }
31. return extProperties;
32. }
```
