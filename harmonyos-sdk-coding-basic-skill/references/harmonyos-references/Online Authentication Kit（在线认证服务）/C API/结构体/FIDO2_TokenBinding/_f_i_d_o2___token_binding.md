---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___token_binding
title: FIDO2_TokenBinding
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_TokenBinding
category: harmonyos-references
scraped_at: 2026-06-11T16:11:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91963143abd4718267dee5ce4a3e685cb0798f48f6e03fbb8c2d25077eaeeeb8
---
## 概述

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_TokenBindingStatus](../../模块/通行密钥/passkey.md#fido2_tokenbindingstatus-1) [status](_f_i_d_o2___token_binding.md#status) | 客户端的绑定状态。 |
| char \* [id](_f_i_d_o2___token_binding.md#id) | 令牌绑定标识符。 |

## 结构体成员变量说明

### id

```
1. char* FIDO2_TokenBinding::id
```

**描述**

令牌绑定标识符。

### status

```
1. FIDO2_TokenBindingStatus FIDO2_TokenBinding::status
```

**描述**

客户端的绑定状态。
