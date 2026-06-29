---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-470
title: 如何去掉Tabs组件自定义tabBar的自带无障碍朗读
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何去掉Tabs组件自定义tabBar的自带无障碍朗读
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:da07e9ee50d00815ab879a6648172da03ec8688f5fc32372a3b2d29b701ae6a5
---
**问题描述**

想去掉Tabs组件自定义tabBar的自带无障碍朗读，请问如何实现。

**解决措施**

可对Tabs组件设置无障碍朗读模式属性[accessibilityGroup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/无障碍属性/ts-universal-attributes-accessibility.md#accessibilitygroup)为true。
