---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-35
title: 如何实现Web和Webview对前端常用框架（如Vue，React）的适配
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何实现Web和Webview对前端常用框架（如Vue，React）的适配
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13726dccf44acc4a811e5e1bb52dc0838767fedf7d37a7ccb65c15b1975e4ae4
---
以Vue工程为例，使用runJavaScript API和javaScriptProxy API实现与Vue工程的交互。

* runJavaScript API异步执行JavaScript脚本并返回结果。
* javaScriptProxy API注入JavaScript对象到window对象并调用方法。
* 可以将Vue中的方法绑定到document对象上，实现Vue与JavaScript脚本的交互。

**参考链接**

[runJavaScript](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#runjavascript>)

[javaScriptProxy](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#javascriptproxy>)
