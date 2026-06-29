---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-overview
title: ArkTS卡片界面开发概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片界面开发概述
category: harmonyos-guides
scraped_at: 2026-06-11T14:37:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:af44338261c950151d8bcc889c08d077be3275da916ed8f6e8df7925a7989b28
---
ArkTS卡片开发采用通用[ArkTS语言](../../../../../../基础入门/学习ArkTS语言/learning-arkts.md)，开发者可以使用[ArkTS声明式开发范式](<../../../../../ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI开发（ArkTS声明式开发范式）概述/arkts-ui-development-overview.md>)开发ArkTS卡片页面。

如下卡片页面由DevEco Studio模板自动生成，开发者可以根据自身的业务场景进行调整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/9SPdsUMXSDWEvCMod1FoTQ/zh-cn_image_0000002622698265.png?HW-CC-KV=V1&HW-CC-Date=20260611T063652Z&HW-CC-Expire=86400&HW-CC-Sign=F909257161B5B34FFA80E3C98632B9DBF63F5DF28211D1AAA7888BE9EE5B03D2)

## ArkTS卡片支持的页面能力

ArkTS卡片具备JS卡片的全量能力，并且新增了动效能力和自定义绘制的能力，支持[ArkTS声明式开发范式](<../../../../../ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI开发（ArkTS声明式开发范式）概述/arkts-ui-development-overview.md>)的部分组件、事件、动效、数据管理、状态管理能力。

对于支持在ArkTS卡片UI界面中使用的接口，会添加“卡片能力”的标记，如：从API version 12开始，该接口支持在ArkTS卡片中使用。同时请留意卡片场景下的能力差异说明。

例如：以下说明表示CircleShape可在ArkTS卡片中使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ZfVlNmppRv-HCHlsiW4agw/zh-cn_image_0000002592218704.png?HW-CC-KV=V1&HW-CC-Date=20260611T063652Z&HW-CC-Expire=86400&HW-CC-Sign=CE3C954570548A22A1D277F9D561F69491B3F993AC527DDF67A1424F8A2D3E6C)
