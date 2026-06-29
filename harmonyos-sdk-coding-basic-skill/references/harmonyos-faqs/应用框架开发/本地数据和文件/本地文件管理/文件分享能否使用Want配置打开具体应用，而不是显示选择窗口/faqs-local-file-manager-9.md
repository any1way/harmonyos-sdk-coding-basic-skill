---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-9
title: 文件分享能否使用Want配置打开具体应用，而不是显示选择窗口
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 文件分享能否使用Want配置打开具体应用，而不是显示选择窗口
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3b9c10c4ad67341048c9189830891a058bd90feb57756cccdff428fa0a33b394
---
目前不支持使用Want配置打开具体应用。当前拉起的打开方式是通过设备内应用配置action: "ohos.want.action.sendData"来识别的，不能由业务自行指定。

**参考链接**

[应用文件分享](<../../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用文件分享/share-app-file.md>)
