---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start
title: ohpm-repo start
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo start
category: harmonyos-guides
scraped_at: 2026-06-01T15:17:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:51c66426900c0b021a8c5d76250aab66720400d164f41a116bb49468bafaf733
---
启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](<../ohpm-repo install/ide-ohpm-repo-install.md>)，并按要求刷新环境变量。

## 命令格式

```
1. ohpm-repo start
```

## 功能描述

用于启动ohpm-repo服务，创建一个ohpm-repo实例。

说明

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件中，其中<deploy\_root>为[ohpm-repo私仓部署目录](../../配置文件/ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```
1. ohpm-repo start
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/C8A69ZlEQC-YXwiM89BtGg/zh-cn_image_0000002602064957.png?HW-CC-KV=V1&HW-CC-Date=20260601T071720Z&HW-CC-Expire=86400&HW-CC-Sign=76DB7E19E5449F917AB5CE3AA2C1EEFFEC45FDC345462D2C1389F6A86B9366F0 "点击放大")
