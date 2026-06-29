---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-launch-case
title: 案例：应用冷启动首帧完成时延问题分析
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > 案例：应用冷启动首帧完成时延问题分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:34+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f9ed8f7cd7c8d49dcfcd4adbca867000607eebb8af029061b8acbc71c1cf8170
---
应用冷启动首帧完成时延是指从用户点击桌面应用图标离手开始，到应用进程首帧绘制结束的时间。本案例介绍如何找到应用冷启动首帧完成时延起止点，以及如何通过调用栈和trace信息分析应用运行逻辑，定位应用冷启动首帧完成时延超预期的原因。

应用冷启动分析基础功能请参考[Launch模板基本操作](../Launch模板基本操作/ide-insight-session-launch.md)。

## 分析步骤

分析冷启动首帧完成时延类问题步骤如下：

1. 确认应用冷启动首帧完成时延起止点。
2. 框选应用冷启动首帧完成时延起止点位置，查看耗时是否超预期。
3. 若超过预期，根据调用栈和trace信息进一步确认问题点。

## 录制Launch模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Launch**模板，点击**Create Session**或双击Launch图标即可创建一个Launch的录制模板。
2. 创建模板后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/XdTm8W6uSKKDAWLftv_03g/zh-cn_image_0000002602066279.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=E99D0BE42B77F6336D3E41CFEDD6578C61141D740174E2168FD2A48E4B79C465)切换启动模式为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Z3_0qWr8SGCBNioT3dPBxg/zh-cn_image_0000002602186309.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=CAAFD732895F383A84ABA8103CA089331C169C5DB54A2B9C0BC8748B4C4F14F4)手动启动。
3. 在工具控制栏中点击齿轮图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/qZarY9l2RCOS-BA6jd2cVw/zh-cn_image_0000002602186317.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=3D8B41C770206B61ACC99FD06039195DA5B298806F9FF1B0A6E4448396887CAF)后勾选Hitrace > multimodalinput。用于采集多模子系统的trace信息，这部分信息会包含硬件传递过来的离屏信号，即多模子系统收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9BfowT0HTCqQPNRvp_zlGQ/zh-cn_image_0000002602186327.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=5277118AAB086107B3025E8335D7ABDFBB5F968487468AE4C97760D8D2071E30 "点击放大")
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/fTR_jbPuTI2MSX2UhhOhng/zh-cn_image_0000002571387152.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=259155A3FD66154AEEF8D42A0A1CFB078430D345449EF0B2E9032A029C4DB0A7)即开始录制。等待界面出现弹窗提示启动应用后，需要手动点击设备上的应用图标启动应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/tyIS5PGZTW-dHO1xyfHjww/zh-cn_image_0000002571546786.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=CB5A05D188AAB4CFEF789F6A516088B3001171F6A51E2002788D4512D802762F "点击放大")
5. 待右侧泳道全部显示recording则表明正在录制中，等待应用冷启动结束后可以点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/S8v6JDnlTqiTAV8WbzFvMQ/zh-cn_image_0000002602066257.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=64406EAA264F5A3EA9F3FF582A27ADCE49C14F4DA4AA2C437D87E969D4346760 "点击放大")

## 分析Launch数据

### 确认首帧完成时延起止点

**冷启动首帧完成时延起点确认：**

首帧完成时延起点是用户点击桌面应用图标离手的时刻，即多模子系统收到硬件传递过来的离屏信号的时刻。

由于离屏信号对应的trace点耗时较短且不方便记忆。因此，需要优先找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）来辅助定位首帧完成时延的起点位置。具体步骤如下：

1. 找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）。在Profiler面板点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在搜索框中输入H:DispatchTouchEvent后回车，通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/-vyOEIPSRb2PSCN3leS9jg/zh-cn_image_0000002602066269.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=463748D57357FC3A6990D0860CA3617A26359407883AAA1124A5CB789DC7120A)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/jPizxogTTxysSRI6u6n9_g/zh-cn_image_0000002571387154.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=8FBFF11A276FAE455159F8C7FEADED4817BA35966895A80A5460291FE1A7389E)按钮切换搜索结果，找到桌面进程泳道（ohos.sceneboard）中type=1（0：手指按下；1：手指抬起；2：滑动）的H:DispatchTouchEvent点并添加标记，为方便后续查找，可以通过双击标记，在弹出的标记属性框中修改标记描述为点击离手事件。该trace点就代表桌面进程收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/dCyCTs7BTSWJy16kYGh-Gw/zh-cn_image_0000002602066259.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=5E949E34ED2C594E1A383B55717F108DA2A9FD2A453C512728B1E3E404F605AD "点击放大")
2. 搜索多模子系统泳道（mmi\_service）。点击搜索框选项区选择**Search Units搜索泳道**，在输入框中输入mmi\_service后回车，该泳道可能有多条，需要通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KAz5eWI4SRWo8wvNpay6EA/zh-cn_image_0000002602186325.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=BCE7A5FBA51D8AC3C8574E60EC712BAADEEF4E1689187F08E6684B091EDFC2E1)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/r4_xYyPcTB2Yy8hOOSF-iA/zh-cn_image_0000002602186323.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=505D53C57DA23A2F363EA7852DADB3584D27091E1789888369E0DD761C760121)按钮切换搜索结果，找到包含trace片段的mmi\_service泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/vlbjVwSfQ4GGNuM0Cz63DA/zh-cn_image_0000002571546792.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=AD82D87D65013647D88C0F0DE378D93AA40D95CA70FCCE4630F92EC57D0B1294 "点击放大")
3. 借助桌面进程收到点击离手事件trace点，继续定位多模子系统收到点击离手事件的trace点。

   在mmi\_service泳道中找到位于点击离手事件标记位置前方的CPU Running条块（此段时间表示多模子系统正在运行），在该条块下方找到H:service report touchId:{id}, type: up（或H:service report pointerId:{id}, type: button-up）的trace点并添加标记，然后修改标记描述为首帧完成时延起点。该trace点代表的是多模子系统收到点击离手事件，即冷启动首帧完成时延的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/e9C9LCs9SGaD9IoH_VcXhA/zh-cn_image_0000002571387142.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=38C103813C38272A80A0D175F0201460852290CE9ABA8EB076B0FFCE34024BF6 "点击放大")

**冷启动****首帧完成****时延止点确认：**

首帧完成时延止点是应用进程启动后收到的首个硬件垂直同步信号的时间点，即Render Service（统一渲染服务进程）将应用首帧渲染结果呈现到屏幕上的结束点。定位首帧完成时延止点具体步骤如下：

1. 找到应用进程启动后的首个垂直同步信号trace点H:ReceiveVsync，这个trace点代表应用的首帧开始绘制。选择应用进程子泳道，点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在输入框中输入H:ReceiveVsync后回车，找到第一个H:ReceiveVsync点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ud_zDI_dS7-ShXQo57ATow/zh-cn_image_0000002602066251.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=62A730D0178F4FAAD25F8DBA6BDDA992E9C31537B8FBFB0D680684F3CF8DDD07 "点击放大")
2. 应用进程启动后收到首个垂直同步信号时，会通知Render Service进程进行图形渲染，因此需要优先找到应用进程通知Render Service进程进行图形渲染的三个trace（H:FlushMessages > H:SendCommands > H:MarshRSTransactionData）。由于这三个trace耗时较短，不便查看，因此需要使用搜索功能来确定。框选H:ReceiveVsync trace点，点击搜索框选项区选择**Search Units Data**搜索泳道数据，在输入框中输入FlushMessages后回车。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/G8CM6RTtQxuXVbO5EtTQiA/zh-cn_image_0000002571546780.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=9320ADB5C50B9B7732B256508E4F9827D449B94F516999CD5CDF566F3A2F12B2 "点击放大")
3. 找到trace点H:FlushMessages（代表绘制消息） 后，继续在该trace点下方逐层分析，先找到trace点H:SendCommands（代表发送绘制指令给Render Service进程进行图形渲染），在下方再找到trace点H:MarshRSTransactionData（代表发送了绘制指令），这3个trace点就代表应用进程通知Render Service进程进行图形渲染的流程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3BNmBiJtSOmw9YaJAmwU_g/zh-cn_image_0000002602186335.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=AF9BAFD7837EBBCB3EA19C2884782A5230C6A1526438AF7BC6BB1C591BD48C62 "点击放大")
4. 接着需要找Render Service进程收到应用进程首帧渲染通知的trace点，点击H:MarshRSTransactionData条块，“Slice Detail”区域可以查看该trace详情，包括trace名称、所属进程等。点击“Slice Detail”区域中Name后方跳转按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ds_XICqdQt-6SgjBKRapuw/zh-cn_image_0000002571546784.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=A732EC53BD0C1EBB485DA5BE8614324C82450B31315064559D510E96CB487263)跳转到render\_service泳道的H:RSMainThread::ProcessCommandUni trace点并添加标记，然后修改标记描述为收到渲染通知。该trace点就代表Render Service进程收到应用进程首帧渲染通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/o_gbHHWLRcG1pJ0n_jlrVQ/zh-cn_image_0000002602186331.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=FFEA0E14275117ECEC509601BB7E4225C7CA7531910A4706280A0242007BFFDA "点击放大")
5. 接着找到Render Service将应用首帧提交硬件上屏的trace点，该操作在Render Service送显线程（CompThread）中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入CompThread后回车，查找位于收到渲染通知标记位置后方的第一个H:CommitLayers并添加标记，然后修改标记描述为提交硬件上屏。该trace点代表Render Service将应用首帧提交硬件上屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/1Cr_cBJmTyStOuIQlbJcBg/zh-cn_image_0000002571387166.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=4B0666F398244FB5101E8B00E27F058CE5DA87048A6C0740D7A5B0DFBDF45BF4 "点击放大")
6. 最后找到Render Service将应用首帧渲染结果呈现到屏幕上的trace点，该操作在PresentFence中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入PresentFence后回车，查找位于提交硬件上屏标记位置后方的第一个H:Waiting for PresentFence，该trace点代表Render Service将应用首帧渲染结果呈现到屏幕上，trace点的结束位置就是冷启动首帧完成时延的止点，在此处添加标记并修改标记描述为首帧完成时延止点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ENDSd4CgRoOpWFMG2Ik7Rg/zh-cn_image_0000002602186333.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=ACE982606C1346EDA907FC87D4255A86E63EE147D147FBBFD6A5729E72E864AF "点击放大")

### 案例：应用首页加载耗时较长导致应用冷启动首帧完成时延不达标

说明

* 本案例基于应用进程启动过程中，在Ability的生命周期回调函数中做了耗时操作。
* 预期冷启动首帧完成时延不超过600ms。

框选应用冷启动首帧完成时延起止点位置，通过框选区间的时间长度看出，冷启动首帧完成时延超过800ms，比预期的600ms长。

切换到应用进程Process泳道，查看主线程（线程号与进程号一致）的trace。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/CtLh5zsFRlCtkwR10msi8Q/zh-cn_image_0000002571546794.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=C946B8BFC8FD4751D7472B4F7B7C76FA2175F7B428D50CDA045EAB5C8FD47548 "点击放大")

下方详情区展示Details信息，包括trace名称、起始时间、持续时长。将持续时间（Duration）降序排序，可以看到主要耗时在H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction，该阶段主要是AbilityStage/Ability的启动生命周期在执行相应的回调。从这里可以看出，是因为AbilityStage/Ability启动生命周期的回调执行时间较长。接下来需要分析调用栈，通过调用栈分析回调执行时间长的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/b7FjMnrhTjuiqWHwg1KPTA/zh-cn_image_0000002602066253.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=9138F33929EFCE2193E83C0E8BF90BFC4AE2CE20010C63B695F299A1C7964F67 "点击放大")

接着切换到ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看线程号与进程号一致的ArkVM子泳道（该泳道为主线程调用栈），可以看到ArkTS侧一些方法的耗时。从下图中可以看到ArkTS侧无函数执行，需要切换到Callstack泳道看ArkTS和Native混合函数调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/fPnLvZOpQdG1PBaqcqwi7w/zh-cn_image_0000002571546776.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=EAE452882E30BA6C3362DC4D6CBA36B712C4A83BD2A95C0E7AACA5833F252AC7 "点击放大")

最后切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，查看下方Heaviest Stack区域，滑动观察权重占比最大的函数调用栈，定位到耗时主要是EntryAbility.ets文件下第79行代码引起，双击该栈帧可以直接跳转到源码文件的对应位置上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/FREGn5ySSxW1Ec6yIvgJ9Q/zh-cn_image_0000002571387136.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=FE823BFED467941DE4FECED532FAB575B385DB55E4EA65E69B348AA2D285C474 "点击放大")

结合业务代码查看，可以看到是因为在EntryAbility.ets文件下onCreate()中做了耗时操作。耗时操作建议通过异步任务延迟处理或者放到其他线程执行，以降低主线程负载，缩短应用冷启动首帧完成时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/-vAnZuGARKqEl_84o23B8g/zh-cn_image_0000002602186321.png?HW-CC-KV=V1&HW-CC-Date=20260611T073133Z&HW-CC-Expire=86400&HW-CC-Sign=3A96DB1DEE46B9C145058B5FA2B770BFB50F1A2E9EEF32895D576CC3804C9F42)

更多应用冷启动优化方案，请参考[应用冷启动时延优化](../../../../best-practices/性能/性能场景优化案例/应用启动与响应优化/应用冷启动时延优化/bpta-application-cold-start-optimization.md)。
