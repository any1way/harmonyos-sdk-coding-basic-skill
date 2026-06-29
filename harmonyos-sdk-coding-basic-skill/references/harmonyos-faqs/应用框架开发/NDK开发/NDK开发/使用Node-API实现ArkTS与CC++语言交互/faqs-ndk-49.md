---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-49
title: 使用Node-API实现ArkTS与C/C++语言交互
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 使用Node-API实现ArkTS与C/C++语言交互
category: harmonyos-faqs
scraped_at: 2026-06-12T10:25:20+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:1b663b7be0e669981331f4a0f77c63df860b8d81856931455a19ac3df996a6cc
---
在ArkTS侧不能向C++层注册对象或函数，开发者需要在C++层自行处理。Env可以长期持有，但在使用Env时，必须在创建该Env的ArkTS线程中进行。

**参考链接**

[Native与ArkTS对象绑定](../../../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md)
