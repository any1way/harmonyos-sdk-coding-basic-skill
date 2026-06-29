---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu
title: GPU活动分析
breadcrumb: 指南 > 优化应用性能 > GPU活动分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:46+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:fb452fda3025e01f753a12971ff665e13fa6ff93fb79061e2cf6e37709b0bd32
---
从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

## 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 仅支持Phone设备。

## 操作步骤

1. 创建GPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)。

   GPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/w7pd6DE1Q3CaCyhUeGaKqA/zh-cn_image_0000002571546692.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=2D8CC9C0C4B7587DD6F125E3028B6522AE9E4A42314BA971B1C1EA4A948F7CF4)指定要录制的泳道。单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Qn7NzMUHSsqqxk3yECrK3A/zh-cn_image_0000002571546696.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=B522D4FEBD0A0BB792588004BFA028119C5970ADA7AA89795F386DB08E7E16FC)按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
2. “Counters”泳道显示当前设备GPU的使用率，“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息请参考[基础耗时：Time分析](../基础耗时：Time分析/ide-insight-session-time.md)和[CPU活动分析](../CPU活动分析/ide-insight-session-cpu.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/KqlsZvYJRuaP40uOApmwLQ/zh-cn_image_0000002602186227.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=4B84B3917400EA42E7BCE8D69522319647892AE1323F409ADA2012494A955064 "点击放大")
3. 将“Counters”泳道展开，子泳道显示GPU各项活动信息，包括counters\_gather、GPU执行命令的频率、GPU执行命令的持续时间等。除counters\_gather外，其他子泳道信息可参考[GPU Counters](https://developer.huawei.com/consumer/cn/doc/Tools-Guides/gpu-counters-0000001886127538)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/S1fv4fSJRxSsmaX_UDg5NQ/zh-cn_image_0000002571546700.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=97D83C72BAA35D31BE8435909850D1AF8A654B3F6395A2B9AA4060B5FB7931DE "点击放大")
4. counters\_gather泳道显示线程对各CPU核心的占用情况。单击运行状态的时间片段，显示线程在该时间片段的起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态，并且支持跳转到上个或者下个线程运行状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Cozoey_uTxCzUVHB6O079A/zh-cn_image_0000002571387058.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=FBB094F23387243924A53C5D131EA47066E3F5B3F8FB862BFBA0F8470A38AD6A "点击放大")
5. 框选counters\_gather泳道，可查看此时间段内的统计信息，包括线程状态统计信息、CPU单线程使用情况、线程中的中载重载数据统计。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/iHr7MiUTQpWXYYMgjm3IIw/zh-cn_image_0000002571546698.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=621D2B9209B9625759638793D69DDA8CC81612FD28EEA7AF42DBAA836FAEF315 "点击放大")
