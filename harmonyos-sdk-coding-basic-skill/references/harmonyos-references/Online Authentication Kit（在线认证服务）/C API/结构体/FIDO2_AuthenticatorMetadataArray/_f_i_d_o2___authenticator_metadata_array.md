---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array
title: FIDO2_AuthenticatorMetadataArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorMetadataArray
category: harmonyos-references
scraped_at: 2026-06-11T16:11:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fff2924af4ed2d7b066cb51675a4dde38202cf35f00cad1459e83e4d1a3c29f6
---
## 概述

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [number](_f_i_d_o2___authenticator_metadata_array.md#number) | 认证器数目。 |
| [FIDO2\_AuthenticatorMetadata](../FIDO2_AuthenticatorMetadata/_f_i_d_o2___authenticator_metadata.md) \* [authenticators](_f_i_d_o2___authenticator_metadata_array.md#authenticators) | 认证器支持的扩展。 |

## 结构体成员变量说明

### authenticators

```
1. FIDO2_AuthenticatorMetadata* FIDO2_AuthenticatorMetadataArray::authenticators
```

**描述**

认证器支持的扩展。

### number

```
1. uint32_t FIDO2_AuthenticatorMetadataArray::number
```

**描述**

认证器数目。
