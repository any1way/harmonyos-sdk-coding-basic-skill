---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netconncallback
title: NetConn_NetConnCallback
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetConnCallback
category: harmonyos-references
scraped_at: 2026-06-01T16:07:14+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:d3eb656c34c5f6bc7ca748117440277256935ef6838a93bc445ba02ae90f61ec
---
```
1. typedef struct NetConn_NetConnCallback {...} NetConn_NetConnCallback
```

## 概述

PhonePC/2in1TabletTVWearable

网络状态监听回调集合，所有回调事件需全部注册，无需关注的回调可以设为空实现。

**起始版本：** 12

**相关模块：** [NetConnection](../../模块/NetConnection/capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](../../头文件/net_connection_type.h/capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_NetConn\_NetworkAvailable](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_networkavailable) onNetworkAvailable | 网络可用回调。 |
| [OH\_NetConn\_NetCapabilitiesChange](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_netcapabilitieschange) onNetCapabilitiesChange | 网络能力集变更回调。 |
| [OH\_NetConn\_NetConnectionPropertiesChange](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_netconnectionpropertieschange) onConnetionProperties | 网络连接属性变更回调。 |
| [OH\_NetConn\_NetLost](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_netlost) onNetLost | 网络断开回调。 |
| [OH\_NetConn\_NetUnavailable](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_netunavailable) onNetUnavailable | 网络不可用回调, 在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。 |
| [OH\_NetConn\_NetBlockStatusChange](../../头文件/net_connection_type.h/capi-net-connection-type-h.md#oh_netconn_netblockstatuschange) onNetBlockStatusChange | 网络阻塞状态变更回调。 |
