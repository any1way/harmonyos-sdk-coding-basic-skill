---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_attestation_response
title: FIDO2_AuthenticatorAttestationResponse
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorAttestationResponse
category: harmonyos-references
scraped_at: 2026-06-11T16:11:25+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:c5505010dfd8e078103674a5b6e2d2c7151922f6e02cb0f26423ab5531c29579
---
## 概述

认证器声明响应。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [attestationObject](_f_i_d_o2___authenticator_attestation_response.md#attestationobject) | 声明对象。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [clientDataJson](_f_i_d_o2___authenticator_attestation_response.md#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [publicKey](_f_i_d_o2___authenticator_attestation_response.md#publickey) | publicKey凭证请求的选项，字节流。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [authenticatorData](_f_i_d_o2___authenticator_attestation_response.md#authenticatordata) | 认证器数据，字节流。 |
| [FIDO2\_Algorithm](../../模块/通行密钥/passkey.md#fido2_algorithm-1) [publicKeyAlgorithm](_f_i_d_o2___authenticator_attestation_response.md#publickeyalgorithm) | 密码算法。 |
| [FIDO2\_AuthenticatorTransportArray](../FIDO2_AuthenticatorTransportArray/_f_i_d_o2___authenticator_transport_array.md) [transports](_f_i_d_o2___authenticator_attestation_response.md#transports) | 定义身份认证器访问类型数组。 |

## 结构体成员变量说明

### attestationObject

```
1. Uint8Buff FIDO2_AuthenticatorAttestationResponse::attestationObject
```

**描述**

声明对象。

### authenticatorData

```
1. Uint8Buff FIDO2_AuthenticatorAttestationResponse::authenticatorData
```

**描述**

认证器数据，字节流。

### clientDataJson

```
1. Uint8Buff FIDO2_AuthenticatorAttestationResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

### publicKey

```
1. Uint8Buff FIDO2_AuthenticatorAttestationResponse::publicKey
```

**描述**

publicKey凭证请求的选项，字节流。

### publicKeyAlgorithm

```
1. FIDO2_Algorithm FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```

**描述**

密码算法。

### transports

```
1. FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorAttestationResponse::transports
```

**描述**

定义身份认证器访问类型数组。
