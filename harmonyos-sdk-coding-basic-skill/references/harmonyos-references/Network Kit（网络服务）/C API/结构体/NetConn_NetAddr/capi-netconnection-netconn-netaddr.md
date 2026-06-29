---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr
title: NetConn_NetAddr
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetAddr
category: harmonyos-references
scraped_at: 2026-06-01T16:07:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:23861898a15ea90c209000717fe5deb1e26305073f1fe91c0fd0efd462666ef6
---
```
1. typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```

## 概述

PhonePC/2in1TabletTVWearable

网络地址。

**起始版本：** 11

**相关模块：** [NetConnection](../../模块/NetConnection/capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](../../头文件/net_connection_type.h/capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t family | 网络地址族。 |
| uint8\_t prefixlen | 前缀长度。 |
| uint8\_t port | 端口号。 |
| char address[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 地址。 |
