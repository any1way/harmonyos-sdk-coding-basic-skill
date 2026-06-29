---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-06-11T14:43:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cbe5658c84da1cb187d3b6aba01a7ea255e68e204ec5b8e8330ce549ed9c220c
---
在开通Device Security服务前，请先参考“[应用开发准备](../../../../../应用开发准备/应用开发准备/application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

说明

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测能力、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/gkZAcDvGT86zWOihBsBNgg/zh-cn_image_0000002592218800.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=9EE800CEBCA19F453E98D0A7488D0B65A2F4D3F4AD6E94B6D2D1CB0856259344)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/QoaIRpk-RqCowyv3k0Rglw/zh-cn_image_0000002592378734.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=D4818600F3469B5F3272497696E4A6E00906E7024A62CD05212C495C48FFD23F)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/nxumBp59R8aZmfzvyJJMBg/zh-cn_image_0000002622858241.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=336F932D5B13D9C6CB9E84C036A586824C2AB4714544954255865414575F167E)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/3FAp9kLkRiKcV4S-_54vqQ/zh-cn_image_0000002622698363.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=98BFE8C5BA9189E838F84C7322BECB7763E1585054C9D7D3D88D8C1110D16215)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     说明

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/gFRlaVFoRG-DileI92Hd1g/zh-cn_image_0000002592218802.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=207DF8E01A4231779D94245F70C1EFCEBEE79B040EE457DE7BD05A3D82B3DE94)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/1qo2DgpLSP6I272hsG_ZzQ/zh-cn_image_0000002592378736.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=E6557C3D272403C2BCFC7FD84017980FD2199AE2B96223164B39B72649205D21)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](../../个人数据处理说明/devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sJplMrdqTRi77cr5qxJjJA/zh-cn_image_0000002622858243.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=8390FBE3FE4A3C8CC8BB5794E1E14EB21A441684A2D030F52E2C9919AF291127)

     说明

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
   * **数字盾服务**：点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“数字盾服务”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。

     ② 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/vadw1oT-SHWy-spPb6Y2gw/zh-cn_image_0000002622698365.png?HW-CC-KV=V1&HW-CC-Date=20260611T064340Z&HW-CC-Expire=86400&HW-CC-Sign=22FE2060A71F65CC31A77C07842191BCCC3CE64DE75BA5AC98B9E66618C69C51)

     说明

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。

   说明

   在开通服务后，需要重新申请Profile（.p7b）文件。
