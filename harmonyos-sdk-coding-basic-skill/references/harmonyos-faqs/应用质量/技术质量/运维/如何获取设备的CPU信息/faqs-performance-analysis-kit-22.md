---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-22
title: 如何获取设备的CPU信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的CPU信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:12b8dbc716effe6f9ebcd3c544a2a9e0d758350c7100e131fa47317ee238dc08
---

可以通过以下命令来查看CPU信息：

```
1. // 查看CPU信息
2. hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/8T5YgLz-S3q2b68kUTfddg/zh-cn_image_0000002229758737.png?HW-CC-KV=V1&HW-CC-Date=20260612T021932Z&HW-CC-Expire=86400&HW-CC-Sign=0F1F72293C867CC2E7D1A0EC72B7828E342586B8F573A070DDF19CB7D89F6F11 "点击放大")
