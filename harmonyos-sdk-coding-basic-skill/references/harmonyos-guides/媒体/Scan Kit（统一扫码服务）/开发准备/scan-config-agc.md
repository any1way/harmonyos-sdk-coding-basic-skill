---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-config-agc
title: 开发准备
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-06-01T11:31:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a0b7280b68c5f15681911c34aa59082226e7195f3428bf411e0b9b2379ed37b
---
1. 参考“[应用开发准备](../../../应用开发准备/应用开发准备/application-dev-overview.md)”完成基本准备工作。
2. （**仅针对“扫码直达”必选**）接入[App Linking](<../../../应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md>)，您需要完成以下步骤：

   1. 在AGC控制台开通App Linking服务。
   2. 在开发者网站上关联应用。
   3. 在App Linking中配置二维码、条形码关联的网址域名。
   4. 在应用的module.json5文件中关联域名。

说明

* App Linking方式当前仅支持HTTPS网址，具备应用和网页两种呈现方式。当应用安装时则优先直达应用内服务页，当应用未安装时，浏览器也可以为用户提供服务。
* App Linking还广泛应用于社交分享、沉默唤醒、广告引流等场景。
* 接入App Linking不能使用DevEco的自动签名功能，必须使用[手动签名](../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)。
