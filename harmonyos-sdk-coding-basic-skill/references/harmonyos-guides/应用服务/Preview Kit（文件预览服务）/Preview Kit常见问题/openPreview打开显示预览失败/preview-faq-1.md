---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-faq-1
title: openPreview打开显示预览失败
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > Preview Kit常见问题 > openPreview打开显示预览失败
category: harmonyos-guides
scraped_at: 2026-06-01T15:09:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c03298ed15d709f3247c17b9bebdc04bef8ff6cccb85980a39b253dd795273cb
---
Preview Kit的[openPreview](<../../../../../harmonyos-references/Preview Kit（文件预览服务）/ArkTS API/filePreview（文件预览）/preview-arkts.md#openpreview>)接口在传入文件预览信息时，当前仅支持传入文件的[uri](<../../../../应用框架/Core File Kit（文件基础服务）/用户文件/用户文件URI介绍/user-file-uri-intro.md>)，不支持传入文件的沙箱路径。

如果调用openPreview接口后，显示预览失败，请检查传入的是否为uri并且检查传入的uri是否存在。
