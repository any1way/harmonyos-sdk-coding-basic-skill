---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy
title: 能耗诊断：Energy分析
breadcrumb: 指南 > 优化应用性能 > 能耗诊断：Energy分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:43+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:bca2604f8025da8cab1864ed2bab2cd7d72b3ae874ebddfff322211cd4723aa5
---
从DevEco Studio 5.1.0 Release版本开始，DevEco Profiler提供Energy模板，帮助用户在应用运行过程中查看能耗信息，包括不同器件的能耗、整机温度以及能耗异常帧，从而方便用户对能耗问题进行调优。此外，Energy模板还集成了Frame、Time、CPU场景分析任务的功能，方便开发者在分析能耗问题的同时同步对比同一时段的其他资源占用情况。

说明

TV设备暂不支持使用Energy模板进行应用性能分析。

## 定位能耗问题

1. 创建Energy模板任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据。
2. 录制结束等待处理数据完成。默认包含Energy Anomaly、Temperature以及Energy三条能耗相关泳道：
   * Energy Anomaly泳道：展示能耗相关的异常帧信息。该泳道暂不支持在Wearable设备上进行应用性能分析；
   * Temperature泳道：展示整机的温度信息。该泳道暂不支持在2in1设备上进行应用性能分析；
   * Energy泳道：展示各器件的能耗信息及整机电流信息。
3. 点击Temperature泳道，鼠标悬浮于泳道上可以查看对应时间范围的温度以及温度等级，帮助用户明确温度是否有明显上升，从而进行进一步的能耗定位。观察下方Detail区域，可以看到所选范围内的平均温度、最大温度以及最小温度。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ev2g-jBsRgCRusljih4nOw/zh-cn_image_0000002602066115.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=2A12F0A69B4A770D4D144CF8D5ED94E3F70CF32BDCC5770EB019D5800CF5BCA4 "点击放大")
4. 点击Energy泳道，可在下方数据区查看录制范围内具体器件消耗的电量，器件包含：CPU、\*Display（屏幕显示耗电量）、GPU、Location（定位模块耗电量）、Camera（相机耗电量）、Bluetooth（蓝牙功能耗电量）、Flashlight（闪光灯功能耗电量）、Audio（声音模块耗电量）、Wifi（无线功能耗电量）、Modem（信号模块耗电量）。\*Device表示整机电流消耗情况。

   框选Energy泳道数据，Energy Detail中呈现框选时间段内的详情信息。根据不同器件的消耗可结合Callstack泳道的调用栈信息进行进一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ouiC0CnRRdCKlaStLe_imQ/zh-cn_image_0000002602066111.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=081927D48DDBD56B8B77E0E3131E5CAC3CD386DC508C0D11F5116E812455387A "点击放大")
5. 点击Energy Anomaly泳道，鼠标悬浮于泳道上，可以查看空跑的渲染帧数（RS Empty Run）、不能正常调用动态系统合成器（DSS）合成而直接使用GPU进行渲染导致能耗恶化的帧的次数（GPU Consumption）、UI空跑次数（UI Empty Run）以及CPU高负载异常次数（High CPU Load）。观察下方Details区域，可以看到所选范围内的能耗异常详情，包括能耗异常类型、开始时间、结束时间、能耗异常信息、能耗异常原因、能耗异常数量。

   说明

   * 从DevEco Studio 6.1.0 Beta1版本开始，支持查看能耗异常原因、能耗异常数量。
   * 2in1设备暂不支持查看RS Empty Run和GPU Consumption。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/8RlAqhRHTJCjBUyurdquzg/zh-cn_image_0000002571386996.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=06E2A919EADD5567C31638E257A5DA109D20A255E0ACA7E708BCDA32651F195D "点击放大")
6. 点击对应的异常类型数据（RS Empty Run、UI Empty Run和GPU Consumption），右侧More区域展示该异常帧信息，包括帧编号、RS VsyncId、帧持续时间。点击右侧跳转按钮可以跳转到Frame泳道中对应的具体帧，可以根据[查看指定Frame页面布局信息](../卡顿丢帧分析/Frame分析/ide-insight-session-frame.md#section58691959194312)详细查看页面组件的布局情况，以及识别存在能耗问题的组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/t9-SzNs_Qq2yWkzWoOf0OQ/zh-cn_image_0000002571386998.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=3E65CED4803B8085CD6FEE3E619DB189D8DAD44F24C582B3A3B52406A061A0AC "点击放大")
7. 点击CPU高负载异常数据，右侧More区域展示该异常帧信息，包括进程ID、线程ID、负载值。点击右侧跳转按钮可以跳转到对应线程调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/jLAsQPrsQMi-G6x2xx1pQg/zh-cn_image_0000002602066113.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=39C6F5F0A877B5EB6C0A1FD089A0DC8AA37E62DC26D54B08C2EE39B09ED50794 "点击放大")
