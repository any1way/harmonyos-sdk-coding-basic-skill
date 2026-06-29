---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-2
title: Web组件的onLoadIntercept返回结果是否影响onInterceptRequest
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件的onLoadIntercept返回结果是否影响onInterceptRequest
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:df1cf56b587549d9d72a2734172b8a30d452a1a08ff8f4b3c5d981a3c71f6384
---
Web组件的onLoadIntercept的不同返回结果对应不同的操作：

* onLoadIntercept返回true时，直接拦截URL请求。
* onLoadIntercept返回false时，系统将触发onInterceptRequest回调。

**参考链接**

[onLoadIntercept](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/事件/arkts-basic-components-web-events.md#onloadintercept10>)
