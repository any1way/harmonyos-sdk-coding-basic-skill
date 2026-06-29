---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-faq-2
title: 使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > Preview Kit常见问题 > 使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败
category: harmonyos-guides
scraped_at: 2026-06-01T15:09:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c6fbbb8b87c6dc72f6ccb18d6dfac6b47c7e8cb518329a9fbbb5bf20263d341f
---
DocumentViewPicker拿到的文件uri应用仅有临时权限，该权限无法分享给预览，导致预览失败。可先对uri[持久化权限](<../../../../应用框架/Core File Kit（文件基础服务）/用户文件/选择与保存用户文件/授权持久化/file-persistpermission.md>)，然后再采用openPreview打开文件；或者可以先将文件拷贝至应用沙箱内，再预览沙箱内文件。
