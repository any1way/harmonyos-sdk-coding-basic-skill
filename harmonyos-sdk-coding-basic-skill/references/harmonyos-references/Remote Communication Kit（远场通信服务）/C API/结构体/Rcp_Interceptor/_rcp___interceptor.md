---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor
title: Rcp_Interceptor
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Interceptor
category: harmonyos-references
scraped_at: 2026-06-01T16:08:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d69d22714e7635c199b0ab6fa5fc7101ff2133700175508fa9a2f672e0463643
---
## 概述

PhonePC/2in1TabletTVWearable

异步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t(\* [intercept](_rcp___interceptor.md#intercept) )([Rcp\_Request](../Rcp_Request/_rcp___request.md) \*request, const [Rcp\_RequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requesthandler) \*next, const [Rcp\_ResponseCallbackObject](../Rcp_ResponseCallbackObject/_rcp___response_callback_object.md) \*responseCallback) | 指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### intercept

PhonePC/2in1TabletTVWearable

```
1. uint32_t(* Rcp_Interceptor::intercept) (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback)
```

**描述**

指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp\_Request](../Rcp_Request/_rcp___request.md)的指针。 |
| next | 指向下一个异步处理器的指针[Rcp\_RequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requesthandler)。 |
| responseCallback | 指向[Rcp\_ResponseCallbackObject](../Rcp_ResponseCallbackObject/_rcp___response_callback_object.md)的指针。 |

**返回：**

uint32\_t 返回表示拦截器的返回值。
