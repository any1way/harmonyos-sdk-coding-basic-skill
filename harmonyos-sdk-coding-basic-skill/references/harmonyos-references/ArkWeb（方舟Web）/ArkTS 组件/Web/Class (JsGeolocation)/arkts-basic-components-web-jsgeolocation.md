---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsgeolocation
title: Class (JsGeolocation)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (JsGeolocation)
category: harmonyos-references
scraped_at: 2026-06-01T15:55:23+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6eda8bc4ba95234ba3aec54861e24134c8b01054da828c1abccca3455baae5f9
---
Web组件返回授权或拒绝权限功能的对象。示例代码参考[onGeolocationShow事件](../事件/arkts-basic-components-web-events.md#ongeolocationshow)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

PhonePC/2in1TabletTVWearable

constructor()

JsGeolocation的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## invoke

PhonePC/2in1TabletTVWearable

invoke(origin: string, allow: boolean, retain: boolean): void

设置网页地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串。 |
| allow | boolean | 是 | 设置的地理位置权限状态。  true表示开启地理位置权限，false表示不开启地理位置权限。 |
| retain | boolean | 是 | 是否允许将地理位置权限状态保存到系统中。可通过[GeolocationPermissions9+](<../../../ArkTS API/@ohos.web.webview (Webview)/Class (GeolocationPermissions)/arkts-apis-webview-geolocationpermissions.md>)接口管理保存到系统的地理位置权限。  true表示允许将地理位置权限状态保存到系统中，false表示不允许将地理位置权限状态保存到系统中。 |
