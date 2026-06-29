---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-222
title: @Style 和 @Extend 是否支持export导出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > @Style 和 @Extend 是否支持export导出
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8b6b68f6a4d0f4c76dc4fe71ffa911ff241a83afaed52a4736ebea11aed1e4ad
---
1.@Styles 和 @Extend 目前不支持 export 导出，后续这两个装饰器将不再演进。

2.推荐使用新的样式复用方法。通过attributeModifier属性动态设置组件，并通过自定义类继承基础组件的Modifier，在类中设置复用的属性，自定义类没有导出限制。然而，虽然推荐使用attributeModifier，但需注意其目前不支持事件和手势处理，这两个功能的需求正在跟踪中。

**参考链接**

[attributeModifier](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/动态属性与自定义/动态属性设置/ts-universal-attributes-attribute-modifier.md#attributemodifier)
