---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-debug
title: 调试意图
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 意图框架开发指导 > 调试意图
category: harmonyos-guides
scraped_at: 2026-06-01T10:58:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1329004f779e26b1219a1dcf7754894f519f112cbcc016e840287f8cea910cbd
---
## 概述

意图框架提供了一个意图调试工具，便于接入意图框架后进行意图调试。该工具支持查询意图、执行意图。

## 约束限制

仅支持在手机上进行意图调试，且对应的API版本不低于20。

## 功能接入

1. 开启意图调试能力。

   1. 打开设备的“设置”应用。
   2. 选择“系统”菜单。
   3. 选择“开发者选项”菜单。
   4. 选择“意图框架调试”菜单，开启该功能开关。
2. 查看意图：在意图框架调试页面，点击“查看设备上所有意图”。

   开发者可以在当前页面查看所有已注册的意图。
3. 调试意图。

   1. 配置意图参数。
   2. 点击“执行意图”。

      如果开发者实现的意图正确，则执行成功。执行结果：

   | 装饰器类型 | 执行模式 | 意图调用结果 |
   | --- | --- | --- |
   | [@InsightIntentLink](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintentlink>) | UI\_ABILITY\_FOREGROUND | 页面跳转，下方出现半模态窗口展示意图调用返回结果。 |
   | [@InsightIntentPage](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintentpage>) | UI\_ABILITY\_FOREGROUND | 页面跳转，下方出现半模态窗口展示意图调用返回结果。 |
   | [@InsightIntentEntry](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintententry>) | UI\_ABILITY\_FOREGROUND | 页面跳转，下方出现半模态窗口展示意图调用返回结果。 |
   | [@InsightIntentEntry](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintententry>) | UI\_ABILITY\_BACKGROUND | 下方出现半模态窗口展示意图调用返回结果。 |
   | [@InsightIntentEntry](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintententry>) | UI\_EXTENSION\_ABILITY | 下方出现半模态窗口展示内嵌[UIExtensionAbility](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)/js-apis-app-abili_64670486.md#uiextensionability>)页面。 |
   | [@InsightIntentFunctionMethod](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod>) | UI\_ABILITY\_BACKGROUND | 下方出现半模态窗口展示意图调用返回结果。 |
   | [@InsightIntentForm](<../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)/js-apis-app-ability-insightintentdecorator.md#insightintentform>) | - | 内嵌卡片页面，点击卡片可跳转至应用 |
