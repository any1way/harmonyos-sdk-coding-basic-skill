---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-introduction
title: Pen Kit简介
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > Pen Kit简介
category: harmonyos-guides
scraped_at: 2026-06-11T14:51:21+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:1bc3474fa241f26734d84fcc884c4b1888845239ab39fb5249cd1bf24455c553
---

Pen Kit（手写笔服务）是华为提供的一套手写套件，提供笔刷效果、笔迹编辑、报点预测、一笔成形、全局取色和手写交互的功能。Pen Kit可以为产品带来优质手写体验，为您创造更多的手写应用场景。

目前Pen Kit提供了五种能力：手写套件、报点预测、一笔成形、全局取色和手写交互。

## 手写套件

三方应用直接集成手写套件组件，提供如下功能。

* 画布

  笔迹绘制、笔迹保存、画布缩放、一笔成形功能。
* 工具栏

  + 笔刷：圆珠笔、钢笔、铅笔、马克笔、荧光笔、马赛克笔、激光笔七种笔刷效果，5档笔宽，100+种颜色选择。
  + 橡皮擦：笔划擦除、像素擦除、仅擦除荧光笔、清空画布。
  + 套索：框选、移动、剪切粘贴、复制粘贴、删除、调整大小。
  + 其他功能：撤销、重做、禁止手指书写。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/JTTaeeq9QVuQ4WgTC6d9NA/zh-cn_image_0000002592218904.gif?HW-CC-KV=V1&HW-CC-Date=20260611T065120Z&HW-CC-Expire=86400&HW-CC-Sign=FB50FDB529D4F53D14EF2C225D5995167AAC9FD10AB5AF8A8F584A95ADEF7A44)

## 报点预测

根据书写轨迹预测报点提前进行绘制，提高手写跟手性，手写套件已默认开启报点预测，您也可以在应用中单独集成报点预测功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/CixaLG4qTLmZOpuEn5zy-A/zh-cn_image_0000002592378838.gif?HW-CC-KV=V1&HW-CC-Date=20260611T065120Z&HW-CC-Expire=86400&HW-CC-Sign=51BA7695E3384FF09A3290166442A896C7910F98961CCCAA2152EE5626F70A45)

## 一笔成形

在连续的一笔绘制结束时，手写笔/手指在屏幕上停顿一定时间后，将触发一笔成形功能，该功能会将这一笔绘制内容识别成规整图形，手写套件已默认开启一笔成形功能，您也可以在应用中单独集成一笔成形功能。Pen Kit支持以下图形的识别：

| 图形类型 | 具体图形 |
| --- | --- |
| 线段 | 直线段、带箭头线段（单向、双向） |
| 圆 | 圆、椭圆 |
| 多边形 | 三角形、矩形、平行四边形、菱形、正五边形、五角星形 |
| 曲线 | 抛物线、带箭头抛物线（单向、双向） |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/jqKs1v9iTc2FZh4QOnWnBw/zh-cn_image_0000002622858345.gif?HW-CC-KV=V1&HW-CC-Date=20260611T065120Z&HW-CC-Expire=86400&HW-CC-Sign=6D36C7C62F307405A8ED68182ACB4E58DFF83860A96C2C8F3F2BF4FDE0DF9CEF)

## 全局取色

提供全屏取色基础能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/yvtF_YrIS6emxnJPqtpbAQ/zh-cn_image_0000002622698467.png?HW-CC-KV=V1&HW-CC-Date=20260611T065120Z&HW-CC-Expire=86400&HW-CC-Sign=081F2EF4AA97ABB4AD04D67FBCED1C45D91F0A9845C7AFE79F951FF567CBF463)

## 手写交互

提供监听手写笔双击/轻捏事件能力。

## 约束和限制

### 支持的国家和地区

只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

本Kit仅适用于Phone、Tablet和2in1设备。

支持手写笔硬件的手机、Tablet和2in1的型号可参见[华为手机支持的手写笔设备清单](https://consumer.huawei.com/cn/support/content/zh-cn15869694/)和[华为手写笔与平板/笔记本电脑适配清单](https://consumer.huawei.com/cn/support/content/zh-cn00737675/)。

## 模拟器支持情况

本Kit暂不支持模拟器。
