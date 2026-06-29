---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendar-service
title: 注册并管理一键服务日程
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 注册并管理一键服务日程
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:13+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:0cc6111a1d2665e334113f5f9188f49d3c75ab3b28f2fc9191af155b738f14bc
---
## 场景介绍

Calendar Kit提供日程一键服务功能，比如一键入会、一键追剧、一键购物、一键查看等。注册日程一键服务后，用户可通过点击对应按钮拉起跳转链接，一步直达服务落地页，方便快捷。

## 服务器注册（配置一键服务跳转链接）

若需使用“日程一键服务”功能，需要按照以下步骤完成注册。

1. 进入[开发者管理中心](https://developer.huawei.com/consumer/cn/console/overview)，登录[企业账号](<../../AppGallery Kit（应用市场服务）/应用归因服务/开发准备/注册企业账号/store-attribution-config-agc.md>)（暂不支持个人开发者）。企业主账号无需手动添加权限；若使用团队成员账号，请确保使用企业主账号为其添加“小艺开放平台”的管理员权限，具体添加可见下图。

   选择团队账号，点击编辑，为对应的账号添加权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/v8S57fGHQxCrrwl9vApwlA/zh-cn_image_0000002622858691.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=848B5A953F5CA8A421D7232665FF1D73F76479AF5F5D03C7299107EEFD8AAE7A)

   确认对应的信息后，点击下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/C85VeLNwRCmdqj3CsFZrYw/zh-cn_image_0000002622698811.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=EA6D5AB775FE3606427574932F1F97093A9A352B437C4AB2FCFC7150BBC84DB3)

   勾选小艺开放平台管理员，选择下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/LZgW7s_WRbGGr1SXccUtYA/zh-cn_image_0000002592219250.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=185F67B63ADA265BF1A990F6A1FB3ECF10F226E9270A44B86833BFC1732444D4)
2. 登录成功后，在侧边栏菜单中**生态服务**下选择**智慧服务**，点击进入**小艺开放平台**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/UbXoOfhsSWy8vEnt_NIL8g/zh-cn_image_0000002592379184.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=17EB4867F8FE3E097BAB1C6A0F6D464C349F7E3549C8ACD7AE5C8191F4CF3E6B)
3. 进入页面后，选择右侧**资源管理**，点击选择**其他服务**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/rPV7iLofT7mZ1goU6xFJ4A/zh-cn_image_0000002622858693.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=839CD6A9F910C07B649766F100C9A63D3F480B86E024646B90D081CBD35736C5)
4. 进入页面后，点击右侧**创建服务**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/t5VYVE9WTOijJpXhC8ShvA/zh-cn_image_0000002622698813.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=3A9A862F14569639F31BACD0A381AD7BA1B3A2F73FCAF8CAAF17848BD5E3FD4E)
5. 选择服务模型。

   选择**自定义模型**，填写**服务名称**、**服务分类**、**默认语言**，点击**创建**按钮。

   **服务名称**：可由用户自定义，推荐使用“应用名+日历一键服务”的组合命名形式。

   **服务分类**：开发者根据实际业务类型自行选择。

   **默认语言**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/WxVK6eoeQVeLMdZwxCwcfw/zh-cn_image_0000002592219252.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=E5293349BAE10DF83701078F9AEB70DA5E1F7778BC604826ABB168EAFD60596D)
6. 创建完成后，填写服务的**基本信息**，点击**保存**按钮。

   **服务分类**：选择实用工具/日历。

   **服务版本号**和**版本描述**可由开发者自定义，平台审核不关注此信息。

   **服务分级**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Tq70ujL1SkS2eIemyQSZNw/zh-cn_image_0000002592379186.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=9B555C6647F7FA56CF3E55ADBD60EF42161A33BC5351CC7E33BC62044214DDAA)
7. 填写**服务呈现信息**，点击**保存**按钮。

   此页面必填字段均由开发者根据业务选择配置。建议在服务预览处上传用户界面示意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/OApOQ1wBSIeYh4ShzZJvlw/zh-cn_image_0000002622858695.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=E58745C389E6CDF2DB6A5343FEC704AEEF605818DEECDA481E282171292A1C36)
8. 进入**配置**，选择**新增用户意图**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/rf_BEZe2TDSVcSIyfCJXyQ/zh-cn_image_0000002622698815.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=68A3CA3941C3C1FECB1743C015ACFA7262CBFED0D76F46D5C54B2435FA586FE3)
9. 配置意图。

   1. 设置**意图标识**、**意图名称**和**意图分类**，勾选一键服务。意图分类选择“查日历”。
   2. 勾选一键服务之后，选择**服务类型**（请与Calendar Kit提供的日程服务类型[ServiceType](<../../../../harmonyos-references/Calendar Kit（日历服务）/ArkTS API/@ohos.calendarManager (日程管理能力)/js-apis-calendarmanager.md#servicetype>)一致），点击**添加关联**按钮，输入**app包名**及**app名称**（请确保app包名及app名称准确匹配，否则一键服务无法生效）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/zO47cGLYTWqdFxgAsxFPXA/zh-cn_image_0000002592219254.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=78AD509AD670170A53070E3813C6C9928205DB996C7103EA5EABB179F2B1E1FB)
10. 配置意图的**实现类型**，选择**APK/RPK/FA/H5 link**，选择**新增实现**，点击**配置**按钮。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/mg5qesm9TAOyLWPVXdQPag/zh-cn_image_0000002592379188.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=943B80AB210729AFDC628D280BB07FB4E3021D9ABBC822F1ECEC73202FD2E39A)
11. 进入新增实现页面，填写**基本信息**和**配置方式**后，选择**保存**。

    1. 填写基本信息。实现名称由开发者根据业务自定义，推荐使用“应用名+一键服务类型”命名。
    2. 选择配置方式，勾选**HAP LINK**。

       填写准确的**App名称**（若下拉菜单中无匹配项，可直接输入）和**App包名**。

       填写**跳转链接**，即用户在系统日历中点击一键服务按钮拉起的落地页；请勿打开**跳转参数**开关。

       说明

       跳转链接为链接模板，实际[EventService](<../../../../harmonyos-references/Calendar Kit（日历服务）/ArkTS API/@ohos.calendarManager (日程管理能力)/js-apis-calendarmanager.md#eventservice>)填入的uri需遵循此模板。例如，若填写跳转链接为“demo://mobile/player?params=”，则对应可匹配的uri为“demo://mobile/player?params=AAAABBBBCCCCDDDD”，其中“=”及“=”之前的部分为强校验，“=”之后的部分可由业务方根据需要自定义。

       其他必填字段，由开发者根据业务自行配置。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/zW8LRU9NRFaxFWiE6a8PIQ/zh-cn_image_0000002622858697.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=27DFDA21B28DF7606B5B52C0BFED4058BBC1244A84C013ABF8FCCAAF0D504920)

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Wjs_t6Z0T6C5FQynU36Vrw/zh-cn_image_0000002622698817.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=EFCAB4E5B7318DD0ECE33633930CD1D4D2437DC4D4ED6F6B80710AA9712D5400)
12. 完成以上所有配置后，切换到**发布**模块，点击**上架**按钮，等待后台审核后，完成意图发布。

说明

若已完成上架的服务，支持根据上文步骤再次调整修改，修改完成后，点击**升级**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Fk1Jz0VYQG26yO3CKhiI_g/zh-cn_image_0000002592219256.png?HW-CC-KV=V1&HW-CC-Date=20260611T070512Z&HW-CC-Expire=86400&HW-CC-Sign=57D2E2BD362A849DF1A4B15AC27958D5D27F70C78942E822450B50BCE5D47871)

## 客户端添加一键服务日程

一键服务注册成功后，即完成系统日历跳转链接配置（支持在系统日历界面显示对应功能按钮）；若想实现一键服务体验，还需在客户端进行相关配置。

配置步骤如下：

1. 在module.json5文件中，配置相关字段。

   需配置"exported"字段为true。

   并配置["skills"](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#skills标签)中的"actions"字段，"actions"标识能够接收的Action值集合，取值通常为系统预定义的action值，也允许自定义。actions不能为空，actions为空会造成目标方匹配失败，常见的action取值可见[action常数说明](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/已停止维护的接口/@ohos.ability.wantConstant (wantConstant)/js-apis-ability-wantconstant.md#action>)。

   最后配置"uris"字段，"uris"需与注册时的链接模板相匹配。

   比如，服务器端注册时填写的uri模板链接若为"demo://mobile/player?params="，则“=”前的内容为强校验，“=”后的内容为**业务需要使用的参数列表**，可在使用日历服务写入日程时根据各业务实际情况进行指定。参数列表中不得直接包含字符“=”或“&”，请注意使用decodeURI()/encodeURI()进行转换。

   ```
   1. {
   2. "module": {
   3. "name": "xxx",
   4. "type": "xxx",
   5. // ...
   6. "abilities": [
   7. {
   8. "name": "xxxxxxx",
   9. // ...
   10. "exported": true,
   11. "skills": [
   12. {
   13. // ...
   14. "actions": [
   15. "ohos.want.action.viewData"
   16. ],
   17. "uris": [
   18. {
   19. "scheme":"demo",
   20. "host":"mobile",
   21. "pathStartWith": "player"
   22. }
   23. ],
   24. }
   25. ]
   26. }
   27. ],
   28. }
   29. }
   ```
2. 在被拉起的落地页EntryAbility中的onCreate、onNewWant接口中的[want对象](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)内存在对应的拉起信息，开发者可通过对应参数实现对应跳转逻辑，本文不再赘述。
3. 调用[addEvent](<../../../../harmonyos-references/Calendar Kit（日历服务）/ArkTS API/@ohos.calendarManager (日程管理能力)/js-apis-calendarmanager.md#addevent>)接口添加日程数据，后续即可见日历内出现含一键服务按钮的日程，点击即可跳转至对应落地页。

## 约束限制

* 普通日程（EventType.NORMAL）可以提供一键服务按钮的露出；重要日程（EventType.IMPORTANT）因数据结构和产品规格限制，即使配置正确也无法提供一键服务。
* 该服务仅在用户设备联网下载对应协议后，开发者写入的日程才会显示对应按钮。
* 一键服务按钮的展示规则为：日程详情内始终展示，月视图、桌面卡片在日程开始前15分钟展示。
* 在服务器端注册的服务协议完成上架，审核通过后，设备恢复出厂设置，或待当天零点后，功能可正式生效。
* 请确保服务器端填写的链接模版（[服务器注册（配置一键服务跳转链接）](calendar-service.md#服务器注册配置一键服务跳转链接)）、设备端三方应用侧写入的Event.Service.uri、module.json5配置的"uris"字段信息（[客户端添加一键服务日程](calendar-service.md#客户端添加一键服务日程)）相互匹配。
