---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-1
title: 点击服务卡片如何跳转至指定的页面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 点击服务卡片如何跳转至指定的页面
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e7d34c4eb5111876c6e285021edcdcff4f8675655b9ef548d45af4d99bf4a0c2
---
配置卡片事件，指定目标UIAbility进行跳转。

* 如果应用不在后台，可以在目标UIAbility的onWindowStageCreate()中调用loadContent加载指定的页面。
* 如果应用已在后台，可在目标UIAbility的onNewWant()中调用loadContent加载指定页面。

**参考链接**

[启动UIAbility的指定页面](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/启动应用内的UIAbility组件/uiability-intra-device-interaction.md#启动uiability的指定页面>)
