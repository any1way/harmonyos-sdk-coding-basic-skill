---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6d5184648878feec98b8bb2ed61514abd12946b121ce1daff3aaccb1fc6f8bb3
---
如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](../agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到AGC应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/2816p9YOS6WHOxx73-VeAg/zh-cn_image_0000002214858725.png?HW-CC-KV=V1&HW-CC-Date=20260601T071817Z&HW-CC-Expire=86400&HW-CC-Sign=F0A2C75376074FBD805ED87424847FB70B09E761EE3483B1BCDDA4E9D47D212E)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ieBf93utT3yGspNvQIPLSg/zh-cn_image_0000002277950390.png?HW-CC-KV=V1&HW-CC-Date=20260601T071817Z&HW-CC-Expire=86400&HW-CC-Sign=78F7875F2BB65AF1E4D1C0D8F198DDE3C3691537DBE082E212CA4B6E4B6C37EE)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
