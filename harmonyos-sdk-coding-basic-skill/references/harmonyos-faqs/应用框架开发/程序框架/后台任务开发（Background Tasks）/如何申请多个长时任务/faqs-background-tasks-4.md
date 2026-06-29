---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-4
title: 如何申请多个长时任务
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何申请多个长时任务
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:760757de2c88eaf0b36aa3fea66ad01f095786e5c96abfd7ff7ba758141e7b1e
---
**问题现象**

应用在后台运行多个任务，需申请多个长时任务。

**解决措施**

同一时刻，一个UIAbility只能申请一个长时任务。需要创建多个UIAbility来申请不同种类的长时任务。不同时刻可以申请不同种类的长时任务。

**参考链接**

[长时任务](<../../../../../harmonyos-guides/应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)
