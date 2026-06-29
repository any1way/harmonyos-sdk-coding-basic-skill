---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59d65146e3dcc41ec1b1351228c7a8c38fcb2e00e9acf54fab0936f42aabadc7
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/D4p2jxXwThOMfDnQkq6LxA/zh-cn_image_0000002622699301.png?HW-CC-KV=V1&HW-CC-Date=20260611T071743Z&HW-CC-Expire=86400&HW-CC-Sign=9C109EC3FF01CA358D4C2DA43A6216563DAF0B912B5FCD21860FDA33ADC5B086)

## 功能描述

* 支持加载.om模型。
* 支持展示拓扑结构和数据流shape。
* 支持查看模型的format、input和output等参数。
* 支持查看编译后模型的子图和算子设备信息。
* 支持查看节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。
* 支持保存可视化结果导出为图片。

## 使用可视化工具

### 安装工具

1. 下载最新的[Netron](https://github.com/lutzroeder/netron/tags)。
2. 安装Netron。

   * macOS: 下载.dmg文件或者执行brew cask install netron。
   * Linux: 下载.AppImage文件或者执行snap install netron。
   * Windows: 下载.exe文件或者执行winget install netron。
   * Python服务器：执行pip install netron安装Netron，然后通过netron [FILE]或netron.start('[FILE]')加载模型。
   * 浏览器：无需安装，直接打开网页端[Netron](https://netron.app/)可使用。
3. 安装完成后，将模型拖入窗口即可打开。

### 查看子图

对于编译后有子图的模型，可按照如下操作查看。

1. 将编译后的模型拖入[Netron](https://netron.app/)工具，即可打开。
2. 点击子图节点，在右侧查找"ATTRIBUTES->subgraph"，点击"subgraph"的属性值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/wzHLt0L8SwGfAsGf3EMwFg/zh-cn_image_0000002592219740.png?HW-CC-KV=V1&HW-CC-Date=20260611T071743Z&HW-CC-Expire=86400&HW-CC-Sign=57CA649BD1595D3409BA452CAE406424E88EDA048E55DD403CE02689B046D661)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/X9n5aYd4SnSbna2Bun77cg/zh-cn_image_0000002592379674.png?HW-CC-KV=V1&HW-CC-Date=20260611T071743Z&HW-CC-Expire=86400&HW-CC-Sign=A9E9D5EC785539A61490CCCFA8FEA2052760BC38728E396FE4C9CC9117398C8D)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/zZp5BJkSRfSL6ATQTyik0w/zh-cn_image_0000002622859183.png?HW-CC-KV=V1&HW-CC-Date=20260611T071743Z&HW-CC-Expire=86400&HW-CC-Sign=F32428587C5E3F9212B6330EB482F6BE0546B933251DE23DA35435C6AE06B558)
