---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-information-display-common
title: 信息展示公共接口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > 信息展示公共接口
category: harmonyos-references
scraped_at: 2026-06-11T15:48:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d931577fa3dc21776d798f2ca78371e9b74e108a19bdcb204f31ebf0586d835
---
用于修饰组件，为[Gauge](../Gauge/ts-basic-components-gauge.md)和[DataPanel](../DataPanel/ts-basic-components-datapanel.md)组件提供信息展示能力的公共接口。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## MultiShadowOptions

PhonePC/2in1TabletTVWearable

投影样式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | 是 | 投影模糊半径。  API version 10及以前，默认值：5  API version 11及以后，默认值：20  单位：vp  number类型取值范围大于0。  **说明：**  设置小于等于0的值时，按默认值显示。 |
| offsetX | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | 是 | X轴偏移量。  number类型取值范围不做限制。  默认值：5  单位：vp |
| offsetY | number | [Resource](../../公共定义/基础类型定义/ts-types.md#resource) | 否 | 是 | Y轴偏移量。  number类型取值范围不做限制。  默认值：5  单位：vp |
