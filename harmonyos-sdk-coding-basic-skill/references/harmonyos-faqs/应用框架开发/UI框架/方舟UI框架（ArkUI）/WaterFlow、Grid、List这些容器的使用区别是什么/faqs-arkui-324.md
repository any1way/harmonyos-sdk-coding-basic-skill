---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-324
title: WaterFlow、Grid、List这些容器的使用区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > WaterFlow、Grid、List这些容器的使用区别是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:68a083c56345dd63427ce3ab5a172d4bdc2c023c6c1573c8ea2fb1f8452a356a
---
[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)适用于高度不固定的多列瀑布流布局。

[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)专为网格布局优化，而[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)的[lanes](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#lanes9)属性仅提供基础多列支持，也能实现类似网格布局的效果，但是Grid组件对item的拖拽支持更好。

List适用于相同列宽，需要连续，多行呈现的列表布局场景。

| 特性 | Grid | List lanes |
| --- | --- | --- |
| 拖拽支持 | 支持 | 不支持️ |
| 布局优化 | 自动对齐 | 需手动计算 |
