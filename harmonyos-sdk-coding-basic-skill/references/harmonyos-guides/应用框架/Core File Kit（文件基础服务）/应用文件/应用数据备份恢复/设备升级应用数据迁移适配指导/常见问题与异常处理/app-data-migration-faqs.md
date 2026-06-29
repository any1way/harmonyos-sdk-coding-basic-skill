---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-06-11T14:36:54+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:478ed669b93fde6a8019f8218b1af7a717cd598552f4d38d3618b7fee398c954
---
## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/yhaCM2VpR4ufoADfdbQ5UQ/zh-cn_image_0000002622858123.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=3B4D22D20E05771AD3F5E172F6CF86CCCEFD80DC5F7E7345E9F4A2CB436E7BAC)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/M7uUVY1oTEq8nMnwKJChUA/zh-cn_image_0000002622698245.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=4FB9542E5D5CB8A586063316890DA2031DB2D32BF9E551348E84DB308888B974)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/uJDRQTVXRqCRJ2HrLHK7_A/zh-cn_image_0000002592218684.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=8BE98ED3246CCCDE2097FAEB6B902C311365B2BCDD45523C02E5208C36F4EB4D)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/BbDg0yX8SFqAJuVnbtvdAw/zh-cn_image_0000002592378618.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=4A72BA77CFFF9EFD393F582551E2947890C5E8BFE4757B9B87541C474217CE43)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Y7UeeHd7QCCUZy5RuHyvag/zh-cn_image_0000002592218682.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=92D79996D415F2DCAC0CD8A6702E36523FBF67D2070B1E412E5E2E9316D4FFE3)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

说明

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

## 启动迁移按钮无法点击

**问题现象**

在迁移调试界面，输入应用包名后启动迁移按钮无法点亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/k3AaiTcHRpSbgXubJmLIfA/zh-cn_image_0000002622858125.png?HW-CC-KV=V1&HW-CC-Date=20260611T063653Z&HW-CC-Expire=86400&HW-CC-Sign=4367AB5F1385C79E73DD6E860F85269A6A198FA5DD10F3F4F6F10C6695EB4CD6)

**可能原因**

迁移调试工具版本过低（版本号低于6.0.0.190）。

**解决方法**

请参考[开发者自验证](../适配流程/adaptation-process.md#开发者自验证)下“迁移调试”工具获取方式，申请最新版迁移调试工具。
