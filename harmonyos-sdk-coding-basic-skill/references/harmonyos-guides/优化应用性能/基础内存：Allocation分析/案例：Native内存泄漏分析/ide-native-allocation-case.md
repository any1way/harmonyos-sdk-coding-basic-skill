---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:41+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:2ea427013d999a417bc5ae734f4bd708716e11250c6f978058d26c2bdb738a84
---
本案例介绍如何判断应用存在Native内存泄漏。

[6.1.0(23) Beta1](<../../../../harmonyos-releases/HarmonyOS 6.1.0(23)/版本概览/overview-610.md#section174491130173414>)以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

[6.1.0(23) Beta1](<../../../../harmonyos-releases/HarmonyOS 6.1.0(23)/版本概览/overview-610.md#section174491130173414>)及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](../../使用Profiler进行性能调优/性能问题定界：实时监控/realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/iuJkgtz6S7GfYMBRCV_HAA/zh-cn_image_0000002602185993.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=56C6E423A8F6FD5EFFEE03F59AD01C224127617979345096E0242776A005FC19 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   说明

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/tn1SXOHeQuCPp5fGJVJnnQ/zh-cn_image_0000002602185999.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=E47FFD2629F71B0ABACA271D78A8BC96240C7E8C05C7CC6E00C6832A4C35ABE8)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/e-UKhTgnRxaEhpgjlggOqQ/zh-cn_image_0000002602065945.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=28FD713B48553C1C73A0484B2D5A0A29379D963B0134D7DEEC40695B8818C2F6)即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/TlGEb9U7Q4iTQmMNmstrEA/zh-cn_image_0000002571386828.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=2D941558FA0640B514F9152539AA7888E64B3329DFDFEBB931ADD091139053E0 "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/XRjTvD8DQJ6VgN67bvJ3RQ/zh-cn_image_0000002571386832.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=B111F5AB63E4B841699BD393F3717AA9FCE6F10C44DA267C378FE61B959D26BE "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3CdRPTjQQZmhsSKpTYxUkw/zh-cn_image_0000002571546458.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=1E95CF164586D97CCC9CAF5AE7E54ACFB73DBC791EEF2490DCFB7D5EE560C64D)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/GkaoHPg5TiiV_Lo9jiDKSw/zh-cn_image_0000002602065935.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=18E3F594ABF9625CD4710C362D60E792A0C9B3C302E462F0148BF13D8C28718F "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/sibFatLxT5ywnAP7z4dA2w/zh-cn_image_0000002571546466.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=460EDD9CAF14E696A1C8C6B43400EEB500E9AF47555B57CCD890D832EE73ABAF "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/_ryzSCxfQZy9Yuso1XMdYw/zh-cn_image_0000002602185989.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=A2376271EF0744DE5D98B9F9510F7D1B11E181518F59479DD8ADF8BF31B37677 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/OZQlKcKLThGOEEv84O12BQ/zh-cn_image_0000002602185995.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=8DA1F7A21AC660D413AEFCC3DAB26808B30D2F41864D5776ABD26A6ABE86CDCB "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考[离线符号解析](<../../DevEco Profiler调优工具简介/数据区/ide-profiler-data.md#zh-cn_topic_0000001710155373_section11376118192614>)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/yfMTCazLS8CrwxwaXMJdVA/zh-cn_image_0000002571386822.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=3F4531A67505F8842DD31E30C1A2937DF9D99F36EE250144AA0AD04AED136E2B)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/X9TH2FQnSiiYOTzfbMaBmQ/zh-cn_image_0000002602065937.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=3FD549401B9173B563AC2A287DD43892FD5944F99BC630B0AA82DBDACEF25FCC "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/-clvfD5ZSVCsKP-rDKDSxw/zh-cn_image_0000002571386820.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=7F19F29AB45635B193CF779240880971B96B9F2C7FFAC4872DA3DF2C1B3E9FD8 "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Ju_GBNmlTiu9rjumav4kbA/zh-cn_image_0000002571546464.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=9DF1423DEE0E07C3ED9D201142BBBFB024363DBA39DD06D344D22DFC040A99B4 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Yd33YR3SS3qHRdg56S9fzA/zh-cn_image_0000002602065939.png?HW-CC-KV=V1&HW-CC-Date=20260611T073141Z&HW-CC-Expire=86400&HW-CC-Sign=3B521C8995FE4FCDAB01F98EBDD45FC6ACB2190FCAC03A28214FBFD7EF41BE0E "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](<../../DevEco Profiler调优工具简介/数据区/ide-profiler-data.md#zh-cn_topic_0000001710155373_section11376118192614>)）。
