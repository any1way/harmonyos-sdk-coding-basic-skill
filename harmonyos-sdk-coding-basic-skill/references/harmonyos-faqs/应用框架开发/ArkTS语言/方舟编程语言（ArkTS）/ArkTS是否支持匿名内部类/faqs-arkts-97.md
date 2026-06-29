---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-97
title: ArkTS是否支持匿名内部类
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持匿名内部类
category: harmonyos-faqs
scraped_at: 2026-06-12T10:23:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37f1f6d39468afa488dd1392b6c9d347a7083c9d77627c69b50ee47a2b0c5eba
---
ArkTS不支持匿名类，建议使用嵌套类实现。

因为使用匿名类创建的对象类型未知，这与ArkTS[不支持structural typing](../../../../../harmonyos-guides/基础入门/学习ArkTS语言/从TypeScript到ArkTS的适配指导/从TypeScript到ArkTS的适配规则/typescript-to-arkts-migration-guide.md#不支持structural-typing)和对象字面量的类型冲突。限制主要是考虑运行时的性能开销，需要显式声明类。

**参考链接**

[不支持使用类表达式](../../../../../harmonyos-guides/基础入门/学习ArkTS语言/从TypeScript到ArkTS的适配指导/从TypeScript到ArkTS的适配规则/typescript-to-arkts-migration-guide.md#不支持使用类表达式)
