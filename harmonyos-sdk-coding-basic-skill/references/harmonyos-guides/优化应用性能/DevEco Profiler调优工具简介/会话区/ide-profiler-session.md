---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:24+08:00
doc_updated_at: 2026-05-21
content_hash: sha256:857aefaf263658b7cd116b302db8702be48f6ac48dee0b27e60c77d4909040e0
---
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/wQHyBJVaSISd02Wrpd0rtQ/zh-cn_image_0000002602186763.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2818ECB676A961D8104F88F0C761FA76FD765D29740E5C3507F3369D065B5924 "点击放大")

DevEco Profiler左侧为会话区，可以分为三个部分：

① 调优目标选择区域：选择设备、需要分析的应用和应用进程。

② 会话列表区域：

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/P-yo2J_lS0KPJ79H0cpOqQ/zh-cn_image_0000002602066701.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=373566A4DBEFFCC199DDCB6264C1AE7DE03ECBCCBC9A2ECFBCA2809E14C4EFD8)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/d9XK_dIJTaa4maSzuousiA/zh-cn_image_0000002571387598.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=811C85F9CF9FBC733983992899048F9A2E0640BBC0DEFF5017BFF8D1458B4745)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/wlhPAMx7TxCfeIo_6W3S_A/zh-cn_image_0000002602186771.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=7B435B020538FF8C0B064018AED99ECBF2B0A072F3DA41E939AE4C762ED9736A)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/99UXt_hHT6q-S7vrUBP3Eg/zh-cn_image_0000002572650118.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=8000F0D4FAB1B3458A2BBF487B0CC7B54EEC44993259C640283D53F553BE5458)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/5leNh9D6Qs2Y1S93In2EUg/zh-cn_image_0000002571547232.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=459D810357E8C48F6ACA506666021213082E2DFCE770D61A1FBD8B9EA74B60A1)将删除该会话。

说明

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/S4u5QnwsR9GYzCRXGGH-iA/zh-cn_image_0000002602186767.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=4AAA7BEE4AA5E983D12C2AA57E534ACC2DA0F0D616F6B82EE58B76DBADFD0070)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便的在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](../../../使用AI智能辅助编程/智慧调优/ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/9bDnWEpoTn6IedYwV8b2xw/zh-cn_image_0000002602186777.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=397AA4ABAECA8C6A588A05467A729871BF8344CFFCECA89749F19E5252ACA706 "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域：

* **创建会话：**DevEco Profiler提供[Frame](../../卡顿丢帧分析/Frame分析/ide-insight-session-frame.md)、[Launch](../../冷启动：Launch分析/ide-launch-overview.md)、[Snapshot](../../内存泄露：Snapshot分析/ide-insight-session-snapshot.md)、[Allocation](../../基础内存：Allocation分析/ide-insight-session-allocations.md)、[ArkUI](../../卡顿丢帧分析/ArkUI分析/ide-arkui-analysis.md)、[ComMemory](../../UI组件内存：ComMemory分析/ide-commemory.md)、[Energy](../../能耗诊断：Energy分析/ide-profiler-energy.md)、[ArkWeb](../../加载丢帧：ArkWeb分析/ide-profiler-arkweb.md)、[Network](../../网络诊断：Network分析/ide-profiler-network.md)、[Concurrency](../../并行并发：Concurrency分析/ide-parallel-concurrency-analysis.md)、[GPU](../../GPU活动分析/ide-profiler-gpu.md)、[Time](../../基础耗时：Time分析/ide-insight-session-time.md)、[CPU](../../CPU活动分析/ide-insight-session-cpu.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/HgQ6cDFfRIC9SVuzCGUXGA/zh-cn_image_0000002571387588.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2D23491F4F296F893EBF9928462BF2129B08DF3C6CBD949ED046718FB5F04B3A)：Frame卡顿丢帧场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/y581GegNTeCyM41OCs3fDg/zh-cn_image_0000002603249263.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=82CFB82E77609A6EA65DD503A3BF9E72706B63B25CA80B27A0DB7566DCBE5428)：Launch冷启动场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/u5FcETK4TteMB4K2XJoXog/zh-cn_image_0000002603369203.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=33FBADE1AD5F4C57A756043A1534B043131DEC0DA52487D385D6F50720710C07)：Snapshot ArkTS内存泄漏场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/SrDY0b7FSlmQyW-8nAns1w/zh-cn_image_0000002572809750.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2CA9EDCFBC6F7CC60D080D1579FEB9C3FDAC903CDB1C9AAB8B5561EBAE095C80)：Allocation Native内存泄漏场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/XEqmMCfNQrONoeXl15FUmg/zh-cn_image_0000002572650120.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2EFE2448B556B83110D361EE9742C37E4A53013CE7B711021E9456B42BA75670)：ArkUI卡顿丢帧场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Jluc6xKsQRifXiPv_PqKiA/zh-cn_image_0000002603249265.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2426D2C0CB15D1781E5E5B4A9D61BF31B3D50C8ADC44F659A41C4DFD3EB17A57)：ComMemory UI组件内存泄漏场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/-edctjdBQ7CPex7eVW_RHw/zh-cn_image_0000002603369205.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=0861F103C7AD9A0A8BCA7FAB81D34F47A0CC006CC6D97FA8771FB1ED172C2172)：Energy能耗诊断场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/jezpV4wySyCOmcqlrVDAwA/zh-cn_image_0000002572809752.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=59B9057D498FF4601A1037966ED3303AB72368529B2904C355E4941709358112)：ArkWeb加载丢帧场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UOtUPRCkS6-156UVZdJcNg/zh-cn_image_0000002572650122.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=2602C59EA9FF659CF70B76B70A6B0595F8E10AD2569E402C4BBBD8D5027578CA)：Network网络诊断场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/2whrohQWQaujRveyTty1Iw/zh-cn_image_0000002603249267.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=25DDFCBDA7E1E59D4E7F44236F1E7FD239A2B962614940A957C507FCF63A5A82)：Concurrency并行并发场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ggfDIoBfRLuqXEA4LmTcEg/zh-cn_image_0000002603369207.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=63E51555EA865083E7B8ABEC8E36A7EFC3DEDB4F657DD3EDCF7379AB64F36552)：GPU活动场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/luOu86E6QA2cRriqU2ffQg/zh-cn_image_0000002572809754.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=5D1630574FC9ED9AAA8716FB6DCF6334F8161C80B091C0C3EEDE58AD9820524A)：Time函数耗时场景化模板。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/vMGt4T9DTR-1X2dWGPXoyQ/zh-cn_image_0000002572650124.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=22DF8BC18030B7498FD3369FC675DD22DEC63FE1016B252413C28FB43B777E19)：CPU调度场景化模板。

* **数据导入**：点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件。
* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/ekNxskFxTtCDvKFm7cMVGA/zh-cn_image_0000002602186761.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=87246505063FE0AD1F0E0AA17A60717B50B43C84A3603DD78916BDC75AF6EBC4)设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/KEw0zppESKu8hFWvkMfJqg/zh-cn_image_0000002603249269.png?HW-CC-KV=V1&HW-CC-Date=20260611T073123Z&HW-CC-Expire=86400&HW-CC-Sign=F4F8E60AF6C9EC50FE3B7117C5C6B00B21ABD0363EBD430657006ED9CF85C1C9)
