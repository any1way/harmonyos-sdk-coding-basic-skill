---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js
title: 查看ArkTS/JS预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看ArkTS/JS预览效果
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6082305be57beabc03d09904092108895dd4af42779d214153631a4a23ed93f7
---
预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。

说明

* 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。
* 预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。
* 预览时将不会运行Ability生命周期。
* 从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP[设置Mock实现](../预览数据模拟/ide-previewer-mock.md)。
* 预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。
* 预览不支持组件拖拽。
* 部分API不支持预览，如Ability、App、MultiMedia等模块。
* Richtext、Web、Video、XComponent组件不支持预览。
* 不支持调用C++库的预览。
* HAR在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发HAR模块，请注意被元服务使用时预览器效果与真机效果的不同。

* **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/4xr0VBVWS0a49LLPa4syug/zh-cn_image_0000002571546628.png?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=F6074F729248ED99A8CA822177E9630E2706B272DD1B99FC92E5233D3DBB630B)按钮，关闭实时预览功能。

  说明

  开发者修改resources/base/profile目录下的配置文件（如main\_pages.json/form\_config.json），不支持触发实时预览，开发者需要点击重新加载![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/xjARc5l4TOu1iS2caAYY8w/zh-cn_image_0000002571386986.png?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=327815E99E59C3E6D2F39192DD6008FFF9389A54A668FDA3C55F79F1BB9B6673)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gz1fZnhIQwWlJ5NIqeYYGQ/zh-cn_image_0000002571386988.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=8CA0DEB77E2CD87399040F10CC06547271288537A4B786F976C7D829510F239B "点击放大")
* **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/BAbbGqnjQ8SEkuqPLD1keQ/zh-cn_image_0000002571546630.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=1606BB3F48D09D326449B9505DA173F01F03DA94A9C0862348DC13AF90D79F10 "点击放大")

以ArkTS为例，使用预览器的方法如下：

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。
   * 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/QqatlxGjQ3GK64MhOQhoiw/zh-cn_image_0000002571546626.png?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=AD43AEBEBC79D784B73947FE55C306FACCEEA785CA20384441F9360284705529 "点击放大")
4. 点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/YIL522IJQcuVEN6YjDcIaQ/zh-cn_image_0000002602066109.png?HW-CC-KV=V1&HW-CC-Date=20260611T072809Z&HW-CC-Expire=86400&HW-CC-Sign=BDCAAE3CEE881B044A09C1230DC7718D6F1C27499B6A05C4CDE3F92EF9BDA676)，停止预览。
