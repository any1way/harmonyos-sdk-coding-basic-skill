---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-v1-parameter
title: 状态管理V1装饰器参数
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器参数
category: harmonyos-references
scraped_at: 2026-06-01T15:45:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bd5211d67829b8b5c27a4ce4d69e8e110b4ef1bada38b0ba84bdd87c4c7f6998
---
说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ProvideOptions

PhonePC/2in1TabletTVWearable

[@Provide](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md>)参数，用于配置@Provide的支持重写，具体例子可见[@Provide支持allowOverride参数](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md#provide支持allowoverride参数>)。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| allowOverride | string | 否 | 是 | 配置@Provide支持重写。默认不支持重写。 |
