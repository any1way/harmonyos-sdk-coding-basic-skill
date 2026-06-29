---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob
title: NetStack_CertBlob
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_CertBlob
category: harmonyos-references
scraped_at: 2026-06-01T16:07:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:002ea3a2fe8b09fb8ba6bc10b6a02c0031498310c840ce1c8f462b68fc4eb816
---
```
1. struct NetStack_CertBlob {...}
```

## 概述

PhonePC/2in1TabletTVWearable

证书数据结构体。

**起始版本：** 11

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| enum [NetStack\_CertType](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md#netstack_certtype) type | 证书类型。 |
| uint32\_t size | 证书内容长度。 |
| uint8\_t \*data | 证书内容。 |
