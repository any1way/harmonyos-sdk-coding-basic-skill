---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-version
title: ohpm version
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm version
category: harmonyos-guides
scraped_at: 2026-06-11T15:32:15+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:19c4dbdbda90fd00c67ca19e320147c074bfbb7e4bd5bb11710b8934ebcf9b2c
---

管理模块版本。

## 命令格式

```
1. ohpm version [options] [<newversion> | major | minor | patch]
```

## 功能描述

在模块目录中运行此命令以获取或升级版本号，同时将数据回写入 oh-package.json5 中。

## 参数说明

### 无参数

当无参数使用ohpm version命令时，则会将当前模块的版本号打印至标准输出中。

### newversion

newversion 参数应为一个合法的语义化版本，命令会将当前模块版本改写为 newversion 并打印在标准输出中。

### major

当参数为 major 时，有以下几种情况：

* 若无先行版本号，则将主版本号递增 1，其他位置为 0；
* 若存在先行版本号：
  + 当次版本号、修订号都为 0 时，则主版本号不变，而将先行版本号删掉。即 1.0.0-beta.1 升级为 1.0.0；
  + 当次版本号、修订号任意一个不为 0 时，则将主版本号递增1，其他位置为 0，并删除先行版本号。即 1.0.1-beta.1 升级为 2.0.0。

### minor

当参数为 minor 时，固定主版本号，变化次版本号与修订号，有以下几种情况：

* 若无先行版本号，则将次版本号递增 1，修订号置为 0；
* 若存在先行版本号:
  + 当修订号为 0 时，则次版本号不变，而将先行版本号删除。即 1.1.0-beta.1 升级为 1.1.0;
  + 当修订号不为 0 时，则将次版本号递增 1，修订号置为 0，同时删除先行版本号，即 1.1.1-beta.1 升级为 1.2.0。

### patch

当参数为 patch 时，固定主版本号与次版本号，变化修订号，有以下几种情况：

* 若无先行版本号，则修订号递增 1。即 1.0.0 升级为 1.0.1；
* 若存在先行版本号，则仅删除先行版本号。即 1.0.0-beta.1 升级为 1.0.0。

## Options

### prefix

* 默认值：""
* 类型： string

可以在 version 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。

### parameterFile

* 默认值：无
* 类型： string
* 别名：pf

可以在 version 命令后面配置 --pf <string> 或者 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 version 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

当前模块为 entry，版本号为 1.0.0，在当前模块的根目录执行：

```
1. ohpm version
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/TBdy3GP6RyeWccod3z9JBA/zh-cn_image_0000002602066043.png?HW-CC-KV=V1&HW-CC-Date=20260611T073214Z&HW-CC-Expire=86400&HW-CC-Sign=B99EA87990FE55166E35397127C0391544775F4786AC6DBD284AF04ECBD256EC "点击放大")

接着执行：

```
1. ohpm version 1.0.1-beta.1
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sLMK_RekRbmkMH0r3j-L2g/zh-cn_image_0000002571386926.png?HW-CC-KV=V1&HW-CC-Date=20260611T073214Z&HW-CC-Expire=86400&HW-CC-Sign=E3B97F105EBE77F2415D34695E01C700612612310281B1CC8AFA3DF97736F61B "点击放大")

接着执行：

```
1. ohpm version major
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/lJ_msJlmRVaTyfmfaRApPQ/zh-cn_image_0000002571386928.png?HW-CC-KV=V1&HW-CC-Date=20260611T073214Z&HW-CC-Expire=86400&HW-CC-Sign=E071F4DED9D16AAC2BC296E8108C9237C8F9D158BB84D4EB6FEEDBC8239EBCA4 "点击放大")
