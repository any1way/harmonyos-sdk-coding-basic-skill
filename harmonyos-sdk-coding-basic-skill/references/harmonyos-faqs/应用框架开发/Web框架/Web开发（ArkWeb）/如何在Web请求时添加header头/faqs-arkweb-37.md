---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-37
title: 如何在Web请求时添加header头
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在Web请求时添加header头
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aef0862875b2b7f8a2d6da9c836d3f35b3730d1dcfb6fafa69beaea387e21ac0
---
可以通过loadUrl方法设置headers。该方法接收两个参数：url表示需要加载的URL，headers为数组类型表示附加的HTTP请求头。

```
1. // With parameter headers
2. this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
```

[AddHeader.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/AddHeader.ets#L34-L35)

**参考链接**

[loadUrl](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#loadurl>)

[WebHeader](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Interfaces (其他)/arkts-apis-webview-i.md#webheader>)
