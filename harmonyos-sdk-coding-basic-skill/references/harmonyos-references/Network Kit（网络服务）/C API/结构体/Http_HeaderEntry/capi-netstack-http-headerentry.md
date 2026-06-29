---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry
title: Http_HeaderEntry
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_HeaderEntry
category: harmonyos-references
scraped_at: 2026-06-01T16:07:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28e9124ff9325343691b37c9fc73abd37c50faa43b6043c6a2c3e1b06706e1c7
---
```
1. typedef struct Http_HeaderEntry {...} Http_HeaderEntry
```

## 概述

PhonePC/2in1TabletTVWearable

请求或者响应的标头的所有键值对。

**起始版本：** 20

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [net\_http\_type.h](../../头文件/net_http_type.h/capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*key | 请求或者响应的标头中的键。 |
| [Http\_HeaderValue](../Http_HeaderValue/capi-netstack-http-headervalue.md) \*value | 请求或者响应的标头中的键对应的值，参考[Http\_HeaderValue](../Http_HeaderValue/capi-netstack-http-headervalue.md)。 |
| struct Http\_HeaderEntry \*next | 链式存储。指向下一个Http\_HeaderEntry。 |
