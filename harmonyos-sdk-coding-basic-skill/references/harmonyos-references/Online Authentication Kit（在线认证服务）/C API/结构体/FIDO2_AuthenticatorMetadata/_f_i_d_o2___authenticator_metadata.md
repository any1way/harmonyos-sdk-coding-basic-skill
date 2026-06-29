---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata
title: FIDO2_AuthenticatorMetadata
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorMetadata
category: harmonyos-references
scraped_at: 2026-06-11T16:11:25+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:7637c0f06107c883a38c6404ccc9c6665b4281c056896bc9006e46bcc6bb6ea5
---
## 概述

认证器元数据。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [aaguid](_f_i_d_o2___authenticator_metadata.md#aaguid) | 认证器的aaguid。 |
| [FIDO2\_Uvm](../../模块/通行密钥/passkey.md#fido2_uvm-1) [uvm](_f_i_d_o2___authenticator_metadata.md#uvm) | 支持的认证器类型。 |
| bool [isAvailable](_f_i_d_o2___authenticator_metadata.md#isavailable) | 认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。 |

## 结构体成员变量说明

### aaguid

```
1. Uint8Buff FIDO2_AuthenticatorMetadata::aaguid
```

**描述**

认证器的aaguid。

### isAvailable

```
1. bool FIDO2_AuthenticatorMetadata::isAvailable
```

**描述**

认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。

### uvm

```
1. FIDO2_Uvm FIDO2_AuthenticatorMetadata::uvm
```

**描述**

支持的认证器类型。
