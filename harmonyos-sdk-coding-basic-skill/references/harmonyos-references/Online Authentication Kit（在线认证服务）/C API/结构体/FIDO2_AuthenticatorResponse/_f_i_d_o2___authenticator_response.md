---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_response
title: FIDO2_AuthenticatorResponse
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorResponse
category: harmonyos-references
scraped_at: 2026-06-11T16:11:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4ef6fd53ee7c0e51e51667e0106cda62f32b7d3a79ab0b006f6c1020478292b
---
## 概述

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [authenticatorData](_f_i_d_o2___authenticator_response.md#authenticatordata) | 身份认证器数据。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [signature](_f_i_d_o2___authenticator_response.md#signature) | 签名。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [userHandle](_f_i_d_o2___authenticator_response.md#userhandle) | 用户句柄（用户ID）。可选。 |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [clientDataJson](_f_i_d_o2___authenticator_response.md#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |

## 结构体成员变量说明

### authenticatorData

```
1. Uint8Buff FIDO2_AuthenticatorResponse::authenticatorData
```

**描述**

身份认证器数据。

### clientDataJson

```
1. Uint8Buff FIDO2_AuthenticatorResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

### signature

```
1. Uint8Buff FIDO2_AuthenticatorResponse::signature
```

**描述**

签名。

### userHandle

```
1. Uint8Buff FIDO2_AuthenticatorResponse::userHandle
```

**描述**

用户句柄。可选。
