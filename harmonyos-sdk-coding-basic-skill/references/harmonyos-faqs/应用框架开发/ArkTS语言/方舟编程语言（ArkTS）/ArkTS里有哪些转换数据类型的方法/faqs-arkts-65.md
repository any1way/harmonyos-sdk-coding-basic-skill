---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-65
title: ArkTS里有哪些转换数据类型的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS里有哪些转换数据类型的方法
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:57+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8ee4d7689131e0817d32d705cdeb4ebf2c27ec91c9f389addd8a9256d19c17ee
---
ArkTS支持通过JavaScript/TypeScript的内置方法进行类型转换，例如Number(), String(), Boolean()等。

ArkTS支持TS语义的as类型转换，不支持使用<>运算符进行类型转换。当前as类型转换只能用在编译时，无法通过as在运行时进行类型转换。

**参考链接**

[从TypeScript到ArkTS的适配规则](../../../../../harmonyos-guides/基础入门/学习ArkTS语言/从TypeScript到ArkTS的适配指导/从TypeScript到ArkTS的适配规则/typescript-to-arkts-migration-guide.md)
