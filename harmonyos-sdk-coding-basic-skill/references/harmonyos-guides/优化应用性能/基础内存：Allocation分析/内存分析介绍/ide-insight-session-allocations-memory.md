---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:40+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:070612ae29617a67323785c22ca8e932e067a5b1555ca5070c3896c1b1922cca
---
应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

从DevEco Studio 6.1.0 Beta1版本开始，Allocation分析任务新增支持录制All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道，不支持录制Native Allocation泳道。

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](../../../构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/s4gyFsMwToOCKL4yDp4QqA/zh-cn_image_0000002602066191.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=2764C4AAE2AD45894FCED798C63E63EB1134F82D235DA5DC45C56B728E097A00)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/oLsGVxFaRcS8qeMQdpTWbA/zh-cn_image_0000002602186233.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=5D77393F3D27A3206EFC4784F2D7E02EB612C3E2C600DF7F0D7987390278F981)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/YEmnXp3ZRYSodu8IXY9TsA/zh-cn_image_0000002602066187.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=49C0C037CAF14ED775AFDF88E93909BAA383B3C18BBAF5515A2465DB62BDB871 "点击放大")

   说明

   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](../../基础耗时：Time分析/ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/NL1_Cl8LRiaZuQ1YR5dkFw/zh-cn_image_0000002602066171.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=0912DA162DCC67C795A9162BB9DC0AEBECC5FA231471C88391EEFA9CCA3596C5)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/UYwYXLoZSqK-zrGsY1uR0g/zh-cn_image_0000002571546666.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=F591EF3EF12A060F6C74ECCE36CF05267BF05539C4BA696CD7C0568B2514C405)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/9RmBSBIDTaG8xTgb_T2SwA/zh-cn_image_0000002571387018.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=0098A9BBC6060B0A6DD1D61D5A63EE72B69A898AF8E924A6E755046D225D7B7C "点击放大")

     | 子泳道 | 说明 |
     | --- | --- |
     | ArkTS Heap | ArkTS堆的内存占用。 |
     | Native Heap | Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。 |
     | GL | 包括应用和RS，应用为纹理内存，RS为纹理和图形渲染内存。 |
     | Graph | 该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator\_host申请的dma buffer。 |
     | Guard | 保护段所占内存。 |
     | AnonPage Other | 其他所有匿名页所占内存（非heap、anon:native\_heap、anon:ArkTS heap开头的匿名页）。 |
     | FilePage Other | 其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用。 |
     | Dev | 进程加载的以/dev开头的文件所占内存。 |
     | Stack | 栈内存。 |
     | .hap | 进程加载的.hap文件所占内存。 |
     | .so | 进程加载的.so动态库所占内存。 |
     | .ttf | 进程加载的.ttf字体文件所占内存。 |
   * **ArkTS Allocation泳道**：DevEco Studio 6.1.0 Release新增，用于显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/hRG_Po_zTQCnDt3tfRhydQ/zh-cn_image_0000002571387064.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=C089FF915C82FE18221C5AD18CB13E7D71BE7B9ACE28470627312EA577B161A0)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     说明

     + 该泳道即将下线，推荐使用[Snapshot模板](../../内存泄露：Snapshot分析/ide-insight-session-snapshot.md)分析ArkTS内存泄漏。
     + 由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：
       - ArkTS Snapshot泳道
       - All Heap & Anonymous VM泳道
       - All Heap泳道
       - All Anonymous VM泳道
       - System Resources泳道
       - Graphic Memory泳道
   * **ArkTS Snapshot泳道**：DevEco Studio 6.1.0 Release版本新增，用于抓取ArkTS堆内存快照，结束录制时会自动录制一次快照，默认不支持录制该泳道。如需录制，在录制前单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/42H6LslVTa-EZ2eDirILeA/zh-cn_image_0000002571546678.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=D33E02E48509274BFB5388AB34C37AF83FEEA74FFF56256067C36687669BFAE2)按钮关闭统计模式（Statistics Mode）。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/bxQ9-UiUSvWDdYd92dpv3w/zh-cn_image_0000002602066161.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=75EFA7DE5BA8E2A6C7E25225488F845CE0FCB5AA698A90A8FC5E5D9DF58DB400 "点击放大")
   * **All Heap & Anonymous VM泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Z5_QIDdVQOmMq3PBdJXI0A/zh-cn_image_0000002602186225.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=223DC4636933BA11B1D34C5E1E16B4FB48FAA43C12B18CFF10988344781AAB87)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、内存数据采样大小、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/wCK3hhI1SFyuor18PXRIJQ/zh-cn_image_0000002603025925.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=2329423F73B57B8369E0CE2699B5D850AF2DEDD25C15C7460EA477B45F6BE54D "点击放大")

     | 配置项 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | All Heap & Anonymous VM Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。  可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Sampling Size | DevEco Studio 6.1.1 Release版本新增。  内存数据采样大小，可配置范围为1-1048576Bytes，默认为4096Bytes。  配置后，仅对Native Heap和All Anonymous VM泳道中的mmap类型数据生效。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。  在DevEco Studio 6.1.0 Beta2之前版本，默认关闭。  从DevEco Studio 6.1.0 Beta2版本开始，默认开启。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Stack | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |
     | Sync Backtrace Depth | DevEco Studio 6.1.1 Beta1版本新增。  同步回栈深度。仅当Record Async Stack开启的情况下存在，其层数代表着JS与Native的共同同步回栈深度。可配置范围为5-100，默认20层。 |
     | Record Async Stack | DevEco Studio 6.1.1 Beta1版本新增。  用于开启[异步栈缝合](<../../附录/DevEco Profiler术语/ide-devecostudio-glossary.md#section58492173810>)。仅当Backtrace Mode选择为FP模式的情况下可以开启。开启后，在异步回栈时支持多回一层异步栈帧，最大异步回栈深度为16层，且暂不支持设置异步回栈深度。默认关闭。 |
     | Record Data Range Options | DevEco Studio 6.1.0 Release版本新增。  用于设置采样数据范围，包含Malloc、Local Handle和Global Handle，默认勾选Malloc。。  + Malloc记录malloc系列函数的内存分配。 + Local Handle用于管理JS对象生命周期的引用句柄（napi\_value），仅支持Phone和PC设备。 + Global Handle允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。 |

     说明

     + 若勾选Local Handle，在应用生命周期内首次录制时会重启应用。若应用在生命周期内被强制终止后重启，再次录制时仍会重启应用。
     + 最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。
     + 最小跟踪内存设置的数值大小不影响Local Handle和Global Handle。
     + 统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。
   * **All Heap泳道**：显示Heap类型数据之和。展开主泳道，包括Native Heap、ArkTS Heap、JS Heap子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Native Heap子泳道：用于显示Malloc、ArkLocalHandle和ArkGlobalHandle内存分配。
     + ArkTS Heap子泳道：用于显示ArkTS对象内存分配。
     + JS Heap子泳道：用于显示JS对象内存分配。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/IdSTP4ZGRoa3WZKkWrnrCQ/zh-cn_image_0000002602479847.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=2ACD60B459580826FE48843C9B7473DB6571818C406842C949765E2A1C9BD13D)
   * **All Anonymous VM泳道**：显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + VM:ION子泳道：用于显示DMA内存分配数据。
     + VM:ASHMem子泳道：用于显示匿名共享内存。
     + VM:.so子泳道：用于显示.so文件内存消耗。
     + VM:others子泳道：用于显示除ION、ASHMem、**.**so外的mmap类型数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/k2yOaWQRSpGi3Z8Ml2FanA/zh-cn_image_0000002602186215.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=213BAFA51554B9FDE79F06E09595F27E57E879960AA08DE6AB1C96377225791A "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + File Descriptors子泳道：用于显示进程的文件句柄使用情况。
     + Threads子泳道：用于显示进程的线程使用情况。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/coLm7LyjR-y83FoflgFpkQ/zh-cn_image_0000002602186185.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=FB08E33B3A541DFBFE0599B358F2E3BC8D8FA1214841F1EB2C44CCD4B3E3CD20 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ljjxtUdmRVWDAlfA9Md3Ug/zh-cn_image_0000002602186223.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=AAC3B73E19CD4D04778225CB2C32279D7B77756BB4BE1AEF511F6BA59E425CE1)图标，勾选Graphic Memory泳道。展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Vulkan子泳道：用于显示GPU\_VK类型的内存分配数据。
     + OpenGL ES子泳道：用于显示GPU\_GLES类型的内存分配数据。
     + OpenCL子泳道：用于显示GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/kQTwRfTpQZG_UkhVPCd5OA/zh-cn_image_0000002602066195.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=05BE748AC5037DF3FD778D955A7A55D45A4524BCD548B1EAEF86464FC3E5B3BF "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，查看此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + Details页签中显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。包括时间戳、PSS内存大小、共享脏内存大小、共享干净内存大小、私有脏内存大小、私有干净内存大小、Swap内存大小、Swap PSS内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/nUd6FtwlQdqzWfVRFU0WAQ/zh-cn_image_0000002602399527.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=925FF3E82A184287AF18223E994EA337BEC7A74E4E05C27A5BA7782A50871E85)
     + 子泳道的Details页签中显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/O6XyjmzXSDynrup9x8KJjg/zh-cn_image_0000002602066159.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=E97CC03B14C5CD82145836257F41BB902313B5D1FE8A957A99C4DFAE2D316DD7 "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/RoY8yVLAR9-2rRrjtDxqHA/zh-cn_image_0000002571387056.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=7025CE1CA74AADF493B401E33345B57A0C4A79F04275AEB147B191D717C030F0)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/jDOHFeNLRbqEN19tbo1bOg/zh-cn_image_0000002602186241.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=C86BBF6CC7BFFA9C91A5BC9257D608BF813C2E1BE391B7544A644987EF0BF253 "点击放大")
   * **ArkTS Snapshot泳道**：泳道的紫色区块表示一次快照完成。在“Statistics”页签中点击任一对象后，右侧More区域“Native List”页签将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/xGQh270rSAqGk-guzqQGZg/zh-cn_image_0000002602186213.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=3C1559704E1D9A1D04897E412FE4D37E54F86AF1704E4EB0061EACDC1FE72DC6 "点击放大")
   * **All Heap & Anonymous VM或All Heap或All Anonymous VM或System Resources或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       在System Resources泳道的Statistics页签中不提供内存大小数据。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。

       在System Resources泳道的Call Trees页签中不提供分配大小数据。

       当未开启统计模式，以及录制了ArkTS Snapshot泳道时，框选All Heap & Anonymous VM或All Heap或Native Heap子泳道，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。否则，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0WvvAF0YRz-KNOajcKIFxg/zh-cn_image_0000002571546702.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=C0678DA4F055A269E884DA7308828CD13CFE69E4DF148C9E910A6458102E9836 "点击放大")

       点击“ArkTS Object List”列表中的跳转按钮，跳转到ArkTS Snapshot泳道中的目标对象节点。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/iBJqPJyARx-GvRkDwzYQcw/zh-cn_image_0000002602186183.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=964C59E8F181D9B1766E2D3483941B59C07714DC4DB8CF524EB750A54DDC19A6 "点击放大")
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。在System Resources泳道的Allocations List页签中不提供内存块起始地址和大小。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/3uKqHE5MSGmrz96GAJigoA/zh-cn_image_0000002571387034.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=FD752210A73B7ECB16DDBE302F15D75887B041277F32D895EDFF592E707CD297 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](../../../构建应用/配置文件/模块级build-profile.json5文件/ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FN61LYQVSnKQNaKFgSHMJw/zh-cn_image_0000002571546694.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=64360EE7F2EB1D976485ECD86F623B0D1D6A1ABDB4CB74229EAF006F60F25733)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/RqazYnK8Rvmy7LqcMZ9jKw/zh-cn_image_0000002571546688.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=68D0EF3B355ED90639C9415E0604010871640692076F76DCD54A5AD312C07091)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/rxjMhmG7TK2vjGa5g_6Lgw/zh-cn_image_0000002571546650.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=0FA1FA27C3B3FF093A640DD4097DE532B2739EDCAF2E215FE85B208E1FDA78A0 "点击放大")

   说明

   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](../../基础耗时：Time分析/ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/7e5bkK8TRnWJGfBOt4Fzqg/zh-cn_image_0000002571546716.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=A2CB787B3705C09BC7F410BDD2F3566CA873486CE8BDEB3F9CB61B90A535B808)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Q34p0jXDSM6P71s2ojIF4A/zh-cn_image_0000002571546686.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=9198A9410607EE4D58FD1AC9F5E622CC8D427007B000BBB8A33831C965A0C214) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/GS6V5D_MQRyd-2o3X6Z0-Q/zh-cn_image_0000002571387074.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=3693A7A98C7501B2834945F7502D166A0A3688FDDBE87BA347A8B62B8D25B7A2) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/p_wxVY_MQEWukl8MfbEKwQ/zh-cn_image_0000002571387028.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=234B0F253CDF2726B1CA74DB586ADD8624F3AEF6D223AA3E935912AA6A3BF374) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Hnaxv0rbR7ijM01GP4W99Q/zh-cn_image_0000002602066147.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=52359F08FE3A40D86245C280EAF8923F93A2EE9B0B8F6CFAD924BB336C30ACAF)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/qp50iM4ITWG-NILlyklWew/zh-cn_image_0000002571546690.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=ED03980C465142DDC9E833F1F308F8EE5D5A3AD09F7D597B7F427EFE4A8ED6E6 "点击放大")

     | 子泳道 | 说明 |
     | --- | --- |
     | ArkTS Heap | ArkTS堆的内存占用。 |
     | Native Heap | Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。 |
     | GL | 包括应用和RS，应用为纹理内存，RS为纹理和图形渲染内存。 |
     | Graph | 该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator\_host申请的dma buffer。 |
     | Guard | 保护段所占内存。 |
     | AnonPage Other | 其他所有匿名页所占内存（非heap、anon:native\_heap、anon:ArkTS heap开头的匿名页）。 |
     | FilePage Other | 其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用。 |
     | Dev | 进程加载的以/dev开头的文件所占内存。 |
     | Stack | 栈内存。 |
     | .hap | 进程加载的.hap文件所占内存。 |
     | .so | 进程加载的.so动态库所占内存。 |
     | .ttf | 进程加载的.ttf字体文件所占内存。 |
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/BMTxmXchQXmYySS9KBdk8w/zh-cn_image_0000002602066137.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=8A1D41595F3640B53389CE126D22AB21D6D7C64A938BA04B598F4DB8E871C242)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     说明

     由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：

     + All Heap & Anonymous VM泳道
     + All Heap泳道
     + All Anonymous VM泳道
     + System Resources泳道
     + Graphic Memory泳道
   * **All Heap & Anonymous VM泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/N9ayV8bmThiBqeanYkMRyw/zh-cn_image_0000002571387038.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=843C4B08C974EC99956BFDD3D49E081436D8B21CC937C9F159408097A5E33EDA)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/6ANIdkjqSuOuH89WioziQw/zh-cn_image_0000002602186197.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=D3D6C885087172F985284A180D059D87C3CB05B63CE699F8EAE376FF2FF66529 "点击放大")

     | 配置项 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | All Heap & Anonymous VM Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Stack | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |

     说明

     + 最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。
     + 统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。
   * **All Heap泳道**：显示Heap类型数据之和。展开主泳道，包括Native Heap、ArkTS Heap、JS Heap三条子泳道。其中Native Heap子泳道显示Malloc、ArkLocalHandle和ArkGlobalHandle内存分配，ArkTS Heap子泳道显示ArkTS对象内存分配，JS Heap子泳道显示JS对象内存分配。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/kYxCdK6-TdOg3d90CkqPnQ/zh-cn_image_0000002602066185.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=9317AE6184BF6A7DEDF4502E7425737DFFBB790C495E1D59E5CC66D6D21F7CBE "点击放大")
   * **All Anonymous VM泳道**：显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。VM:ION子泳道显示DMA内存分配数据，VM:ASHMem子泳道显示匿名共享内存，VM:.so子泳道显示.so文件内存消耗，VM:others子泳道显示除ION、ASHMem、**.**so外的mmap类型数据。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/1fRoP-bXSuCx1bHiko-AEA/zh-cn_image_0000002571387080.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=ADFAEFDF8A176FDE0009C4B8B474A18E0AE75804F981A8706F31B88992C8A4AD "点击放大")
   * **System Resources泳道**：显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。File Descriptors子泳道显示进程的文件句柄使用情况，Threads子泳道显示进程的线程使用情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/3Dg2vr-uRdCH1Kmjorz1MQ/zh-cn_image_0000002602066155.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=60A129C372310C5F3EECACBB903D1DB84694657FB277C343A250B0E1CCE19F2E "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1新增，用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/aLWFQ_CSQxmYni8LlMmSzA/zh-cn_image_0000002602066135.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=6EDF9D6F3623373DBD80F2D114558FA6C00EF2C78846D55E2D455CE417EFB4F2)图标，勾选Graphic Memory泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/PflFXeOTQEOQYHZqdUN1zA/zh-cn_image_0000002602186237.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=39E6B0AD36E1EC16D2754FA95BACDA620AB9FBED85E741218D89F6BCCEE91E33 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道：**
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/plvE6GSVSgqS5DJUmPJnSw/zh-cn_image_0000002602066193.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=1260AB1191D302E3B6CF82EB417E31754A746BAF1976DE5AD93FB83927BA26B8 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/JcHf8AYBRiCej1TXNTMh5g/zh-cn_image_0000002571387036.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=C91FC386A39E16DC9A578DCCFDBBCB43E1813E8D6C07097A292A52B9C883A10E "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/woC5MxYQRvWy-F6H3GnbGw/zh-cn_image_0000002602186203.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=0403A6004939171287ABFD5F554371210A4E7B7524EF88C176DDA6A3EC1FC7FF)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/sRBYMqOsRLKEUc5onW4tvQ/zh-cn_image_0000002602066177.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=16B821EDB01661F671B0ECD2E8460D92FDA1138BE27391AF84463E2BC7C1D146 "点击放大")
   * **All Heap & Anonymous VM或All Heap或All Anonymous VM或System Resources或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       在System Resources泳道的Statistics页签中不提供内存大小数据。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。

       在System Resources泳道的Call Trees页签中不提供分配大小数据。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。在System Resources泳道的Allocations List页签中不提供内存块起始地址和大小。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/07gSux4tQ-auHn9fT0oRTg/zh-cn_image_0000002602066175.png?HW-CC-KV=V1&HW-CC-Date=20260611T073139Z&HW-CC-Expire=86400&HW-CC-Sign=DC72505B50E7646770B839FE661745C01AE056ACF380930CA35F556FFBDD6CCB "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。
