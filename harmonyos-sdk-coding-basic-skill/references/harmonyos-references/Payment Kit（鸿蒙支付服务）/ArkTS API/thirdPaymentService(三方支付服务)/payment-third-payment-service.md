---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-third-payment-service
title: thirdPaymentService(三方支付服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > thirdPaymentService(三方支付服务)
category: harmonyos-references
scraped_at: 2026-06-01T16:37:09+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:850f5cb9123daa691fbc70ca81bb17d8cc4179f16958cc2d8238224769908a34
---
本模块提供直接通过依赖包拉起第三方支付方式收银台能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { thirdPaymentService } from '@kit.PaymentKit';
```

## PayMethod

PhonePC/2in1Tablet

三方支付方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WECHAT\_PAY | wechat\_pay | 微信支付。 |
| ALI\_PAY | ali\_pay | 支付宝支付。 |
| WECHAT\_MINI\_PROGRAM | wechat\_mini\_program | 拉起微信小程序。 |

## ThirdPayClient

PhonePC/2in1Tablet

支付请求客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

### constructor

PhonePC/2in1Tablet

constructor(context: common.UIAbilityContext, payMethod: PayMethod, thirdAppId: string);

构造器，构造三方支付等请求客户端ThirdPayClient实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | 是 | UIAbility上下文。 |
| payMethod | [PayMethod](payment-third-payment-service.md#paymethod) | 是 | 支付方式。 |
| thirdAppId | string | 是 | 三方支付应用appID。 |

**示例**：

```
1. import { thirdPaymentService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @State private thirdPayClient: thirdPaymentService.ThirdPayClient | null = null;

9. aboutToAppear() {
10. try {
11. const thirdAppid ='third_appid_123456'
12. // 初始化第三方支付客户端
13. this.thirdPayClient = new thirdPaymentService.ThirdPayClient(
14. this.getUIContext().getHostContext() as common.UIAbilityContext,
15. thirdPaymentService.PayMethod.WECHAT_PAY,
16. thirdAppid
17. );
18. } catch (error) {
19. console.error("支付客户端初始化失败:", error);
20. // 可在此处提示用户或跳转错误页面
21. }
22. }
23. payButtonClicked() {
24. if (!this.thirdPayClient) {
25. console.error("支付客户端未初始化");
26. return;
27. }
28. // 调用支付接口，传递订单信息
29. this.thirdPayClient.pay('{"xxx1":"***", "xxx2":"***", "token":"***"}');
30. }

32. build() {
33. Column() {
34. Button("立即支付")
35. .onClick(() => {
36. this.payButtonClicked();
37. })
38. }
39. .width("100%")
40. .height("100%")
41. .justifyContent(FlexAlign.Center)
42. }
43. }
```

### pay

PhonePC/2in1Tablet

pay(payInfo: string): Promise<void>;

该方法提供拉起三方支付方式收银台等功能，调用方法前请确保网络已连接，调用该方法后会拉起三方支付收银台，完成后使用Promise异步返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| payInfo | string | 是 | 拉起收银台传入的订单信息，payInfo是json字符串的格式（具体参数根据三方支付方式拉起收银台要求传递，参考[payInfo](../../数据模型说明/payment-model.md#payinfo)）。示例为{"xxx1":"**", "xxx2":"**", "token":"\*\*\*"} |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](<../ArkTS API错误码/payment-error-code.md>)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022830000 | The operation was canceled by the user. |
| 1022830001 | Pay failed. |
| 1022830002 | The payInfo invalid. Possible causes: 1.Data format is not json string; 2.Mandatory parameters are left unspecified. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件基本用法/uiability-usage.md#获取uiability的上下文信息>)

```
1. import { thirdPaymentService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

6. @Entry
7. @Component
8. struct Index {
9. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
10. thirdPaymentServicePayPromise() {
11. thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, "appid_123456");
12. // 不同支付方式参数构建参考示例如下：
13. // PayMethod.WECHAT_PAY：'{"appId":"***","partnerId":"***","prepayId":"***","packageValue":"***","nonceStr":"***","timeStamp":"***","sign":"***","extData":"***","token":"***"}'
14. // PayMethod.ALI_PAY：'{"orderInfo":"***", "token":"***"}'
15. // PayMethod.WECHAT_MINI_PROGRAM：'{"userName":"原始id", "path":"小程序启动路径", "miniProgramType":"小程序的类型，0-正式版 1-开发版 2-体验版 默认0", "extData":"***", "token":"***"}'
16. const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
17. thirdPayClient.pay(payInfo).then(() => {
18. // 支付成功
19. console.info('succeeded in paying.');
20. })
21. }

23. build() {
24. Column() {
25. Button('thirdPaymentServicePayPromise')
26. .type(ButtonType.Capsule)
27. .width('50%')
28. .margin(20)
29. .onClick(() => {
30. this.thirdPaymentServicePayPromise();
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

### handlePayCallback

PhonePC/2in1Tablet

handlePayCallback(want: Want): boolean;

该方法提供处理支付处理结果回调功能，调用方法前请确保网络已连接，请求处理完成后使用返回布尔类型结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| want | [Want](<../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 应用组件间的信息传递的载体。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 回调处理结果（该结果为用户支付操作处理结果，非实际支付结果，实际支付结果以三方支付结果为准）。  - true：用户支付操作成功  - false：用户支付操作失败 |

**示例**：

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. // 需要从thirdPayClient对象定义文档中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
3. import { thirdPayClient } from '../pages/thirdPaymentServicetest';

5. // 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
6. export default class EntryAbility extends UIAbility {
7. onNewWant(want: Want): void {
8. // 需要和拉起支付收银台的三方支付客户端对象为同一个
9. if (thirdPayClient) {
10. console.info('clientForThirdPayment handlePayCallback');
11. let handlePayCallback = thirdPayClient.handlePayCallback(want);
12. console.info(`clientForThirdPayment handlePayCallback result: ${handlePayCallback}`);
13. }
14. }
15. }
```
