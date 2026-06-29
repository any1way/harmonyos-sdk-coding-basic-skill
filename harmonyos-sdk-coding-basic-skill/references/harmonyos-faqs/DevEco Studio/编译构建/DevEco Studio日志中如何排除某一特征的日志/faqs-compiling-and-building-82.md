---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-82
title: DevEco Studio日志中如何排除某一特征的日志
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio日志中如何排除某一特征的日志
category: harmonyos-faqs
scraped_at: 2026-06-01T17:06:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d13bafe9481601f7261ec91a2ac6a64528a36758cde02f25549a4d6df506b0c8
---
使用^(?!.\*xxx).\*$排除正则搜索日志，适用范围包括全量日志、domain 和 tag。

**参考链接**

[过滤日志](../../../../harmonyos-guides/编写与调试应用/日志与故障分析/日志分析/ide-setup-hilog.md#section1022292292216)
