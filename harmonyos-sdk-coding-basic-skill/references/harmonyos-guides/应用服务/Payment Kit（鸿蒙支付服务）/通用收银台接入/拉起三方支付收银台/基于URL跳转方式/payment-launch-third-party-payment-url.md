---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-launch-third-party-payment-url
title: 基于URL跳转方式
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 拉起三方支付收银台 > 基于URL跳转方式
category: harmonyos-guides
scraped_at: 2026-06-01T15:08:16+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:e010c1510018adcecf8ef7993f0047880cb13e7e3962e5fa5a5394d78bb6c890
---
1. 商户客户端根据Payment Kit接口返回的支付信息[PayResult](<../../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/paymentService (鸿蒙支付服务)/payment-paymentservice.md#payresult>)(混合支付场景）/[PickerResult](<../../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/paymentService (鸿蒙支付服务)/payment-paymentservice.md#pickerresult>)（纯外部支付场景），按照三方支付平台接入要求创建订单获取拉起三方支付收银台链接并构建**订单支付跳转信息**[orderStr](<../../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/数据模型说明/payment-model.md#orderstr>)请求[requestPayment](<../../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/paymentService (鸿蒙支付服务)/payment-paymentservice.md#requestpayment>)接口跳转或拉起三方支付收银台。

   跳转三方支付收银台示例代码如下：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { paymentService } from '@kit.PaymentKit';
   3. import { common } from '@kit.AbilityKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   9. requestPaymentPromise() {
   10. // 请使用开发者自己的订单信息（orderStr），跳转三方支付方式。
   11. const orderStr = '{"nextAction":"L","linkUrl":"","scheme":"","clientToken":"***"}';
   12. paymentService.requestPayment(this.context, orderStr, "AP")
   13. .then((payResult: paymentService.PayResult) => {
   14. // 支付成功
   15. console.info('succeeded in paying, pay result: ', payResult);
   16. })
   17. .catch((error: BusinessError) => {
   18. // 支付失败
   19. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
   20. });
   21. }

   23. build() {
   24. Column() {
   25. Button('requestPaymentPromise')
   26. .type(ButtonType.Capsule)
   27. .width('50%')
   28. .margin(20)
   29. .onClick(() => {
   30. this.requestPaymentPromise();
   31. })
   32. }
   33. .width('100%')
   34. .height('100%')
   35. }
   36. }
   ```
2. 开发者按照三方支付平台要求完成订单支付后的下一步业务处理，如对返回的支付结果信息验签等。
