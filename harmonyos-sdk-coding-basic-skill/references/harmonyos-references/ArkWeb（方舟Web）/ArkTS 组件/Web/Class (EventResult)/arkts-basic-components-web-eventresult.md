---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-eventresult
title: Class (EventResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (EventResult)
category: harmonyos-references
scraped_at: 2026-06-01T15:55:18+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:8c56512f396ed560be64526ba55f45fac23fc7ffdc1ea32f2f861955dae6a5b2
---
通知Web组件同层事件消费结果，支持的事件：[TouchType](../../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#touchtype)（触摸事件的类型）和[MouseAction](../../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#mouseaction8)（鼠标事件的类型），鼠标仅支持左中右按键，通过[MouseButton](../../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#mousebutton8)定义鼠标按键的类型。

如果应用不消费该事件，则应设置消费结果为false，事件将会被Web组件消费；反之如果应用消费了该事件，则应将消费结果设置为true，Web组件将不消费该事件。若应用设置消费结果不符合以上使用规格，将产生与开发者预期不匹配的现象。

触摸事件示例代码参考[onNativeEmbedGestureEvent](../事件/arkts-basic-components-web-events.md#onnativeembedgestureevent11)事件。

鼠标事件示例代码参考[onNativeEmbedMouseEvent](../事件/arkts-basic-components-web-events.md#onnativeembedmouseevent20)事件。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

EventResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## setGestureEventResult12+

PhonePC/2in1TabletTVWearable

setGestureEventResult(result: boolean): void

设置手势事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该手势事件。  true表示消费该手势事件，false表示不消费该手势事件。  传入null或undefined时为true。 |

**示例：**

请参考[onNativeEmbedGestureEvent](../事件/arkts-basic-components-web-events.md#onnativeembedgestureevent11)事件。

## setGestureEventResult14+

PhonePC/2in1TabletTVWearable

setGestureEventResult(result: boolean, stopPropagation: boolean): void

设置手势事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该手势事件。  true表示消费该手势事件，false表示不消费该手势事件。  传入null或undefined时为true。 |
| stopPropagation | boolean | 是 | 是否阻止冒泡，在result为true时生效。  true表示阻止冒泡，false表示不阻止冒泡。  传入null或undefined时为true。 |

**示例：**

请参考[onNativeEmbedGestureEvent](../事件/arkts-basic-components-web-events.md#onnativeembedgestureevent11)事件。

## setMouseEventResult20+

PhonePC/2in1TabletTVWearable

setMouseEventResult(result: boolean, stopPropagation?: boolean): void

设置鼠标事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该鼠标事件。  true表示消费该鼠标事件，false表示不消费该鼠标事件。  传入null或undefined时为true。 |
| stopPropagation | boolean | 否 | 是否阻止冒泡，在result为true时生效。  true表示阻止冒泡，false表示不阻止冒泡。  传入null或undefined时为true。  默认值：true。 |

**示例：**

请参考[onNativeEmbedMouseEvent](../事件/arkts-basic-components-web-events.md#onnativeembedmouseevent20)事件。
