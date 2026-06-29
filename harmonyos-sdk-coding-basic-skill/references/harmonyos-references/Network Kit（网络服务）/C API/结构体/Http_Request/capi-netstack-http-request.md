---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request
title: Http_Request
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Request
category: harmonyos-references
scraped_at: 2026-06-01T16:07:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:ea8e1eaa08012231702efac8da68da7b2f05929f71807834da3fbfd47fcd20fa
---
```
1. typedef struct Http_Request {...} Http_Request
```

## 概述

PhonePC/2in1TabletTVWearable

HTTP请求结构体。

**起始版本：** 20

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_http\_type.h](../../头文件/net_http_type.h/capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t requestId | HTTP请求的ID。 |
| char \*url | HTTP请求的URL。 |
| [Http\_RequestOptions](../Http_RequestOptions/capi-netstack-http-requestoptions.md) \*options | HTTP请求配置，指向Http\_RequestOptions的指针，参考[Http\_RequestOptions](../Http_RequestOptions/capi-netstack-http-requestoptions.md)。 |
