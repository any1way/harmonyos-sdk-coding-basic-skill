---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-64
title: http请求传输大于5M文件报错2300023
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求传输大于5M文件报错2300023
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:79b5ff3e1ae22b6b51bcffcfdc79ed50952f29b11f4edd498d163b072efb97b7
---
http请求默认规格最大可传输5M数据文件（自API Version 23开始，该默认规格扩充至50MB），当http请求数据超过5M时，可在[HttpRequestOptions](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.http (数据请求)/js-apis-http.md#httprequestoptions>)的maxLimit中进行设置，将最大接收数据扩大到100M。如果超过100M大小，或者不确定数据大小但有可能超过100M时，建议使用[requestInStream](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.http (数据请求)/js-apis-http.md#requestinstream10>)接口发起流式请求。参考文档：[发起http流式传输请求](<../../../../../harmonyos-guides/系统/网络/Network Kit（网络服务）/访问网络/使用HTTP访问网络/http-request.md#发起http流式传输请求>)。
