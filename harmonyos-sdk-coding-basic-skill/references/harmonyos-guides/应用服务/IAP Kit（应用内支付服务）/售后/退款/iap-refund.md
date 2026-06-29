---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund
title: 退款
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 售后 > 退款
category: harmonyos-guides
scraped_at: 2026-06-11T15:08:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80e24f8396ad88c4230ec2bd36a581afb4c81904ccd30107646b8d4483acd332
---
当[用户申请退款](iap-refund.md#用户申请退款)时，对于非游戏类应用，开发者可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上审核退款订单，实现用户的退款。

说明

* 退款只能由用户发起，具体参见[用户申请退款](iap-refund.md#用户申请退款)。
* 对于游戏类应用，[用户申请退款](iap-refund.md#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

## 开发者审核退款订单

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](https://developer.huawei.com/consumer/cn/doc/app/agc-help-manageaccount-0000001099996700#section151241455193313)。

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

1. 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP”。 在应用列表中点击待处理退款订单的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/dUBuCUnVQjGOdpdOOyeBLA/zh-cn_image_0000002592219374.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=CF09CB47843FAADAF39307D4351D5739D672A4BB2BD4BD0A24A14159D9D44EFE)
2. 在“运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/PBMPgtK8R8mP_QJA67Bzow/zh-cn_image_0000002592379308.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=561324E50AF0B4F5D25E294B1F20ABC6A2051AD50E76BC36EB3E152455F566BF)
3. 审核或查询退款订单。

   **同意退款**：如果开发者同意退款，可在 “退款金额“下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/UQRL50p8SCqbUxkaOWhuDw/zh-cn_image_0000002622858817.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=B940B7F86796E1DE383D346C148D0F86A07CB4240DF002BA0324707142189EB5)

   **驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/N3rC0dExTfeEukopBsZ0Pg/zh-cn_image_0000002622698937.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=A82ADE531A8BE65655A9E2F46B81093436D413C483E87ADFDE7BF0F8634D50A8)

   **退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/mIrN20m-QVSH5LkiUc-6tQ/zh-cn_image_0000002592219376.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=D435A76E0EFAD1BFC510E74A987C471676E172E7DCF3EDDDA19CAEF415814359)

   **查询退款订单**：点击“已完成”页签，开发者可以查看所有已处理的退款订单。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/qJxasJdLQu2k87DJOI9IGQ/zh-cn_image_0000002592379310.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=1038EAD7CECC9B2C52F4B6ACAD1340B1273AE799323DF8565F8DF6D30D4A465E)

   退款订单状态如下：

   | **序号** | **退款订单状态** | **说明** |
   | --- | --- | --- |
   | 1 | 申请已拒绝 | 开发者驳回退款订单。 |
   | 2 | 申请已通过 | 开发者同意退款订单。 |
   | 3 | 退款成功 | 开发者同意退款，且华为操作退款成功。 |
   | 4 | 退款失败 | 开发者同意退款，且华为操作退款失败。 |
   | 5 | 超期未处理 | 开发者未按规定时间处理退款订单时，退款订单由华为运营进行审核。 |

## 用户申请退款

说明

* 生态应用订单退款最低系统版本要求为6.16.10（检查版本可参考以下路径“系统设置-华为账号-付款与账单-更多设置-关于”）。
* 退款申请后到退款完成非实时，一般从发起申请退款到完成需要7个工作日左右。

若用户购买应用内数字商品后需要申请退款，可选择某笔订单后根据页面指引，提交退款信息。开发者审核完成后，用户可收到退款金额。

用户可按照以下步骤申请订单退款：

1. 在“手机设置 > 华为账号 > 付款与账单 > 购买记录”中点击待退款的订单，跳转至详情页面，点击“对订单有疑问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/puJZxeEMQiG0LM5ZtxB6nA/zh-cn_image_0000002622858819.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=79A1BA2E3F09AB4FC1457AD7B375FC97816B2E0A9ECBBA18DA784716540E0F6D)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/XENP6T14Slu6rDobIU7M3w/zh-cn_image_0000002622698939.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=2F081F8921117B21F7A5CEC52BFD8BA53E9B1C087CC6F3B2628ED2AC2CD54960)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/bjavsdaVRhOTsxJMazyKCQ/zh-cn_image_0000002592219378.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=9B4A86E98B0F4A191571DE4BD70661E4EBE702D1536492DE367016F82C87A4BF)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/pfQ5Pa9tSFi5vOlAldhQSA/zh-cn_image_0000002592379312.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=BC5494EA9560AE29648DBFD4D04CD8FF4279F69FDCB94EEADD90DBC7C640CC11)

   用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/R5ShfrfPTLWVV0ktUZP9BQ/zh-cn_image_0000002622858821.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=03DB0F3F82D0D7251FA01871BB9D8D1F3518BD8320BEC1949CBA1C50D1B61ACF)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/kzehzr5MQQiSkMyd7YeZTA/zh-cn_image_0000002622698941.png?HW-CC-KV=V1&HW-CC-Date=20260611T070832Z&HW-CC-Expire=86400&HW-CC-Sign=67B3F695A22D224E4D942196B2F265C7BD778D8C52A6814BA3116CFBCBBA7ECD)

## 应用内接入退款入口

说明

* 仅支持非游戏类应用接入。
* 该退款入口仅支持应用本身所产生的订单的退款。

**拉起退款**

用户发起退款后，应用客户端向IAP Kit发送[createRefundRequest](<../../../../../harmonyos-references/IAP Kit（应用内支付服务）/ArkTS API/IAP/iap-iap.md#iapcreaterefundrequest>)请求拉起退款页面，请求中需携带待退款的订单号（purchaseOrderId）。

**代码示例**

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {

9. /**
10. * 拉起退款界面
11. */
12. createRefundRequest(context: common.UIAbilityContext) {
13. // 调用iap.createRefundRequest拉起退款，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.createRefundRequest(context, purchaseOrderId).then(() => {
16. // 退款成功
17. console.info('Succeeded in creating refund request.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 退款失败
21. console.error(`Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }

26. build() {}
27. }
```
