---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult
title: Class (JsResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (JsResult)
category: harmonyos-references
scraped_at: 2026-06-01T15:55:23+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:760958598ac43fb35614a941523726b57a5c2f858cd87273c6e661ba0ecf2da2
---
Web组件返回的弹窗确认或取消功能对象。示例代码参考[onAlert事件](../事件/arkts-basic-components-web-events.md#onalert)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

PhonePC/2in1TabletTVWearable

constructor()

JsResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## handleCancel

PhonePC/2in1TabletTVWearable

handleCancel(): void

通知Web组件用户取消弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handleConfirm

PhonePC/2in1TabletTVWearable

handleConfirm(): void

通知Web组件用户确认弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handlePromptConfirm9+

PhonePC/2in1TabletTVWearable

handlePromptConfirm(result: string): void

通知Web组件用户确认弹窗操作及对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | string | 是 | 用户输入的对话框内容。 |
