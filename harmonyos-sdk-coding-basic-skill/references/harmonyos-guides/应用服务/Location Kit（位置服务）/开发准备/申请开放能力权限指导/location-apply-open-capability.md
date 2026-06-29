---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:26+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:a13c181c736338d4f4f73a4a4665d3cb7a595febf69d04a2a75ad3cae4df6dc3
---
## 开放能力申请准备

请先参考[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 室内高精度定位

为了更好的用户体验，系统侧对室内高精度定位服务功能做了权限保护处理，使用相关接口开发者需先提交“室内高精度定位”能力开关的申请，请在申请通过后，再使用该能力。

室内高精度定位仅支持商场、高铁站、机场和医院等场所，支持的建筑列表如下。

[支持室内定位建筑列表](https://openlocation-portal-drcn.partner.petalmaps.com/indoormap/index.html#/homePage)

在这些建筑中支持楼层识别，定位精度约10~20米左右。

未开通室内高精度定位服务时Location Kit仍然支持在室内场景进行网络定位获取定位结果。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请室内高精度定位功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“室内高精度定位”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ERLWISm8QoulZGa7F7C8aQ/zh-cn_image_0000002592219422.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=EAABE7A0D1B0C4523638D037F1AB189DC4D2267AAE93E42E71A18F8C419BBC7F)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/vqCdQFxITFO9s-FJdrhzCA/zh-cn_image_0000002592379356.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=E4D4DE13B39F5D9A3D9B0EB8DA8E4DC6E06ADE67A901C5BC550950F246D5B719)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/hq5BnvbFQluYr9fP2KoDuQ/zh-cn_image_0000002622858865.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=4EA389FF46FC9D125F4BD7F2D80F9CEFA8F4C0A9069613195C8849EEA5C8C6B6)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/gbbBghg4TlOWRmuxDqTaLw/zh-cn_image_0000002622698985.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=9826CCFB6A08A20309FC9C4E3C099359817DBFF4E90E563F6147EB6634A4BE19)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/WRsG65ycTYSZ_9Cx2dDg0g/zh-cn_image_0000002592219422.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=7A69A57038C0C9EEF4564A52A3B15E17B0CD9F401E68E99AFE8FDC5DBA1D7C92)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/c4WYVM5CQQ2F5HQYfv4MgQ/zh-cn_image_0000002592219424.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=2C0367A7FC16993D17C5951EB8B98D7D6F4BAD4EC4B17C356C86723E69D4DD6B)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/C3kf9aznTZOjqY0gVodtWg/zh-cn_image_0000002592379358.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=15A02954CB0A1EB6E47D902ACBF726773F05AA6690D4498418BCC401B8A1DFD5)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/MjLwjt-rRUW-Vtm-wZOGnw/zh-cn_image_0000002622858867.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=72558BDFB6A1F26642B78AF06A555ECB540A40D25FED72C9A4F761D88EC477FD)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/HK76eeEwTZ-ZHKHsm-SUeA/zh-cn_image_0000002592219422.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=6AE279ABB42C4DB2EE73CB883D040C925EAA303C72369B4183C2DF1483CCD5F6)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/NpASD0KOSDafXKcdqWFzAQ/zh-cn_image_0000002622698987.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=75B9AF2FB95CC0B8646471ECFC269832755791D588D630CDC6F5D074AB6B0F88)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ssj2rZ35RP2uWe1VZBv6Jg/zh-cn_image_0000002592219426.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=D62E34661AC486FA8EDD546AB6D1B9CF3D72B5638AF7914F3240940EAE5FC549)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启Beacon围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/N698uilAR-C2NeikKEz9gg/zh-cn_image_0000002592379360.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=1A06CCE5A05303C5D9D8D31F18994DDB00CD61D8BF5417890B75D94FADD7F61B)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Vlr4wj3WQq2HsfP7BICXgg/zh-cn_image_0000002592219422.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=517F41A6604EAC87774637929141F9736FF5AFDA68E9E8427A91EABC4470B41C)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/GO3JqQArQdyNCxHHdXt9JA/zh-cn_image_0000002622858869.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=1319D27A2313A81ED219202F54F496FA8339B61F67E299E5F30BDDB655592026)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/reTVDMOOQE6GtIPYfEvzbg/zh-cn_image_0000002622698989.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=907F17640C7FEDC3B6AC4A1CFB4ABE7FA85A968ED26EB0CE285BC63ECBF5FEE0)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/CnDS25IESpOv55WSX1I2DA/zh-cn_image_0000002592219428.png?HW-CC-KV=V1&HW-CC-Date=20260611T070925Z&HW-CC-Expire=86400&HW-CC-Sign=8217DFD657A3E344DFDBF78A3526D275C211F51520538C7275B9266C6C33596D)
