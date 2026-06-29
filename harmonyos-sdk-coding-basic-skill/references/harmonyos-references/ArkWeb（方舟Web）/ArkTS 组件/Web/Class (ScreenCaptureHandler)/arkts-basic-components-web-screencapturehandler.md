---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler
title: Class (ScreenCaptureHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (ScreenCaptureHandler)
category: harmonyos-references
scraped_at: 2026-06-01T15:55:25+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:f2f288d8167876b978b7cf3c457415ba20f57eab92891c42ad502316fe0d64ab
---
Web组件返回授权或拒绝屏幕捕获功能的对象。示例代码参考[onScreenCaptureRequest](../事件/arkts-basic-components-web-events.md#onscreencapturerequest10)事件。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 10开始支持。
* 示例效果请以真机运行为准。

## constructor10+

PhonePC/2in1TabletTVWearable

constructor()

ScreenCaptureHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## deny10+

PhonePC/2in1TabletTVWearable

deny(): void

拒绝网页所请求的屏幕捕获操作。

**系统能力：** SystemCapability.Web.Webview.Core

## getOrigin10+

PhonePC/2in1TabletTVWearable

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |

## grant10+

PhonePC/2in1TabletTVWearable

grant(config: ScreenCaptureConfig): void

对网页访问的屏幕捕获操作进行授权。

说明

需要配置权限：ohos.permission.MICROPHONE。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ScreenCaptureConfig](../Interfaces（其他）/arkts-basic-components-web-i.md#screencaptureconfig10) | 是 | 屏幕捕获配置。 |
