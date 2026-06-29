---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-2
title: 证书链校验器的参数如何获取
breadcrumb: FAQ > 系统开发 > 安全 > 证书管理（Device Certificate） > 证书链校验器的参数如何获取
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5b21c7176924512818ea4d355944423dd9f5bcb2230507a22482d3b926f3a1f4
---
可通过[getSubjectName](<../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md#getsubjectname>)和[getPublicKey](<../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md#getpublickey>)接口获取CASubject和CAPubKey的字节数据，然后将值传入CertChainValidationParameters。
