---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-6
title: 登录时浏览器提示不安全，“你的连接不是私密连接”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 登录时浏览器提示不安全，“你的连接不是私密连接”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:53+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:95509aad532d833016aed018a117a0abec7764b4b3f96eda6c34a2cc54d43f65
---

**问题现象**

使用模拟器时，需通过浏览器登录授权。如果浏览器提示网站“不安全”或“连接不是私密连接”，请检查网络连接或联系技术支持。

**解决措施**

DevEco Studio云端服务平台使用的是ACTALIS颁发的商业证书。主流浏览器通常预置了ACTALIS公司的根证书。如果遇到上述问题，可以通过以下措施解决：

1. 检查是否已安装ACTALIS公司的根证书（不同浏览器的查看方法请自行查阅）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/7nyaI11YRbmMN1Kq8raXGA/zh-cn_image_0000002194158872.png?HW-CC-KV=V1&HW-CC-Date=20260612T024352Z&HW-CC-Expire=86400&HW-CC-Sign=7835CA6149C194788B57E9567F794D3D8B565E51A3C896080C0492BB0084F3C1 "点击放大")

   * 已安装：检查Actalis证书是否被禁用。
   * 未安装：请前往[https://www.actalis.it/area-download#](https://www.actalis.it/area-download)下载和安装“Actalis Authentication Root CA”，安装完成后重启浏览器即可。
2. 打开命令行工具，执行**certmgr.msc**命令，打开证书管理界面。
3. 在**受信任的根证书颁发机构 > 证书**中，找到 Actalis Authentication Root CA，右键点击并选择“属性”。
4. 选择“启用此证书的所有目的(E)”，点击**确定**，然后重启浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/NC8gjiLfR7G35gem6o8SXg/zh-cn_image_0000002229758745.png?HW-CC-KV=V1&HW-CC-Date=20260612T024352Z&HW-CC-Expire=86400&HW-CC-Sign=A97F6E0B77DD942743CBB907764994D49BCC568CC90F104C1E6C2BAE8142FCA8)
