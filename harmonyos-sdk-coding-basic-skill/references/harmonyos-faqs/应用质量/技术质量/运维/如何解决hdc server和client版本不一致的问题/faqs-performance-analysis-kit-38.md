---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-38
title: 如何解决hdc server和client版本不一致的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决hdc server和client版本不一致的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:40+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:7c99c593ce5fdd67299ee4c268e456352c4cc21a2e76c5d21244b7c1fcbcace7
---

**问题现象**

hdc.log 中的报错信息为“Daemon Session Handshake failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/AsVlOI_NRuaMIQv45haBsQ/zh-cn_image_0000002194318252.png?HW-CC-KV=V1&HW-CC-Date=20260612T021939Z&HW-CC-Expire=86400&HW-CC-Sign=3D1C44F37AE2A7EAC1C81C775E86156EA0821569F2A64D7FC03C5E2E2326F55D "点击放大")

**解决措施**

1. 通过以下命令检查server和client的版本是否匹配。

   hdc checkserver
2. 执行以下命令，终止其他版本的服务器。

   hdc kill
