---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis
title: ArkUI分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > ArkUI分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:30+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:0e3c30cd65691c1300ad4b807cc2f5660cbf862eaa703dbc77fbd316979bb098
---
ArkUI分析用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：

场景1：布局嵌套过多引起的性能问题；

场景2：数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；

场景3：父组件中的子组件重复绑定同一个状态变量进行更新；

场景4：未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝。

## ArkUI Component 泳道：查看组件绘制耗时

开发者通过ArkUI Component泳道可以直观感知组件绘制频率、耗时等统计情况。

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区Summary列表给出录制时段内定制组件以及系统组件的绘制统计情况，包括绘制次数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/fmu7LvCOSlGJ2tLjf0HeDg/zh-cn_image_0000002602066017.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=58002B21C4FBDF6AD2C51A830545DE8C550F80760A5CF9B5B65FA8D04F611D71 "点击放大")
3. 详情区Details列表可以查看按照时间线排序的组件详情，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/C_GBLUo9SQGVWcLFUNEWLA/zh-cn_image_0000002602186065.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=9DECD12A1862DC56B75D3183212CE030F6AB526E5D64E560364516DF80269D36 "点击放大")
4. 点选ArkUI Component泳道中的条块，展示Slice Detail数据，Slice Detail中的Name支持跳转至对应Process子泳道并选中trace信息，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/WtQKUwIYS7yqfme-I_31tw/zh-cn_image_0000002571386898.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=53E490841E16C9FB56EBC94875254535AD459BA119A4D11198658CAFD449FA7A "点击放大")

   说明

   由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

## ArkUI State 泳道分析

1. 点击ArkUI模板创建session并启动录制，录制过程中触发组件刷新。
2. 录制结束等待处理数据完成。点击ArkUI State泳道，可在下方数据区查看录制过程中发生的状态变量变化。Summary区域可查看状态变量名称，变化次数，状态变量类型、所属组件和所属类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/RtcWbMM1Q7Sp_KSvri0qXA/zh-cn_image_0000002571386894.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=606991E55BF81B8F5AC6FBED2EA7F5518B54899BB57C40C1440422F1683DEA44 "点击放大")

   Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/uwZjuoLQR_O-NFPswDWCsg/zh-cn_image_0000002571546536.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=04EDEDEDF9EB910ED65CE4B7C3547847EA9CDE1C3AC9250513C7507559FB2140 "点击放大")
3. 选择Current Value中某一个数据，泳道区域将以虚线展示其时间位置。同时，右侧More区域展示该状态变量影响的组件关联关系。打开页面下方的**Delivery Chain**开关，该状态变量影响的组件关联关系将以图形展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/juzNQcg6S_aJh439Cu88BA/zh-cn_image_0000002571546532.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=FADFCAC5456700E7B939ACE9D90D9FA7139A3F482A9FB47A4AA09F9811304801 "点击放大")
4. 定位到可能造成卡顿的状态变量变化时间点，框选对应时间段，选择ArkUI Component泳道查看对应组件刷新时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/dJqrUs1_Qm2TShVSuCJiHQ/zh-cn_image_0000002571386902.png?HW-CC-KV=V1&HW-CC-Date=20260611T073130Z&HW-CC-Expire=86400&HW-CC-Sign=5DF638105B49E66662238931B7908EC55F522B7BCD78EF50E60663F711006C44 "点击放大")

说明

* 如需查看其他泳道信息，请参考[Frame分析](../Frame分析/ide-insight-session-frame.md)。
* 由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
