---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-7
title: 如何配置DevEco Studio的代理
breadcrumb: FAQ > DevEco Studio > 环境准备 > 如何配置DevEco Studio的代理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6a66c347188af985658cb8a0d25a40162349aa654c49ccf9b99c83f1c366c202
---

DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。

如果使用个人或家庭网络，无需设置代理信息；企业网络受限时，需设置DevEco Studio的代理信息。

1. 打开**File > Settings > Appearance & Behavior > System Settings > HTTP Proxy**配置界面。
2. 勾选**Manual proxy configuration**，设置DevEco Studio的HTTP Proxy。
   * HTTP配置项，设置代理服务器信息。如果不确定代理服务器信息，可以联系网络管理员获取。
     + **Host name**：代理服务器主机名或IP地址。
     + **Port number**：代理服务器对应的端口号。
     + **No proxy for**：不需要通过代理服务器访问的URL或者IP地址（地址之间用英文逗号分隔）。
   * **Proxy authentication**配置项，如果代理服务器需要认证鉴权，请设置相应的配置项。否则，可以跳过此配置。
     + **Login**：访问代理服务器的用户名。
     + **Password**：访问代理服务器的密码。
     + **Remember**：勾选，记住密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/15gZNcoCRwiUjj8UGqsa9w/zh-cn_image_0000002229603741.png?HW-CC-KV=V1&HW-CC-Date=20260612T024008Z&HW-CC-Expire=86400&HW-CC-Sign=914EF95DA659F0DFBBFCBA2602D3A6D529AA499C770601045F3D7FA9962A20C9)
3. 配置完成后，点击“Check connection”，输入网络地址，检查网络连通性。提示“Connection successful”表示代理设置成功。点击“OK”按钮完成配置。
