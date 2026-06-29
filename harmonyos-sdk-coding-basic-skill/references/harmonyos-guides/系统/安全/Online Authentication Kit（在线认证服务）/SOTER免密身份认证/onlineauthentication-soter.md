---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-soter
title: SOTER免密身份认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > SOTER免密身份认证
category: harmonyos-guides
scraped_at: 2026-06-11T14:45:22+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:8201554dd1f21878315a23171ee24c0ab4dd86b90a74bc567656a0a6d5c2ac56
---
## 场景介绍

用户可以利用生物特征来代替传统的密码验证，实现免密身份认证。

* 开通：提供移动端开通SOTER生物特征（指纹/3D人脸）免密身份认证的能力。
* 认证：提供移动端采用生物特征（指纹/3D人脸）进行SOTER免密身份认证的能力。
* 注销：提供移动端注销SOTER生物特征（指纹/3D人脸）免密身份认证的能力。

## 基本概念

SOTER旨在提供一套生物认证平台和标准，使得业务可以采用设备上的传感器（如人脸传感器/指纹传感器）进行安全、高效的免密登录、免密支付等操作，当前已广泛应用于微信小程序/公众号、指纹支付等业务场景。

## 相关权限

* 获取网络权限：ohos.permission.INTERNET。
* 获取振动权限：ohos.permission.VIBRATE。
* 获取生物识别权限：ohos.permission.ACCESS\_BIOMETRIC。

## 约束与限制

* 开发者应用需要部署SOTER服务器。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { userAuth } from '@kit.UserAuthenticationKit';

  4. try {
  5. // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
  6. userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
  7. console.info('current auth trust level is supported');
  8. } catch (error) {
  9. const err: BusinessError = error as BusinessError;
  10. console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  11. }
  ```
* 移动端设备使用此服务时需要处于联网状态。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/r1nx1rsrRRGPU_JUhWlBVw/zh-cn_image_0000002592378762.png?HW-CC-KV=V1&HW-CC-Date=20260611T064522Z&HW-CC-Expire=86400&HW-CC-Sign=2C34FF1D1F05B86C127FF8F4E30E9BCCDBB2C4BE52B82C84F1732B47E1AAB8D4)

## 接口说明

**表1** 开通、认证、注销的所需要的接口

| 接口名 | 描述 |
| --- | --- |
| [generateAppSecureKey](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#generateappsecurekey>)(keyType: [KeyType](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#keytype>)): Promise<Uint8Array> | 生成应用密钥。 |
| [generateAuthKey](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#generateauthkey>)(keyAlias: string, keyType: [KeyType](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#keytype>)): Promise<[SignedResult](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#signedresult>)> | 生成认证密钥。 |
| [generateChallengeSync](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#generatechallengesync>)(keyAlias: string): Uint8Array | 生成Challenge。 |
| [signWithAuthKeySync](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#signwithauthkeysync>)(keyAlias: string, authToken: Uint8Array, info: string): [SignedResult](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#signedresult>) | 使用认证密钥对业务数据签名。 |
| [deleteAuthKey](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/SOTER/onlineauthentication-soter-api.md#deleteauthkey>)(keyAlias: string): Promise<void> | 删除认证密钥。 |

## 开发步骤

1. 导入SOTER模块。

   ```
   1. import { soter } from '@kit.OnlineAuthenticationKit';
   2. import { userAuth } from '@kit.UserAuthenticationKit';
   ```
2. 生成应用密钥和认证密钥用于后续的开通、认证流程。

   ```
   1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   2. let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名

   4. // 生成应用密钥
   5. try {
   6. let appSecureKey: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
   7. } catch (error) {
   8. const err = error as BusinessError;
   9. console.error(`Failed to generate app secure key. Code is ${err.code}, message is ${err.message}`);
   10. }
   11. // 生成AuthKey
   12. try {
   13. let authKey: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
   14. } catch (error) {
   15. const err = error as BusinessError;
   16. console.error(`Failed to generate auth key. Code is ${err.code}, message is ${err.message}`);
   17. }
   ```
3. 使用认证密钥签名，实现SOTER免密认证。

   ```
   1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   2. let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名
   3. let info: string = 'Message to be signed.'; // info需要开发者的三方应用服务器下发，SOTER服务完成签名后需要重新上传给三方应用服务器

   5. // 获取此次免密支付的challenge
   6. let soterChallenge: Uint8Array = new Uint8Array([0]);
   7. try {
   8. soterChallenge = soter.generateChallengeSync(keyAlias);
   9. } catch (error) {
   10. const err = error as BusinessError;
   11. console.error(`Failed to generate challenge. Code is ${err.code}, message is ${err.message}`);
   12. }
   13. let authParam: userAuth.AuthParam = {
   14. challenge: soterChallenge,
   15. authType: [userAuth.UserAuthType.FINGERPRINT],
   16. authTrustLevel: userAuth.AuthTrustLevel.ATL4
   17. };
   18. // 使用preAuthResult请求身份认证
   19. try {
   20. let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
   21. // 未获取到authToken则会返回错误码1。
   22. userAuthInstance.on('result', {
   23. onResult(result) {
   24. let authToken = result.token;
   25. try {
   26. // 生物特征认证成功后，调用soter认证
   27. console.info('soter auth start');
   28. // 使用soter.signWithAuthKeySync接口为待认证数据签名。开发者根据业务需求选择同步/异步接口。
   29. let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info);
   30. console.info('Succeeded in doing authSyn authResult');
   31. // 开发者处理authResult
   32. } catch (err) {
   33. console.error(`Failed to signWithAuthKeySync. Code: ${err.code}, message: ${err.message}`);
   34. }
   35. }
   36. });
   37. userAuthInstance.start();
   38. } catch (error) {
   39. const err = error as BusinessError;
   40. console.error(`Failed to user auth. Code is ${err.code}, message is ${err.message}`);
   41. }
   ```
4. 关闭免密认证时，删除认证密钥。

   ```
   1. // 删除AuthKey
   2. let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名
   3. try {
   4. soter.deleteAuthKey(keyAlias);
   5. } catch (error) {
   6. const err = error as BusinessError;
   7. console.error(`Failed to delete auth key. Code is ${err.code}, message is ${err.message}`);
   8. }
   ```
