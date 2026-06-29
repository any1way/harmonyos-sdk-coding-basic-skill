---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-3
title: 如何实现文件不存在则创建文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何实现文件不存在则创建文件
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:50+08:00
doc_updated_at: 2026-05-15
content_hash: sha256:25f90135ba6965fb58953bea6a3fcf1a088919c55d1ef1e6f11e03ef0ff943f7
---
可以通过调用fileIo.open函数来实现，open(path: string, mode?: number)，指定第二个参数mode为fileIo.OpenMode.CREATE，表示如果文件不存在，则创建文件。

**参考链接**

[文件管理](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md>)
