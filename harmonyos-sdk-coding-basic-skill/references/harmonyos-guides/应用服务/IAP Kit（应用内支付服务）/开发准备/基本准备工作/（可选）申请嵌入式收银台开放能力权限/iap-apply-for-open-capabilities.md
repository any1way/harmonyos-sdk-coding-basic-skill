---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-06-11T15:08:16+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:2301b3468c7dcedd05da7808a832c959e95077d2edae25889fe39c0665305821
---
如果使用接入嵌入式收银台能力，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](../../../../../应用开发准备/应用开发准备/application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请嵌入式收银台功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为应用内购买服务（HarmonyOS NEXT），然后点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/R45CXNMKQjmGNSbGPdPYdg/zh-cn_image_0000002622858799.png?HW-CC-KV=V1&HW-CC-Date=20260611T070815Z&HW-CC-Expire=86400&HW-CC-Sign=30904AA7E0B65CCFFE752F85600316713B956DD62A1EDAF297DC0ADD0B74AA5D)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/5SOS0SPQRoSx-RGNFB1IAw/zh-cn_image_0000002622698919.png?HW-CC-KV=V1&HW-CC-Date=20260611T070815Z&HW-CC-Expire=86400&HW-CC-Sign=18BDA9B3F536EBAFC606AB68BFB38F16278A0A8FEF7BCCFB1515F21E7C233ED3)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Iab_KoGXTGuz_bVRaymeVA/zh-cn_image_0000002592219358.png?HW-CC-KV=V1&HW-CC-Date=20260611T070815Z&HW-CC-Expire=86400&HW-CC-Sign=A34677CD210C1422FC425D5CBEE38A464AB54D01D2BC0ACD153D92165D9F2D91)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/TywuXioxShGIOz8FAwFqzg/zh-cn_image_0000002592379292.png?HW-CC-KV=V1&HW-CC-Date=20260611T070815Z&HW-CC-Expire=86400&HW-CC-Sign=594D49DE350A1742CBAD5C1776ABCB1AF545E6A1BFAD8BD4CFD88EDF8A7258AF)
