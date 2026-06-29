---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-49
title: AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:136741d456e9c017793db9725581952d457cb8c49ce93b851726e6917df2e60c
---
AppStorage 支持应用主线程中多个 UIAbility 实例之间的状态共享。AppStorage 是与 UI 相关的数据，必须在 UI 线程中运行，无法与其他线程共享。当前没有替代方案。

**参考链接**

[AppStorage：应用全局的UI状态存储](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md>)
