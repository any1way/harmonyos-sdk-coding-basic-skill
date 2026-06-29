---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-web-fling-jank-events
title: ArkWeb抛滑丢帧事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > ArkWeb抛滑丢帧事件 > ArkWeb抛滑丢帧事件介绍
category: harmonyos-guides
scraped_at: 2026-06-01T11:25:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48aa7ee5757da173a4be94140ed3dcba6ccd069d9a06f6a904c8057ce8b61912
---
## 简介

[ArkWeb](../../../../../../../../应用框架/ArkWeb（方舟Web）/ArkWeb简介/web-component-overview.md)提供了Web组件，用于在应用程序中显示Web页面内容，为开发者提供了丰富的控制Web页面能力。页面滑动一般分为两个阶段：拖滑和抛滑。拖滑指触摸屏幕时的滑动。抛滑指在手指离开屏幕后，页面仍以一定速度滑动。从API version 23开始，支持订阅ArkWeb抛滑丢帧事件，用户在使用应用时滑动web页面，如果出现抛滑丢帧且卡顿持续时间超过50ms及以上，就会被定义为ArkWeb抛滑丢帧，并生成相关丢帧数据。

本文面向开发者介绍ArkWeb抛滑丢帧事件检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅ArkWeb抛滑丢帧事件，请参考以下文档。

* [订阅ArkWeb抛滑丢帧事件（ArkTS）](../订阅ArkWeb抛滑丢帧事件（ArkTS）/hiappevent-watcher-web-_90540707.md)

说明

ArkWeb抛滑丢帧事件仅提供发生卡顿的Web组件对应的web\_id，最长丢帧时长及其他相关数据，不提供卡顿日志等信息。开发者可以借助web\_id，参考“订阅ArkWeb抛滑丢帧事件（ArkTS）”文件中的示例代码获取到发生丢帧的网页地址，再结合业界成熟的[DevTools工具](../../../../../../../../应用框架/ArkWeb（方舟Web）/Web调试维测/使用DevTools工具调试前端页面/web-debugging-with-devtools.md)复现并排查根因。

从API version 23开始，ArkWeb抛滑丢帧事件支持在[应用分身](../../../../../../../../基础入门/开发基础知识/典型场景的开发指导/创建应用分身/app-clone.md)、元服务及[输入法应用](<../../../../../../../../应用框架/IME Kit（输入法开发服务）/实现一个输入法应用/inputmethod-application-guide.md>)场景下使用 HiAppEvent 进行订阅。

## 检测原理

ArkWeb在渲染绘制完成之后会生成buffer，并将生成的buffer送至图形缓冲区，图形侧取出buffer进行送显。在抛滑阶段，通过检测ArkWeb前后两次与图形侧交换buffer的时间差判断是否超时异常，来判断ArkWeb侧是否发生了丢帧。

## params字段说明

ArkWeb抛滑丢帧事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| start\_time | number | 抛滑动效开始时间，为一个时间戳。 |
| duration | number | 抛滑动效持续时长，单位为ms。 |
| web\_id | number | 发生丢帧组件对应的web\_id。 |
| max\_app\_frame\_time | number | 抛滑期间最长连续丢帧时长，单位为ms。 |
