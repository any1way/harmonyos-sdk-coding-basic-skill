---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions
title: Class (BackForwardCacheOptions)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (BackForwardCacheOptions)
category: harmonyos-references
scraped_at: 2026-06-11T16:00:17+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:061c4acce05f12be2a8f43bbc6557ac26ad5059622c0d174d9608c8deb22bd39
---

前进后退缓存相关设置对象，用来控制Web组件前进后退缓存相关选项。

说明

* 本模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

**系统能力：** SystemCapability.Web.Webview.Core

## 属性

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size12+ | number | 否 | 否 | 设置每个Web组件允许缓存的最大页面个数。  默认为1，最大可设置为50。  设置为0或负数时，前进后退缓存功能不生效。  Web组件会根据内存压力对缓存进行回收。 |
| timeToLive12+ | number | 否 | 否 | 设置每个Web组件允许页面在前进后退缓存中停留的时间。  设置为0或负数时，前进后退缓存功能不生效。  默认值：600。  单位：秒。 |

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

BackForwardCacheOptions的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
