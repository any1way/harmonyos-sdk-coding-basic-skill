---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-502
title: 变更说明
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-06-12T11:47:57+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0b44ce8afd3c8e4a5638277b85cd49ab21f14d27924288888dcadb0246d9d431
---

## 5.0.5.315至5.0.7.100

### 编译构建对签名配置的name字段增加非空字符串校验

升级到DevEco Studio 5.0.2 Beta1（5.0.7.100）及以上版本，工程级build-profile.json5文件中signingConfigs下的name字段不允许为空字符串。

**变更影响**

如果历史工程的工程级build-profile.json5文件中signingConfigs下的name字段为空字符串，编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/vmbRbq_0SP-2xocoRRXOMA/zh-cn_image_0000002336615601.png?HW-CC-KV=V1&HW-CC-Date=20260612T034756Z&HW-CC-Expire=86400&HW-CC-Sign=ABE67E36E52AFFD89CA360648074F23AE4D9BD71174B07AC2C55B305DBA18E48)

**适配指导**

将signingConfigs下的name字段配置为非空字符串。
