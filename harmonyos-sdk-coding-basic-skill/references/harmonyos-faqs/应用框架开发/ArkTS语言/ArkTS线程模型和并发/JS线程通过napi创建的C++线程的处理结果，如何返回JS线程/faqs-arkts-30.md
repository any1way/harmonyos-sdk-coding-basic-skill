---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-30
title: JS线程通过napi创建的C++线程的处理结果，如何返回JS线程
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > JS线程通过napi创建的C++线程的处理结果，如何返回JS线程
category: harmonyos-faqs
scraped_at: 2026-06-12T10:24:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:27c302cba4610d649ccfd7dbdcc8a602b37a35d5fe8716d3102775219b04a758
---
使用napi\_create\_threadsafe\_function在JS线程创建可被任意线程调用的函数，在C++线程调用napi\_call\_threadsafe\_function将结果回调给主线程。

**参考链接**

[使用Node-API接口进行线程安全开发](../../../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API典型使用场景/使用Node-API接口进行线程安全开发/use-napi-thread-safety.md)
