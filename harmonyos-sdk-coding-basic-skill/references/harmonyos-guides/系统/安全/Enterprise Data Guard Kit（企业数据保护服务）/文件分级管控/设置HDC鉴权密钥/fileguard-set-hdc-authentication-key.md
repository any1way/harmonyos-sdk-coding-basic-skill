---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-hdc-authentication-key
title: 设置HDC鉴权密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置HDC鉴权密钥
category: harmonyos-guides
scraped_at: 2026-06-01T11:17:09+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:bd37a6979d789078622716583d7b3d56c7828e1fb5c388528446ca8cf14522c4
---
说明

从6.1.1(24)版本开始，新增HDC鉴权密钥设置接口，支持用户在企业设备上开展安全调试，进一步强化设备安全性。

## 场景介绍

该接口可为上位机和下位机配置HDC鉴权密钥，确保仅在双方均为企业设备的特定场景下才允许连接和调试，从而有效保障企业资产不被篡改和泄露。

## 接口说明

详细接口说明可参考[接口文档](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md>)。

| 接口名 | 描述 |
| --- | --- |
| [setHdcAuthenticationKey](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#sethdcauthenticationkey>)(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void> | 使用Promise方式设置上下位机间的HDC鉴权密钥。 |

## 开发步骤

1. 应用需要通过OpenSSL在本地生成一个3072位的RSA密钥对。

   通过OpenSSL生成私钥：

   ```
   1. openssl genpkey -algorithm RSA -out private_key_3072.pem -pkeyopt rsa_keygen_bits:3072
   ```

   根据私钥提取公钥：

   ```
   1. openssl rsa -in private_key_3072.pem -pubout -out public_key_3072.pem
   ```
2. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   ```
3. 初始化[FileGuard](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#fileguard>)对象guard，调用接口[setHdcAuthenticationKey](<../../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#sethdcauthenticationkey>)，设置上下位机之间的HDC鉴权密钥。上位机需要下发私钥，下位机下发公钥，从而实现上位机对下位机的安全调试。

   ```
   1. function testSetHdcAuthenticationKey() {
   2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   3. let devType: fileGuard.AuthenticateDeviceType = fileGuard.AuthenticateDeviceType.UPPER;
   4. let keyType: fileGuard.AuthenticateKeyType = fileGuard.AuthenticateKeyType.PUBLIC_KEY;
   5. // 将对应的密钥转为Uint8Array类型
   6. let key: Uint8Array = new Uint8Array([0]);

   8. guard.setHdcAuthenticationKey(devType, keyType, key).then(() => {
   9. console.info(`Succeeded in setting the HDC authentication key.`);
   10. }).catch((error: BusinessError) => {
   11. console.error(`Failed to set the HDC authentication key. Code: ${error.code}, message: ${error.message}.`);
   12. })
   13. }
   ```
