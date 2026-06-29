---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-118
title: UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a46e386e1a18c8baee9404cbf275c3f8ae87092c8dd4270cb68f10aca4a4a95c
---
1. Ability的上下文是AbilityContext。ArkUI实例的上下文是[UIContext](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/UI系统场景化能力/使用UI上下文接口操作界面（UIContext）/arkts-global-interface.md>)，由窗口创建并管理所有UI对象。窗口可以通过[windowStage.loadContent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#loadcontent9>)拉起ArkUI实例。
2. Ability是应用管理生命周期的对象，持有window对象。
3. UIAbility的上下文是UIAbilityContext。UIContext与UIAbilityContext没有直接联系，无法互相转化。
