---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-180
title: 子组件事件能否传递到父组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 子组件事件能否传递到父组件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:42+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:6e1b592b2724e65b901c418eeed5ae8c336fc4f52cd262fc914843d8a16be5cc
---
ArkUI目前不支持直接的事件传递链机制。可以通过状态同步@Link或@Provide和@Consume进行父子组件间的状态通知，结合@Watch将状态变量的修改在组件间传递，实现类似功能。

**参考链接**

[@Link装饰器：父子双向同步](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Link装饰器：父子双向同步/arkts-link.md>)

[@Provide装饰器和@Consume装饰器：与后代组件双向同步](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Provide装饰器和@Consume装饰器：与后代组件双向同步/arkts-provide-and-consume.md>)

[@Watch装饰器：状态变量更改通知](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理组件拥有的状态/@Watch装饰器：状态变量更改通知/arkts-watch.md>)
