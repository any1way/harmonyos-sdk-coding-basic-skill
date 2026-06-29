---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview
title: 列表与网格概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 列表与网格概述
category: harmonyos-guides
scraped_at: 2026-06-11T14:30:30+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:cf0e46f6e81d619d423a209518e2e2febc8c48796f8d2c0ed923bdb111dd5721
---
许多应用存在滚动展示同类项目集合的需求，例如显示图片、视频、音乐、新闻、商品等。此类场景可以根据项目排列方式分别选择[List](<../创建列表 (List)/arkts-layout-development-create-list.md>)、[Grid](<../创建网格 (GridGridItem)/arkts-layout-development-create-grid.md>)、[WaterFlow](../创建瀑布流（WaterFlow）/arkts-layout-development-create-waterflow.md)实现，在圆形屏幕推荐使用[ArcList](<../弧形列表 (ArcList)（圆形屏幕推荐使用）/arkts-layout-development-create-arclist.md>)。

## 列表

List适合单列和多列宽度相同的场景，如通讯录、音乐列表、购物清单等。

直播评论、即时聊天等应用场景需要在列表底部插入数据时，内容应自动向上滚动，以展示新插入的节点，此功能可通过配置[stackFromEnd](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#stackfromend19)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/x-1pUEcxR8ae4Pp3evZn8g/zh-cn_image_0000002622697723.png?HW-CC-KV=V1&HW-CC-Date=20260611T063029Z&HW-CC-Expire=86400&HW-CC-Sign=B3CADD86D669F3965849D6A06129F4A15AC7E4178F4AFB1364228F7BE930407D)

## 网格

网格布局由“行”和“列”分割的单元格组成，通过指定“项目”所在单元格实现多种布局，应用场景包括九宫格图片展示、日历、计算器等。

对于部分项目占用多行或多列的场景，可以通过在创建Grid时传入合适的[GridLayoutOptions](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#gridlayoutoptions10对象说明)来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/-MJWtEDTSoG02YuyBogP2w/zh-cn_image_0000002592218162.png?HW-CC-KV=V1&HW-CC-Date=20260611T063029Z&HW-CC-Expire=86400&HW-CC-Sign=DE9AED8599570687C7306620DCCF5BFEA5D6C5111E637B01149C250ADB6BD213)

## 瀑布流

瀑布流布局是一种多列等宽但高度不等的布局方式，适用于需要错落排列的场景，如图片和视频展示、商品推荐等。

同一个页面内有不同列数分段混合布局的场景，可以通过设置[WaterFlowOptions对象说明](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md#waterflowoptions对象说明)的sections实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ELFi5vKySGOw1ugjidN4VQ/zh-cn_image_0000002592378096.png?HW-CC-KV=V1&HW-CC-Date=20260611T063029Z&HW-CC-Expire=86400&HW-CC-Sign=4F663E996247556F9A10A832B07FDDBCAC093660DEE6EAA322E7FC9043100DBF)

## 弧形列表

弧形列表是一种专为圆形屏幕设备设计的特殊列表，支持列表项在接近屏幕上下两端自动缩放的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/CDV9hd25TzykDfM9cX4keQ/zh-cn_image_0000002622857603.png?HW-CC-KV=V1&HW-CC-Date=20260611T063029Z&HW-CC-Expire=86400&HW-CC-Sign=7BB97105AC376659E4CBED0AEECE8766BA2E825C5BF65309C74713C658D48D56)

## 能力对比

| 业务场景 | List | Grid | WaterFlow | ArcList |
| --- | --- | --- | --- | --- |
| 滚动通用能力 | 支持 | 支持 | 支持 | 支持 |
| 项目分组 | [ListItemGroup](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ListItemGroup/ts-container-listitemgroup.md) | [GridLayoutOptions](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#gridlayoutoptions10对象说明) | [WaterFlowSections](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md#waterflowsections12) | 不支持 |
| 指定项目吸顶 | 支持通过[sticky](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#sticky9)属性实现吸顶 | 不支持 | 不支持 | 不支持 |
| 项目拖拽排序 | 支持[拖拽排序](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/拖拽排序/ts-universal-attributes-drag-sorting.md)，包括内置动画和拖动到边缘自动滚动 | 仅所有项目都占1行1列时支持内置动画[supportAnimation](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#supportanimation8)，且不支持拖动到边缘自动滚动 | 不支持 | 不支持 |
| 项目横滑 | 支持通过[swipeAction](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ListItem/ts-container-listitem.md#swipeaction9)属性实现横滑 | 不支持 | 不支持 | 不支持 |
| 项目间距 | 支持 | 支持 | 支持 | 支持 |
| 项目分割线 | 支持 | 不支持 | 不支持 | 不支持 |
