---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-parameter
title: 自定义组件参数
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件参数
category: harmonyos-references
scraped_at: 2026-06-01T15:44:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:83bcf06f84f1c88390b7e652f288e723b7b673fb7fda891581784eee024972cd
---
说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ComponentOptions

PhonePC/2in1TabletTVWearable

自定义组件参数，用于配置是否支持组件冻结。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

从API version 11开始，支持通过此参数配置[@Component](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#component>)组件冻结。例子可见[自定义组件冻结](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/自定义组件冻结/自定义组件冻结功能（V1）/arkts-custom-components-freeze.md>)。

从API version 12开始，支持通过此参数配置[@ComponentV2](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#componentv2>)组件冻结。例子可见[自定义组件冻结](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/自定义组件冻结/自定义组件冻结功能（V2）/arkts-custom-components-freezev2.md>)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| freezeWhenInactive | boolean | 否 | 否 | 配置自定义组件支持组件冻结。true：开启组件冻结，false：不开启组件冻结。当开发者未指定ComponentOptions时，freezeWhenInactive将使用false作为默认值。 |
