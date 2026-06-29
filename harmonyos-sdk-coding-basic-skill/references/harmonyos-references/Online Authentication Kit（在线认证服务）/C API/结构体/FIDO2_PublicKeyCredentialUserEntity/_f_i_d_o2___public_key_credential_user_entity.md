---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_user_entity
title: FIDO2_PublicKeyCredentialUserEntity
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialUserEntity
category: harmonyos-references
scraped_at: 2026-06-11T16:11:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db5f6a19bfd30d03bf483c9a257003c06997d44267a2f649dd9e7e5e36e54280
---
## 概述

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](../Uint8Buff/_uint8_buff.md) [id](_f_i_d_o2___public_key_credential_user_entity.md#id) | 凭据的标识符。 |
| char \* [displayName](_f_i_d_o2___public_key_credential_user_entity.md#displayname) | 前台显示的用户名。 |
| char \* [name](_f_i_d_o2___public_key_credential_user_entity.md#name) | 用户名。 |

## 结构体成员变量说明

### displayName

```
1. char* FIDO2_PublicKeyCredentialUserEntity::displayName
```

**描述**

前台显示的用户名。

### id

```
1. Uint8Buff FIDO2_PublicKeyCredentialUserEntity::id
```

**描述**

凭据的标识符。

### name

```
1. char* FIDO2_PublicKeyCredentialUserEntity::name
```

**描述**

用户名。
