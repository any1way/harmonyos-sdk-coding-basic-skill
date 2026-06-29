---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-37
title: HAR如何转换为HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR如何转换为HSP
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f0c4c4426ea0a98b4d51e20cd189433171dd529ccaa04c3c0c15686749f65665
---
[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)转为[HSP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)主要是通过修改配置文件实现。具体步骤如下：

1. 在HAR的module.json5中，将type字段的值改为“shared”，并配置deliveryWithInstall字段为“true”。
2. 若HSP需要对外声明可跳转的页面，在module.json5文件中添加pages字段，并在“resources/base”目录下创建“profile/main\_pages.json”文件，配置“src”。
3. 将HAR的hvigorfile.ts文件中的“harTasks”更改为“hspTasks”。
4. HAR的build-profile.json5文件中默认生成consumerFiles字段，该项字段HAR可配置，为默认导出的[混淆加固](../../../../harmonyos-guides/构建应用/混淆加固/ide-build-obfuscation.md)规则，需要删除。

配置更改后重新编译。
