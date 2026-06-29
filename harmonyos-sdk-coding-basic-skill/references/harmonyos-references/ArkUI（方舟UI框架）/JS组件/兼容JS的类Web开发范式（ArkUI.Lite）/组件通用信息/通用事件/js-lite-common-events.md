---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-events
title: 通用事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 组件通用信息 > 通用事件
category: harmonyos-references
scraped_at: 2026-06-01T15:47:27+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:629ffd2dc1ca0fbd4cd83f430db6e000ba20a8390ee807c60726d22d3e8dd603
---
## 事件说明

PhonePC/2in1TabletTVWearableLite Wearable

相对于私有事件，大部分组件都可以绑定如下事件。

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | SwipeEvent | 组件上快速滑动后触发。 |

## BaseEvent

PhonePC/2in1TabletTVWearableLite Wearable

基础事件类型。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 当前事件的类型，比如click、longpress等。 |
| timestamp | number | 该事件触发时的时间戳。  单位：ms |
| deviceId8+ | number | 触发该事件的设备ID信息。 |
| target12+ | [Target](../../../兼容JS的类Web开发范式（ArkUI.Full）/组件通用信息/通用事件/js-components-common-events.md#target对象6) | 触发该事件的目标对象。 |

## SwipeEvent

PhonePC/2in1TabletTVWearableLite Wearable

继承自[BaseEvent](js-lite-common-events.md#baseevent)。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| direction | string | 滑动方向，可能值有：  1. left：向左滑动；  2. right：向右滑动；  3. up：向上滑动；  4. down：向下滑动。 |
