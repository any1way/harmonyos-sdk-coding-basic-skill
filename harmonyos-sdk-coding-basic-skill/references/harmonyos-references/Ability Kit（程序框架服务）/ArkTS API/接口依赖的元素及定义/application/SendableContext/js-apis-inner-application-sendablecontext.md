---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext
title: SendableContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > SendableContext
category: harmonyos-references
scraped_at: 2026-06-01T15:31:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:52d1e14969b31598a8b82c6fd1a308f7ec6fdc52635ff465a7cc7cd5d6e344cf
---
SendableContext符合[Sendable协议](../../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/并发线程间通信/线程间通信对象/Sendable对象/Sendable对象简介/arkts-sendable.md#sendable协议)，继承自[lang.ISendable](<../../../../../ArkTS（方舟编程语言）/ArkTS API/@arkts.lang (ArkTS语言基础能力)/js-apis-arkts-lang.md#langisendable>)。

说明

* 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableContextManager } from '@kit.AbilityKit';
```

## SendableContext

PhonePC/2in1TabletTVWearable

SendableContext符合[Sendable协议](../../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/并发线程间通信/线程间通信对象/Sendable对象/Sendable对象简介/arkts-sendable.md#sendable协议)，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。
