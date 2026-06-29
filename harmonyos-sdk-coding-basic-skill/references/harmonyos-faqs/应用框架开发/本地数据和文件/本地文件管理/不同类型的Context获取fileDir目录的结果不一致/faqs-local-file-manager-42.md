---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-42
title: 不同类型的Context获取fileDir目录的结果不一致
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 不同类型的Context获取fileDir目录的结果不一致
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6b9f7b66895b7a0a2c8d103850b836d4cedeb3fb023ddf1da673d092b5d53f3a
---
**问题描述**

不同类型的Context获取fileDir目录的结果存在差异。

1. 使用Application的Context获取的目录是“/data/storage/el2/base/files”。

2. 使用Ability的Context获取的目录是“/data/storage/el2/base/haps/entry/files”。

**问题澄清**

当前设计如下：Application可能包含多个Ability，每个Ability对应沙箱目录下的一个hap路径。

**参考链接**

[应用沙箱目录与应用沙箱路径](<../../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径>)
