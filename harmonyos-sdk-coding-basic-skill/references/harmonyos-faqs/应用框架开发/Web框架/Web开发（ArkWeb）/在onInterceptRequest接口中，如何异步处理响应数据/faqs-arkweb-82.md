---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-82
title: 在onInterceptRequest接口中，如何异步处理响应数据
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 在onInterceptRequest接口中，如何异步处理响应数据
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4ee88a2af887cb11186a481721e6b343cbfdcf3c1e5bdf510519a7301a661456
---
可以使用[setResponseIsReady](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/Class (WebResourceResponse)/arkts-basic-components-web-webresourceresponse.md#setresponseisready9>)设置资源响应数据是否已经就绪。例如，在异步获取数据后，需调用`setResponseIsReady(true)`通知系统响应数据已准备就绪，具体可参考[onInterceptRequest](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/事件/arkts-basic-components-web-events.md#oninterceptrequest9>)示例代码。
