---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue
title: Http_HeaderValue
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_HeaderValue
category: harmonyos-references
scraped_at: 2026-06-01T16:07:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dff4c33c6af1183785d5284ca73c94ea70b4d10fea3a14f8dde49d82f263d522
---
```
1. typedef struct Http_HeaderValue {...} Http_HeaderValue
```

## 概述

PhonePC/2in1TabletTVWearable

请求或者响应的标头映射的值类型。

**起始版本：** 20

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_http\_type.h](../../头文件/net_http_type.h/capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*value | 标头键值对的值。 |
| struct Http\_HeaderValue \*next | 链式存储。指向下一个Http\_HeaderValue。 |
