---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-3
title: 输入华为账号后，未出现“允许”按钮，浏览器界面无跳转
breadcrumb: FAQ > DevEco Studio > 签名服务 > 输入华为账号后，未出现“允许”按钮，浏览器界面无跳转
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9f2f7a69032a7e27ee3f9a16facc76c1afc2f51aab08e8b1b1d6a86bcf2096a4
---

**问题现象**

使用浏览器登录华为账号后，如果账号已实名认证但未出现授权的“允许”按钮，界面也未跳转或提示。

**解决措施**

该问题由浏览器兼容性问题导致。模拟器登录授权已在Chrome、IE11和Safari浏览器中进行了充分验证，建议将默认浏览器设置为其中一种。

1. 设置或更改默认浏览器。
   * **Windows****平台**：以Windows 10为例，打开“**控制面板 > 程序 > 默认程序 > 设置默认程序**”，更改或设置默认浏览器。
   * **macOS平台**：以macOS 15为例，打开**系统设置，选择“桌面与程序坞”，再选择“默认网页浏览器****”**，更改或设置默认浏览器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Px5k8Z_1TSGiWhCaCwDgcw/zh-cn_image_0000002523427811.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=C74C4DB284837E24A6E1D3859C179434FB06DA4B2C40C1B0498FA2B22E2535CD "点击放大")

     使用Safari浏览器时，点击**Safari 浏览器 > 偏好设置>****隐私/高级**，取消“防止跨站跟踪”和“阻止所有Cookie”设置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ro8B_hfVTh6iy5X4njMOag/zh-cn_image_0000002491108268.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=65B7B30F85DD957D4A81B3F22D82654415A3FE7D1948A5CCBAD6A9B1B0E2AA09 "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/5lc2PqHzTwmsHIhbczk6bQ/zh-cn_image_0000002523268149.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=F7F7F3D3FDBD1059CE611523BB35BFFAA2301921B3A6B8C8C49380D1BA3C0067 "点击放大")
2. 在DevEco Studio界面，点击**Cancel**按钮，然后重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Hsc8QXzAT-yvogaN0btiQQ/zh-cn_image_0000002229603917.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=EABB6ECD2EAE8415BACEB2F9965451D09490AFFBD95BBB05FABB7DC21533F24F)
