---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-clientcert
title: Http_ClientCert
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_ClientCert
category: harmonyos-references
scraped_at: 2026-06-01T16:07:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:81ef8be4eb4f54e0513e88a2b71673a7a6d13934c31f8f95042f4f3efd9d5a99
---
```
1. typedef struct Http_ClientCert {...} Http_ClientCert
```

## 概述

PhonePC/2in1TabletTVWearable

发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。

**起始版本：** 20

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_http\_type.h](../../头文件/net_http_type.h/capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*certPath | 证书路径。 |
| [Http\_CertType](../../头文件/net_http_type.h/capi-net-http-type-h.md#http_certtype) type | 证书类型，默认是PEM，参考[Http\_CertType](../../头文件/net_http_type.h/capi-net-http-type-h.md#http_certtype)。 |
| char \*keyPath | 证书密钥的路径。 |
| char \*keyPassword | 证书密钥的密码。 |
