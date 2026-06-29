---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-exception-detection
title: 使用方舟异常信息增强检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 使用方舟异常信息增强检测
category: best-practices
scraped_at: 2026-06-12T10:17:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9890d69cf200d277526ec57bf2ef98e3f35edcceccb4d29f23498f044772eeef
---

## 概述

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

## 启用方舟native模块加载异常信息增强

可以通过以下两种方式启用方舟native模块加载异常信息增强

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/N5mclDLMRxC1PHlLdUIeFg/zh-cn_image_0000002404125161.png?HW-CC-KV=V1&HW-CC-Date=20260612T021726Z&HW-CC-Expire=86400&HW-CC-Sign=18F227E629BFBD8C994C6488BD64C5F64DF0CFEC9C0455E4518361A6040BD65E)

* 方式二

  通过命令行开启。

  ```
  1. aa start {abilityName} {bundleName} -E
  ```

## 启用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/G6ySfffDRFaOpN5CGDZ4_w/zh-cn_image_0000002370405608.png?HW-CC-KV=V1&HW-CC-Date=20260612T021726Z&HW-CC-Expire=86400&HW-CC-Sign=8468100767C4E26D34E14799B30C34383D3E2239D23E55AF946FB1E3AE28F07F)
