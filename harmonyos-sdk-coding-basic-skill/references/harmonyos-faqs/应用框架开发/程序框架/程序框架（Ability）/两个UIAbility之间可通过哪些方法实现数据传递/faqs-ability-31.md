---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-31
title: 两个UIAbility之间可通过哪些方法实现数据传递
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 两个UIAbility之间可通过哪些方法实现数据传递
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3d1e46e3736d9859cad54d8c24a09de64ec48d112abffd432ecf2dfe7abb9bb6
---
两个UIAbility之间数据传递的方法如下，建议优先采用排序在前的方法。

* 方法一：调用startAbility接口启动另一个UIAbility时，通过wantInfo添加启动参数。也可以使用startAbilityForResult接口，获取被调用方UIAbility在关闭时返回的信息。
* 方法二：使用应用级别的状态管理，如 AppStorage、PersistentStorage、Environment，实现应用级或多个页面的状态数据共享。
* 方法三：在同一个应用中，UIAbility 之间的数据传递可以使用 AppStorage 或 LocalStorage 进行数据同步。
* 方法四：使用Emitter和Worker进行线程间通信。
* 方法五：使用CES（公共事件服务）进行进程间通信。
* 其他方法：通过Call调用实现UIAbility交互。

**参考链接**

[启动应用内的UIAbility组件](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/启动应用内的UIAbility组件/uiability-intra-device-interaction.md>)

[管理应用拥有的状态概述](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/管理应用拥有的状态概述/arkts-application-state-management-overview.md>)

[UIAbility组件与UI的数据同步](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件与UI的数据同步/uiability-data-sync-with-ui.md>)

[线程模型](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/线程模型/thread-model-stage.md>)

[公共事件简介](<../../../../../harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/进程线程通信/使用公共事件进行进程间通信/公共事件简介/common-event-overview.md>)
