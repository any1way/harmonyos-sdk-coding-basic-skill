---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-36
title: 对于HAP包中引用的HSP包是否有数量限制
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 对于HAP包中引用的HSP包是否有数量限制
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d8735054797cd2d4daf2e5ebaabf28cf015c2afe06a8c52598d5192312f35952
---
目前没有明确的数量限制。

但是由于每个加载的[HSP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)都需要占用一定的系统资源，过多的HSP包会对应用的性能造成影响。

如果应用中HSP包数量过多，建议使用单[HAP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAP/hap-package.md)与多[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)方案，在动态加载场景中使用HSP。
