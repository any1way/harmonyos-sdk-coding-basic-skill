---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-11T15:07:14+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c12ffd3b63225b2781479c21c751f62ae7a29accffe51f3a7e0386f9ba2e3d3f
---
## 创建小游戏

在华为应用市场发布小游戏，要求前往AppGallery Connect创建小游戏类元服务，具体操作请参见[创建小游戏](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-minigame-0000002434138360)。其中：

* “应用类型”：选择“元服务”。
* “应用分类”：选择“小游戏”。

说明

用于正式上架的游戏包名建议不要包含test、dev等信息。

## 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](https://developer.huawei.com/consumer/cn/doc/games-guides/game-center-identification-applyfor-0000002392353221)。

## 申请备案

请参考[APP核准（APP备案）指引](https://developer.huawei.com/consumer/cn/doc/App/50130)、[快游戏核准（备案）指南](https://developer.huawei.com/consumer/cn/doc/quickApp-Guides/quickgame-filing-guide-0000001806139508)和[国产游戏小程序核准（备案）准备](https://developer.huawei.com/consumer/cn/doc/games-guides/quickgame-filing-chinese-preparation-0000001979934858)完成小游戏备案，并保存好备案信息。

## 申请JSVM权限和存储空间管理开放能力

小游戏上架必须申请JSVM权限和存储空间管理开放能力，具体操作请参见[申请ACL权限和开放能力](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-minigame-acl-and-ability-0000002425276004)。

## 生成签名证书

数字证书和Profile文件等签名信息可以确保小游戏的完整性：

* 调试阶段：[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)、[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)、[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。
* 发布阶段：[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)、[申请发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-cert-0000002283336729)、[申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)。

## 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-cert-fingerprint-0000002278002933)。

说明

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

## 配置APP ID、Client ID和权限信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/dbbfryaPSnu7BzIosDaQMw/zh-cn_image_0000002592219330.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=B0DF41598B37930DFFCE1B76CA1F915FF8126052AEA15381D76DB60F44561863)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置ACL权限和开放能力。如下所示：

   ```
   1. "module": {
   2. "name": "entry",
   3. "type": "xxx",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
   13. },
   14. {
   15. "name": "app_id",
   16. "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
   17. }
   18. ],
   19. "requestPermissions": [ // 配置JSVM权限和存储空间管理开放能力
   20. {
   21. "name": "ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY"
   22. },
   23. {
   24. "name": "ohos.permission.atomicService.MANAGE_STORAGE"
   25. }
   26. ]
   27. }
   ```

## 配置APP ID映射关系

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/1M4_UdlZTbWtcu7YaWzdDQ/zh-cn_image_0000002592379264.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=733F2BAE72E53276BAEE24803E4D16565CCF6285FDEF91FEDAB3D1567FB66752)
2. 在弹出的“新增配置信息”窗口中填写信息，完成后点击“下一步”。

   说明

   请正确配置HAP小游戏与RPK快游戏的映射关系。若开发者配置错误类型的游戏，将会提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/y4WfxH1RRcaFnucGqedLFg/zh-cn_image_0000002622858773.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=1E14CF58461D350C2E3D393F066E6DA0562FC6D22E32740F3C887E2323E2BC2A)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP小游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或草稿态的RPK快游戏。 |
3. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/LLUImyBUQBGp3xyUXDSNtQ/zh-cn_image_0000002622698893.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=17FB79DFF4AF2C9CF150F190A49D56EAB5E21DF23F135953EC3F079A0373766C)
4. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/GAZyinM8Q3eV4kbQxZdLug/zh-cn_image_0000002592219332.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=F7F7C9EBE3941DDB6D8E777BAE96D62CB8DDFA8EC18BF463B868F4271251B32F)
5. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/u-R05ya7Q0CNJwmvIjbH4g/zh-cn_image_0000002592379266.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=9B4003E8615E3309D3FB0AB899AF9DBE3EAF80B063650C68BA4C8F6553D9748D)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/BovrRhxqQQGTDj9-MMWYBA/zh-cn_image_0000002622858775.png?HW-CC-KV=V1&HW-CC-Date=20260611T070713Z&HW-CC-Expire=86400&HW-CC-Sign=9BFB25DC86B7051B2B7C6CF0F51BE75725B3873EFE1885FEB17611FC6BC5BB5B)
