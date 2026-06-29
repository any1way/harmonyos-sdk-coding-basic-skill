---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule
title: Class (ProxyRule)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (ProxyRule)
category: harmonyos-references
scraped_at: 2026-06-11T16:00:27+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:c50f3d9d77f7658e5c62dab598cb3bd978804738d770e10f8158a222395e72a9
---
[insertProxyRule](<../Class (ProxyConfig)/arkts-apis-webview-proxyconfig.md#insertproxyrule15>)中使用的代理规则。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 15开始支持。
* 示例效果请以真机运行为准。

## getSchemeFilter15+

PhonePC/2in1TabletTVWearable

getSchemeFilter(): ProxySchemeFilter

获取代理规则中的ProxySchemeFilter信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProxySchemeFilter](../Enums/arkts-apis-webview-e.md#proxyschemefilter15) | 代理规则中的ProxySchemeFilter信息。 |

**示例：**

完整示例代码参考[removeProxyOverride](<../Class (ProxyController)/arkts-apis-webview-proxycontroller.md#removeproxyoverride15>)。

## getUrl15+

PhonePC/2in1TabletTVWearable

getUrl(): string

获取代理规则中的代理的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 代理规则中的代理的URL信息。 |

**示例：**

完整示例代码参考[removeProxyOverride](<../Class (ProxyController)/arkts-apis-webview-proxycontroller.md#removeproxyoverride15>)。
