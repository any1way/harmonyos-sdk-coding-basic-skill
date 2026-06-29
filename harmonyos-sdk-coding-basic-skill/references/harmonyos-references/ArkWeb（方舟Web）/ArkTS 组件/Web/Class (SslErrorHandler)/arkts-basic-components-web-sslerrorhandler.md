---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-sslerrorhandler
title: Class (SslErrorHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (SslErrorHandler)
category: harmonyos-references
scraped_at: 2026-06-01T15:55:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2760c683196b9bce5d483d199aaf015d638d406c46cb617431c223901519a0c7
---
Web组件返回的SSL错误通知事件的处理对象。示例代码参考[onSslErrorEvent](../事件/arkts-basic-components-web-events.md#onsslerrorevent12)事件。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

SslErrorHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## handleCancel9+

PhonePC/2in1TabletTVWearable

handleCancel(): void

通知Web组件取消此请求。

**系统能力：** SystemCapability.Web.Webview.Core

## handleConfirm9+

PhonePC/2in1TabletTVWearable

handleConfirm(): void

通知Web组件继续使用SSL证书。

**系统能力：** SystemCapability.Web.Webview.Core

## handleCancel20+

PhonePC/2in1TabletTVWearable

handleCancel(abortLoading: boolean): void

通知Web组件取消此请求，并根据参数abortLoading决定是否停止加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abortLoading | boolean | 是 | 是否在取消请求后停止加载页面。  true表示停止加载页面，false表示继续加载页面。  默认值为false。 |
