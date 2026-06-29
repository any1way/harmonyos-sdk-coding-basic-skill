---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-13
title: 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:91839ba47a4000a5e22afdb6c7fa8b2ac4650c9e03b9f59ccdf4b5cbfddcc44b
---
**问题详情**

ArkTS层创建的ArrayBuffer和Uint8Array对象在Native层无法正确区分。

**解决措施**

1. 使用[napi\_is\_arraybuffer](../../../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API使用指导/使用Node-API接口进行ArrayBuffer相关开发/use-napi-about-arraybuffer.md#napi_is_arraybuffer)接口判断数据是否为ArrayBuffer类型，若类型符合则结果为true。
2. 使用[napi\_is\_typedarray](../../../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API使用指导/使用Node-API接口进行array相关开发/use-napi-about-array.md#napi_is_typedarray)接口判断Uint8Array类型数据，若类型符合则结果为true。
