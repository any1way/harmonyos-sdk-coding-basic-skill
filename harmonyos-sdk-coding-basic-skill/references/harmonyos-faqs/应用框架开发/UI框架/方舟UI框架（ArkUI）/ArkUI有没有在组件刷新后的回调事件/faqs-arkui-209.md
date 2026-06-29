---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-209
title: ArkUI有没有在组件刷新后的回调事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArkUI有没有在组件刷新后的回调事件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a868cf93fc117b8c8704b3eaaccee462543983ea4f60fb5b0cb6f5da1e44dbdd
---
当组件状态变量改变时，会刷新组件。具体分为以下两种情况：

1. 如果是组件的属性刷新，可以将属性存储为状态变量，并使用@Watch监听状态变量的变化。

2. 如果是组件大小变化，可以通过onSizeChange()，监听到组件区域的变化。

**参考链接**

[状态变量变化监听](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/状态管理与渲染控制/状态变量变化监听/ts-state-management-watch-monitor.md)
