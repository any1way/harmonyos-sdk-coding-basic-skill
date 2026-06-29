---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-ui-standby-form-development
title: ArkTS待机屏保卡片开发指导
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS待机屏保卡片开发指导
category: harmonyos-guides
scraped_at: 2026-06-11T14:37:58+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e24f96fa848a00e513456a59324ab3a4fa04a5de01cfbed44607053af9b0191a
---
从API version 23开始，Form Kit提供在设备待机屏保界面（即横屏充电锁屏状态下显示的界面）上显示卡片的能力，用以展示重要信息，旨在待机下也可陪伴用户。待机屏保卡片用于展示天气、日历等信息，并支持用户个性化定制。

本文介绍了待机屏保卡片的使用步骤、约束限制，并给出开发指导。

说明

在待机屏保界面下默认为深色模式不会跟随系统。

## 亮点/特征

* 丰富待机显示，提供个性美观的待机显示页面，打造全场景、个性化的“百变”心灵陪伴。
* 提供情感陪伴和情绪价值，在工作的时候，日程待办，提升工作效率；在学习的时候，作为时钟摆台，陪伴学习。

## 约束和限制

1. 待机屏保卡片只支持 2\*2尺寸的卡片。
2. 待机屏保卡片不推荐展示用户个人隐私敏感数据。
3. 待机屏保卡片有明确的UX设计规范。具体请参考设计指南中的[待机屏保](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-service-widget-0000002087671904#section966618274556)。

## 开启方式

待机屏保功能在系统上默认是开启的，功能开关路径“设置>桌面和个性化>待机屏保设置”，开关界面如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/3LiL8sLUQ96He-S_Beyc2Q/zh-cn_image_0000002592378654.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=4677040C38C47F44E0381CCF1C9BC17AE57D96CD27DEBC27D3BF912F246A0EBB "点击放大")

## 使用步骤

待机屏保支持卡片展示与卡片编辑功能（添加、移除），具体操作步骤如下：

1. 进入待机屏保界面：插入充电器或开启“不充电可显示” 开关，设备横屏锁屏并与桌面夹角45°~90°稳定摆放（折叠机需切换为外屏；同时折叠机支持帐篷模式显示），即可进入待机屏保界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/7jYpeDMwSciAgh52prTvDQ/zh-cn_image_0000002622858161.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=36A35DACB04663CEFECA7990BFC808D3A8F860CA34D158212D451C26A727E2F0 "点击放大")
2. 进入待机屏保编辑界面：在待机屏保界面长按或双指捏合即可进入编辑界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/thkBqmu8T666LfDG_Me4-A/zh-cn_image_0000002622698283.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=DCF1244693931099A773DF65DCFB0C9F3BC72022319F92EE90AB5F9BDD391ACD "点击放大")
3. 进入待机屏保卡片中心界面：在待机屏保编辑界面，上滑左侧或右侧列表至最后，点击“+”弹出卡片管理页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/oMft0OoHQ9qd43oc6ZuAag/zh-cn_image_0000002592218722.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=B600AA35C61E18D1D5C2D24C8C9FF213C9DA79CB5D89E1BBF1862AE2D002F9B1 "点击放大")
4. 进入待机屏保卡片管理页面：在待机屏保卡片中心点击“建议”会显示推荐的卡片，或者点击应用列表中的应用，弹出对应的卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/zMEXOp-TTFuVT1Jfpan5tg/zh-cn_image_0000002592378656.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=A18505E370D6AAA3CA440406D88FCED3AD12FA471D44E5FED9A800D43E36466F "点击放大")
5. 添加卡片：在待机屏保卡片管理页面，选择好卡片后，点击“添加”按钮即可添加到待机屏保界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/XZDqpAfZS162Gyyf2jkQiQ/zh-cn_image_0000002622858163.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=D29A4881FB36B64ED1A966F75AA9F313111C497975AD5BD70D6B1175FEEDBFD3 "点击放大")
6. 移除卡片：进入待机屏保编辑界面，点击卡片右上角的“-”即可移除卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/LXScMn6tSZizBUt7wgmjLg/zh-cn_image_0000002622698285.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=D4AF6294D7D302E01A4594D1EAB9EE7F6185DEE8863CEB0C82B710157384B83F "点击放大")

## 开发准备

### 待机屏保开放能力申请

待机屏保卡片会展示在设备的待机屏保界面，开发者需申请上架开放能力，用以保护数据隐私安全。

因此在应用调试或发布时，必须使用[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)，并在手动签名[申请Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)过程中[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)，创建应用时参考如下指导为应用接入开放能力。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/x_membj-SVq3xTd55vxehQ/zh-cn_image_0000002592378650.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=47E6071879D478ACED35B594B9F3994E53186EFFD5F3859B9E7EBAB35816678A "点击放大")
2. 在项目列表中找到您的项目，并点击选择需开启开放能力的应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/nIm4MrcRSzuhKibvwmup3g/zh-cn_image_0000002622858157.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=02F1514998620DE5D356366A64AEC2F57691F5E677B0BFC16E45E4ED9DEF412F "点击放大")
3. 在“开放能力管理”页面，点击待机屏保卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/9fpXWvy2R16BozUrJaqg_w/zh-cn_image_0000002592218724.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=886CA68FD6DB54C014BE6F37278ECFF322E537B749C3B78CC612CA0DCB42F31F "点击放大")
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。

   申请原因：必填，包括应用介绍、使用场景、申请用途，不超过512个字符。

   上传附件：选填，提供对应卡片UI设计释义材料，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Uilb7jNfQLWx10ci2gej2Q/zh-cn_image_0000002592378658.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=1EC85B3A6BFACDA15E620FFE50B31C81C0321A3D62D3C40D9BF1B2B29F078B4B "点击放大")
5. 返回“开放能力管理”页面，原“申请”按钮变为置灰显示的“申请”，待机屏保卡片的能力开关已勾选。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/7THLfOxLSkadEi_UwHBvKQ/zh-cn_image_0000002622858165.png?HW-CC-KV=V1&HW-CC-Date=20260611T063757Z&HW-CC-Expire=86400&HW-CC-Sign=D2D5B751BE63EC9B2696BFCBC4DE31B95F57751AFCE4345FA9563784E184EB6A "点击放大")

   至此，您的应用已成功开通待机屏保开放能力。

## 开发步骤

下面给出示例，实现待机屏保卡片展示。

1. [创建卡片](../../创建ArkTS卡片/arkts-ui-widget-creation.md)。
2. 配置卡片在待机屏保界面展示。

   如果卡片不需要展示在待机屏保界面，配置isSupported字段为false;如果卡片已适配待机屏保卡片UX规范，配置isAdapted字段为true，系统会把卡片布局组件中backgroundImage移除；如果卡片涉及隐私敏感信息，需要配置isPrivacySensitive字段为true，用户将卡片添加到待机屏保界面则会有蒙版覆盖。具体参考[配置文件字段说明](../../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md#配置文件字段说明)。

```
1. // entry/src/main/resources/base/profile/form_config.json
2. {
3. "forms": [
4. {
5. "name": "widget",
6. "displayName": "$string:widget_display_name",
7. "description": "$string:widget_desc",
8. "src": "./ets/widget/pages/WidgetCard.ets",
9. "uiSyntax": "arkts",
10. "isDynamic": true,
11. "isDefault": true,
12. "updateEnabled": false,
13. "scheduledUpdateTime": "10:30",
14. "renderingMode": "autoColor",
15. "updateDuration": 1,
16. "defaultDimension": "1*2",
17. "supportDimensions": [
18. "1*2",
19. "2*2"
20. ],
21. "standby": {
22. "isSupported": true,
23. "isAdapted": true,
24. "isPrivacySensitive": false
25. }
26. }
27. ]
28. }
```
