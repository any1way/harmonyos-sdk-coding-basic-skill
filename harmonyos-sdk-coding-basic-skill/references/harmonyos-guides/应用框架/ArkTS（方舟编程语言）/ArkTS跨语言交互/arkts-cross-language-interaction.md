---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-cross-language-interaction
title: ArkTS跨语言交互
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS跨语言交互
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fd1440a3c6033dedbb1ac1e17fa38520e6195eb5fe4cb1a3721bb010e479720c
---
除了支持使用ArkTS开发外，开发者还可以通过Node-API实现ArkTS与C/C++(Native)的跨语言交互能力。

HarmonyOS的Node-API是基于Node.js社区版本的扩展实现，但与原生Node-API并不完全兼容。

开发者可参考[使用Node-API进行跨语言开发流程](../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md)，基于[Node-API支持的数据类型](../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API支持的数据类型和接口/napi-data-types-interfaces.md#node-api的数据类型)和[Node-API接口](../../../../harmonyos-references/Node-API/napi.md)进行Native能力的开发和封装，并通过在ArkTS侧导入Native模块的方式实现跨语言调用。

[Node-API扩展能力接口](../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API使用指导/使用Node-API进行扩展能力功能开发/use-napi-about-extension.md)提供了增强功能，支持更灵活的ArkTS交互和自定义对象创建。开发者可结合Node-API的扩展能力进行功能扩展，并参考[Node-API开发规范](../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API开发规范/napi-guidelines.md)和[Node-API常见问题](../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API常见问题汇总/Node-API常见问题/use-napi-faqs.md)进行跨语言功能开发。
