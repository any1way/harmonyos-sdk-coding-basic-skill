---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-boot-memory
title: 启动时内存分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 启动时内存分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:59614e5b24080428ef346b98ec2a7ee5a2445f5c3db96ee99026fba026c34362
---
应用/元服务在启动过程中对内存资源的占用情况，是开发者较为关心的问题。DevEco Profiler的Allocation分析任务，提供了启动内存分析能力，协助开发者优化启动过程的内存占用。

针对调测应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用停止，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/ZgsMU5J0RKC5npWmIfdaCA/zh-cn_image_0000002571546538.png?HW-CC-KV=V1&HW-CC-Date=20260611T073140Z&HW-CC-Expire=86400&HW-CC-Sign=D51CA9D7596EF0ED246D6DB24A343044AB2AA87BC752F987E228AF68D89748D1)按钮。

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同，请参考[内存分析介绍](../内存分析介绍/ide-insight-session-allocations-memory.md)、[内存分析数据筛选](../内存分析数据筛选/ide-insight-session-allocations-data-filtering.md)。
