---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-13
title: 签名密钥库文件口令错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名密钥库文件口令错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8f1c53da7ff9184151bbb1d06ef8683150d1d96c1f5dfe576e364c9b8f4e189d
---

**问题现象**

打包签名提示“**Init keystore failed: keystore password was incorrect**”错误。

**可能原因**

签名密钥库文件口令错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/CG4gX5PoSxq6qst1d_h-Tw/zh-cn_image_0000002487813226.png?HW-CC-KV=V1&HW-CC-Date=20260612T024359Z&HW-CC-Expire=86400&HW-CC-Sign=E58881B75655DF10FDD86CD6C16DE50BA818496C6ADE52CB3E96753AE4D240D0)

**解决措施**

使用正确的密钥库文件口令，密钥库文件口令验证方式如下：

打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：keytool -list -keystore ${Store file} -storepass ${Store password}。

* 口令正确示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/GFFQWznBQKGbKDU2d3wVZg/zh-cn_image_0000002376396373.png?HW-CC-KV=V1&HW-CC-Date=20260612T024359Z&HW-CC-Expire=86400&HW-CC-Sign=2FEC5F3EB47C37119D5572AA5ABD8E3FF9EBBDE6B6D9A988489C9D96BCDB6FAC)

* 口令错误示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/rCg_iuynR2CFfHzZQal4cQ/zh-cn_image_0000002342678234.png?HW-CC-KV=V1&HW-CC-Date=20260612T024359Z&HW-CC-Expire=86400&HW-CC-Sign=3A1D8AA425C1DF5FF4454C558F74621A09277400B4C0ECB37F70D8DA594744E0)
