---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160
title: Stack布局设置Alignment.Bottom没有生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Stack布局设置Alignment.Bottom没有生效
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e2cf63c5bf050c9516a3bcfc787f4ad1c980177ef90beab66ef34eb715cf9052
---

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/393kaMcCSlei-R1FVIfnfA/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260612T022820Z&HW-CC-Expire=86400&HW-CC-Sign=5136D065400D46A9F4D89214927E3B3E2A4A5985CCE9A4F75B4C7EF86CAFA667)

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
