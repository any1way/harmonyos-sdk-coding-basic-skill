---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback
title: Rcp_OnHeaderReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnHeaderReceiveCallback
category: harmonyos-references
scraped_at: 2026-06-01T16:08:48+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:f8c80083f26c3791e7405e16549bc70fce63e6ef5f4219859015be06d0c2a42c
---
## 概述

PhonePC/2in1TabletTVWearable

[Rcp\_EventsHandler](../Rcp_EventsHandler/_rcp___events_handler.md)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

**所在头文件：** [rcp.h](../../头文件/rcp.h/rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnHeaderReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onheaderreceivecallbackfunc) [callback](_rcp___on_header_receive_callback.md#callback) | 接收到的headers的回调函数。 |
| void \* [usrObject](_rcp___on_header_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnHeaderReceiveCallbackFunc Rcp_OnHeaderReceiveCallback::callback
```

**描述**

接收到的headers的回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnHeaderReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
