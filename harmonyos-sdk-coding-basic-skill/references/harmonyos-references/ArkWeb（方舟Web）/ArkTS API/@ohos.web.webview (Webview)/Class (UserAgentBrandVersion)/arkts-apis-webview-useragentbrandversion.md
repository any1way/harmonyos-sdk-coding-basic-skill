---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-useragentbrandversion
title: Class (UserAgentBrandVersion)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (UserAgentBrandVersion)
category: harmonyos-references
scraped_at: 2026-06-01T15:54:51+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:edbc172ac8efda4c4d0b162d40b25f8ab91698734f2c1e2d7be68b09b84c3523
---
可以通过该类提供的接口对UserAgentBrandVersion进行配置。

说明

* 本模块首批接口从API version 24开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 24开始支持。
* 示例效果请以真机运行为准。

## setBrand

PhonePC/2in1TabletTVWearable

setBrand(brand: string): void

设置品牌名称。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brand | string | 是 | 品牌名称，不能为空字符串。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。

## getBrand

PhonePC/2in1TabletTVWearable

getBrand(): string

获取品牌名称。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 品牌名称。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。

## setMajorVersion

PhonePC/2in1TabletTVWearable

setMajorVersion(majorVersion: string): void

设置主版本号。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| majorVersion | string | 是 | 主版本号，不能为空字符串。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。

## getMajorVersion

PhonePC/2in1TabletTVWearable

getMajorVersion(): string

获取主版本号。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 主版本号。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。

## setFullVersion

PhonePC/2in1TabletTVWearable

setFullVersion(fullVersion: string): void

设置完整版本号。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullVersion | string | 是 | 完整版本号，不能为空字符串。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。

## getFullVersion

PhonePC/2in1TabletTVWearable

getFullVersion(): string

获取完整版本号。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 完整版本号。 |

**示例：**

完整示例代码参考[setUserAgentClientHintsEnabled](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)。
