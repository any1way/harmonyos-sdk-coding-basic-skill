---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory
title: UI组件内存：ComMemory分析
breadcrumb: 指南 > 优化应用性能 > UI组件内存：ComMemory分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:42+08:00
doc_updated_at: 2026-05-21
content_hash: sha256:593f386ee48f151173599b0042457ad28b79f316e39ef3d0c8a23bd4394dfa63
---
从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

## 操作步骤

1. 创建ComMemory分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/-owyfEfxTtmRWWnRYJyDCA/zh-cn_image_0000002602186069.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=F4B09FDB9E721001B80693B30D7F0E9E364FCB179FBD1CFF552AEFA5D682BCF9)指定要录制的泳道；或者在[会话区](<../DevEco Profiler调优工具简介/会话区/ide-profiler-session.md>)选择**Open File**，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Afu4Wa5LS2atqRw0Nv-LjQ/zh-cn_image_0000002571386918.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=4D42A867E901174B777DFD198761DDE3D3CA9DD899A1BB20A910ECFA0D1DBAF7)
2. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/4X-seC0VQwSLRiCL9IfOkQ/zh-cn_image_0000002602186085.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=D3BC090699037452851CA153B76CF1535719F72FA8D567670A15FC5B99B2A2A1)启动一次快照，“ArkUI Snapshot”泳道的紫色区块表示一次快照完成。

   在“Details”页签中显示当前快照的详细信息；点击Open按钮，将在[ArkUI Inspector](../../编写与调试应用/应用调试/布局分析/ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/lp0ve176Sq-YXh7fEGsZYA/zh-cn_image_0000002602066035.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=309D346AC239E77BF72032D31471E69DF7FE0C44ABF84D57E68B31AD972A7D83 "点击放大")
3. 在ArkUI Inspector中查看组件树。

   默认勾选“Show Component Size”，显示各组件的内存占用情况。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Xm6zPSE7Tz-2bwO1tEPACA/zh-cn_image_0000002571386896.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=C86560A7F122B50A806B8FD246B09B2BDDA661DBD6CF132A1A85B3DBA60343DE)，可勾选“Show Recursive Size”，显示各组件为根的子树的内存占用情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/GxvpwARYQZi-X3Db7iF6JA/zh-cn_image_0000002571546534.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=7F59D6BA0AF8D69932C308D04A0A8B0A9DBA501998DC456290D87480935DF795)
4. 在ArkUI Inspector的**Memory** >**Statistics**中，查看组件的内存统计信息。
   * Current：当前组件ArkTS内存和Native内存的占用情况。
   * ArkTS：当前组件对应的ArkTS堆快照对象的[Retained Size](../内存泄露：Snapshot分析/Snapshot模板基本操作/ide-snapshot-basic-operations.md#li19851458524)。
   * Native：当前组件新增占用的Native内存。
   * Subtree：当前组件及其子组件的Current内存之和。
   * nativeCount：当前组件存活的Native分配内存个数。
   * arktsCount：当前组件的ArkTS堆快照对象个数。
   * recursive：递归统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/nlSexJy7QlqvlzKZkOvDyA/zh-cn_image_0000002602186091.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=1A4DFAC84A235F6B9A3D95F375131981B41761B425E69D7CAFED88C82DE886BD "点击放大")
5. 在ArkUI Inspector的**Memory** > **Details**中，点击Details中任一项后，打开DevEco Profiler查看显示组件的详情。
   * ShowAllocationDetail：显示当前组件的Allocation详情。
   * ShowSnapshotDetail：显示当前组件的Snapshot详情，系统组件不显示该项。
   * ShowRecursiveAllocationDetail：显示当前组件及其子组件的Allocation详情。
   * ShowRecursiveSnapshotDetail：显示当前组件及其子组件的Snapshot详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/7aVAtFqDS0On9o43gjxgag/zh-cn_image_0000002602066029.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=989E438C36DCAD5B84944F08FA7711568DAC0ED4CBF75559F794756D0E5B13BE "点击放大")
6. 在ArkUI Inspector的**Memory** > **State****s**中，查看UI组件的状态变量内存。memory字段表示该状态变量在对应组件的ArkTS堆快照中的Retained Size，更多请参考[查看UI组件的状态变量](../../编写与调试应用/应用调试/布局分析/ide-arkui-inspector.md#section19923158103412)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/cK-0PZUvTP-L2vbcPH0Oug/zh-cn_image_0000002602066015.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=5506D326E248EE6F7D90145D24528A82C711B80221024BFC0736909F58C5BEC7)
7. 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/wdgDic4PQCiQ_R3LvNKWCQ/zh-cn_image_0000002602066031.png?HW-CC-KV=V1&HW-CC-Date=20260611T073142Z&HW-CC-Expire=86400&HW-CC-Sign=5F8D7149C59C6B856286AFE71F65371DC33CEAEBA225EC42BDD844B536B8E2CC)可以将包含内存信息的组件树快照导出到本地。
