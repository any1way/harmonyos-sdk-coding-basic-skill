---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-request
title: OH_Http_Interceptor_Request
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Request
category: harmonyos-references
scraped_at: 2026-06-01T16:07:37+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a59826b931bb8e296d92b2687975ccddbcc6cbd72203da685819d3cb4f91ddd2
---
```
1. typedef struct OH_Http_Interceptor_Request {
2. Http_Buffer url;
3. Http_Buffer method;
4. OH_Http_Interceptor_Headers *headers;
5. Http_Buffer body;
6. } OH_Http_Interceptor_Request;
```

## 概述

PhonePC/2in1TabletTVWearable

定义拦截器的HTTP请求数据包结构。

**起始版本：** 24

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| Http\_Buffer url | 请求URL，详情请参考[Http\_Buffer](../Http_Buffer/capi-netstack-http-buffer.md)定义。 |
| Http\_Buffer method | 请求方法，详情请参考[Http\_Buffer](../Http_Buffer/capi-netstack-http-buffer.md)定义。 |
| OH\_Http\_Interceptor\_Headers \*headers | HTTP请求头信息，详情请参考[OH\_Http\_Interceptor\_Headers](../OH_Http_Interceptor_Headers/capi-netstack-http-interceptor-headers.md)定义。 |
| Http\_Buffer body | 请求体内容，详情请参考[Http\_Buffer](../Http_Buffer/capi-netstack-http-buffer.md)定义。 |
