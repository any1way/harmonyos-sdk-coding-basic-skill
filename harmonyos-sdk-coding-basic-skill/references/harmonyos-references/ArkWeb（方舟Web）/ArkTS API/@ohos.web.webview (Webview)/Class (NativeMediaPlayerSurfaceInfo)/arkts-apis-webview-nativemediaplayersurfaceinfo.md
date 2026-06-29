---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo
title: Class (NativeMediaPlayerSurfaceInfo)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (NativeMediaPlayerSurfaceInfo)
category: harmonyos-references
scraped_at: 2026-06-01T15:54:26+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:32055b7c41b1b0c94c3a6370637535d4333179f944080d1bcb63d1467b77a18a
---
使用[enableNativeMediaPlayer](<../../../ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#enablenativemediaplayer12>)来进行同层渲染的surface信息配置，以开启应用接管网页媒体播放功能。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id12+ | string | 否 | 否 | surface的id，用于同层渲染的NativeImage的surfaceId。  详见[NativeEmbedDataInfo](<../../../ArkTS 组件/Web/Interfaces（其他）/arkts-basic-components-web-i.md#nativeembeddatainfo11>)。 |
| rect12+ | [RectEvent](<../Interfaces (其他)/arkts-apis-webview-i.md#rectevent12>) | 否 | 否 | surface的位置信息。 |
