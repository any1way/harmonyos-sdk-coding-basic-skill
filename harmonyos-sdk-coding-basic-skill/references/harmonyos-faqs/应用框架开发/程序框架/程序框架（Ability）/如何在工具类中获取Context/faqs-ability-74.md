---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-74
title: 如何在工具类中获取Context
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在工具类中获取Context
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:53+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:37083ac67947065959473d93059875b7bb034920ccd8f134a24735abbcd1357b
---
工具类中无法直接获取Context。可以在获取应用上下文Context后保存至AppStorage。工具类中使用AppStorage获取Context。

**参考链接**

[应用上下文Context](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md>)

[AppStorage：应用全局的UI状态存储](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md>)
