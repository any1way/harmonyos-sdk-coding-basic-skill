---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-16
title: 是否允许HAR的循环依赖
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 是否允许HAR的循环依赖
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:08ad037237ad1237419fcf13ca2d4a958486ca9824427cfcc8424971775635c0
---
不允许循环依赖。可以把公共部分放到一个共享包中，或者使用[HAR模块间动态import依赖解耦](../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS运行时/ArkTS模块化/动态加载/arkts-dynamic-import.md#har模块间动态import依赖解耦)。
