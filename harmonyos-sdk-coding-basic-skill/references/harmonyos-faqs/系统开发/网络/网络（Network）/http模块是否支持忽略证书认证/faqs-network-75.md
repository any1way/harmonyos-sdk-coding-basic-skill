---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-75
title: http模块是否支持忽略证书认证
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http模块是否支持忽略证书认证
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3c2a9fc6b85dddfb723bc2b6ef44d8eb65703e7fdf63fabac6610bc1c089218a
---
在API18及以上版本中，http模块支持忽略SSL证书认证过程。可通过设置参数HttpRequestOptions中的remoteValidation为skip，以跳过验证服务端证书。

**参考链接**

[RemoteValidation](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.http (数据请求)/js-apis-http.md#remotevalidation18>)
