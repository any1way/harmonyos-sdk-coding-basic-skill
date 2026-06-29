---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-102
title: 如何实现Sendable类型和JSON数据的转换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现Sendable类型和JSON数据的转换
category: harmonyos-faqs
scraped_at: 2026-06-12T10:23:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2dac3188ad5a4ee3c89366cecf3ef57cd876ade1def3400f1c1bfb79007f1435
---
可以通过从API version 12开始支持的，ArkTS新增的[ArkTSUtils.ASON](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@arkts.utils (ArkTS工具库)/ArkTSUtils.ASON/arkts-apis-arkts-utils-ason.md>)工具实现。

ASON支持解析JSON字符串并生成共享数据，用于跨并发域传输。ASON还支持将共享数据转换为JSON字符串。
