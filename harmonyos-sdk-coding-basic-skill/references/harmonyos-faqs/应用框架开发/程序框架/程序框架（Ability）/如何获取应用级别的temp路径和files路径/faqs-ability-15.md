---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-15
title: 如何获取应用级别的temp路径和files路径
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取应用级别的temp路径和files路径
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7184286d7ef29e9cdd5b7dcace2cc816e4299ad716414ddb66a1e8fe64a7017f
---
通过上下文 context 获取。例如：

* temp路径：通过 this.context.getApplicationContext().tempDir 获取。
* 文件路径：可通过 this.context.getApplicationContext().filesDir 获取。

**参考链接**

[获取应用文件路径](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#获取应用文件路径>)
