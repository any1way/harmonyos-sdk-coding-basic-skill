---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-avatar-nickname
title: 获取头像昵称
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取头像昵称
category: harmonyos-guides
scraped_at: 2026-06-11T15:02:44+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:b9f2196932bcf03b603f570c5f8c1d1cf2560e6646f42176e430492ad3699bdd
---
## 场景介绍

当应用需要获取用户头像昵称信息，可使用Account Kit提供的头像昵称授权能力，用户允许应用获取头像昵称后，可快速完成个人信息填写。以下对Account Kit提供的头像昵称授权能力进行介绍。此外，开发者也可通过场景化控件中的[选择头像Button](<../../../Scenario Fusion Kit（融合场景服务）/场景化Button/选择头像Button/scenario-fusion-button-chooseavatar.md>)获取用户头像。

**图1** 手机端获取头像昵称（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/CAbPV6TzSu-iezMQHt9gkQ/zh-cn_image_0000002592379118.png?HW-CC-KV=V1&HW-CC-Date=20260611T070243Z&HW-CC-Expire=86400&HW-CC-Sign=37C0D036A82F01F0201EA2A96170E0622E06A0921DC14B239D75E2CE62A00381 "点击放大")

**图2** Wearable设备获取头像昵称（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/yJcTZM3gSCyDnWDAUZQAUw/zh-cn_image_0000002622858625.png?HW-CC-KV=V1&HW-CC-Date=20260611T070243Z&HW-CC-Expire=86400&HW-CC-Sign=2BF04A43B7A1F77497560EB94792DF3234E669AC3426EA8AEBFD481968711286 "点击放大")

## 约束与限制

获取头像昵称能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/DCXUGj_nQM6HqvU-pTahXw/zh-cn_image_0000002622698747.png?HW-CC-KV=V1&HW-CC-Date=20260611T070243Z&HW-CC-Expire=86400&HW-CC-Sign=2F72D4EF0FE13D59185D71390C96A05A77DB9B931474A499CC08423807901BDD)

流程说明：

1. 应用传对应scope调用授权API请求获取用户头像昵称。
2. 如用户已给应用授权，则开发者能直接获取用户头像昵称。
3. 如用户未授权，则授权请求会拉起授权页面，在用户确认授权后，开发者能获取到用户头像昵称。
4. 获取到头像url信息，开发者可以通过该url下载并使用用户头像。

## 接口说明

获取头像昵称关键接口如下表所示，具体API说明详见[API参考](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md>)。

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#createauthorizationwithhuaweiidrequest>)(): [AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>) | 获取授权请求对象接口，通过在[AuthorizationWithHuaweiIDRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidrequest>)对象中传入头像昵称的scope：profile及Authorization Code的permission：serviceauthcode，即可在授权结果中获取到用户头像昵称和Authorization Code。 |
| [constructor](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#constructor>)(context?: [common.Context](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.common (Ability公共模块)/js-apis-app-ability-common.md#context>)) | 创建授权请求Controller。 |
| [executeRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#executerequest-1>)(request: [AuthenticationRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authenticationrequest>)): Promise<[AuthenticationResponse](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authenticationresponse>)> | 通过Promise方式执行授权操作。  头像昵称，可从[AuthenticationResponse](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authenticationresponse>)的子类[AuthorizationWithHuaweiIDResponse](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authorizationwithhuaweiidresponse>)中解析，具体解析方法请参考[客户端开发](account-get-avatar-nickname.md#客户端开发)的示例代码。 |

注意

1.上述接口需在页面或自定义组件生命周期内调用。

2.未设置昵称默认返回华为账号绑定的匿名手机号/邮箱。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](../../开发准备/配置签名和指纹/account-sign-fingerprints.md)、[配置Client ID](<../../开发准备/配置Client ID/account-client-id.md>)。此场景无需申请账号权限。

注意

若未正确配置公钥指纹，将报错[1001500001 应用指纹证书校验失败](<../../Account Kit常见问题/1001500001 应用指纹证书校验失败的可能原因和解决办法/account-faq-1.md>)。

## 开发步骤

### 客户端开发

1. 导入[authentication](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md>)模块及相关公共模块。

   ```
   1. import { authentication } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { util } from '@kit.ArkTS';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建授权请求并设置参数。

   ```
   1. // 创建授权请求，并设置参数
   2. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   3. // 获取头像昵称需要传如下scope
   4. authRequest.scopes = ['profile'];
   5. // 若开发者需要进行服务端开发以获取头像昵称，则需传如下permission获取authorizationCode
   6. authRequest.permissions = ['serviceauthcode'];
   7. // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   8. authRequest.forceAuthorization = true;
   9. // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
   10. authRequest.state = util.generateRandomUUID();
   ```
3. 调用[AuthenticationController](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#authenticationcontroller>)对象的[executeRequest](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/authentication (华为账号应用统一认证服务)/account-api-authentication.md#executerequest-1>)方法执行授权请求，并处理授权结果，从授权结果中解析出头像昵称和Authorization Code。

   ```
   1. // 执行授权请求
   2. try {
   3. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   4. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
   5. controller.executeRequest(authRequest).then((data) => {
   6. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
   7. const state = authorizationWithHuaweiIDResponse.state;
   8. if (state && authRequest.state !== state) {
   9. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
   10. return;
   11. }
   12. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
   13. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
   14. const avatarUri = authorizationWithHuaweiIDCredential?.avatarUri;
   15. const nickName = authorizationWithHuaweiIDCredential?.nickName;
   16. // 开发者处理avatarUri, nickName
   17. const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
   18. // 涉及服务端开发以获取头像昵称场景，开发者处理authorizationCode
   19. }).catch((err: BusinessError) => {
   20. dealAllError(err);
   21. });
   22. } catch (error) {
   23. dealAllError(error);
   24. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError): void {
   3. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
   4. // 在应用获取头像昵称场景下，涉及UI交互时，建议按照如下错误码指导提示用户
   5. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   6. // 用户未登录华为账号，请登录华为账号并重试
   7. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   8. // 网络异常，请检查当前网络状态并重试
   9. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
   10. // 用户取消授权
   11. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
   12. // 系统服务异常，请稍后重试
   13. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
   14. // 重复请求，应用无需处理
   15. } else {
   16. // 获取用户信息失败，请稍后重试
   17. }
   18. }

   20. export enum ErrorCode {
   21. // 账号未登录
   22. ERROR_CODE_LOGIN_OUT = 1001502001,
   23. // 网络错误
   24. ERROR_CODE_NETWORK_ERROR = 1001502005,
   25. // 用户取消授权
   26. ERROR_CODE_USER_CANCEL = 1001502012,
   27. // 系统服务异常
   28. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   29. // 重复请求
   30. ERROR_CODE_REQUEST_REFUSE = 1001500002
   31. }
   ```

### 服务端开发（可选）

开发者根据业务需要选择是否进行服务端开发。

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/开放接口调用凭证/获取用户级凭证/account-api-obtain-user-token.md#接口原型>)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[获取用户信息接口](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/获取用户信息/获取华为账号用户信息-获取头像昵称/account-api-get-user-info-get-nickname-and-avatar.md#接口原型>)获取用户信息，从用户信息中获取用户头像昵称。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/获取用户信息/获取华为账号用户信息-获取头像昵称/account-api-get-user-info-get-nickname-and-avatar.md#错误码>)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/开放接口调用凭证/刷新用户级凭证/account-api-obtain-refresh-token.md#接口原型>)向华为账号服务器请求获取新的Access Token。

   说明

   1. 当Access Token失效时，若您不使用Refresh Token向账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，业务可重新登录授权获取Authorization Code，向账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](<../../../../../harmonyos-references/Account Kit（华为账号服务）/REST API/开放接口调用凭证/刷新用户级凭证/account-api-obtain-refresh-token.md#错误码>)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
