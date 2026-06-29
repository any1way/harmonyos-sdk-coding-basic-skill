---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning
title: NetStack_CertificatePinning
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_CertificatePinning
category: harmonyos-references
scraped_at: 2026-06-01T16:07:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b4e49bd62f8f2194f46d482a2c48c0d485f4d73f9572940427e6cf9f5a0d3fbd
---
```
1. typedef struct NetStack_CertificatePinning {...} NetStack_CertificatePinning
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书锁定信息。

**起始版本：** 12

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [NetStack\_CertificatePinningKind](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md#netstack_certificatepinningkind) kind | 证书锁定类型。 |
| [NetStack\_HashAlgorithm](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md#netstack_hashalgorithm) hashAlgorithm | 哈希算法。 |
| char \*publicKeyHash | 哈希值。 |
