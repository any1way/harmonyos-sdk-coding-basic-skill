---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo
title: NetConn_TraceRouteInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_TraceRouteInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:07:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:46d221eaf525ee0fc29d73eda6c4b4af85d44b590f9c7195f46f8566f8e9a749
---
```
1. typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义跟踪路由信息。

**起始版本：** 20

**相关模块：** [NetConnection](../../模块/NetConnection/capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](../../头文件/net_connection_type.h/capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t jumpNo | 跳数。 |
| char address[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 主机名或地址。 |
| uint32\_t rtt[[NETCONN\_MAX\_RTT\_NUM]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 往返时间（单位：毫秒)，包含最大、最小、平均、标准差。 |
