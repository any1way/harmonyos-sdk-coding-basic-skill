---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-45
title: 如何让两个HSP不相互依赖，使用对方的组件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何让两个HSP不相互依赖，使用对方的组件
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee4731f0a747d3397aa503a99467f0b684e70203f2bf8b3a30ec7e2370475c88
---
可以将需要共用的组件抽离出来，然后放到一个共享包中使用，或者使用动态import实现依赖解耦。

**参考链接**

[HAR模块间动态import依赖解耦](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS运行时/ArkTS模块化/动态加载/arkts-dynamic-import.md#har模块间动态import依赖解耦)
