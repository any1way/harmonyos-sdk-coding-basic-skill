---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_option_array
title: FIDO2_CredentialCreationOptionArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CredentialCreationOptionArray
category: harmonyos-references
scraped_at: 2026-06-11T16:11:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b648e3c9674a8abd17ac672d8df0b992be8e893e39a116272e99860b450be66e
---
## 概述

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [pubKeyCredParamNum](_f_i_d_o2___credential_creation_option_array.md#pubkeycredparamnum) | PubKeyCredParam参数数目。 |
| [FIDO2\_PublicKeyCredentialParameters](../FIDO2_PublicKeyCredentialParameters/_f_i_d_o2___public_key_credential_parameters.md) \* [pubKeyCredParams](_f_i_d_o2___credential_creation_option_array.md#pubkeycredparams) | 认证凭据的附加参数。 |

## 结构体成员变量说明

### pubKeyCredParamNum

```
1. uint32_t FIDO2_CredentialCreationOptionArray::pubKeyCredParamNum
```

**描述**

PubKeyCredParam参数数目。

### pubKeyCredParams

```
1. FIDO2_PublicKeyCredentialParameters* FIDO2_CredentialCreationOptionArray::pubKeyCredParams
```

**描述**

认证凭据的附加参数。
