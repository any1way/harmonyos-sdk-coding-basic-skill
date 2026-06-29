---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-select-invoice-title
title: 获取发票抬头
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取发票抬头
category: harmonyos-guides
scraped_at: 2026-06-11T15:02:49+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a93a942ea5ebb19960e3cdb19697378ea7d07b1ae5ce2701a25af7a45117e6a1
---
## 场景介绍

当应用需要获取用户发票抬头时，可使用Account Kit提供的发票助手能力，打开发票抬头选择页面，帮助用户快速选择或管理发票抬头。以下对Account Kit提供的发票助手能力进行介绍，获取发票抬头功能还可使用场景化控件[选择发票抬头Button](<../../../Scenario Fusion Kit（融合场景服务）/场景化Button/选择发票抬头Button/scenario-fusion-button-invoice-title.md>)进行实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/RV0a1IVCRDaLV86EWOOF_w/zh-cn_image_0000002592379122.png?HW-CC-KV=V1&HW-CC-Date=20260611T070248Z&HW-CC-Expire=86400&HW-CC-Sign=BDEB695084C58D32EA8DD0B6D551AE12951BBCA712A23789800434AC6DA11E5C "点击放大")

## 约束与限制

Wearable、TV设备暂不支持使用获取发票抬头功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/tEhou_L1TzCiGB22BGa-JA/zh-cn_image_0000002622858629.png?HW-CC-KV=V1&HW-CC-Date=20260611T070248Z&HW-CC-Expire=86400&HW-CC-Sign=B060D6CD0639E9A62CCE392091570E51F551E5B37A960119D5DC4409C157ACE2)

流程说明：

1. 用户需要使用发票抬头时，应用程序调用选择发票抬头API，打开华为账号发票抬头选择页。
2. 用户可以在发票抬头选择页选择已有发票抬头或者跳转到发票抬头管理页进行增加，点击确认后可将选择的发票抬头返回给应用。

## 接口说明

获取发票抬头关键接口如下表所示，具体API说明详见[API参考](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/invoiceAssistant (华为账号发票助手服务)/account-api-invoiceassistant.md>)。

| 接口名 | 描述 |
| --- | --- |
| [selectInvoiceTitle](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/invoiceAssistant (华为账号发票助手服务)/account-api-invoiceassistant.md#selectinvoicetitle>)(context: [common.Context](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.common (Ability公共模块)/js-apis-app-ability-common.md#context>)): Promise<[InvoiceTitle](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/invoiceAssistant (华为账号发票助手服务)/account-api-invoiceassistant.md#invoicetitle>)> | 调用该方法打开发票抬头选择页面，使用Promise异步回调返回选择的发票抬头。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](../../开发准备/配置签名和指纹/account-sign-fingerprints.md)、[配置Client ID](<../../开发准备/配置Client ID/account-client-id.md>)。此场景无需申请账号权限。

## 开发步骤

1. 导入[invoiceAssistant](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/invoiceAssistant (华为账号发票助手服务)/account-api-invoiceassistant.md>)模块及相关公共模块。

   ```
   1. import { invoiceAssistant } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[selectInvoiceTitle](<../../../../../harmonyos-references/Account Kit（华为账号服务）/ArkTS API/invoiceAssistant (华为账号发票助手服务)/account-api-invoiceassistant.md#selectinvoicetitle>)方法选择发票抬头页面。

   ```
   1. // 执行请求
   2. if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
   3. try {
   4. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   5. invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
   6. .then((data: invoiceAssistant.InvoiceTitle) => {
   7. hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
   8. const type: string = data.type;
   9. const title: string = data.title;
   10. const taxNumber: string = data.taxNumber;
   11. const companyAddress: string = data.companyAddress;
   12. const telephone: string = data.telephone;
   13. const bankName: string = data.bankName;
   14. const bankAccount: string = data.bankAccount;

   16. // 开发者处理type, title, taxNumber, companyAddress, telephone, bankName, bankAccount
   17. // ...

   19. })
   20. .catch((error: BusinessError<Object>) => {
   21. dealAllError(error);
   22. });
   23. } catch (error) {
   24. dealAllError(error);
   25. }
   26. } else {
   27. hilog.info(0x0000, 'testTag',
   28. 'The current device does not support the invoking of the selectInvoiceTitle interface.');
   29. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError<Object>): void {
   3. hilog.error(0x0000, 'testTag', `Failed to selectInvoiceTitle. Code: ${error.code}, message: ${error.message}`);
   4. }
   ```
