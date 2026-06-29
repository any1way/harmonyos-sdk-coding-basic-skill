---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-06-11T15:11:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:dce23471a54742aee87a623d6688d787498b02d9c0db5b909fa27ea18bf06a3e
---
请先参考“[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

说明

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](../../../../应用开发准备/应用开发准备/application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/u2I92YbbSE2VjIKB3cbNzQ/zh-cn_image_0000002592219510.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=285A64E8CF9EC60CDBF48594B26D94EE86261D01D12DC4499CF596C212628DB9)
2. 在项目列表中找到项目（如未创建项目可点击添加项目先完成项目创建），在项目下的应用列表中选择需要开通Payment Kit的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/0GBPChCwR-Crkl6K0wciKg/zh-cn_image_0000002592379444.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=22F491DEE76DF087A739C2604BD6C51ED029B27FAAE1BA26579B2B32CE702E18)
3. 开通服务，操作路径如下：

   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 立即开通”。
   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Pu5P8aCfSkWDNT23Sek0MA/zh-cn_image_0000002622858953.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=750F8D647D81949AF85FA508290F8429B612B253A245281621EC6C8E4B002BFE)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](../商户号绑定AppID/payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](../商户入网和获取商户号/payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/Srnf3gbgRYyN1uTTu_DZkA/zh-cn_image_0000002622699073.png?HW-CC-KV=V1&HW-CC-Date=20260611T071125Z&HW-CC-Expire=86400&HW-CC-Sign=EE114C1475DC61A6A2BBACC53D8AB4D9FE166E19220B8BF0EE28CC43016CF4CC)
