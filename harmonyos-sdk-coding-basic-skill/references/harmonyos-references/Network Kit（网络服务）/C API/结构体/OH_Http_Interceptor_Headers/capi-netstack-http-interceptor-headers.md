---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers
title: OH_Http_Interceptor_Headers
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Headers
category: harmonyos-references
scraped_at: 2026-06-01T16:07:37+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9dc753140d00417611a1e9221953efa88c2f540841f96374f0aa761b839865b9
---
```
1. typedef struct OH_Http_Interceptor_Headers {
2. char *data;
3. struct OH_Http_Interceptor_Headers *next;
4. } OH_Http_Interceptor_Headers;
```

## 概述

PhonePC/2in1TabletTVWearable

定义拦截器的请求/响应头信息。

**起始版本：** 24

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*data | 拦截器请求/响应头信息。 |
| struct OH\_Http\_Interceptor\_Headers \*next | 指向下一个头信息的指针。 |
