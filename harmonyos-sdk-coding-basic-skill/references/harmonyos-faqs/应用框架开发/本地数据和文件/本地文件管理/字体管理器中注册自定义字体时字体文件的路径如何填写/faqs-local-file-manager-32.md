---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-32
title: 字体管理器中注册自定义字体时字体文件的路径如何填写
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 字体管理器中注册自定义字体时字体文件的路径如何填写
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:00728d7a9b401610087b9675b3377f8d95e5fa057791712af2771938461dd71a
---
建议将字体文件放置在rawfile目录中，通过路径/data/storage/el1/bundle/entry/resources/rawfile/进行访问。请注意，放置文件会占用应用安装所需的存储空间，避免放置过大的文件。

**参考链接**

[资源分类与访问](../../../../../harmonyos-guides/基础入门/资源分类与访问/resource-categories-and-access.md)
