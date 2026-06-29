---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-23
title: 从HAP的拆包中，如何区分是HAR和HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 从HAP的拆包中，如何区分是HAR和HSP
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:95d0f6991c565acb8f036575b59c14a23aca106e5c5c2837707d777399dc3bcc
---
HAP包拆包只能在module.json文件的dependencies字段看到引用的HSP模块名，看不到引用的HAR。HAR在编译时已打包在HAP包里，而HSP是单独成包的。.app文件安装时，HSP与HAP处于同一级别。

**参考链接**

[HAP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAP/hap-package.md)、[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)、[HSP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)
