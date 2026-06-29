---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-431
title: Tabs是否支持懒加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs是否支持懒加载
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:53eed08e85c015a8bd37084c7954d9a74ef05a327c4dd3ed8dc5da04c79180e0
---
当SDK版本<=API18时，Tabs组件不支持懒加载，可以通过使用自定义TabBar与Swiper配合LazyForEach实现页面懒加载和释放。示例可参考：[页面懒加载和释放](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#示例13页面懒加载和释放)。

API19及之后，Tabs组件新增了[cachedMaxCount](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#cachedmaxcount19)属性，可设置子组件的最大缓存个数和缓存模式。在缓存范围外的子组件会进行释放。示例可参考：[释放Tabs子组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#示例18释放tabs子组件)**。**
