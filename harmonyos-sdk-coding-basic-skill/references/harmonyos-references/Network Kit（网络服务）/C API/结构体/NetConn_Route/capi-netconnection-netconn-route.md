---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-route
title: NetConn_Route
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_Route
category: harmonyos-references
scraped_at: 2026-06-01T16:07:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7120d15431bb1fae7959a9ebb07a2d5870db91326a91fd034c09dd21fc1036a7
---
```
1. typedef struct NetConn_Route {...} NetConn_Route
```

## 概述

PhonePC/2in1TabletTVWearable

路由配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](../../模块/NetConnection/capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](../../头文件/net_connection_type.h/capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char iface[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络接口 |
| [NetConn\_NetAddr](../NetConn_NetAddr/capi-netconnection-netconn-netaddr.md) destination | 目标地址 |
| [NetConn\_NetAddr](../NetConn_NetAddr/capi-netconnection-netconn-netaddr.md) gateway | 网关地址 |
| int32\_t hasGateway | 是否存在网关 |
| int32\_t isDefaultRoute | 是否是默认路由 |
