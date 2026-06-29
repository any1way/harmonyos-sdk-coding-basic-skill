---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback
title: Rcp_OnStatusCodeReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnStatusCodeReceiveCallback
category: harmonyos-references
scraped_at: 2026-06-01T16:09:12+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:be5318b13f16a7e971d0535015701c0b3d07129ba7f0a45b77a251fc3b18fee2
---
## 概述

PhonePC/2in1TabletTVWearable

响应的状态码接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)为请求设置相应回调函数。

**起始版本：** 6.0.1(21)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnStatusCodeReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc) [callback](_rcp___on_status_code_callback.md#callback) | 请求过程中接收响应状态码的回调函数。 |
| void \*[usrObject](_rcp___on_status_code_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnStatusCodeReceiveCallbackFunc Rcp_OnStatusCodeReceiveCallback::callback
```

**描述**

响应状态码接收回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnStatusCodeReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
