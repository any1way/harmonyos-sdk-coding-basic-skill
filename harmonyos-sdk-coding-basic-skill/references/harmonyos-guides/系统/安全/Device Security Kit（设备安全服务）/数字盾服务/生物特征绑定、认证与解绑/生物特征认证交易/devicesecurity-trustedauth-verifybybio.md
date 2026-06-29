---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-verifybybio
title: 生物特征认证交易
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 生物特征认证交易
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:07+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:b8ae34579969d2472e49860ff04d6b2604c301b38234e92e01c7cd19a67a309d
---
## 场景介绍

在完成对应生物特征认证能力开通后，用户即可通过已绑定的生物特征（人脸或指纹）完成认证交易。

## 约束与限制

1. 本功能在API 24之前版本仅支持Phone；API24及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#checkconfirmuitextformat>)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。
2. 当前仅支持绑定一个指纹或人脸用于支付认证。
3. 本功能需应用服务器端完成接口接入，以配合端云协同认证流程。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/wTuWl5paQF-UY7afngFnBg/zh-cn_image_0000002592378750.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T064406Z&HW-CC-Expire=86400&HW-CC-Sign=76D8856B5901D07E7FF5581F5331F92E087D090B7FBDC0DA34D45A45D110E730)

## 接口说明

接口及使用方法请参见[API参考](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/ArkTS API错误码/TrustedAuthentication （数字盾服务）/devicesecurity-arktsapi-errcode-trusted-auth.md>)。

| 接口名 | 描述 |
| --- | --- |
| [procContentAuthentication](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#proccontentauthentication>)(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken> | 交易信息处理接口 |
| [getBiometricAuthToken](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#getbiometricauthtoken>)(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken> | 获取生物特征交易认证的authToken信息 |

## 生物特征认证交易界面介绍

如图表示使用人脸进行交易认证对应的UI界面示例，当用户确认交易信息内容后，则会拉起系统人脸认证界面完成对应生物特征认证交易。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/A_U1z1_pSMa9pOB49D_dFA/zh-cn_image_0000002622858257.png?HW-CC-KV=V1&HW-CC-Date=20260611T064406Z&HW-CC-Expire=86400&HW-CC-Sign=E2C68E8E4D2B735CAEB2B08954919412883FE9195427166420ED0234800B8181)

## 开发步骤

1. 导入huks 、userAuth 、trustedAuthentication 和相关依赖模块。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit'
   2. import { huks } from '@kit.UniversalKeystoreKit';
   3. import { userAuth } from '@kit.UserAuthenticationKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   6. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   7. import { hilog } from '@kit.PerformanceAnalysisKit';
   8. import { common } from '@kit.AbilityKit';
   ```
2. 首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起生物特征认证交易。
3. 发起生物特征认证交易前，需从服务器获取当前账号在[设置数字盾密码](../../数字盾密码管理/设置数字盾密码/devicesecurity-trustedauth-setpwd.md)时获取的authID。
4. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>)，初始化签名会话。
5. 调用数字盾交易信息处理接口[procContentAuthentication](<../../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md#proccontentauthentication>)发起生物特征认证前的交易信息确认申请。

   ```
   1. async function FaceAuthContent(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   2. try {
   3. const authID: bigint = 11842183505170721246n; //实际填充为从服务器获取到的账号对应的authID值
   4. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   5. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   6. const reqParams:trustedAuthentication.AuthReqParams = {
   7. reqType: trustedAuthentication.AuthType.AUTH_TYPE_FACE,
   8. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"], //实际使用时填充为交易信息，每一行交易信息为其中的一个字符串成员
   9. }
   10. const buffer = fileData.buffer;
   11. const label:trustedAuthentication.TUILable = {
   12. image: buffer as ArrayBuffer,
   13. title: "人脸交易认证",
   14. }
   15. const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
   16. return result;
   17. } catch (err) {
   18. hilog.error(0x0000, 'testTag', `Failed to procContentAuthentication, code:${err.code}, message:${err.message}`);
   19. throw new Error('Content verify by face failed:' + (err as BusinessError).message);
   20. }
   21. }
   22. const rand = cryptoFramework.createRandom();
   23. const len: number = 32;
   24. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data; //实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   25. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   26. const authToken: trustedAuthentication.AuthToken = await FaceAuthContent(challenge, context);
   ```
6. 通过用户认证服务提供的接口，拉起生物特征认证控件并[发起认证](<../../../../User Authentication Kit（用户认证服务）/用户身份认证开发指导/发起认证/start-authentication.md>)。
7. 当订阅的生物认证结果获取到后，将数字盾交易信息确认结果和生物特征认证结果统一整合，发起生物特征认证交易请求。

   ```
   1. let tuiAuthToken = new Uint8Array(1024);//实际使用时请替换为步骤5获取的交易信息确认authToken
   2. let bioAuthToken = new Uint8Array(1024);//实际使用时请替换为步骤6获取的生物特征认证authToken
   3. let operType = trustedAuthentication.OperateType.OPERATE_TYPE_CONTENT_AUTH;
   4. trustedAuthentication.getBiometricAuthToken(operType, tuiAuthToken, bioAuthToken).then((newBioAuthToken) => {
   5. let authToken = newBioAuthToken.authToken as Uint8Array;
   6. });
   ```
8. 参考密钥管理服务提供的[签名/验签指导](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/密钥使用/签名验签/签名验签(ArkTS)/huks-signing-signature-verification-arkts.md>), 对返回的authToken数据和交易信息明文进行签名，并结束签名会话。
9. 应用在交易信息验签通过后，可在应用对应服务器比对已绑定的生物特征凭证（credential）与当前交易认证采集的生物特征标识符（credential ID），确保账号绑定的生物特征信息与交易请求认证使用的生物特征信息的一致性。
