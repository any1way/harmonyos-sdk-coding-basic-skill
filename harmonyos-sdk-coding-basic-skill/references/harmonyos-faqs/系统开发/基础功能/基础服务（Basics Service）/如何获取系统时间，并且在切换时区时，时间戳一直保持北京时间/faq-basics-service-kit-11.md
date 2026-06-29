---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-11
title: 如何获取系统时间，并且在切换时区时，时间戳一直保持北京时间
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何获取系统时间，并且在切换时区时，时间戳一直保持北京时间
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9a7d62f7a1335caf08bbcdf1c53699788f5e8d1302ae940cbc39a7a77a28fc6d
---
使用[systemDateTime.getTime()](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.systemDateTime (系统时间、时区)/js-apis-date-time.md#systemdatetimegettime10>)可以获取自Unix纪元以来经过的时间。getTime获取的是Unix时间戳，Unix时间戳和时区无关，在任何时区返回的值都是一致的。
