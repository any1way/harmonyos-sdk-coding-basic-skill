---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-185
title: 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8b4a7a1a3393b22b0e1d56e2b0bb8c5c927c0778a200bb66a7084454947aec00
---
@Watch用于快速计算，在UI重新渲染之前执行。不建议在@Watch函数中调用async和await，因为异步行为会延迟组件的重新渲染，可能导致性能问题。

**参考链接**

[@Watch装饰器：状态变量更改通知](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Watch装饰器：状态变量更改通知/arkts-watch.md>)
