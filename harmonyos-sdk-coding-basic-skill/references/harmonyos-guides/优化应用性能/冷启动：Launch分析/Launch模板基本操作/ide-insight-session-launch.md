---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch
title: Launch模板基本操作
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > Launch模板基本操作
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:32+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a28cdd397e2393f2214dc22f183db77a5e27fb20784af9e2b8bf5ecae839ebc5
---
开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。此外，Launch任务窗口还集成了Time、CPU、Frame、Network场景分析任务的功能，方便开发者在分析启动耗时的过程中同步对比同一时段的其他资源占用情况。

此处仅介绍“Launch”泳道相关内容，集成的Time、CPU、Frame、Network场景分析任务的功能请参考对应任务的章节。

说明

* 不支持命令拉起的Release应用不能进行Launch分析。
* 锁屏状态下可进行Launch录制。

## 启动模式

启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/wlwMJRHQTCSLrIEYJgViCQ/zh-cn_image_0000002602186087.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=09CD5480E2AD705C33E190F10088A6B3BB765ADAA4C9A7E556E245317A786E0E)自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Krh4h38rTFmvuNuXE85L9g/zh-cn_image_0000002602186093.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=B7C4B456E8F5DAC8DA950702628F9C660F8CC238BA1CFFD6B62EC2D3A3B02264)手动启动，可点击图标切换两种不同模式：

* 若选择自动启动模式，当用户使用Launch模板并开始录制时，将主动重启所选应用；
* 手动启动模式在开始录制时，只会主动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

## 查看启动过程中各阶段的耗时情况

1. 创建Launch场景调优分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据。

   说明

   * 在任务分析窗口中，可通过[快捷键](../../附录/快捷键/ide-shortcut-key.md)缩放时间轴、移动时间轴、添加时间标签等。
   * Launch分析支持离线符号解析能力，请参见[离线符号解析](../../基础耗时：Time分析/ide-insight-session-time.md#section186881175012)。
   * Launch分析支持动效场景调优，请参见[支持动效场景调优](../../卡顿丢帧分析/Frame分析/ide-insight-session-frame.md#section258014238619)。

   Launch分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Li3tCbcqR0y09aPSrzF4Vg/zh-cn_image_0000002571546548.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=F4F820AA73F6B53E77640B44C0CA9E1EE722821FFF48C7C67FFDBAAC59DD2767)指定要录制的泳道。“Launch”泳道显示启动生命周期各阶段的耗时分布情况。
2. 单击“Launch”泳道上的单个阶段，或框选多个阶段，在下方的“Details”页签中，可查看到所选阶段的耗时统计情况。

   展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息。单击跳转按钮，可直接跳转至相关线程打点任务中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ANxI0LR4QpCOdGMLdGm-8w/zh-cn_image_0000002602186081.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=368E6D5200D8E11A6A2308F8940FA20B910E6C09727D605BE8A808A8CE19E841 "点击放大")
3. 切换到“Load ETS Files”页签，从DevEco Studio 6.0.0 Beta1版本开始，支持查看冷启动过程中ETS文件的加载情况。各字段含义如下：
   * Category：该ETS文件在应用启动过程中是否被使用。
   * Weight**：**该ETS文件加载子节点文件（不包括自身）的总耗时。
   * Self：该ETS文件自身加载的耗时。
   * Import Count：该ETS文件被其他文件导入的次数。
   * File Name：该ETS文件的名称。
   * Path：该ETS文件构建产物的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/sgDtvX5JQv2w9YTKJJs2hQ/zh-cn_image_0000002602186083.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=EEAA251DE58C0BAC624C3AAEA34C89B4FE2E2AE38575F1E7D1AF964FD1730589 "点击放大")
4. 切换到“TOP Redundant”页签，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/XrDYCaB5Q5q66pljyRaDXg/zh-cn_image_0000002571546554.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=104C91B6269FA01EB7EE4CDE6CBB5495852B0ADAEF31D4E64F7E553061D0BB9B "点击放大")

说明

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中ETS文件的加载情况。

## 分析静态资源库加载耗时

1. 展开“Launch”泳道，其中的“Static Initialization”子泳道展示启动过程中各静态资源库的加载耗时。
2. 单击单个静态资源库色块，或框选多个静态资源库，下方的“Details”区域展示所选对象的耗时统计信息。

   针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/SvyXRwW1Td-je-K7QCVG1Q/zh-cn_image_0000002571386920.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=B1953162AE754D1466540CA83C60D9D83EEC2CF5436BE0CBC07B52ADD2EEAB76 "点击放大")

## 查看核心线程在CPU Core的运行情况

1. 展开“Launch”泳道，其中的“Running CPU Cores”子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2. 单击单个进程色块，或框选多个进程，下方的“Details”区域展示所选对象的运行情况统计信息。

   单击对应CPU的跳转按钮，可进一步跳转到CPU Core泳道查看详细的调度信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/c9yvTdYoSgyxVqPsmE1VAw/zh-cn_image_0000002571546558.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=C544E995BAD6400A7014C8BE6FEA404A01D09EEF5750F84A58F3A1F12239BFC5 "点击放大")

## 查看启动过程相关的线程Trace数据

1. 展开“Launch”泳道，除“Static Initialization”、“Running CPU Cores”外，还包含启动过程的关键线程的状态和Trace数据。
2. 单击单个切片色块，或框选多个切片，可查看所选对象的详情。
   * “Details”区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
   * “Thread States”区域展示线程的状态统计信息。
   * “Thread Usage”区域展示线程的使用情况。
   * “Slice List”区域展示所选对象的切片统计信息。
   * “Load Statistics”区域展示所选对象的中载重载信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/MwSOLvjSS2KmcmtLkBUqqw/zh-cn_image_0000002571386916.png?HW-CC-KV=V1&HW-CC-Date=20260611T073132Z&HW-CC-Expire=86400&HW-CC-Sign=03350DA36897460237F1169BEB44693C0D0E99B16653B7FBD01B33B0D2B6E663 "点击放大")
