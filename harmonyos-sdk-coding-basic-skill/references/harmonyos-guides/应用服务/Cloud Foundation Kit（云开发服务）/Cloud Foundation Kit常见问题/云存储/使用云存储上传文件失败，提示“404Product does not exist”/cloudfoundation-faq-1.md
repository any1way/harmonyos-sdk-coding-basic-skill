---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-1
title: 使用云存储上传文件失败，提示“404:Product does not exist”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，提示“404:Product does not exist”
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:16+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:7c557eeecd0194fe6afbce36593575b1a0bea7372d80c04ced58dc4a46cb8b6d
---
**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/XWVCkciKTDOzeLXTh68Ujg/zh-cn_image_0000002622858755.png?HW-CC-KV=V1&HW-CC-Date=20260611T070615Z&HW-CC-Expire=86400&HW-CC-Sign=CB8E91036815DAE088765490B1DB3729042F2CBC7BF738EE3E3DAA5084A00021)

**解决措施**

此错误由云存储服务端返回，原因是云存储服务未开通。请[开通云存储服务](../../../开发准备/开通云存储服务/cloudfoundation-enable-storage.md)。
