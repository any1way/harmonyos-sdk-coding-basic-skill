---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:27+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:58fc02831627f47024d2c07072871fd196231ab368fd2d1865edbbcc13a396e5
---

开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景：

* Frame：主要用于深度分析应用/元服务的卡顿丢帧原因。
* Launch：主要用于分析应用/元服务的启动耗时，分析启动周期各阶段的耗时情况、核心线程的运行情况等，协助开发者识别启动瓶颈。
* Snapshot：支持多次拍摄ArkTS堆内存快照，分析单个内存快照或多个内存快照之间的差异，定位ArkTS的内存问题。
* Allocation：主要用于应用/元服务内存资源占用情况的分析，可深度采集内存相关数据，直观呈现不同分类的内存趋势，提供内存实例分配的调用栈记录，深入分析内存问题。
* ArkUI：主要用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。
* ComMemory：主要用于定位UI组件内存占用情况。
* Energy：主要用于应用/元服务的能耗异常分析。
* ArkWeb：主要用于定位web应用加载和丢帧问题。
* Network: 主要用于定位http协议栈网络信息诊断，用于网络请求分段耗时分析。
* Concurrency：主要用于显示并行并发应用的实际运行情况，用于帮助优化并行并发代码。
* GPU：主要识别GPU利用率低以及执行图形和计算工作负载性能瓶颈的根本原因。
* Time：主要用于改进函数执行效率的分析，深度录制函数调用栈及每帧耗时等相关运行数据，并完整展现ArkTS到Native的跨语言调用栈，支撑Native API典型问题分析。
* CPU：通过深度采集CPU内核相关数据，直观地呈现出当前选择调优应用/元服务进程的CPU使用率、CPU各核心时间片调度信息、CPU各核心频率信息、CPU各核心使用率信息、系统各进程的CPU使用情况、线程状态及Trace信息等。

1. 选择场景模板，创建会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/an4K7YeUTMWKKxEPhUCnSA/zh-cn_image_0000002602066095.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=7BF22D524D082FC6A4998AD1D5952305C2F675C1681BDCDF2974DD7057AD7935)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/l7t5nE_PQHW8AqZRyXw_QA/zh-cn_image_0000002602066089.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=399B2D10B575B876BC4B1684927271F48B737AB8A5F05E077584F2A5689A6303)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/8uHl5HKNQNmhY0FFzuyOpA/zh-cn_image_0000002571386974.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=37D6AC23B168174030675D9F8645522C9289358F19E5146D27FFD7A23E47EC5A)：在DevEco Profiler主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。创建后的分析任务，将显示在界面左侧的任务列表中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/07K_2k8SQKqHZwJrRhJITg/zh-cn_image_0000002602186147.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=8A1E88EFAE5E1764960B316A3F3F1D693261A128645FBCA1D3DB0BFD7DECFD0B "点击放大")
2. 配置并确认会话环境。在录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/JaozzkpRScSXgQtjI8Bh-Q/zh-cn_image_0000002571546612.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=9B4A9C8CEB88750411DAD73D8DED9CBF7E1862639D2554D019F28C4A668F20B7)
3. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/mTTbWvl9RfKtd0cWDQGtfw/zh-cn_image_0000002571386978.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=295C0A380FF21CE37DC0923CE36EE1F49CCBB592BAC79CF08E63318D8B9CDC06)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/tkoKMJK1SViUY7Kl2XJTgw/zh-cn_image_0000002571386972.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=C202EC23237C860CD27231DD8202BC2123752D188CC81B874D3D6CBB669532BB)，启动录制。在调优设备操作APP，执行要验证的操作，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/31NWZNacT3GC0WS4rbF0wA/zh-cn_image_0000002571546608.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=CC023F7CEB4B7AF385CC706218E27CACD1103C2CD1CD9E5394BE2BEB6FE6E99A "点击放大")
4. 性能劣化场景完成，停止录制。

   单击停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/PrjUY1D-REeB85kbd5LSCQ/zh-cn_image_0000002571386980.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=5B8364E1A020BD559DE3DE4B19837A01960D452B94E044842B3B8FAA8C4CBED1)，进入数据解析阶段，泳道任务状态由“analyzing”变为“rendering”时解析结束，右侧调优详情区域显示具体调优内容。解析过程可能包含大量的数据，请耐心等待解析完成。

   说明

   若录制结束后，ArkTS Callstack/Callstack/Native Allocation/ArkTS Allocation泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/RgiSxjZOTGWJPedHtD9eYw/zh-cn_image_0000002571546618.png?HW-CC-KV=V1&HW-CC-Date=20260611T073126Z&HW-CC-Expire=86400&HW-CC-Sign=0ED26E370D6A96769CA540C7161D9D16DBD7940F9B70CC619821207AA45CCCE3)
