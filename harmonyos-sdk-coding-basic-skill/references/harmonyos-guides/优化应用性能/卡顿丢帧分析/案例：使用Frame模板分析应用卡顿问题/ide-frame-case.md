---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-frame-case
title: 案例：使用Frame模板分析应用卡顿问题
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > 案例：使用Frame模板分析应用卡顿问题
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:31+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:b7fb394efbe44b560a8f3b229bab1f77ffa00c0fe6eac2d0f84130ec7a1e9b8c
---
本案例介绍如何判断应用存在卡顿帧，再通过调用栈和trace信息分析应用运行逻辑，找出应用卡顿的原因。

应用卡顿分析基础功能请参考[Frame分析](../Frame分析/ide-insight-session-frame.md)。

## 分析步骤

分析应用卡顿类问题步骤如下：

1. 确认是否存在卡顿帧。
2. 若存在卡顿帧，根据调用栈和trace等信息进一步确定问题点。

## 分析Frame数据

### 分析应用是否存在卡顿

1. 框选Frame泳道，窗口下方的“Statistics”区域中会以进程维度对选定时间段内的Frame信息进行统计，当Jank Count大于0时，说明存在卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/P0rC-yzwR7qo_Mv2j35Xxw/zh-cn_image_0000002602066519.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=1627A79777FECE0603CEA455F9B6C8F1C6E0ACA6F8CE4A98EC45628EA6E16671 "点击放大")
2. 找到“Statistics”页签中存在卡顿帧的进程，点击进程名称后方跳转按钮，跳转到“Frame List”页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/UhurYM0bQiimiBQtpsshsg/zh-cn_image_0000002571547044.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=98B809CDE581B22939BC70C94ABE6E51295C9F692FCD6BAF2B147C0C0FDC6164 "点击放大")
3. “Frame List”页签会展现该进程对应的Frame列表。在“Frame List”页签中对卡顿丢帧类型（Jank Type）进行升序排序，单击“Frame List”页签中任意一卡顿帧，直接跳转到该帧且泳道上该帧被反选。

   说明

   * 在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * AppDeadlineMissed：App侧的卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/UK30ZstMT62G35x995aCgQ/zh-cn_image_0000002571547042.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=E9DD82F22E56B571646FEC02E53B2E2EA55A670D86AA787A874009544B7E2B93 "点击放大")
4. 点选该卡顿帧，窗口下方的“Details”区域中显示卡顿帧的关键信息。右侧应用进程前方跳转按钮可以跳转到应用进程Trace。
   * Expected Duration：一帧绘制的期望耗时。与fps的大小有关，如fps为120，对应的Vsync周期为8.3ms，即App侧/Render Service侧的帧耗时，一般需要在8.3ms以内。
   * Actual Duration：一帧绘制的实际耗时。

   如下图，可以看到该帧的期望耗时为8ms 330μs，实际耗时为44ms54μs，远远超过了期望耗时，因此被识别为卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/7b9EA8NcSyW5_nxDvIYk0A/zh-cn_image_0000002571547048.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=E3E89A8AFE8347C4C7118420064084ACDB4D372DA17500583EC57806B07B7B7F "点击放大")
5. 框选该异常帧时间范围，结合ArkTS Callstack泳道、Callstack泳道和Trace等信息进一步分析异常点。

### 案例：分析应用卡顿原因

1. 找到并框选要分析的异常帧，查看ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看主线程调用栈，即线程号与进程号一致的ArkVM子泳道。可以看到ArkTS侧一些方法的耗时。
2. 查看下图调用栈，除(program)外，其他调用栈耗时小于一帧绘制的期望耗时8.3ms（被调优的设备fps为120），因此该卡顿帧主要分析调用栈(program)的耗时。

   (program)代表程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或者Native调用ArkTS情况，一般很难通过这里分析出有效的信息，需要切换到Callstack泳道看具体的调用栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/aqaXMvFjQAGi9RJX6SnEhw/zh-cn_image_0000002602186577.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=64112F474DBDAB8D49212465A92054AFCAC63D975FF6E13F0E77416092E11B7A "点击放大")
3. 切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，滑动观察下方Heaviest Stack区域“%”列中占比最大的函数调用栈，Category中亮色代表开发者调用栈，灰色代表系统调用栈，可以看出下图中耗时主要在系统侧的so，无法识别具体异常原因，接下来进一步分析应用进程Trace。

   说明

   也可通过底部的“Call Trees”选择框来隐藏系统调用栈，减少干扰信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/CV5pWi_oTv2n4z4mRKeTdw/zh-cn_image_0000002602066525.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=AFFED908FC460C0EDBF04D6D38772F8F4B2A6FA430057B303D68B98EEB67134A "点击放大")
4. 切换到应用进程Process泳道，查看主线程（线程号与进程号一致）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/mEs7V1rtRpmisONq_tUZfg/zh-cn_image_0000002602066529.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=44CCF159CCDB799F49B3020AD0551C2F8F8471923EC1B34664A7EF5AB055D839 "点击放大")
5. 窗口下方详情区可查看到Trace统计信息列表，逐层展开耗时最长的Trace，定位到主要耗时是在3次H:CreateImagePixelMap。接下来进一步分析这3次H:CreateImagePixelMap耗时的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/h2sGirl2TnaFkSw6yeMZww/zh-cn_image_0000002602186585.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=58056C0C7DEE262D8A7808DAE03A6D5560709BCEAF5947AB406A706AA1DC39D6 "点击放大")
6. H:CreateImagePixelMap和图片加载相关，再结合业务代码查看，可以看到是因为同步加载网络图片，建议修改为异步加载。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/qS5gSQh0RtKa9EQV03SgzQ/zh-cn_image_0000002571387416.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=FECC9037649B4DE9DC5333EEF78222792A32A70D579DF84E835F441849E71815 "点击放大")

   说明

   一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。不建议图片加载较长时间时使用同步加载。
