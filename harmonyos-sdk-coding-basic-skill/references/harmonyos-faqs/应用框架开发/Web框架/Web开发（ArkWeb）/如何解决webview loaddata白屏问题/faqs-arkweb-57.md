---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-57
title: 如何解决webview loaddata白屏问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决webview loaddata白屏问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:78a83428e430c8288ca2245d1b7b05253dfbedde1c6b2e8f4b2250762a9dce26
---
loadData使用不同的参数会有不同的效果，如果参数不对可能会造成白屏现象。如果html中存在非法字符，例如css中的color: "#333"，有"#"的时候会加载不了，需要使用文档中提供的加载本地资源的方法，后面两个参数要设置为空格" "，" "。具体实现可参考[loadData](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#loaddata>)。
