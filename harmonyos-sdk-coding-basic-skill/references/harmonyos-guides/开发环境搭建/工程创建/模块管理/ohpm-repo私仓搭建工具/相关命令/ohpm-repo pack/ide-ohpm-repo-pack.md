---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack
title: ohpm-repo pack
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo pack
category: harmonyos-guides
scraped_at: 2026-06-01T15:17:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b94cb34f8979dc43af9a979b098a4ae3825b6981ad38f3b4f5de67c1e2664f99
---
打包ohpm-repo部署目录文件。

## 前提条件

已成功执行[start 命令](<../ohpm-repo start/ide-ohpm-repo-start.md>)或者[restart 命令](<../ohpm-repo restart/ide-ohpm-repo-restart.md>)，ohpm-repo服务启动成功。

## 命令格式

```
1. ohpm-repo pack <deploy_root>
```

## 功能描述

用于打包ohpm-repo部署目录[deploy\_root](../../配置文件/ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)下的conf ，db和meta目录。

说明：

* 如果数据存储db模块使用的是mysql，则命令只打包conf和meta目录内容。
* 如果数据存储db模块使用的是filedb，则命令打包conf、db和meta目录内容，且在命令执行过程中，会先将ohpm-repo服务设置为只读模式，等打包完成以后，再将ohpm-repo服务重置为读写模式。
* 打包产物可通过ohpm-repo restore命令自动解压至<deploy\_root>目录。

## 参数

### <deploy\_root>

* 类型： String
* 必填参数

必须在pack命令后面配置<deploy\_root>参数，指定待打包的[ohpm-repo私仓部署目录](../../配置文件/ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```
1. ohpm-repo pack D:\ohpm-repo
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/OkieZGn4QTGA9J67QZCIWQ/zh-cn_image_0000002602064933.png?HW-CC-KV=V1&HW-CC-Date=20260601T071726Z&HW-CC-Expire=86400&HW-CC-Sign=6A1C844095EC7AFFB685F39F24E660A3ABC7CC73FB76C7ADF9B6D92183E1D8FC "点击放大")
