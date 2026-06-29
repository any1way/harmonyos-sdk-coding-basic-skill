---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates
title: NetStack_Certificates
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_Certificates
category: harmonyos-references
scraped_at: 2026-06-01T16:07:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a609cf8fe72d7dacb60f4212ad061fd65f037ca40938030ce79a7350b74f4982
---
```
1. typedef struct NetStack_Certificates {...} NetStack_Certificates
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书信息。

**起始版本：** 12

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](../../头文件/net_ssl_c_type.h/capi-net-ssl-c-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*\*content | 证书的PEM内容。 |
| size\_t length | 证书数量。 |
