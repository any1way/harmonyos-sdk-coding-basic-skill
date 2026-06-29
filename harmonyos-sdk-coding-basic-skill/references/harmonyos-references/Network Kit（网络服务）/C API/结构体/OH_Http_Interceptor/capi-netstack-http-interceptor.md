---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor
title: OH_Http_Interceptor
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor
category: harmonyos-references
scraped_at: 2026-06-01T16:07:39+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:d270afed837a70822c2cdc84d8c8b58e41b331a6d268f3da739cf2aba2b82f36
---
```
1. typedef struct OH_Http_Interceptor {
2. int32_t groupId;
3. OH_Interceptor_Stage stage;
4. OH_Interceptor_Type type;
5. OH_Http_InterceptorHandler handler;
6. int32_t enabled;
7. } OH_Http_Interceptor;
```

## 概述

PhonePC/2in1TabletTVWearable

定义HTTP全局拦截器的配置信息。

**起始版本：** 24

**相关模块：** [netstack](../../模块/Netstack/capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t groupId | 拦截器组ID。 |
| OH\_Interceptor\_Stage stage | 拦截器的执行阶段，详情请参考[OH\_Interceptor\_Stage](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md#oh_interceptor_stage) 枚举定义。 |
| OH\_Interceptor\_Type type | 拦截器的类型，详情请参考[OH\_Interceptor\_Type](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md#oh_interceptor_type) 枚举定义。 |
| OH\_Http\_InterceptorHandler handler | 拦截器处理函数，详情请参考[OH\_Http\_InterceptorHandler](../../头文件/http_interceptor_type.h/capi-net-http-interceptor-type-h.md#oh_http_interceptorhandler) 函数指针定义。 |
| int32\_t enabled | 拦截器的启用状态。0代表未启用，非0代表启用。 |
