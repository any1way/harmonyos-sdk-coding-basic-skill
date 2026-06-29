---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations
title: Snapshot模板基本操作
breadcrumb: 指南 > 优化应用性能 > 内存泄露：Snapshot分析 > Snapshot模板基本操作
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:36+08:00
doc_updated_at: 2026-05-21
content_hash: sha256:7f973820c536120d596ffb5ca0d5bcff28cc023170aa8e52f5aac021238c8dbb
---
## 功能介绍

针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

在DevEco Studio 6.0.2及之前版本，Memory泳道统计时支持选择PSS/RSS/USS中的一个或多个，可以从多维度度量当前进程的物理内存使用情况。从DevEco Studio 6.1.0 Beta1开始，Memory泳道统计时固定为PSS、GL、Graph总和，在会话区不支持选择PSS/GL/Graph。

### 约束与限制

由于隐私安全政策，已上架应用市场的应用不支持使用Snapshot分析模板。

## 查看快照详情

1. 创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)。
2. 设置Snapshot泳道。单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/IbRqxxj9QeyR0pTBIr9B-g/zh-cn_image_0000002602066447.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=E19C38BC4BBA0EFA9E7BB6DDCD3BDCA709285C41EE3EDAC40F9BA7DB1F0A0618)筛选泳道，再次单击此按钮可关闭设置并生效。
3. 单击ArkTS Snapshot泳道的“options”下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/r-axySWWSd-uztwYsFQWxQ/zh-cn_image_0000002602066435.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=04E47007BF4BDFC566E16EE6D47F3850579084FF4C31AA0F2D32927C46627017)
4. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/zWo06fZpT1eJBvlK5fcr6w/zh-cn_image_0000002602066451.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=8168A024D9FDC5F9E5258CF872B48AA2992663D0EE102AABFB88A867A5D3E8AA)启动一次快照。

   “ArkTS Snapshot”泳道的紫色区块表示一次快照完成。

   说明

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/fem8aXjKSS63xUpMu-5oSQ/zh-cn_image_0000002602186499.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=F27BFC345A5FC3961AEFDCAF6B6755F2F817AA1B951A4FC284B8B066545A3643)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Gkz4c7D5Tre617E3EzG10w/zh-cn_image_0000002602186471.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=EEBB1F671E81D09FDB7EA33DD2FBAC5655EE2799D3911F5DD97071E18FCF3145 "点击放大")

   在“Statistics”页签中显示当前快照的详细信息：

   * Constructor：构造器。
   * Count：该对象的数量。
   * Distance：从GC Root到这个对象的距离。
   * Shallow Size：该对象的实际大小。
   * Retained Size：当前对象释放时，总共可以释放的内存大小。
   * Native Size：该对象所引用的Native内存大小。
   * Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
   * 带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/0Anl7I-vSy6DxXHJ03hUSw/zh-cn_image_0000002602186481.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=249DFCB170AE488C00BB354812F4797E15B44AFC9715D9FD26E99327CDD8283B)标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/O7lvdUM-TAW0Z3OEP5Q4QQ/zh-cn_image_0000002602186491.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=11133C26B8992E0AF9D300FCAE7467581AE4962EFFA2A088890A12B99B12B0A7 "点击放大")

## 应用对象名称解析

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始，支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

1. 系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以\_GLOBAL开头。
2. 方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：

   ```
   1. com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)[MainModule] //格式为BundleName/SelfModule@Version/FilePath/File#Class(line: xx)[RefModule]
   ```
3. 其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

* Module：模块信息。
* Class：属性名称。
* Path：编译后的源码路径。支持通过点击属性名称旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/KIkpc0_JS9SB7ZJJGaqrNg/zh-cn_image_0000002571546932.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=7884371DFEF81F7B205DA2D8D30BB1A33DB912F4AEA4C1971E68DCA550E94037)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/L5w_Z9xYSqWTDx72ozaaBA/zh-cn_image_0000002602066413.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=D2A77F2333F5F97E736CC81FBB8B25B60FE3D18BCA108264957DDE09AE6EB73F "点击放大")

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/JNl_6e7vT9SgBHDWlazwXA/zh-cn_image_0000002571387300.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=ECC5091A3E051C352E901D87996C55D95E1BF1C985CC19DF121B2A8082AEFF3B "点击放大")

说明

* 确保工程代码路径与解析信息匹配，否则跳转可能失败。
* 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
* 对象名称后的line=0时表示无效行号，不支持跳转。

## 节点属性与引用链

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/uHycOS5fTjWBD8BstEACTQ/zh-cn_image_0000002571387316.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=67885C833C41E87A270FD6E70E88AC75E372479756462577E43A994E4A1F8B95 "点击放大")

## 节点跳转

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/4EtA_YnkR5GzvFQygj6cXA/zh-cn_image_0000002602186477.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=44649E7595C67FD888CF5F4413C8B083D00E1B9951FBD945E8FD59DF44D08A95 "点击放大")

## 历史节点前进/后退

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/hgh_j4IESlW7ri_uzQupaw/zh-cn_image_0000002602186473.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=9803C755F8C4B10D212F2EFAB9B840E92CC483FC306C5D49674E265F0355DBEF "点击放大")

## 比较快照差异

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/h1Cxng3dRz2CARD6yhft1Q/zh-cn_image_0000002602186469.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=FB47B02AC9C567E415A0FAF274583F2A2001656FE2A26131F70D96A8C8C87C18 "点击放大")

在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/kCI3cK9KS6OmGgQuHaLrog/zh-cn_image_0000002571387322.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=AA45386AF5E03E6422A2205BD7481C4C885EEC32E4994C37BEA0487C0067A727 "点击放大")

## 引用链向最小引用距离展开

Snapshot分析支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

### DevEco Studio 6.1.0 Beta2及之后版本

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/K_b6QwuvTL-KwN47wVbbsA/zh-cn_image_0000002602186503.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=B8481853AEA0ECB9B2DEF99C1D9B4FCE3DE97C0E01B4A32D0055D218C1C809CB "点击放大")

### DevEco Studio 6.1.0 Beta2之前版本

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_SXggBTtQXuaPYJVccQ3aw/zh-cn_image_0000002571387304.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=621CAAA08AD2F45600B2F943191573856557826E94BF418522A2D1120324C1F4 "点击放大")

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/2qVNML5bTdmVYJTQfjvU_g/zh-cn_image_0000002602066417.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=AF9064FCC0F5C758E2D3141E0FFB1E016EA6FF52D1F3DB310CEAAEAFD7D97588 "点击放大")

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/iAGPQ1TaSwiqlc2HTLPZyA/zh-cn_image_0000002602186485.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=E1F334348E72A6FE56C0958163DE8A8DC53FC5495EA7452ABB60BBBF6CF46981 "点击放大")

## 合并展示最小引用距离

从DevEco Studio 6.1.1 Beta1版本开始，在“Statistics”页签中，选中一个构造器或实例结点，点击底部搜索栏的**References**按钮并确认，在右侧**Merged Incoming References**页签可查看该节点构造器下的所有实例到GC Roots的最短路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/PsARqF3yS6iezJDNEkPc1w/zh-cn_image_0000002602186479.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=7D350848AAEA709C66B09B8EEBCE936422A5EB3EB5ACB5BA8662369BB85BE6C7 "点击放大")

## 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，Snapshot模板支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/f8mR8TY_QvOUsTHCHB7bJQ/zh-cn_image_0000002571546946.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=7CB525FC2024B3F57468F537ED8D1F2B15CA949FFF6CD96BDC58B4A268F3EBAB "点击放大")

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

* Retained Size：按照Retained Size从大到小展示周边节点。
* Distance：按照Distance从小到大展示周边节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/KzSezIvYT7ahCwnIjzOP-g/zh-cn_image_0000002571546944.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=EFC1F538BA27E54A4458682336C63CE2CF696161211966F56E5F8D16DE90F615 "点击放大")

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/xmrYspD8SGq8Z3YzFDS9ug/zh-cn_image_0000002602186495.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=3C961307F691F479B259DF9FB4ABDE58AD1CB1AF75D7323B227B24AD15777738 "点击放大")

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

* **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
* **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
* **Redraw with this node**：以该节点为中心重绘。
* **Reveal in Statistics**：在Statistics页面中显示该节点。
* **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/4YwaA4rcTniEjYtcgSFGFA/zh-cn_image_0000002602066433.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=75B2FBF1EF442A311ADB5764FA4B510CE006D21CBC4997FB4BDF0C0BE3B0FF63 "点击放大")

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/7WXymXo4QN6wdJCjYu-Hag/zh-cn_image_0000002602066421.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=17F801F88D3509379E2E1EF7045562E8A3C6F0AF85641279090AAAC0D0BAB87A "点击放大")

## 离线导入内存快照

DevEco Profiler支持离线导入内存快照功能，可导入一个或多个.heapsnapshot及.rawheap文件。

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot或.rawheap文件。

说明

* 导入的单个文件大小不超过1.5G。
* 批量导入的文件数量不超过10个。
* .rawheap文件是应用发生Out of Memory现象时产生的原始内存文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/q2kc5yn6TkmCWDAkCysFrQ/zh-cn_image_0000002602186483.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=EA89AC9C21B0A25AC491EA74E4F5438F1DD0006110C31D3489AAAB9AAD7B2754 "点击放大")

离线导入内存快照成功后，可以导入与.heapsnapshot或.rawheap文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

说明

* 导入的单个jsleaklist文件大小不超过30M。
* 导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
* 可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/sHIOWpX8RgixnPfzl2MXLA/zh-cn_image_0000002571546950.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=DB677377F32ECD63A85FD6281D702AA1A1DCF0C0EEAB536A7766AF8C12216F9F "点击放大")

## 解析内存对象

从DevEco Studio 6.1.0 Beta2开始，DevEco Profiler支持导入[代码混淆产物nameCache](../../../编写与调试应用/日志与故障分析/故障分析/异常堆栈解析原理/ide-exception-stack-parsing-principle.md#section19215122372720)文件和[ArkTS调试产物sourceMap](../../../编写与调试应用/日志与故障分析/故障分析/异常堆栈解析原理/ide-exception-stack-parsing-principle.md#section666114451518)文件，还原文件名称和文件路径。

以nameCache文件为例，文件导入前，Class为d8。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/f0bXxD1ySnetqfYIX0gh9g/zh-cn_image_0000002602186497.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=7BBC338EA5346650493ACD0DE042BE0B976CD41980954558FB28A6E7D71FCDB1 "点击放大")

点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/4RJF-KJaQvutMgddGLkijw/zh-cn_image_0000002571546948.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=6EDDE905F57C29DF0F4F96F9B93FA55CBE2F375CE4862374EA85FE48B987DD2F)按钮，导入nameCache文件，Class显示为文件名称MyAbilityStage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/irUMEChRTOKrXoTZ9BBT6Q/zh-cn_image_0000002571546936.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=BD2FCD7354710CDD1CFD4AD3E923DD713CA5253D1CD977A4B63624EC0D0E2EAB "点击放大")
