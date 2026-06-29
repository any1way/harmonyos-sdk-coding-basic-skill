---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-34
title: 多个UIAbility是运行在一个进程还是多个进程中？三方应用是否支持应用运行在多个进程下？主进程结束了，会影响子进程的运行吗
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多个UIAbility是运行在一个进程还是多个进程中？三方应用是否支持应用运行在多个进程下？主进程结束了，会影响子进程的运行吗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:99a8d8b1d7f60c181f1163f78b178d280f5d6d2e5f856a5e5872a031ba9986b7
---
**PC/2in1设备**

* 不同模块的UIAbility运行在不同的进程中。
* 多个进程相互独立，其他进程的退出不会影响当前进程。

**其他设备**

* 多个UIAbility运行在同一个进程中。
* 三方应用的UIAbility不支持多进程运行，而Extension则运行在独立的进程中。
* 手机设备上的UIAbility均运行在单个进程中，不包含子进程。

**参考链接**

[进程模型](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/进程模型/process-model-stage.md>)
