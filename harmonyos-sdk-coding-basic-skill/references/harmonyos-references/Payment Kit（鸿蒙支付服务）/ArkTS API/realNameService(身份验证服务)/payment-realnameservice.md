---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-realnameservice
title: realNameService(身份验证服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > realNameService(身份验证服务)
category: harmonyos-references
scraped_at: 2026-06-01T16:37:07+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:0001feadee651838fd291f3e7e7f571774017a8f735d407b0190cdb28e7d4a93
---
本模块提供身份验证服务，包括“实名信息验证”、“实名信息授权”和“人脸核身实人验证”三种功能。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

## 导入模块

PhonePC/2in1Tablet

```
1. import { realNameService } from '@kit.PaymentKit';
```

## startRealNameVerification

PhonePC/2in1Tablet

startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供实名信息验证功能，调用该方法后会拉起实名信息验证授权组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | common.[UIExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIExtensionContext/js-apis-inner-application-uiextensioncontext.md>) | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考[实名信息预验证](<../../REST API/通用接口/实名信息验证与授权/实名信息预验证/payment-api-common-verification-preverify.md>)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回实名信息验证ID，用于[实名信息验证结果查询](<../../REST API/通用接口/实名信息验证与授权/实名信息验证结果查询/payment-api-common-verification-result.md>)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/payment-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件基本用法/uiability-usage.md#获取uiability的上下文信息>)

```
1. import { realNameService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. requestStartRealNameVerificationPromise() {
9. // 请使用开发者真实的预验证ID（preVerifyId）
10. let preVerifyId = 'your_pre_verify_id';
11. realNameService.startRealNameVerification(this.context, preVerifyId)
12. .then((verifyResultId: string) => {
13. // 验证成功
14. console.info(`succeeded in verifying, verifyResultId: ${verifyResultId}`);
15. })
16. }

18. build() {
19. Column() {
20. Button('requestStartRealNameVerificationPromise')
21. .type(ButtonType.Capsule)
22. .width('50%')
23. .margin(20)
24. .onClick(() => {
25. this.requestStartRealNameVerificationPromise();
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

## startRealNameAuth

PhonePC/2in1Tablet

startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>

该方法提供实名信息授权功能，调用该方法后会拉起实名信息授权组件，授权完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | common.[UIExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIExtensionContext/js-apis-inner-application-uiextensioncontext.md>) | 是 | UIAbility上下文。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回实名信息授权ID，用于[实名信息授权结果查询](<../../REST API/通用接口/实名信息验证与授权/实名信息授权结果查询/payment-api-common-auth-result.md>)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/payment-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件基本用法/uiability-usage.md#获取uiability的上下文信息>)

```
1. import { realNameService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. requestStartRealNameAuthPromise() {
9. realNameService.startRealNameAuth(this.context)
10. .then((realNameAuthId: string) => {
11. // 授权成功
12. console.info(`succeeded in authorizing, realNameAuthId: ${realNameAuthId}`);
13. })
14. }

16. build() {
17. Column() {
18. Button('requestStartRealNameAuthPromise')
19. .type(ButtonType.Capsule)
20. .width('50%')
21. .margin(20)
22. .onClick(() => {
23. this.requestStartRealNameAuthPromise();
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## startFaceVerification

PhonePC/2in1Tablet

startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供人脸核身实人验证功能，调用该方法后会拉起人脸核身实人验证组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | common.[UIExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIExtensionContext/js-apis-inner-application-uiextensioncontext.md>) | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考[人脸核身实人预验证](<../../REST API/通用接口/人脸核身实人验证/人脸核身实人预验证/payment-api-common-face-verifactaion-preverify.md>)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回验证结果ID，用于[人脸核身实人验证结果查询](<../../REST API/通用接口/人脸核身实人验证/人脸核身实人验证结果查询/payment-api-common-face-verifactaion-result.md>)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/payment-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100006 | The camera permission is not granted. |
| 1020100007 | The liveness detection failed. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件基本用法/uiability-usage.md#获取uiability的上下文信息>)

```
1. import { realNameService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. requestStartFaceVerificationPromise() {
9. // 请使用开发者真实的预验证ID（preVerifyId）
10. let preVerifyId = 'your_pre_verify_id';
11. realNameService.startFaceVerification(this.context, preVerifyId)
12. .then((verifyResultId:string) => {
13. // 人脸验证成功
14. console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
15. })
16. }

18. build() {
19. Column() {
20. Button('requestStartFaceVerificationPromise')
21. .type(ButtonType.Capsule)
22. .width('50%')
23. .margin(20)
24. .onClick(() => {
25. this.requestStartFaceVerificationPromise();
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```
