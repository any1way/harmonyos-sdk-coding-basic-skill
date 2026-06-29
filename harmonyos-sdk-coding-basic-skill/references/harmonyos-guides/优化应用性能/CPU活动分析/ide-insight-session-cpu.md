---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:48+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:df528c06358e512af80c9699cdd6eff94e5b0e08543b21d0c166c264d5b0dae7
---
开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

## 查看各CPU使用情况

1. 创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据。

   CPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/rxy5TQcxSySpmAezew1EBA/zh-cn_image_0000002602066341.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=769B0A1C28773041D4909117E9737FC64805CBFF5BB917107A64AC92A2C35410)指定要录制的泳道。
2. “CPU Core”泳道显示当前选择调优应用或元服务的CPU的使用率。

   可在“CPU Core”右侧的下拉列表中选择显示内容：

   * Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/WhXSwMqbSGmXMQAlbChwNQ/zh-cn_image_0000002602066331.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=9B32B3319F553CAC7078B6ADE0B147C336744332509C88D55D4924F23748904A "点击放大")
3. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   说明

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Ppy6MvX_RGGXpjMSSBvsbQ/zh-cn_image_0000002571387216.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=113BFD69FE5DBB871D2422A4D5DF6C32B6B95AAFB3FDC353CB5CAE2FD3217D64 "点击放大")
4. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HzBw89SzSpG0u5keyZujJA/zh-cn_image_0000002571546862.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=0A7FA1BD544B688B26A2B4716F1960399DD014778F0E6008E0A96E01619D7C5C "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/1xyC4SPTRnS0sMlCQIQ_gA/zh-cn_image_0000002571387228.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=9214DBC7402B0A53A42952764AF83032277AFC8134F8C0A66406FEC16C8B114D "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/BVQiciGdTEy7ifLdc1Fr1g/zh-cn_image_0000002602186397.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=0E6E009AF67B72EE81FDCE8C98CFC2F2173EA7E477838E004E156A2A6EE50A46 "点击放大")

说明

* 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
* 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
* 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
* 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
* 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
* CPU分析支持能耗分析，请参见[能耗诊断：Energy分析](../能耗诊断：Energy分析/ide-profiler-energy.md)。

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/mBbEDf15TZmBgq0AK5sp6g/zh-cn_image_0000002571387224.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=95DB5D30103C3E5014A7BDAA877CA15FDE4CE98BA5D4518ED793CB7FD3C84F22)按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/-AqHOLoqSaaQBe93Rns_Uw/zh-cn_image_0000002571546864.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=348181ED47B021072F194FC8DEDF8A592304062329B30D675B342BCD330E41B6 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Fxe8N1BAS1qGP4BAhhE0GA/zh-cn_image_0000002571546860.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=135D8935D65D4287AC0587CF7BBCFBE7E928952F8796DBCB1C5DDC5562F4AABA "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  说明

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/zhuIRWfUSRO2js87iNhyLg/zh-cn_image_0000002571546858.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=E244BA0111EAAC96E90F2ED93F6A771E4785F49B05C99420E975B92C1D96ECD4 "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  说明

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/TEYgLVlETOulaCBvNyiv-g/zh-cn_image_0000002602186393.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=3675AE73CBFF3BDB9D3F2CA479A45B3121D15429D6925CA3712CDB69F8875796 "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  说明

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Usvx9VRPS1SULREAhTSFDg/zh-cn_image_0000002602186395.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=D2B20699BAD083DC29842F1BF2D7BF9F6CD384729B15B04E281B0F12EA05248C "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Z1W0CA6DSmqbV3g5ZF4t4A/zh-cn_image_0000002602186399.png?HW-CC-KV=V1&HW-CC-Date=20260611T073147Z&HW-CC-Expire=86400&HW-CC-Sign=312069158B4AEE7BC9B466AA76D9E81F785120CC5A3F28E4AB8B51BC46A6354D "点击放大")
