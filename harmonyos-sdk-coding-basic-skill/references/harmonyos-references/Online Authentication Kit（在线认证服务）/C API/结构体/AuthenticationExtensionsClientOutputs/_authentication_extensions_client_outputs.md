---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs
title: AuthenticationExtensionsClientOutputs
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > AuthenticationExtensionsClientOutputs
category: harmonyos-references
scraped_at: 2026-06-11T16:11:23+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:4cc32e0a53de662506d21da3ea91933358285fcafc57d4cc24c513f67935f19f
---
## 概述

身份认证扩展输出。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [placeholder](_authentication_extensions_client_outputs.md#placeholder) | 占位符，表示返回的JSON消息中包含key值"clientExtensionResults"。始终返回NULL。 |

## 结构体成员变量说明

### placeholder

```
1. char* AuthenticationExtensionsClientOutputs::placeholder
```

**描述**

占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。该值始终返回NULL。
