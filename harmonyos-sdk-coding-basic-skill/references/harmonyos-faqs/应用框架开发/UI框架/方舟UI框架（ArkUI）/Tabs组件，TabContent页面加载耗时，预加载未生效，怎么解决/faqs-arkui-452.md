---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-452
title: Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ef7a944763a4449339e13107305c46d5360136973affd60f2edef6a5c1ce4cda
---
**问题分析**

[aboutToAppear()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttoappear)被调用的时候Tabs组件尚未完成渲染，这会导致preloadItems方法预加载不存在的索引。

**解决方案**

TabContent中的[onWillShow()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/TabContent/ts-container-tabcontent.md#onwillshow12)方法能够实现预加载功能，但是Tabs每次切换时都会触发onWillShow()回调，需要做节流处理。
