---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-overview
title: ArkTS卡片页面交互概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > ArkTS卡片页面交互概述
category: harmonyos-guides
scraped_at: 2026-06-01T11:11:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a4293c1f264ec7cf02266db3150b5ac2e983fa940f1f3990a2ac155e12e76310
---
ArkTS卡片提供页面交互能力，包括卡片与卡片提供方（例如：应用）的页面跳转、卡片拉起卡片提供方进程、卡片与卡片提供方的消息传递。其中[动态卡片](../../../ArkTS卡片概述/arkts-form-overview.md#动态卡片)可以使用[postCardAction](<../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/postCardAction/js-apis-postcardaction.md#postcardaction-1>)接口、[静态卡片](../../../ArkTS卡片概述/arkts-form-overview.md#静态卡片)使用[FormLink](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/卡片/FormLink/ts-container-formlink.md)实现页面交互功能。并且postCardAction和FormLink，均支持router、message和call三种类型的事件，具体使用场景如下：

* [router事件](../卡片跳转到应用页面（router事件）/arkts-ui-widget-event-router.md)：可以使用router事件跳转到指定UIAbility，以完成点击卡片跳转至应用内页面的功能。对于非系统应用仅支持跳转到自己应用内的UIAbility。
* [call事件](../卡片拉起应用UIAbility到后台（call事件）/arkts-ui-widget-event-call.md)：可以使用call事件拉起指定UIAbility到后台，再通过UIAbility申请对应后台长时任务完成音乐播放等功能。
* [message事件](../卡片传递消息给应用（message事件）/arkts-ui-widget-event-formextensionability.md)：可以使用message拉起[FormExtensionAbility](<../../../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)，通过[onFormEvent](<../../../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md#formextensionabilityonformevent>)接口回调通知，以完成点击卡片控件后传递消息给应用的功能。
