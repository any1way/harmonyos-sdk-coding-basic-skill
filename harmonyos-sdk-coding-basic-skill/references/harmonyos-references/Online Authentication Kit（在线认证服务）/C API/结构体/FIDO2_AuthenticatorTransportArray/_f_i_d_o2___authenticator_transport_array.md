---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array
title: FIDO2_AuthenticatorTransportArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorTransportArray
category: harmonyos-references
scraped_at: 2026-06-11T16:11:30+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:9af4d435674ed8e53c791bcd01eae08948aa12234943b3015c1734a0aeef1195
---
## 概述

认证器传输方式数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [transportNum](_f_i_d_o2___authenticator_transport_array.md#transportnum) | 传输方式数量。 |
| [FIDO2\_AuthenticatorTransport](../../模块/通行密钥/passkey.md#fido2_authenticatortransport-1) \* [transports](_f_i_d_o2___authenticator_transport_array.md#transports) | 认证器传输方式。 |

## 结构体成员变量说明

### transportNum

```
1. uint32_t FIDO2_AuthenticatorTransportArray::transportNum
```

**描述**

传输方式数量。

### transports

```
1. FIDO2_AuthenticatorTransport* FIDO2_AuthenticatorTransportArray::transports
```

**描述**

认证器传输方式。
