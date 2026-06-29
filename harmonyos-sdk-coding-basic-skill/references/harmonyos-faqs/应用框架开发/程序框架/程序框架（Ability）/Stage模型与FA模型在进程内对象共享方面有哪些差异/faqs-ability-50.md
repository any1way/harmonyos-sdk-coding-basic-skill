---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-50
title: Stage模型与FA模型在进程内对象共享方面有哪些差异
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > Stage模型与FA模型在进程内对象共享方面有哪些差异
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed6df22267b522cdabe4acb4160f28774525035481411109d2dd03dbbede7d0b
---
* Stage模型中，多个应用组件共享同一个ArkTS引擎实例。应用组件之间可以方便地共享对象和状态，从而减少了复杂应用运行对内存的占用。
* FA模型中，每个应用组件独享一个ArkTS引擎实例。

Stage模型是主推的应用模型，开发者可以更方便地开发分布式场景下的复杂应用。

**参考链接**

[通过对比认识FA模型与Stage模型](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/应用模型/application-models.md#通过对比认识fa模型与stage模型>)
