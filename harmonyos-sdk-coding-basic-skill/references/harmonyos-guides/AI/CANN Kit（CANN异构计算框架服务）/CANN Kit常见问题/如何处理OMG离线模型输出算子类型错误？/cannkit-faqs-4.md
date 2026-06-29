---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理OMG离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理OMG离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1cf4dac0e66fc934c56176415506e3e748e1aa4aab4a177f312be61bd1bf8a6f
---
Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在OMG命令中加入--op\_name\_map参数，参考[OMG参数](../../模型转换/离线模型转换/OMG参数/cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/NXVAAR0xSDeUlERa2GaFsw/zh-cn_image_0000002622859171.png?HW-CC-KV=V1&HW-CC-Date=20260611T071739Z&HW-CC-Expire=86400&HW-CC-Sign=35E6E0B58948A91A1F498D438BF1E4CC0BCBB068C6D521D717890294DCA1DF95)
