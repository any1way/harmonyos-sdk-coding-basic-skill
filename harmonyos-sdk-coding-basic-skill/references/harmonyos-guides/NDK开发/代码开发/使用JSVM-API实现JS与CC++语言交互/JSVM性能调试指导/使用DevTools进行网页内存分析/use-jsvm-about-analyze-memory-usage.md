---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:21:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2dfa9dde20ceec5ce798420c63c77a7a3425746c818ec271ed11a9dfb6996d0
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/78vkvsiZSJiPEVq1Vdk3gQ/zh-cn_image_0000002622859265.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=27279AB06A7BE9FC4998747A22DEDE8D5809D87114EFB330707069DEA4676B8F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/ZPEx7KbxTcurVu92wXiW2w/zh-cn_image_0000002622699385.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=8C3AAD85E68F4A9902A1094669A56D3DA665EAA840F76245E29C318FEC3B2EAD)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor):表示对象的构造器
* 距离(Distance):与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/wpb7GbuFTv-ilJqLRZnEtg/zh-cn_image_0000002592219824.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=0F2B18ECC006FD8E7167BFB0454320AEBFAFDB9DFE3DDD3768A785E54434737F)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/C3TkN2H0ThWfU0fOdBo5yQ/zh-cn_image_0000002592379758.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=F6A4B27F40E40545268BBFE0474344F41F1AC41DADDC0C45BBED0CE707C39658)

### 比较(Comparison)

在比较(Comparison)中可以将当前快照与另一个快照比较，跟踪对象属性和内存占用的变化。其中：

* 构造函数：对象的构造器。
* 新对象数(New)：该对象构造器下有多少新的对象被创建。
* 已销毁(Deleted)：该对象构造器下有多少新对象被销毁。
* 增量(Delta)：新对象与被删除对象的差值。
* 分配大小(Alloc Size)：两份快照间分配的内存大小。
* 已释放大小(Freed Size)：两份快照间释放的内存大小。
* 大小增量(Size Delta)：分配大小和已释放大小的差值。

可以根据比较界面不同快照间的差异分析内存问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/UoYdKjeaQ7eA2mPOYffkEQ/zh-cn_image_0000002622859267.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=D3F9F4B24BE13D9D7BF0AFDE2A50CA99C9AA9E9D1D42303CAD7A31DB3DCC27C3)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/2Er8Zi6cT4-iZmHmj_tTAA/zh-cn_image_0000002622699387.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=222B68A0365509363123B36F1AAEB868D79C0F4FBA2A04891953FE365D12D2C8)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/tfqkQ6AdQZW0jdGkS-3h3w/zh-cn_image_0000002592219826.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=CA9CC61476CD7FF6B42247DA51D61A85C9D956B8198CDD976D51C4B9CD93C009)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6d-iPwJMSJaGK81D98-5Uw/zh-cn_image_0000002592379760.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=BF396E03AA003B9C7BED1247530F15B69ABD315FBD4789DB8FDB1054B299F04C)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/_qZNWt8ISDW6TXYnTtaKkQ/zh-cn_image_0000002622859269.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=571CEDFB05916343DD76D4C50A04B490CBE3053577444136E8187E9BC16DE92C)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/iBnzm90dRB-vnbS7knBhLg/zh-cn_image_0000002622699389.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=CE2A0FE0E770D384998DE3CD137D996FA3E6E8DFCB024C795EE283890D73AD3F)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/NHbvhZnBQy-lcYKQ4K-8iQ/zh-cn_image_0000002592219828.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=9180A5C714A8D2E00DB20B1CF0F5B8D91C7A80D32E7418CD8DA292840A537F6A)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/1_PJkqXCQveRQG8dkpe-9A/zh-cn_image_0000002592379762.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=97352A0C0BB89D5D5EC822E0DFFFD2C7B7B4D1E4610A944770BF415D1E96FEB3)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/V4cve3l7SFWMAkevOi_jsw/zh-cn_image_0000002622859271.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=5956CA316FE74A9E29ADCFE5F5A80979A9F56EAA6F85E15D2570A6AC9131302A)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/e7GP6n0xR_KuBmHcdsNIIw/zh-cn_image_0000002622699391.png?HW-CC-KV=V1&HW-CC-Date=20260611T072128Z&HW-CC-Expire=86400&HW-CC-Sign=7F73A9C257064A2561FA26A3ED2C6117DFD858F090F9454BBF52DBB6EE582743)
