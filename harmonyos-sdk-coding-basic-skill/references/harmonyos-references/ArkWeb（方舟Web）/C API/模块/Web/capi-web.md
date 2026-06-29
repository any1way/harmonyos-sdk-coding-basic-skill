---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web
title: Web
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 模块 > Web
category: harmonyos-references
scraped_at: 2026-06-01T15:55:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ae394dd7137459161baef657f073134a845c035248274b4b67ef140b4e3291c5
---
## 概述

PhonePC/2in1TabletTVWearable

为ArkWeb NDK接口发生异常提供错误码。

提供注入对象和执行JavaScript代码的API接口。

提供用于拦截ArkWeb请求的API。

为ArkWeb网络协议栈提供错误码。

提供ArkWeb在Native侧的能力，如网页刷新、执行JavaScript、注册回调等。

更多详细介绍请参考[应用侧与前端页面的相互调用(C/C++)](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/在应用中使用前端页面JavaScript/应用侧与前端页面的相互调用(CC++)/arkweb-ndk-jsbridge.md)、[建立应用侧与前端页面数据通道(C/C++)](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/在应用中使用前端页面JavaScript/建立应用侧与前端页面数据通道(CC++)/arkweb-ndk-page-data-channel.md)和[拦截Web组件发起的网络请求](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/管理网页加载与浏览记录/拦截Web组件发起的网络请求/web-scheme-handler.md)。

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [arkweb\_error\_code.h](../../头文件/arkweb_error_code.h/capi-arkweb-error-code-h.md) | 声明ArkWeb NDK接口异常错误码。 |
| [arkweb\_interface.h](../../头文件/arkweb_interface.h/capi-arkweb-interface-h.md) | 提供ArkWeb在Native侧获取API的接口，及基础Native API类型。 |
| [arkweb\_net\_error\_list.h](../../头文件/arkweb_net_error_list.h/capi-arkweb-net-error-list-h.md) | 声明ArkWeb网络协议栈错误码。 |
| [arkweb\_scheme\_handler.h](../../头文件/arkweb_scheme_handler.h/capi-arkweb-scheme-handler-h.md) | 声明用于拦截来自ArkWeb的请求的API。 |
| [arkweb\_type.h](../../头文件/arkweb_type.h/capi-arkweb-type-h.md) | 提供ArkWeb在Native侧的公共类型定义。 |
| [native\_interface\_arkweb.h](../../头文件/native_interface_arkweb.h/capi-native-interface-arkweb-h.md) | 声明API接口供开发者使用注入对象和执行JavaScript代码等功能。 |
