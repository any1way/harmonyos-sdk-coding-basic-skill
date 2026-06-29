---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-1
title: 登录华为开发者账号后，提示需要实名认证
breadcrumb: FAQ > DevEco Studio > 应用运行 > 登录华为开发者账号后，提示需要实名认证
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8f4bda74bfc09cb8b438ec4268ba0ac0d3015d24dae09b63f49aa6ee2228055a
---

**问题现象**

使用本地模拟器时，需用实名认证的开发者账号登录授权。若账号未实名认证，本地模拟器会提示需要实名认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/icafjQKsSW6IqbDCKK-RjA/zh-cn_image_0000002194158868.png?HW-CC-KV=V1&HW-CC-Date=20260612T024405Z&HW-CC-Expire=86400&HW-CC-Sign=4FB7F50609EAE9DB87BF82EA65BE9ABB671B53ED92602D82819614CDABAF6166 "点击放大")

**解决措施**

原因包括以下两种情况：

* 华为账号未实名认证，请开发者按照如下步骤进行处理。
* 刚完成实名认证但认证未生效，开发者可根据步骤4清除浏览器Cookie后重试。

1. 点击上图中的**Verify Identity**，前往开发者联盟实名认证。
2. 根据浏览器界面提示进行实名认证，具体指导可以参考[实名认证介绍](https://developer.huawei.com/consumer/cn/doc/start/itrna-0000001076878172)。个人开发者可以选择银行卡认证或者身份证认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/GnA3_UsEQv29GqnJENs8ZQ/zh-cn_image_0000002194318476.png?HW-CC-KV=V1&HW-CC-Date=20260612T024405Z&HW-CC-Expire=86400&HW-CC-Sign=7368CB526FC2F5452BAA766F900281717799B11A723DDC1096BA72C7DBCE988E "点击放大")
3. 认证完成后，在DevEco Studio界面，点击右上角个人中心，点击Sign out退出，重新登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/kR32hD_HRqmiR7grBfICwA/zh-cn_image_0000002194318480.png?HW-CC-KV=V1&HW-CC-Date=20260612T024405Z&HW-CC-Expire=86400&HW-CC-Sign=93C5D127FED4D28D4DB4192229A3EE9DE4EF41860F723DED35F0D343F4627848)
4. （可选）如果实名认证后重新登录，仍提示需要进行实名认证，可清除浏览器 **Cookie（快捷键 Ctrl+Shift+Del）**后重试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/yZ7rH5i3SvaQSqN2P127TA/zh-cn_image_0000002229604249.png?HW-CC-KV=V1&HW-CC-Date=20260612T024405Z&HW-CC-Expire=86400&HW-CC-Sign=BE46C27E8064B35F2F26807FED83C304B1811860D3D25777CF90468D4214EF38 "点击放大")
