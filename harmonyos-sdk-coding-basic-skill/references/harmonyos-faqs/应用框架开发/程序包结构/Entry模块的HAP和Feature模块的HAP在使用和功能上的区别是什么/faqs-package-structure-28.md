---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-28
title: Entry模块的HAP和Feature模块的HAP在使用和功能上的区别是什么
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > Entry模块的HAP和Feature模块的HAP在使用和功能上的区别是什么
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e2f600e9f25a617cc7cb28a48fa3d2e53762787721d123b284ca18c8277bec9
---
* Entry类型的HAP：是应用的主模块，在module.json5配置文件中的type标签配置为“entry”类型。在同一个应用中，同一设备类型只支持一个Entry类型的HAP，通常用于实现应用的入口界面、入口图标、主特性功能等。
* Feature类型的HAP：是应用的动态特性模块，在module.json5配置文件中的type标签配置为“feature”类型。一个应用程序包可以包含一个或多个Feature类型的HAP，也可以不包含；Feature类型的HAP通常用于实现应用的特性功能，可以配置成按需下载安装，也可以配置成随Entry类型的HAP一起下载安装。

**参考链接**

[应用程序包结构](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包结构/application-package-structure.md)
