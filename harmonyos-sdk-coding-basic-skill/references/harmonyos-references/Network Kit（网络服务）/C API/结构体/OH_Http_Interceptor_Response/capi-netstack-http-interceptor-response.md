---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-response
title: OH_Http_Interceptor_Response
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Response
category: harmonyos-references
scraped_at: 2026-06-01T16:07:38+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:50b3acb0d28b9f731902c564a6860022972ee5a7848ee1c56d17c0314a31f7fd
---
```
1. typedef struct OH_Http_Interceptor_Response {
2. Http_Buffer body;
3. Http_ResponseCode responseCode;
4. OH_Http_Interceptor_Headers *headers;
5. Http_PerformanceTiming performanceTiming;
6. } OH_Http_Interceptor_Response;
```

## 概述

PhonePC/2in1TabletTVWearable

定义拦截器的HTTP响应数据包结构。

**起始版本：** 24

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| Http\_Buffer body | 响应体内容，详情请参考[Http\_Buffer](../Http_Buffer/capi-netstack-http-buffer.md)定义。 |
| Http\_ResponseCode responseCode | 响应状态码，详情请参考[Http\_ResponseCode](../../头文件/net_http_type.h/capi-net-http-type-h.md#http_responsecode) 枚举定义。 |
| OH\_Http\_Interceptor\_Headers \*headers | HTTP响应头信息，详情请参考[OH\_Http\_Interceptor\_Headers](../OH_Http_Interceptor_Headers/capi-netstack-http-interceptor-headers.md)定义。 |
| Http\_PerformanceTiming performanceTiming | 响应性能信息，详情请参考[Http\_PerformanceTiming](../Http_PerformanceTiming/capi-netstack-http-performancetiming.md)定义。 |
