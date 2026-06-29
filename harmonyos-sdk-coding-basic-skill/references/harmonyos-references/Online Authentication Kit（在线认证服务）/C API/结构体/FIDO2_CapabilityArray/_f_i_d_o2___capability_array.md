---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array
title: FIDO2_CapabilityArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CapabilityArray
category: harmonyos-references
scraped_at: 2026-06-11T16:11:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d119dfa8844eb8f7174a16b281c58a648af0000203c96e6fb439c8daf0d051c8
---
## 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [number](_f_i_d_o2___capability_array.md#number) | 能力的数量。 |
| [FIDO2\_Capability](../FIDO2_Capability/_f_i_d_o2___capability.md) \* [capability](_f_i_d_o2___capability_array.md#capability) | 能力的数组。 |

## 结构体成员变量说明

### capability

```
1. FIDO2_Capability* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。

### number

```
1. uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。
