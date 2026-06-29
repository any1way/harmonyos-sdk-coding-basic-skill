---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h
title: net_ssl_c_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_ssl_c_type.h
category: harmonyos-references
scraped_at: 2026-06-01T16:07:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f624e9ca980942bd3e92e71123f9da4f002bda55037449b2ff5e5cebf5b0d8df
---
## 概述

PhonePC/2in1TabletTVWearable

定义SSL/TLS证书链校验模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net\_ssl/net\_ssl\_c\_type.h>

**库：** libnet\_ssl.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NetStack\_CertBlob](../../结构体/NetStack_CertBlob/capi-netstack-netstack-certblob.md) | - | 证书数据结构体。 |
| [NetStack\_CertificatePinning](../../结构体/NetStack_CertificatePinning/capi-netstack-netstack-certificatepinning.md) | NetStack\_CertificatePinning | 定义证书锁定信息。 |
| [NetStack\_Certificates](../../结构体/NetStack_Certificates/capi-netstack-netstack-certificates.md) | NetStack\_Certificates | 定义证书信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NetStack\_CertType](capi-net-ssl-c-type-h.md#netstack_certtype) | - | 证书类型枚举。 |
| [NetStack\_CertificatePinningKind](capi-net-ssl-c-type-h.md#netstack_certificatepinningkind) | NetStack\_CertificatePinningKind | 定义证书锁定类型枚举。 |
| [NetStack\_HashAlgorithm](capi-net-ssl-c-type-h.md#netstack_hashalgorithm) | NetStack\_HashAlgorithm | 定义哈希算法。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### NetStack\_CertType

PhonePC/2in1TabletTVWearable

```
1. enum NetStack_CertType
```

**描述**

证书类型枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| NETSTACK\_CERT\_TYPE\_PEM = 0 | PEM证书类型 |
| NETSTACK\_CERT\_TYPE\_DER = 1 | DER证书类型 |
| NETSTACK\_CERT\_TYPE\_INVALID | 错误证书类型 |

### NetStack\_CertificatePinningKind

PhonePC/2in1TabletTVWearable

```
1. enum NetStack_CertificatePinningKind
```

**描述**

定义证书锁定类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PUBLIC\_KEY | 公钥锁定类型 |

### NetStack\_HashAlgorithm

PhonePC/2in1TabletTVWearable

```
1. enum NetStack_HashAlgorithm
```

**描述**

定义哈希算法。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SHA\_256 | Sha256 |
