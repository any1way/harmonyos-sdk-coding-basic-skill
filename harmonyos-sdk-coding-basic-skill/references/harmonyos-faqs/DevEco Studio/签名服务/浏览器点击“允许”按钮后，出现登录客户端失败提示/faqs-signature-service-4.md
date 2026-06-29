---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-4
title: 浏览器点击“允许”按钮后，出现登录客户端失败提示
breadcrumb: FAQ > DevEco Studio > 签名服务 > 浏览器点击“允许”按钮后，出现登录客户端失败提示
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:09913a0a04c5d14d4770f00dbcf9c34e4bb522d9141733291c31e5d0cfc6ca78
---
**问题现象**

使用实名认证的华为账号登录后，点击“允许”按钮进行授权。如果浏览器提示“登录HUAWEI DevEco Studio客户端失败”，请检查网络连接或重新尝试登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/XkhvHqwRQgOiqYYF7oViSA/zh-cn_image_0000002229604393.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=15EEF2C1A6BB7B132B75FDBBF6B50EE831EE9D389B443127D23B4D05D7837FD1 "点击放大")

**解决措施**

该问题由DevEco Studio的HTTP代理问题引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/S6MAppxAQHCVLUMnjAn8ug/zh-cn_image_0000002194318608.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=F8E902BD7695E0CB8EAFE41CFD2ED75DA0101E35DD009166DBE96C6FA48DB61E "点击放大")

1. 检查HTTP Proxy设置。
   * 如果网络无需代理即可访问Internet，设置代理会影响模拟器的登录授权。请检查并确保HTTP Proxy设置为“No proxy”。
   * 如果您的网络需要代理访问Internet，未设置代理会影响模拟器的登录授权，请检查并将HTTP Proxy设置为“Manual proxy configuration”，设置方法可参考[配置Proxy代理](../../../../harmonyos-guides/编写与调试应用/附录/配置代理/ide-environment-config.md#section10369436568)。
2. 在DevEco Studio界面，点击**Cancel**按钮，重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ZviSJybaQ7yxKXbu3Smb-w/zh-cn_image_0000002229758881.png?HW-CC-KV=V1&HW-CC-Date=20260612T024350Z&HW-CC-Expire=86400&HW-CC-Sign=328F779E0B6234C7254234CEA188692FE0733DC10BF65CBD928B991E02BE15AC)
