---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_hint_array
title: FIDO2_PublicKeyCredentialHintArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialHintArray
category: harmonyos-references
scraped_at: 2026-06-11T16:11:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1c91e051e129a9174ce0f7a7cdcc0b14ee587ea6f531296a1a8afe95464809d
---
## 概述

认证方式指示数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [hintNum](_f_i_d_o2___public_key_credential_hint_array.md#hintnum) | 认证方式指示数目。 |
| [FIDO2\_PublicKeyCredentialHint](../../模块/通行密钥/passkey.md#fido2_publickeycredentialhint-1) \* [hints](_f_i_d_o2___public_key_credential_hint_array.md#hints) | 认证方式指示列表。 |

## 结构体成员变量说明

### hintNum

```
1. uint32_t FIDO2_PublicKeyCredentialHintArray::hintNum
```

**描述**

认证方式指示数目。

### hints

```
1. FIDO2_PublicKeyCredentialHint* FIDO2_PublicKeyCredentialHintArray::hints
```

**描述**

认证方式指示列表。
