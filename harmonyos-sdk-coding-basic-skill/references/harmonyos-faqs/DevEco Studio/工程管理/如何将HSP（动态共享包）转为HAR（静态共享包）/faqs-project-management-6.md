---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-6
title: 如何将HSP（动态共享包）转为HAR（静态共享包）
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何将HSP（动态共享包）转为HAR（静态共享包）
category: harmonyos-faqs
scraped_at: 2026-06-01T17:05:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3b8d08f2b55ecfd20439a3203e803942b8b4dc293933f6ba1b5d742d46b9b03e
---
[HSP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)转换成[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)可参考如下步骤：

1. 在HSP下的module.json5中，把"type": "shared"修改为"type": "har"，删除"deliveryWithInstall"、"pages"字段。
2. 删除HSP中的页面。如果需要以页面形式使用，应改为命名路由或导航的写法。
3. 找到HSP下的hvigorfile.ts文件，将里面的hspTasks改为harTasks。
4. 编译该模块。如果编译过程中遇到错误，根据提示修改对应位置。
