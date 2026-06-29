---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-45
title: 如何判断文件是不是目录
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何判断文件是不是目录
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:18+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:16da03751e54d0a91b66f45fe2dc39aa37001e33d01b2f43fc3b388fa0797659
---
判断文件是否为目录可以使用方法 fileIo.statSync(dirPath).isDirectory()。返回结果为 true 表示是目录。

**参考链接**

[isDirectory](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#isdirectory>)
