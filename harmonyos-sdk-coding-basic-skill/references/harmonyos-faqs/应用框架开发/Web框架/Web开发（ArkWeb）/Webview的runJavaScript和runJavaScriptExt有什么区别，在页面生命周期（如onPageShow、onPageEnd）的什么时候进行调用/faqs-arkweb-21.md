---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-21
title: Webview的runJavaScript和runJavaScriptExt有什么区别，在页面生命周期（如onPageShow、onPageEnd）的什么时候进行调用
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Webview的runJavaScript和runJavaScriptExt有什么区别，在页面生命周期（如onPageShow、onPageEnd）的什么时候进行调用
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1f4012f275a962beb05e82e4f0b6b11daabde3eddbed20c4d59d5f50966d2fac
---
二者均可异步执行JavaScript脚本，并通过回调或Promise返回执行结果。

区别上讲，[runJavaScript](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#runjavascript>)返回脚本执行的结果只能是string，而[runJavaScriptExt](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#runjavascriptext10>)可以返回的类型支持[JsMessageType](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Enums/arkts-apis-webview-e.md#jsmessagetype10>)，包括字符串、数组类型等。

runJavaScript参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | AsyncCallback<string> | 是 | 回调函数执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。 |

runJavaScriptExt参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | AsyncCallback<[JsMessageExt](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (JsMessageExt)/arkts-apis-webview-jsmessageext.md>)> | 是 | 回调执行JavaScript脚本结果。 |

在调用时间上，二者均需在loadUrl完成后，例如在onPageEnd中调用。
