---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-284
title: struct和class的区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > struct和class的区别是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:30:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d38fb38f4e4f7731fb9bcfa0aaea4fc4a580e9003791edc24a4bd65cbc551002
---
在ArkUI框架中，struct只在自定义组件中使用，@Component装饰的struct构成的自定义组件实例，与class生成的实例具有不同的类型特性。如果开发者需要使用组件作为参数在组件之间传递，可以使用[自定义占位节点](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/使用自定义能力/自定义节点/自定义占位节点/arkts-user-defined-place-holder.md>)。
