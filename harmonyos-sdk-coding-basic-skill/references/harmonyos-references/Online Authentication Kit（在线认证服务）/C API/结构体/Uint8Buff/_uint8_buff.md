---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff
title: Uint8Buff
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > Uint8Buff
category: harmonyos-references
scraped_at: 2026-06-11T16:11:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b037373bc7947ef42cdd4f1b39fad8389e25eb86223df622cd897f81e700e786
---
## 概述

定义uint8\_t字节流。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](../../模块/通行密钥/passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [length](_uint8_buff.md#length) | 字节流的长度。 |
| uint8\_t \* [val](_uint8_buff.md#val) | 字节流的值。 |

## 结构体成员变量说明

### length

```
1. uint32_t Uint8Buff::length
```

**描述**

字节流的长度。

### val

```
1. uint8_t* Uint8Buff::val
```

**描述**

字节流的值。
