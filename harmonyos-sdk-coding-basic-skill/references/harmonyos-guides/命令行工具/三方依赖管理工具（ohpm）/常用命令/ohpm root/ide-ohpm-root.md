---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root
title: ohpm root
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm root
category: harmonyos-guides
scraped_at: 2026-06-11T15:32:14+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:4ef17aa2edc0e1a81568689e3ae29969b8f0d90a26fab6ad97bb2f75ed3f8067
---

在标准输出中打印有效的 oh\_modules 目录路径信息。

## 命令格式

```
1. ohpm root
```

## 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh\_modules 目录路径信息。

## Options

### prefix

* 默认值：""
* 类型： string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh\_modules 目录路径信息。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 root 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

项目结构为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/K1W4t_HKS6-BHmHdeuz40g/zh-cn_image_0000002571386824.png?HW-CC-KV=V1&HW-CC-Date=20260611T073213Z&HW-CC-Expire=86400&HW-CC-Sign=12583296B8A696C0F35AEF2B64BDDD96F5B9D0A3698465036A7D5826074E9BBB)

在entry模块的src目录下执行：

```
1. ohpm root
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/RrRdZt-XSmSrcL1zHSkJ3w/zh-cn_image_0000002571386826.png?HW-CC-KV=V1&HW-CC-Date=20260611T073213Z&HW-CC-Expire=86400&HW-CC-Sign=CF43D45C2672FC1951BE12CF2D4A89A288D948558ED7AA9194283CFBF9040067)
