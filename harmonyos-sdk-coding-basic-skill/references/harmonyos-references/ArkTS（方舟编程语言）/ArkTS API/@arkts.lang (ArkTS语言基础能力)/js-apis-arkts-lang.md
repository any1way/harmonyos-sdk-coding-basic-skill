---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang
title: @arkts.lang (ArkTS语言基础能力)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.lang (ArkTS语言基础能力)
category: harmonyos-references
scraped_at: 2026-06-01T15:35:40+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:24a7705f7109e1b0ca46de6cf779c409b7c30bf623dee78bf28f2281eb94334d
---
本模块提供ArkTS语言的基础类型定义。当前提供ISendable、RetentionPolicy和Retention接口。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { lang, Retention, RetentionPolicy } from '@kit.ArkTS';
```

## lang.ISendable

PhonePC/2in1TabletTVWearable

是所有[Sendable](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS并发/并发线程间通信/线程间通信对象/Sendable对象/Sendable对象简介/arkts-sendable.md#基础概念)类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

ArkTS中，ISendable类型的对象是Object类型的实例，遵循其基本特征，同时支持跨线程传递。

ISendable主要用在开发者自定义Sendable数据结构的场景中，ArkTS语言标准库中的容器类型（如[Array](<../@arkts.collections (ArkTS容器集)/Class (Array)/arkts-apis-arkts-collections-array.md>)、[Map](<../@arkts.collections (ArkTS容器集)/Class (Map)/arkts-apis-arkts-collections-map.md>)、[Set](<../@arkts.collections (ArkTS容器集)/Class (Set)/arkts-apis-arkts-collections-set.md>)等）隐式地继承并实现了ISendable。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**示例：**

```
1. // 构造一个用户自定义的Sendable数据结构
2. @Sendable
3. class CustomData implements lang.ISendable {
4. data1: number;
5. data2: string;
6. constructor(data1: number, data2: string) {
7. this.data1 = data1;
8. this.data2 = data2;
9. }
10. }
```

## RetentionPolicy24+

PhonePC/2in1TabletTVWearable

描述[注解](../../../../harmonyos-guides/基础入门/学习ArkTS语言/ArkTS语言介绍/introduction-to-arkts.md#注解)类型保留策略的枚举类型。其枚举值和[Retention](js-apis-arkts-lang.md#retention24)结合使用，以指定注解的生命周期。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOURCE | "source" | 注解将在编译期被移除。 |
| BYTECODE | "bytecode" | 注解将保留到编译产物中。 |

## Retention24+

PhonePC/2in1TabletTVWearable

系统提供的API注解能力，可用于指定自定义注解的生命周期。此注解只能标注在其他注解声明上。在自定义注解上标注Retention注解后，根据policy的不同取值，编译器会对自定义注解执行不同的保留策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| policy | [RetentionPolicy](js-apis-arkts-lang.md#retentionpolicy24) | 否 | 否 | 注解的保留策略。 |

**示例：**

```
1. import { Retention, RetentionPolicy } from '@kit.ArkTS';

3. // 构造一个用户自定义的源码态注解
4. @Retention({policy: RetentionPolicy.SOURCE})
5. @interface sourceAnnotation {
6. prop1: number
7. prop2: number
8. }

10. // 构造一个用户自定义的字节码态注解
11. @Retention({policy: RetentionPolicy.BYTECODE})
12. @interface bytecodeAnnotation {
13. prop1: number
14. prop2: number
15. }
```
