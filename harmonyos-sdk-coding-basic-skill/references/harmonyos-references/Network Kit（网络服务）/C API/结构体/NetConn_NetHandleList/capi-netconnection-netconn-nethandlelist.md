---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist
title: NetConn_NetHandleList
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetHandleList
category: harmonyos-references
scraped_at: 2026-06-01T16:07:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:db903a851286e271af553ef10e5a2f80ebf3fc54a64747307f2039f746848a6e
---
```
1. typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```

## 概述

PhonePC/2in1TabletTVWearable

网络列表。

**起始版本：** 11

**相关模块：** [NetConnection](../../模块/NetConnection/capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](../../头文件/net_connection_type.h/capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](../NetConn_NetHandle/capi-netconnection-netconn-nethandle.md) netHandles[[NETCONN\_MAX\_NET\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | netHandle列表。 |
| int32\_t netHandleListSize | netHandleList的实际大小。 |
