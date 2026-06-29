---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-46
title: 解决冷启动picker选择器无权限问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 解决冷启动picker选择器无权限问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:18+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:ad8b5ec610a662b3614086ecbf145f1f59a5012189e46daf4547c849b2129aa9
---
在APP冷启动后，由于没有uri的读取权限，可以通过保存草稿操作将对应的文件复制到沙箱路径下，然后在冷启动时获取这些文件。

**参考链接**

[fileIo.copyFile](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#fileiocopyfile>)

[应用沙箱目录](<../../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)
