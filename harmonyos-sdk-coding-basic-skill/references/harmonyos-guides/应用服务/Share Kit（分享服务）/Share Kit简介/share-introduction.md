---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-introduction
title: Share Kit简介
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit简介
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:03+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:c1b32928b10f2c2d5ddf9bf539bb89f96aead4d69386e2e4cb65ef3094348244
---
Share Kit（分享服务）为应用提供文本、图片、视频等内容跨应用、跨端分享能力。

应用把需要分享的内容和预览样式配置给Share Kit，Share Kit将根据不同的场景进行使用：

* 针对应用间分享的场景，根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。
* 针对跨端分享的场景，根据分享的数据类型、数量等信息构建预览界面，用于跨端分享。

如果应用需要显示在分享面板，则需要构建数据处理能力并按照配置要求在应用配置文件中声明，社交类应用可以通过[意图框架](<../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)接口捐献联系人信息，可以让用户一步分享到应用内的指定用户。

Share Kit（分享服务）提供的[SampleCode示例工程](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts)体现了系统分享接入模式、文本/图片等分享示例、碰一碰分享示例及卡片模板，可参考该工程进行应用的相关内容开发。

**图1** 手机分享面板效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/OJf11hVpTYmUZZ5MWGkYFw/zh-cn_image_0000002592219610.png?HW-CC-KV=V1&HW-CC-Date=20260611T071458Z&HW-CC-Expire=86400&HW-CC-Sign=B9B4B13133894E6E6A779C7F70FA5341BF98BB2B8CEEC9F766B4823BA765F682)

**图2** 手机碰一碰跨端发起华为分享效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Xf-pf5DzQTmNvT5bm8z1Lw/zh-cn_image_0000002592379544.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071458Z&HW-CC-Expire=86400&HW-CC-Sign=C47A975A137D658FB6F78B60B460887F80334D11A0EA4FDAD54FCFFB7A05B3F5)

**图3** 手机与PC/2in1设备碰一碰分享效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/2syIDMhCRFWQsXZnjolJeA/zh-cn_image_0000002622859053.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071458Z&HW-CC-Expire=86400&HW-CC-Sign=561247CFC67EE079724BA2A9E4D88D03D546A9981055F13C5C62CA007257825E)

## 基本概念

* 宿主应用

  分享行为的发起者。通过调用分享接口，配置分享的内容、预览样式等信息后展示分享面板。
* 目标应用

  分享内容的接收者。需要在应用中构建数据处理能力并按照目标应用接入指南进行能力声明，使得包管理服务可以识别应用支持的能力。
* 内容区

  负责显示分享内容标题、预览、选择等信息，供用户选择。
* 推荐区

  对接华为分享和[意图框架](<../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)，通过算法高效、精准推荐能够处理内容的设备和目标应用用户。
* 分享方式区

  通过HarmonyOS的包管理服务获取支持分享内容的目标应用。支持2种跳转方式：

  1、跳转目标应用内UIAbility组件。

  2、跳转目标应用提供的ExtensionAbility组件（以下称为“分享详情页”）。

  应用组件需通过在[module.json5配置文件](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中配置UIAbility组件和ExtensionAbility组件的描述信息，以声明支持分享的能力。
* 操作区

  内容相关的操作，由系统提供的复制、保存、另存为、打印等能力。

## 运行机制

**图4** 分享运行机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Alq2kdBxQbi26Y2PUIhiig/zh-cn_image_0000002622699173.png?HW-CC-KV=V1&HW-CC-Date=20260611T071458Z&HW-CC-Expire=86400&HW-CC-Sign=B4C79688108604DDBD77E8985F364DDC5E369B65A3286B6DB3C87B8263836A07)

| 应用类型 | 相关逻辑 |
| --- | --- |
| 宿主应用 | 宿主应用需要对可分享的内容提供分享入口，在用户点击分享时，配置分享内容到分享，拉起系统分享面板。  - [通过分享面板发起分享](../系统分享/宿主应用发起分享/通过分享面板发起分享/share-mobilephone-app-share.md)  - [碰一碰分享](../碰一碰分享/手机与手机碰一碰分享/概述/knock-share-between-phones-overview.md) |
| 目标应用 | 1. 需要在应用中构建具有数据处理能力组件，包括以下两种分享方式。  - [应用内处理分享内容](../系统分享/目标应用处理分享内容/应用内处理分享内容/share-interface-description.md)  - [分享详情页处理分享内容](../系统分享/目标应用处理分享内容/分享详情页处理分享内容/share-sec-panel.md)  2. （可选）社交类应用可遵照[意图框架](<../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)接入规范把最近分享行为联系人相关信息捐献到[意图框架](<../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)，Share Kit可从[意图框架](<../../../AI/Intents Kit（意图框架服务）/Intents Kit简介/intents-introduction.md>)获取推荐信息，当用户选择推荐的联系人时，会把联系人信息随分享数据一起给到目标应用，目标应用可以根据联系人信息直接一步发送内容给指定用户。 |

## 约束与限制

* 设备限制

  | 能力 | 是否支持手机 | 是否支持平板 | 是否支持PC/2in1 | 是否支持TV |
  | --- | --- | --- | --- | --- |
  | 系统分享 | 支持 | 支持 | 支持 | 部分支持（仅支持分享到周边设备，不支持系统操作及分享给其他应用） |
  | 碰一碰分享 | 支持 | 支持 | 支持 | 不支持 |
  | 隔空传送 | 支持 | 支持 | 支持 | 不支持 |
* 使用限制

  + 宿主应用和目标应用定义数据类型须遵照[UDMF](../../../应用框架/ArkData（方舟数据管理）/标准化数据定义/标准化数据定义概述/unified-data-definition-overview.md)（统一数据管理框架）定义的[UTD](<../../../应用框架/ArkData（方舟数据管理）/标准化数据定义/标准化数据类型 (ArkTS)/uniform-data-type-descriptors.md>)（统一类型描述符）规范。目标应用需要在应用配置文件中，配置支持的类型。如支持全部图片类型，可声明为：general.image。
  + 宿主应用单次分享可配置[分享数据描述信息](<../../../../harmonyos-references/Share Kit（分享服务）/ArkTS API/systemShare（分享）/share-system-share.md#shareddata>)总量不能超过200KB，且分享条目总量不能超过500条。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](../../../编写与调试应用/使用模拟器运行应用/概述/模拟器与真机的差异/ide-emulator-specification.md)”。
