---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-ifaa
title: IFAA免密身份认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > IFAA免密身份认证
category: harmonyos-guides
scraped_at: 2026-06-11T14:45:20+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:af919d498e256f42eb33fa617200bd7e5476b4e0eb39fbb79b90b353107ccbfe
---
## 场景介绍

* 开通：提供移动端开通生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已有的生物特征类型进行开通，会开通移动端对应生物特征类型的IFAA免密身份认证能力。
* 认证：提供移动端认证生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征进行认证，认证成功；使用未开通的生物特征进行认证，认证失败。
* 注销：提供移动端注销生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征类型进行注销，会注销移动端对应生物特征类型的IFAA免密身份认证能力。

## 基本概念

互联网金融身份认证联盟（IIFAA），全称为International Internet Finance Authentication Alliance，是一个生物识别框架，它由IIFAA联盟推出并持续维护。

## 相关权限

获取生物识别权限：ohos.permission.ACCESS\_BIOMETRIC。

## 约束与限制

* 开发者应用已接入IIFAA联盟，可以从IIFAA中心服务器获取签名数据。
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/YWTxoDS-RvuRABNCDe1Mng/zh-cn_image_0000002592218828.png?HW-CC-KV=V1&HW-CC-Date=20260611T064519Z&HW-CC-Expire=86400&HW-CC-Sign=60877A2EF955C163801843803D32CD9498CFAF93E1936789CF51CD5D9BB3A76B)

## 接口说明

**表1** 开通、认证、注销的所需要的接口

| 接口名 | 描述 |
| --- | --- |
| [register](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/IFAA/onlineauthentication-ifaa-api.md#register>)(registerData: Uint8Array): Promise<Uint8Array> | 开通指定用户的指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| [auth](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/IFAA/onlineauthentication-ifaa-api.md#auth>)(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array> | 使用指定用户的生物信息类型进行IFAA免密身份认证。 |
| [deregisterSync](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/IFAA/onlineauthentication-ifaa-api.md#deregistersync>)(deregisterData: Uint8Array): void | 注销指定用户指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| [getAnonymousIdSync](<../../../../../harmonyos-references/Online Authentication Kit（在线认证服务）/ArkTS API/IFAA/onlineauthentication-ifaa-api.md#getanonymousidsync>)(userToken: Uint8Array): Uint8Array | 获取IFAA免密认证的匿名化ID。 |

## 开发步骤

1. 注册IFAA免密身份认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。此处new Uint8Array([0])需要替换为开发者定义的用户标识。
   5. let arg = new Uint8Array([0]);
   6. let getAnonIdResult: Uint8Array;
   7. try {
   8. getAnonIdResult = ifaa.getAnonymousIdSync(arg);
   9. } catch (error) {
   10. const err = error as BusinessError;
   11. console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   12. }

   15. // 开发者需使用getAnonIdResult从服务端获取签名后的开通数据
   16. // 开发者将开通数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.register接口。此处new Uint8Array([0])需要替换为有效数据。
   17. let registerTlvFp = new Uint8Array([0]);
   18. try {
   19. let registerPromise: Promise<Uint8Array> = ifaa.register(registerTlvFp);
   20. registerPromise.then(registerResult => {
   21. console.info('Succeeded in doing register.');
   22. // 开通成功，开发者获取ifaa.register结果并处理。
   23. }).catch((err: BusinessError) =>{
   24. console.error(`Failed to call register. Code: ${err.code}, message: ${err.message}`);
   25. // 开通失败，开发者获取ifaa.register错误并处理。
   26. });
   27. } catch (error) {
   28. const err = error as BusinessError;
   29. console.error(`Failed to register. Code is ${err.code}, message is ${err.message}`);
   30. }
   ```
2. 使用IFAA免密身份认证进行认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit';
   2. import { userAuth } from '@kit.UserAuthenticationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。arg需要替换开发者自定义数据。
   6. let arg = new Uint8Array([0]);
   7. let getAnonIdResult: Uint8Array;
   8. try {
   9. getAnonIdResult = ifaa.getAnonymousIdSync(arg);
   10. } catch (error) {
   11. const err = error as BusinessError;
   12. console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   13. }

   15. // 开发者需使用getAnonIdResult从服务端获取签名后的认证数据

   17. // 获取此次免密支付的challenge
   18. let ifaaChallenge: Uint8Array = new Uint8Array([0]);
   19. try {
   20. ifaaChallenge = ifaa.preAuthSync();
   21. } catch (error) {
   22. const err = error as BusinessError;
   23. console.error(`Failed to pre auth. Code is ${err.code}, message is ${err.message}`);
   24. }
   25. let authParam: userAuth.AuthParam = {
   26. challenge: ifaaChallenge,
   27. authType: [userAuth.UserAuthType.FINGERPRINT],
   28. authTrustLevel: userAuth.AuthTrustLevel.ATL4
   29. };
   30. // 使用preAuthResult请求身份认证
   31. try {
   32. let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
   33. userAuthInstance.on('result', {
   34. onResult(result) {
   35. let authToken = result.token;
   36. try {
   37. // 生物特征认证成功后，调用IFAA认证
   38. console.info('IFAA auth start');
   39. // 开发者将认证数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.auth接口。此处new Uint8Array([0])需要替换为有效数据。
   40. let authTlvFp = new Uint8Array([0]);
   41. // 开发者根据业务需求选择同步/异步接口
   42. let authResult: Uint8Array = ifaa.authSync(authToken, authTlvFp);
   43. console.info('authSyn authResult' + authResult);
   44. // 开发者处理authResult
   45. } catch (error) {
   46. const err: BusinessError = error as BusinessError;
   47. console.error(`Failed to call auth. Code is ${err.code}, message is ${err.message}`);
   48. }
   49. }
   50. });
   51. userAuthInstance.start();
   52. } catch (error) {
   53. const err = error as BusinessError;
   54. console.error(`Failed to user auth. Code is ${err.code}, message is ${err.message}`);
   55. }
   ```
3. 注销IFAA免密身份认证。

   ```
   1. import { ifaa } from '@kit.OnlineAuthenticationKit';

   3. // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array, 再使用ifaa.getAnonymousIdSync接口。此处new Uint8Array([0])需要替换为开发者定义的用户标识。
   4. let arg = new Uint8Array([0]);
   5. try {
   6. let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
   7. } catch (error) {
   8. const err = error as BusinessError;
   9. console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   10. }

   13. // 开发者需使用getAnonymousId的结果从服务端获取签名后的注销数据
   14. // 开发者将注销数据（IIFAA协议的TLV格式）转换为Uint8Array, 再使用ifaa.deregisterSync接口。此处new Uint8Array([0])需要替换为有效数据。
   15. let deregisterTlvFp = new Uint8Array([0]);
   16. try {
   17. ifaa.deregisterSync(deregisterTlvFp);
   18. } catch (error) {
   19. const err = error as BusinessError;
   20. console.error(`Failed to deregister. Code is ${err.code}, message is ${err.message}`);
   21. }
   ```

## 常见问题

现象描述：开通IFAA免密身份认证失败。

可能原因：移动端设备没有联网。

处理步骤：移动端设备连接WIFI或热点，再次尝试。
