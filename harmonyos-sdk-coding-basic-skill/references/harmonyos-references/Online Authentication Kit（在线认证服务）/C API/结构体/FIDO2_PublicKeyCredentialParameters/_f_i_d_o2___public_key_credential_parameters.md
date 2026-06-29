---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters
title: FIDO2_PublicKeyCredentialParameters
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialParameters
category: harmonyos-references
scraped_at: 2026-06-11T16:11:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1acb8d61c0fd5d7742d772f7666c2b5beb75769d52cce464c2e2f03e9c3dd54c
---
## 概述

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_PublicKeyCredentialType](../../模块/通行密钥/passkey.md#fido2_publickeycredentialtype-1) [type](_f_i_d_o2___public_key_credential_parameters.md#type) | PublicKey凭证类型。 |
| [FIDO2\_Algorithm](../../模块/通行密钥/passkey.md#fido2_algorithm-1) [alg](_f_i_d_o2___public_key_credential_parameters.md#alg) | 算法。 |

## 结构体成员变量说明

### alg

```
1. FIDO2_Algorithm FIDO2_PublicKeyCredentialParameters::alg
```

**描述**

算法。

### type

```
1. FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialParameters::type
```

**描述**

PublicKey凭证类型。
