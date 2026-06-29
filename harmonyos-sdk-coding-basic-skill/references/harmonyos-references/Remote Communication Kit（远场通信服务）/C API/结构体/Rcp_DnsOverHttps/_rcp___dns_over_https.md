---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https
title: Rcp_DnsOverHttps
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsOverHttps
category: harmonyos-references
scraped_at: 2026-06-01T16:08:35+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:76dc9d314c32d0ea76af04782f2ec1fd6cb40d77b632fe3a269d1b42c328f646
---
## 概述

PhonePC/2in1TabletTVWearable

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___dns_over_https.md#url) | DOH服务器的URL。 |
| bool [skipCertificatesValidation](_rcp___dns_over_https.md#skipcertificatesvalidation) | 判断是否跳过证书验证。true代表跳过，false代表不跳过，默认值为false。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### skipCertificatesValidation

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_DnsOverHttps::skipCertificatesValidation
```

**描述**

判断是否跳过证书验证。默认值为false。

### url

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_DnsOverHttps::url
```

**描述**

DOH服务器的URL。
