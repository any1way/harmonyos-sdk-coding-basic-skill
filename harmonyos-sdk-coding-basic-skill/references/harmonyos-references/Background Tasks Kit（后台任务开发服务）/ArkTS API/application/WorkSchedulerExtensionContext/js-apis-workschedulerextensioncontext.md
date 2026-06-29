---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext
title: WorkSchedulerExtensionContext
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > application > WorkSchedulerExtensionContext
category: harmonyos-references
scraped_at: 2026-06-01T15:56:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42c11dd35d8bbccda7210895924162e1eea6c9c5cf18b2cf0179634dfa655dd3
---
WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](<../../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。

WorkSchedulerExtensionContext可直接作为WorkSchedulerExtension的上下文环境，提供允许访问特定于WorkSchedulerExtensionAbility的资源的能力。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 使用说明

PhonePC/2in1TabletTVWearable

通过WorkSchedulerExtensionAbility子类实例来获取。

```
1. import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';

3. class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
4. onWorkStart(workInfo: workScheduler.WorkInfo) {
5. let WorkSchedulerExtensionContext = this.context; // 获取WorkSchedulerExtensionContext
6. }
7. }
```

## WorkSchedulerExtensionContext

PhonePC/2in1TabletTVWearable

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**模型约束：** 本模块接口仅可在Stage模型下使用。
