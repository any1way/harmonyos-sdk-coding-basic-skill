---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-module
title: 导入和引用模块
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 导入和引用模块
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:01+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f2711bf4eeae89ade662f49b7b9d5ad2febd4c19ec451587c432f28de41d3641
---
DevEco Studio支持通过以下两种方式导入其他工程下的模块：

1. 通过[Import Module](ide-import-module.md#section14353041183813)功能，将其它HarmonyOS模块的功能代码复制到当前工程中；当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
2. 通过在[srcPath字段下配置相对路径](ide-import-module.md#section12737181153918)的方式引用其他工程下的模块，该方式仅引用模块相关信息，不会将模块代码完全复制至本地。当前支持引用其他工程下的HAR和HSP模块。

## 导入模块

1. 在菜单栏单击**File > New > Import... > Import Module。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/hGHUzKRARfSdM1qqHr4PTw/zh-cn_image_0000002602066333.png?HW-CC-KV=V1&HW-CC-Date=20260611T072200Z&HW-CC-Expire=86400&HW-CC-Sign=CAF05916E1732A7AAD7CF0FE9A1CC0E402ECCA7428CA072063D11FDCA6FE0EF5)
2. 选择导入的模块。

   在指定路径下，选择导入的模块，单击**OK**。导入的模块可以为文件夹，也可以为zip格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/2vx0FuYxTG6o2EPMM9BBZQ/zh-cn_image_0000002571387218.png?HW-CC-KV=V1&HW-CC-Date=20260611T072200Z&HW-CC-Expire=86400&HW-CC-Sign=03520562DAA26A713BB6B54BD73E877F7A284CF896A5B7BCC3B321A03A92DE69)

## 引用模块

在工程级build-profile.json5文件中，如下图所示在modules > srcPath字段下配置工程外模块的相对路径，即可引用模块相关信息，不会将模块代码完全复制至本工程中。当前支持引用其他工程下的HAR和HSP模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/OF1gLvGdSlmXqmghIzBJ5A/zh-cn_image_0000002571546852.png?HW-CC-KV=V1&HW-CC-Date=20260611T072200Z&HW-CC-Expire=86400&HW-CC-Sign=05793CBC188E6FA4241771A1955D9D39E2E28CBF9D76700ECE1A8842A7FCE064)
