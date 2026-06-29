---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_attestation_credential
title: FIDO2_PublicKeyAttestationCredential
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyAttestationCredential
category: harmonyos-references
scraped_at: 2026-06-11T16:11:44+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:8348ba5d7f2e7b4cb4242bfd3e6651d5a7958580934577fbb5746b3ee0398452
---
## 概述

定义获取注册结果结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [rawId](_f_i_d_o2___public_key_attestation_credential.md#rawid) | 原始凭据标识符。 |
| [FIDO2\_AuthenticatorAttestationResponse](../FIDO2_AuthenticatorAttestationResponse/_f_i_d_o2___authenticator_attestation_response.md) [response](_f_i_d_o2___public_key_attestation_credential.md#response) | 认证器证明响应。 |
| [FIDO2\_AuthenticatorAttachment](../../模块/通行密钥/passkey.md#fido2_authenticatorattachment-1) [authenticatorAttachment](_f_i_d_o2___public_key_attestation_credential.md#authenticatorattachment) | 认证器信息（平台、漫游）。默认值为FIDO2\_PLATFORM。可选。 |
| const char \* [id](_f_i_d_o2___public_key_attestation_credential.md#id) | 凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。 |
| const char \* [type](_f_i_d_o2___public_key_attestation_credential.md#type) | 此属性返回接口对象中指定凭据类型的插槽，它指定此对象所代表的凭据类型。 |
| [AuthenticationExtensionsClientOutputs](../AuthenticationExtensionsClientOutputs/_authentication_extensions_client_outputs.md) [clientExtensionResults](_f_i_d_o2___public_key_attestation_credential.md#clientextensionresults) | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |

## 结构体成员变量说明

### authenticatorAttachment

```
1. FIDO2_AuthenticatorAttachment FIDO2_PublicKeyAttestationCredential::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。可选。

### clientExtensionResults

```
1. AuthenticationExtensionsClientOutputs FIDO2_PublicKeyAttestationCredential::clientExtensionResults
```

**描述**

客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。

### id

```
1. const char* FIDO2_PublicKeyAttestationCredential::id
```

**描述**

凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。

### rawId

```
1. Uint8Buff FIDO2_PublicKeyAttestationCredential::rawId
```

**描述**

原始凭据标识符。

### response

```
1. FIDO2_AuthenticatorAttestationResponse FIDO2_PublicKeyAttestationCredential::response
```

**描述**

认证器证明响应。

### type

```
1. const char* FIDO2_PublicKeyAttestationCredential::type
```

**描述**

此属性返回接口对象中指定凭据类型的插槽，它指定此对象所代表的凭据类型。
