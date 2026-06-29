---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-joint-commission-test
title: 接入联调测试
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 接入联调测试
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e6491e40f3847b7a825e4fcc964df008de9862b96ef87439dea6d6b200ea10f
---
若开发者需要在设备上调试、验证实况窗，可通过“调测设备管理”入口，添加设备进行调测。添加到调测名单中的设备，不做本地构建实况窗权限的校验。

调测设备管理能力可用于应用实况窗场景上线前的用户验证，开发者可将用户设备添加至调测设备列表中，以体验应用即将上线的实况窗场景。

**在调测设备上对实况窗充分测试后，开发者可申请开通实况窗正式权限**（在申请权限时，请在附件中一并提交调测设备联调的交互效果截图）。

## 约束和限制

* 添加的调测设备管理名单数据，系统将在24小时内处理并生效，调测权限有效期与Push Token有效期保持一致。
* 调测设备管理需根据Push Token添加调测设备，每个应用可添加的设备上限为100。

## 添加调测设备

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中找到开发者的项目，通过“增长 > 推送服务 > 配置”导航到“配置”页签。
2. 选择开发者的应用，点击实况窗-调测设备管理，根据[Push Token](<../../../Push Kit（推送服务）/开发准备/获取Push Token/push-get-token.md>)添加调测设备后即可进行接入调测。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/20x9pT_iSW2E1quOIO55tw/zh-cn_image_0000002592379344.png?HW-CC-KV=V1&HW-CC-Date=20260611T070910Z&HW-CC-Expire=86400&HW-CC-Sign=E381C7F68A64000C55E06FBADE5CB62D6C24C4FDD42B4B7F74661D3188179EE2)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/VAk611KxT-mNBJIzXWd2DA/zh-cn_image_0000002622858853.png?HW-CC-KV=V1&HW-CC-Date=20260611T070910Z&HW-CC-Expire=86400&HW-CC-Sign=AC04E5196480887082BEA03D86664EC7237AF6F4F4D1F97DB8ABFBB56FE43019)
