---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-invoicing
title: 开票
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 开票
category: harmonyos-guides
scraped_at: 2026-06-11T15:08:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc052aee5fe53fbb4d205cea1324aa26ad5a5bbe7424a9a69a6c63c89163de73
---
## 用户申请开发票

从6.1.0（23）开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

用户可按照以下步骤：

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/eYQ68nTFRliC26TU2Jk98Q/zh-cn_image_0000002592219380.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=E2A3DB7D2925FF27F4613422D4D917316F6417D6FD4479A8DB7FE3602E9DCB89)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/5gLFZn1zSUiLKK-5z6dWQA/zh-cn_image_0000002592379314.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=BB3597B12E109F4E0305F4D0B40A04078665AB1C6563A1813B936F844BC4D6D6)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/DcwjSJHRSEqlKxHO2EUUPw/zh-cn_image_0000002622858823.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=7D5DE79AD58DD140A31A6FBFC443FB2A1146B06D274212CB203F1F84E76D42F5)

   用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Zi1dL2MnTTKuiA_JBtIKUA/zh-cn_image_0000002622698943.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=F9EF07F8B2E9B019DF96632A115F1765E68E5A5997C013B7FA74E23B4073D8DF)

## 应用内接入开发票入口

**拉起开发票页面**

用户发起申请开发票后，应用客户端向IAP Kit发送[showManagedInvoices](<../../../../../harmonyos-references/IAP Kit（应用内支付服务）/ArkTS API/IAP/iap-iap.md#iapshowmanagedinvoices>)请求拉起开发票页面，请求中需携带待开发票的订单号（purchaseOrderId）。

**代码示例**

```
1. import { iap } from '@kit.IAPKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct IapTest {
8. /**
9. * 拉起开发票界面
10. */
11. showManagedInvoices() {
12. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. // 调用iap.showManagedInvoices拉起开发票页面，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.showManagedInvoices(context, purchaseOrderId).then(() => {
16. // 请求成功
17. console.info('Succeeded in showing invoice page.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 请求失败
21. console.error(`Failed to show invoice page. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }
25. build() {
26. }
27. }
```
