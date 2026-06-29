---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-binding-appid-to-merc
title: 商户号绑定AppID
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 商户号绑定AppID
category: harmonyos-guides
scraped_at: 2026-06-11T15:11:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ba503168db740deeb780f85f50cf6af1eb25f3bc58066a62911853c95bd84c6c
---
说明

商户号绑定AppID的商户需要通过[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)入网，详见[商户入网和获取商户号](../商户入网和获取商户号/payment-merc-regist-apply.md)。通过[华为开发者联盟官网](https://developer.huawei.com/consumer/cn/)开通[商户服务](https://developer.huawei.com/consumer/cn/doc/app/open-0000001959074873)入网的商户暂不支持直接接入华为支付以及绑定AppID操作。

商户（以下所称商户均包含所有商户模型）后续支付交易依赖于[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[创建应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)生成的AppID与商户号的关联关系。商户在请求预下单接口传递AppID入参，后续可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上基于应用维度查看交易报表数据。传递AppID参数后，华为支付侧会校验商户号与传递的AppID是否匹配，如不匹配则会直接响应异常。因此，接入鸿蒙支付服务前商户需要为商户号绑定AppID，如无商户号则需要先申请，详细介绍参考[商户入网和获取商户号](../商户入网和获取商户号/payment-merc-regist-apply.md)。

AppID绑定详细可参见[AppID管理及关联](https://developer.huawei.com/consumer/cn/doc/pay-docs/hwzf-appidguanli-0000001757041165)。

## 基本概念

**同主体**：商户号与AppID所关联的营业主体信息一致。

**异主体**：商户号与AppID关联的营业主体信息不一致。

## 绑定AppID说明

1. 暂不支持平台子商户及特约商户发起绑定AppID申请。
2. 商户发起绑定AppID申请，异主体绑定需要商户与华为支付侧沟通申请开通异主体绑定权限（可参考[产品开通操作](../（可选）特定场景配置操作/payment-product-configuration.md#场景一产品开通操作)）后才可在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)发起异主体AppID绑定操作。
3. AppID关联的营业主体与特约商户商户号或与服务商商户号关联的营业主体一致，都认为是同主体，可直接发起绑定。
4. 商户发起绑定申请后，商户应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站才能对商户号绑定AppID进行授权（提示“主体不一致”可[参见这里](<../../Payment Kit常见问题/商户号绑定AppID提示“主体不一致”？/payment-faq-26.md>)）。

## 直连商户/平台类商户绑定

1. 请登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理 > 新增关联AppID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/gD6Gj9pCRUqi0yI1ziYx3A/zh-cn_image_0000002592219512.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=B9F11825A69DC0B01410235FF551A0B2589C437BB7D9DDD5636D34FD3C1A324E)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/WWlvPp5QRgakL-Fcu1WSOw/zh-cn_image_0000002592379446.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=28115153BAC9D81F766A69A64F9E2E2AB59B279A4ECA0A3C546119843510EB8B)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/VAVAmCJMSV2Sj4LafG6NDQ/zh-cn_image_0000002622858955.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=D232285235FBCD01E3FA1A2924EC3C488EF0D4425A32B229CBCCD7049149E8FD)

## 服务商绑定

服务商绑定AppID涉及如下场景：

1. **服务商绑定**

   服务商需要绑定服务商应用AppID可直接在华为支付商户平台发起绑定申请。
2. **特约商户绑定**

   特约商户需要绑定特约商户应用AppID，需要服务商在华为支付商户平台发起邀请特约商户绑定AppID才可以进行绑定。

### 服务商绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“服务商绑定的AppID”页签内点击“新增关联AppID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/RMIk5bBVSTCBhxGaPsiAMg/zh-cn_image_0000002622699075.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=8ED67D0ACEB7EF882396FD9B5E5DD8592B1AEFD495F7A8071A532022ED3C12BA)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/4Yjd30njR7-AjsS9TaGQvg/zh-cn_image_0000002592379446.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=5299D717C6E1D8DE65E300F6EBD8D40B1165FC580FB0AA4314C7D01D463A5D39)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/RmqkbaGuRCa03iSHK-adqA/zh-cn_image_0000002622858955.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=F336D8ABDB237710AE3D39F2FF940FC7596E662CC073FE33FE2BB04C0AC3B585)

### 服务商邀请特约商户绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“特约商户绑定的AppID”页签内根据服务商下的特约商户列表，选择特约商户发起AppID绑定申请邀请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/wvvkxR-3THOX81Iu5MLFwQ/zh-cn_image_0000002592219514.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=CE1757A77AB3A71ACD46031035BB9778F0A7AB9604DEAA4DD1CBECE55759AB4C)
2. 特约商户登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”选择“服务商为我绑定的AppID列表”中的数据，点击去确认，对服务商邀请绑定AppID进行确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/441mej9PT5Ccxca-tP4sbw/zh-cn_image_0000002592379448.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=E0C85AB8209ED33E3ACA292699811B416C23B62EDDF288BCC1EC0915663FFD83)
3. 特约商户确认绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/4MWBxoi7TRaaDbymC9fhQA/zh-cn_image_0000002592379446.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=8F4AF9A116BEA878D798720046FA6E53AF1569B45DC4C30050BF1915381B4C1A)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/idPqax8pT4aFAqlaAs3TFA/zh-cn_image_0000002622858955.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=2F7DE71F696F0B5441ADC46D5B6E87A636197C304F157AA2541E1E391AB85FAD)
