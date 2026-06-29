---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-62
title: 使用Web组件，在哪个回调事件中可以设置自定义用户代理
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 使用Web组件，在哪个回调事件中可以设置自定义用户代理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:89581dc8aaa704905a1850ff0ed16559c37d8da757975f6311cabbb69a090181
---
建议在[onControllerAttached](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/事件/arkts-basic-components-web-events.md#oncontrollerattached10>)回调事件中，使用[setCustomUserAgent](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10>)来设置自定义用户代理。
