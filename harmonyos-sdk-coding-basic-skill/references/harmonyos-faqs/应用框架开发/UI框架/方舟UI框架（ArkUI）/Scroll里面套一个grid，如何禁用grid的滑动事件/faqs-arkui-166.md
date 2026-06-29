---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-166
title: Scroll里面套一个grid，如何禁用grid的滑动事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Scroll里面套一个grid，如何禁用grid的滑动事件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cbec631d7ab598fa3058536ad766a4eaf2fd256b6dd9f2c479ca5861dc086bcf
---
可以通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动。具体实现可以参考[Scroll](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)中的示例2。
