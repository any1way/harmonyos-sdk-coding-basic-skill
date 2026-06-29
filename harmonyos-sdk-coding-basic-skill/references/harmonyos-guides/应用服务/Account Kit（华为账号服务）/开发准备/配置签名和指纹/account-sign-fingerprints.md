---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-06-11T15:02:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:625e6ec757acab838ea3ebc65024a8662f33eb778a01dca7081239663ec5d74e
---
请参考“[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息 **（未成年人模式接口支持自动签名，其他接口仅支持手动签名方式）**。
3. 添加公钥指纹。

   注意

   **发布阶段**，请参考[发布流程](../../../../发布应用/发布应用/ide-publish-app.md#section6406135115814)章节，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/JVaEyHe9R6WSLdYVSp_sqg/zh-cn_image_0000002592219176.png?HW-CC-KV=V1&HW-CC-Date=20260611T070230Z&HW-CC-Expire=86400&HW-CC-Sign=159C76BAB11DD8033EFB40F6556B71E29B8DB45640A2B3A765A823D20A6083A0)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/sQvBgaA6R_6pb3MSyBJEwQ/zh-cn_image_0000002592379110.png?HW-CC-KV=V1&HW-CC-Date=20260611T070230Z&HW-CC-Expire=86400&HW-CC-Sign=0D59BEC937B5C987F1C2C557AB4886EF55591BB827961DAC8476D7C567715EC6)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/taTibDtjTaC4wRv6ki-knA/zh-cn_image_0000002622858615.png?HW-CC-KV=V1&HW-CC-Date=20260611T070230Z&HW-CC-Expire=86400&HW-CC-Sign=1B6177202BFAC593D35FC0B16225446BE643DF03F656D8A6FB2C7FDD6B77D268)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/xGTk1IJDQmqhi3GL7jv_Ow/zh-cn_image_0000002622698737.png?HW-CC-KV=V1&HW-CC-Date=20260611T070230Z&HW-CC-Expire=86400&HW-CC-Sign=BE6924EF5CF65EEFB2F677E9D5D10A55958AFAED139D363E98D8E8E4EC6C9185)
