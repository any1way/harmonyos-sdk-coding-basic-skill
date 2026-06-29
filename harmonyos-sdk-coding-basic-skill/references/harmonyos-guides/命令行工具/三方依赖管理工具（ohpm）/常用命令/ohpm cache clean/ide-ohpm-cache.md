---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-cache
title: ohpm cache clean
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm cache clean
category: harmonyos-guides
scraped_at: 2026-06-11T15:32:16+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:37517a7f0961e6192c8e6d1326487f896ea2eeb41c9b3ab3fb799c73dcc360b0
---
清理 ohpm 缓存文件夹。

## 命令格式

```
1. ohpm cache clean [options]
```

## 功能描述

用于清理 ohpm 缓存文件夹。

## Options

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

清理 ohpm 缓存文件夹，可执行以下命令：

```
1. ohpm cache clean
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ogr5tNstQnuY64ojEx6kvw/zh-cn_image_0000002602066587.png?HW-CC-KV=V1&HW-CC-Date=20260611T073215Z&HW-CC-Expire=86400&HW-CC-Sign=96FDD1C3466C49EBB007C493CEF23C77CDB6B1344CDFE065744253AE9DB3D6F2)

### 关于缓存设计的说明

ohpm 将缓存数据存储在配置的 cache 目录下名为 content-v1 的文件夹中，存储所有通过 http 请求获取的 HAR 包数据。包的路径使用包的 sha512 哈希值分割成 3 段，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。

### 配置

缓存的配置方式见 [ohpmrc](../../ohpmrc/ide-ohpmrc.md) 。
