---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5337a366523da75647c082ecea469638f981e4aa35ceeb24041cf0fcb58ddc0
---
请优先[开通地图服务](map-config-agc.md#开通地图服务)后，再参考“[应用开发准备](../../../应用开发准备/应用开发准备/application-dev-overview.md)”完成基本准备工作，然后再继续进行以下开发活动。

说明

* 从HarmonyOS 5.0.2(14)版本开始，开发者无需配置公钥指纹和Client ID。
* 从DevEco Studio 6.0.0 Beta5版本开始，支持在DevEco Studio中开通地图服务。

## 开通地图服务

Map Kit提供2种方式开通地图服务：

* 通过DevEco Studio开通地图服务。
* 通过AppGallery Connect网站开通地图服务。

方式一：通过DevEco Studio开通地图服务

1. 登录DevEco Studio应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/TZfrwDViTKGJnr-BTMWe3w/zh-cn_image_0000002592219432.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=2D4692510A87C0B5DFF50B155FA46EDF10A3C9335B9D51651ECDB7C82A007B87)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/QDdbC_q_RFOiqDXewyeIVg/zh-cn_image_0000002592379366.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=330D092AF4611E994809C3F6D70048EBED6D180C922870A779FA47992769A6B4)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/6_MMTX3CR-yr88d19ZnroA/zh-cn_image_0000002622858875.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=F0108D88C7A08B8797BCED5A3ED746D95D33C691BB17A129196DF67769DBAC3F)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_4OIQ14jRxSXzanPLaZV1Q/zh-cn_image_0000002622698995.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=A605EF005918A67D824C3F0B83CC83E03B6F165BDFE3A6F571E692AF840BD3C6)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/QLlFj05DSK2s1CxshdGVkA/zh-cn_image_0000002592219434.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=C3B97A77CC574DC602839CB4577890A4CB61476B91852563A0AF213454D5055C)

方式二：通过AppGallery Connect网站开通地图服务。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7BO_Xf9HT_yi1t3lbrdXBw/zh-cn_image_0000002592379368.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=EFD2E06690DF01205A2C9B3171C9382050359D116F7CE4CA046626E086D1E706)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要打开“地图服务”的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/03St6HxQSA2EEwmrdTlwGA/zh-cn_image_0000002622858877.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=4009108ED0FD305F355F08807365F354199DE612C01524F35A1E29584241518F)
3. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/HlyQ1B4MS3iF9I6hX42Sog/zh-cn_image_0000002622698997.png?HW-CC-KV=V1&HW-CC-Date=20260611T070938Z&HW-CC-Expire=86400&HW-CC-Sign=913B0BE43A95DEE5EFA2FF93454BC61C0FF78CFFC5A33E54024A2A12C64CC1AD)
4. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugcert-0000001914263178)、[注册设备](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-device-0000002283189937)、开启"地图服务"后重新[申请调试Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)，并完成[手动签名](../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)。
   * 发布阶段必须[申请发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-cert-0000002283336729)、开启“地图服务”后重新[申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)文件，并[配置签名信息](../../../发布应用/发布应用/ide-publish-app.md#section280162182818)。

     说明

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
